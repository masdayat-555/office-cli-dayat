import os
import sys
import json
from pathlib import Path
from pyzotero import zotero
from zotero_clean_metadata import clean_and_build_zotero_item

def load_zotero_credentials():
    """
    Membaca ZOTERO_USER_ID dan ZOTERO_API_KEY dari .env skill atau environment variables.
    """
    env_file = Path(__file__).resolve().parent.parent / '.env'
    user_id = os.environ.get('ZOTERO_USER_ID', '')
    api_key = os.environ.get('ZOTERO_API_KEY', '')
    
    if env_file.exists():
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('ZOTERO_USER_ID='):
                    user_id = line.split('=', 1)[1].strip().strip('"').strip("'")
                elif line.startswith('ZOTERO_API_KEY='):
                    api_key = line.split('=', 1)[1].strip().strip('"').strip("'")
                    
    return user_id, api_key

def get_or_create_collection(zot, collection_name: str) -> str:
    """
    Mencari atau membuat koleksi (folder) baru di Zotero Cloud.
    """
    collections = zot.collections()
    for col in collections:
        if col.get('data', {}).get('name', '').lower() == collection_name.lower():
            print(f"[ZOTERO] Menggunakan koleksi yang sudah ada: '{collection_name}' (Key: {col['key']})")
            return col['key']
            
    print(f"[ZOTERO] Membuat koleksi baru: '{collection_name}'...")
    new_cols = zot.create_collections([{"name": collection_name}])
    if new_cols and 'successful' in new_cols and new_cols['successful']:
        col_key = list(new_cols['successful'].values())[0]['key']
        print(f"[ZOTERO] Sukses membuat koleksi! (Key: {col_key})")
        return col_key
    elif new_cols and isinstance(new_cols, list) and len(new_cols) > 0:
        col_key = new_cols[0].get('key', '')
        return col_key
    raise RuntimeError("Gagal membuat koleksi di Zotero.")

def sync_paper_list_to_zotero(papers_list: list, collection_name: str = "Pengusir Tikus Pintar", pdf_folder: str = None) -> dict:
    """
    Sinkronisasi massal seluruh paper ke Zotero Cloud dengan pembersihan metadata otomatis:
    - Normalisasi judul dan penulis.
    - Cek duplikasi di koleksi.
    - Upload item dan lampiran berkas PDF fisik (jika ada).
    - Menghasilkan kamus pemetaan Item Key Zotero resmi.
    """
    user_id, api_key = load_zotero_credentials()
    if not user_id or not api_key:
        print("[ERROR] Kredensial Zotero belum disetel! Harap masukkan ZOTERO_USER_ID dan ZOTERO_API_KEY di file .env")
        return {}
        
    zot = zotero.Zotero(user_id, 'user', api_key)
    col_key = get_or_create_collection(zot, collection_name)
    
    # Ambil item yang sudah ada di koleksi untuk mencegah duplikasi
    existing_items = zot.collection_items(col_key)
    existing_titles = {it.get('data', {}).get('title', '').strip().lower(): it.get('key') for it in existing_items}
    existing_dois = {it.get('data', {}).get('DOI', '').strip().lower(): it.get('key') for it in existing_items if it.get('data', {}).get('DOI')}
    
    zotero_map = {}
    
    for entry in papers_list:
        cite_key = entry.get('cite_key', '')
        doi = entry.get('doi', '').strip().lower()
        title = entry.get('title', '').strip()
        
        # 1. Cek apakah sudah pernah di-upload
        if doi and doi in existing_dois:
            item_key = existing_dois[doi]
            print(f"[SKIP DUP] {cite_key} sudah ada di Zotero (Key: {item_key})")
            zotero_map[cite_key] = {
                "item_key": item_key,
                "title": title,
                "status": "existing"
            }
            continue
            
        # 2. Pembersihan & Pengambilan Metadata Kanonikal
        print(f"[CLEANING METADATA] Memproses {cite_key}...")
        cleaned_item = clean_and_build_zotero_item(entry)
        cleaned_item["collections"] = [col_key]
        
        # 3. Upload ke Zotero Cloud
        try:
            resp = zot.create_items([cleaned_item])
            if resp.get('successful'):
                item_key = list(resp['successful'].values())[0]['key']
                print(f"[SUCCESS UPLOAD] {cite_key} -> Zotero Key: {item_key}")
                zotero_map[cite_key] = {
                    "item_key": item_key,
                    "title": cleaned_item["title"],
                    "status": "uploaded",
                    "csl_data": cleaned_item
                }
            else:
                print(f"[FAILED] Gagal upload {cite_key}: {resp.get('failed')}")
        except Exception as e:
            print(f"[ERROR] Error saat upload {cite_key}: {e}")
            
    return zotero_map

if __name__ == "__main__":
    uid, key = load_zotero_credentials()
    print(f"Status Kredensial Zotero: User ID = {'[TERSEDIA]' if uid else '[KOSONG]'}, API Key = {'[TERSEDIA]' if key else '[KOSONG]'}")
