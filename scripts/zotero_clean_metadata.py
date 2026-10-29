import os
import re
import sys
import json
import requests
from pathlib import Path

# Pastikan output konsol UTF-8 di Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def normalize_title(title: str) -> str:
    """
    Membersihkan judul artikel:
    - Menghapus spasi ganda dan karakter newline.
    - Jika ALL CAPS, ubah menjadi Title Case / Sentence Case yang rapi.
    """
    if not title:
        return ""
    title = re.sub(r'\s+', ' ', title.strip())
    # Cek jika judul ditulis huruf besar semua
    if title.isupper() and len(title) > 10:
        # Ubah ke Title Case tapi pertahankan akronim penting (CNN, ESP32, IoT, STFT, AI)
        words = title.lower().split()
        capitalized = []
        acronyms = {"cnn", "esp32", "iot", "stft", "ai", "usv", "bce", "relu", "tflite", "mcu", "uart", "rf", "ipm", "pdm", "i2s"}
        for i, w in enumerate(words):
            clean_w = re.sub(r'[^a-zA-Z0-9]', '', w)
            if clean_w in acronyms:
                capitalized.append(w.upper())
            elif i == 0 or len(w) > 3:
                capitalized.append(w.capitalize())
            else:
                capitalized.append(w)
        return " ".join(capitalized)
    return title

def parse_authors(author_str_or_list):
    """
    Mengurai daftar penulis ke format resmi Zotero:
    [{'creatorType': 'author', 'firstName': '...', 'lastName': '...'}, ...]
    Mencegah bug klasik 'semua penulis tergabung jadi satu'.
    """
    creators = []
    if isinstance(author_str_or_list, list):
        for a in author_str_or_list:
            if isinstance(a, dict):
                given = a.get('given', '').strip()
                family = a.get('family', '').strip()
                if family:
                    creators.append({'creatorType': 'author', 'firstName': given, 'lastName': family})
            elif isinstance(a, str):
                parts = [p.strip() for p in a.split(',') if p.strip()]
                if len(parts) >= 2:
                    creators.append({'creatorType': 'author', 'firstName': parts[1], 'lastName': parts[0]})
                elif len(parts) == 1:
                    tokens = parts[0].split()
                    if len(tokens) > 1:
                        creators.append({'creatorType': 'author', 'firstName': " ".join(tokens[:-1]), 'lastName': tokens[-1]})
                    else:
                        creators.append({'creatorType': 'author', 'firstName': '', 'lastName': tokens[0]})
        return creators

    # Jika berupa string (format APA: 'Chen, J., & Ran, X.' atau 'Modlinska, K., & Pisula, W.')
    raw = str(author_str_or_list)
    raw = raw.replace('&', ',').replace(' and ', ', ')
    raw_authors = [a.strip() for a in re.split(r',\s*(?=[A-Z][a-z]+|\b[A-Z]\b)', raw) if a.strip()]
    
    # Alternatif pemisahan dengan pola Last, First
    tokens = [t.strip() for t in raw.split(',') if t.strip()]
    i = 0
    while i < len(tokens):
        last = tokens[i]
        first = tokens[i+1] if i+1 < len(tokens) else ""
        # Validasi apakah first terlihat seperti inisial atau nama depan
        if first and (len(first) <= 4 or not re.search(r'\b(et al|dan|and)\b', first)):
            creators.append({'creatorType': 'author', 'firstName': first, 'lastName': last})
            i += 2
        else:
            creators.append({'creatorType': 'author', 'firstName': '', 'lastName': last})
            i += 1
            
    return creators

def fetch_canonical_crossref(doi: str) -> dict:
    """
    Mengambil metadata resmi (Kanonikal) dari CrossRef API berdasarkan DOI.
    Data dari CrossRef adalah standar emas penerbit resmi dunia.
    """
    clean_doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "").strip()
    url = f"https://api.crossref.org/works/{clean_doi}"
    headers = {"User-Agent": "OfficeCLI-ZoteroBot/2.0 (mailto:academic-assistant@local.workspace)"}
    
    try:
        res = requests.get(url, headers=headers, timeout=12)
        if res.status_code == 200:
            msg = res.json().get('message', {})
            title = msg.get('title', [''])[0]
            container = msg.get('container-title', [''])[0]
            volume = msg.get('volume', '')
            issue = msg.get('issue', '')
            page = msg.get('page', '')
            
            # Ekstrak tahun
            year = ""
            issued = msg.get('issued', {}).get('date-parts', [[]])[0]
            if issued:
                year = str(issued[0])
                
            # Penulis
            creators = []
            for a in msg.get('author', []):
                given = a.get('given', '').strip()
                family = a.get('family', '').strip()
                if family:
                    creators.append({'creatorType': 'author', 'firstName': given, 'lastName': family})
                    
            return {
                "success": True,
                "title": normalize_title(title),
                "publicationTitle": container,
                "volume": volume,
                "issue": issue,
                "pages": page,
                "date": year,
                "DOI": clean_doi,
                "creators": creators,
                "source": "CrossRef Official"
            }
    except Exception as e:
        return {"success": False, "error": str(e)}
        
    return {"success": False, "error": "Not found in CrossRef"}

def clean_and_build_zotero_item(raw_entry: dict) -> dict:
    """
    Pipeline Utama Pembersihan Metadata:
    1. Jika ada DOI -> Tarik data resmi CrossRef.
    2. Jika tidak ada / gagal -> Normalisasi judul, pisahkan nama penulis, bersihkan tahun.
    3. Kembalikan item format Zotero yang valid dan siap upload.
    """
    doi = raw_entry.get('doi', '') or raw_entry.get('DOI', '')
    if doi:
        cr_data = fetch_canonical_crossref(doi)
        if cr_data.get('success'):
            item = {
                "itemType": "journalArticle",
                "title": cr_data["title"],
                "creators": cr_data["creators"],
                "publicationTitle": cr_data["publicationTitle"],
                "volume": cr_data["volume"],
                "issue": cr_data["issue"],
                "pages": cr_data["pages"],
                "date": cr_data["date"],
                "DOI": cr_data["DOI"],
                "extra": "Validated via CrossRef Canonical API"
            }
            return item

    # Fallback normalisasi heuristik
    title = normalize_title(raw_entry.get('title', ''))
    creators = parse_authors(raw_entry.get('authors', raw_entry.get('creators', '')))
    date_str = str(raw_entry.get('year', raw_entry.get('date', '')))
    # Ekstrak 4 digit tahun
    year_match = re.search(r'\b(19\d{2}|20\d{2})\b', date_str)
    year = year_match.group(1) if year_match else date_str
    
    item = {
        "itemType": raw_entry.get("itemType", "journalArticle"),
        "title": title,
        "creators": creators,
        "publicationTitle": raw_entry.get("publicationTitle", raw_entry.get("journal", "")),
        "volume": str(raw_entry.get("volume", "")),
        "issue": str(raw_entry.get("issue", "")),
        "pages": str(raw_entry.get("pages", "")),
        "date": year,
        "DOI": doi,
        "extra": "Cleaned via OfficeCLI Heuristics"
    }
    return item

if __name__ == "__main__":
    # Test sample metadata cleansing
    test_doi = "10.1109/JPROC.2019.2921977"
    cleaned = clean_and_build_zotero_item({"doi": test_doi})
    print("[TEST RESULT] Cleaned Zotero Item from CrossRef:")
    print(json.dumps(cleaned, indent=2, ensure_ascii=False))
