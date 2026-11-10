import os
import sys
import json
import argparse
from pathlib import Path
from pyzotero import zotero
from zotero_clean_metadata import clean_and_build_zotero_item

# Pastikan output konsol UTF-8 di Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

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
    
    existing_items = zot.collection_items(col_key)
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
                
                # Cek lampiran PDF jika ada folder PDF
                if pdf_folder:
                    pdf_candidates = list(Path(pdf_folder).glob(f"*{cite_key.split(',')[0]}*.pdf"))
                    if pdf_candidates:
                        pdf_path = pdf_candidates[0]
                        print(f"  [ATTACH PDF] Mengunggah {pdf_path.name}...")
                        try:
                            zot.attachment_simple([str(pdf_path)], item_key)
                            print(f"  [ATTACH SUCCESS] {pdf_path.name} terhubung ke {item_key}")
                        except Exception as att_err:
                            print(f"  [ATTACH WARN] Gagal melampirkan PDF: {att_err}")
            else:
                print(f"[FAILED] Gagal upload {cite_key}: {resp.get('failed')}")
        except Exception as e:
            print(f"[ERROR] Error saat upload {cite_key}: {e}")
            
    return zotero_map

def upload_single_paper(pdf_path: str = None, doi: str = None, title: str = None, 
                        collection_name: str = "Pengusir Tikus Pintar", cite_key: str = None,
                        keys_file: str = None) -> dict:
    """
    Mengunggah satu paper baru secara cepat ke Zotero Cloud:
    - Menarik metadata resmi dari CrossRef via DOI.
    - Mengunggah item jurnal ke koleksi Zotero Cloud.
    - Melampirkan berkas PDF asli ke item.
    - Memperbarui file pemetaan zotero_item_keys.json.
    - Mencetak OpenXML Field Code Word siap pakai.
    """
    user_id, api_key = load_zotero_credentials()
    if not user_id or not api_key:
        print("[ERROR] Kredensial Zotero belum disetel di .env!")
        return {}
        
    zot = zotero.Zotero(user_id, 'user', api_key)
    col_key = get_or_create_collection(zot, collection_name)
    
    # Siapkan data entri
    raw_entry = {}
    if doi:
        raw_entry['doi'] = doi
    if title:
        raw_entry['title'] = title
        
    cleaned_item = clean_and_build_zotero_item(raw_entry)
    cleaned_item["collections"] = [col_key]
    
    clean_doi = cleaned_item.get('DOI', '').strip().lower()
    item_title = cleaned_item.get('title', '')
    
    # Cek apakah item sudah ada di koleksi
    existing_items = zot.collection_items(col_key)
    existing_dois = {it.get('data', {}).get('DOI', '').strip().lower(): it.get('key') for it in existing_items if it.get('data', {}).get('DOI')}
    existing_titles = {it.get('data', {}).get('title', '').strip().lower(): it.get('key') for it in existing_items if it.get('data', {}).get('title')}
    
    item_key = None
    if clean_doi and clean_doi in existing_dois:
        item_key = existing_dois[clean_doi]
        print(f"[ZOTERO] Item sudah ada di Cloud berdasarkan DOI (Key: {item_key})")
    elif item_title and item_title.lower() in existing_titles:
        item_key = existing_titles[item_title.lower()]
        print(f"[ZOTERO] Item sudah ada di Cloud berdasarkan Judul (Key: {item_key})")
    else:
        print(f"[ZOTERO] Membuat item baru untuk: '{item_title}'...")
        resp = zot.create_items([cleaned_item])
        if resp.get('successful'):
            item_key = list(resp['successful'].values())[0]['key']
            print(f"[ZOTERO] Sukses membuat item baru! (Key: {item_key})")
        else:
            raise RuntimeError(f"Gagal membuat item di Zotero: {resp.get('failed')}")
            
    attachment_key = None
    if pdf_path and Path(pdf_path).exists():
        # Cek apakah attachment sudah ada
        children = zot.children(item_key)
        existing_att = [c for c in children if c.get('data', {}).get('itemType') == 'attachment']
        if existing_att:
            attachment_key = existing_att[0].get('key')
            print(f"[ZOTERO] Berkas PDF attachment sudah ada (Key: {attachment_key})")
        else:
            print(f"[ZOTERO] Melampirkan berkas PDF fisik: {pdf_path}...")
            try:
                att_res = zot.attachment_simple([str(pdf_path)], item_key)
                if att_res and isinstance(att_res, list) and len(att_res) > 0:
                    attachment_key = att_res[0].get('key', '')
                print(f"[ZOTERO] Sukses melampirkan PDF! (Attachment Key: {attachment_key})")
            except Exception as e:
                print(f"[ZOTERO WARN] Gagal mengunggah attachment: {e}")
                
    # Buat cite_key jika belum ada
    first_author = "Author"
    creators = cleaned_item.get('creators', [])
    if creators:
        first_author = creators[0].get('lastName', creators[0].get('name', 'Author'))
    year = cleaned_item.get('date', '2026')
    if not cite_key:
        cite_key = f"{first_author} et al., {year}" if len(creators) > 2 else f"{first_author}, {year}"
        
    # Perbarui file zotero_item_keys.json jika ada
    target_keys_file = Path(keys_file) if keys_file else Path.cwd() / "zotero_item_keys.json"
    if target_keys_file.exists():
        try:
            with open(target_keys_file, 'r', encoding='utf-8') as f:
                keys_data = json.load(f)
            keys_data[cite_key] = item_key
            with open(target_keys_file, 'w', encoding='utf-8') as f:
                json.dump(keys_data, f, indent=2, ensure_ascii=False)
            print(f"[ZOTERO] Peta item keys diperbarui di: {target_keys_file}")
        except Exception as e:
            print(f"[ZOTERO WARN] Gagal memperbarui file {target_keys_file}: {e}")
            
    result = {
        "cite_key": cite_key,
        "item_key": item_key,
        "attachment_key": attachment_key,
        "title": item_title,
        "doi": clean_doi,
        "authors": creators,
        "year": year,
        "collection_key": col_key
    }
    
    print("\n" + "="*60)
    print("HASIL REGISTRASI ZOTERO HEADLESS:")
    print(f"  • Cite Key       : {cite_key}")
    print(f"  • Item Key Zotero: {item_key}")
    print(f"  • Attachment Key : {attachment_key}")
    print(f"  • DOI            : {clean_doi}")
    print(f"  • OpenXML Field  : ADDIN ZOTERO_ITEM ... [itemKey: {item_key}]")
    print("="*60 + "\n")
    
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zotero Headless Cloud Synchronizer (OfficeCLI Suite)")
    parser.add_argument("--upload-pdf", help="Path berkas PDF fisik yang akan diunggah", default=None)
    parser.add_argument("--doi", help="DOI resmi paper (misal: 10.2753/MIS0742-1222240302)", default=None)
    parser.add_argument("--title", help="Judul artikel", default=None)
    parser.add_argument("--collection", help="Nama koleksi di Zotero Cloud", default="Pengusir Tikus Pintar")
    parser.add_argument("--cite-key", help="Kunci sitasi (misal: Peffers et al., 2007)", default=None)
    parser.add_argument("--keys-file", help="Path berkas zotero_item_keys.json", default=None)
    
    args = parser.parse_args()
    
    uid, key = load_zotero_credentials()
    print(f"[ZOTERO STATUS] User ID: {'[TERSEDIA]' if uid else '[KOSONG]'} | API Key: {'[TERSEDIA]' if key else '[KOSONG]'}")
    
    if args.upload_pdf or args.doi or args.title:
        upload_single_paper(
            pdf_path=args.upload_pdf,
            doi=args.doi,
            title=args.title,
            collection_name=args.collection,
            cite_key=args.cite_key,
            keys_file=args.keys_file
        )
