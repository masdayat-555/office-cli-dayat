"""
mendeley_upload.py
==================
Modul untuk upload metadata referensi dan file PDF ke Mendeley via API (Global Version).
Dilengkapi dengan fitur Auto-Refresh Token dan ekspor BibTeX lokal.
"""

import json
import urllib.request
import urllib.parse
import urllib.error
import base64
import os
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
ENV_FILE = SKILL_ROOT / ".env"
TOKEN_FILE = SKILL_ROOT / ".mendeley_token.json"
DOCUMENTS_URL = "https://api.mendeley.com/documents"
FILES_URL = "https://api.mendeley.com/files"
TOKEN_URL = "https://api.mendeley.com/oauth/token"

def load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env

def refresh_access_token():
    if not TOKEN_FILE.exists():
        raise FileNotFoundError("Belum ada token. Jalankan mendeley_setup.py dulu.")
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        token_data = json.load(f)
    
    refresh_token = token_data.get("refresh_token")
    if not refresh_token:
        raise ValueError("Tidak ada refresh_token di file token. Silakan jalankan ulang mendeley_setup.py.")

    env = load_env()
    client_id = env.get("MENDELEY_CLIENT_ID")
    client_secret = env.get("MENDELEY_CLIENT_SECRET")
    
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }).encode("utf-8")

    req = urllib.request.Request(TOKEN_URL, data=data)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    req.add_header("Accept", "application/json")
    auth_b64 = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
    req.add_header("Authorization", f"Basic {auth_b64}")

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            new_token_data = json.loads(response.read().decode("utf-8"))
            # Preserve refresh_token if Mendeley didn't return a new one
            if "refresh_token" not in new_token_data:
                new_token_data["refresh_token"] = refresh_token
            
            TOKEN_FILE.write_text(json.dumps(new_token_data, indent=2), encoding="utf-8")
            print("🔄 Token berhasil di-refresh otomatis.")
            return new_token_data.get("access_token")
    except urllib.error.HTTPError as e:
        print(f"❌ Gagal refresh token: {e.read().decode('utf-8', errors='ignore')}")
        raise e

def get_access_token():
    if not TOKEN_FILE.exists():
        raise FileNotFoundError("Belum ada token. Jalankan mendeley_setup.py dulu.")
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        token_data = json.load(f)
    return token_data.get("access_token")

def api_request(url, method="GET", data=None, headers=None, is_retry=False):
    token = get_access_token()
    req_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Authorization": f"Bearer {token}"
    }
    if headers:
        req_headers.update(headers)
    
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in req_headers.items():
        req.add_header(k, v)

    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read()
            if res_body:
                return json.loads(res_body.decode("utf-8"))
            return None
    except urllib.error.HTTPError as e:
        if e.code == 401 and not is_retry:
            refresh_access_token()
            return api_request(url, method, data, headers, is_retry=True)
        else:
            raise e

def create_document(doc_data: dict, pdf_path: str = None, bibtex_dir: str = None):
    headers = {
        "Content-Type": "application/vnd.mendeley-document.1+json",
        "Accept": "application/vnd.mendeley-document.1+json"
    }
    data = json.dumps(doc_data).encode("utf-8")
    
    try:
        print(f"📤 Upload metadata ke Mendeley: {doc_data.get('title')}")
        doc = api_request(DOCUMENTS_URL, method="POST", data=data, headers=headers)
        print("✅ Metadata berhasil diupload.")
        
        doc_id = doc.get("id")
        
        # 1. Upload file PDF jika path diberikan
        if doc_id and pdf_path and os.path.exists(pdf_path):
            upload_file(doc_id, pdf_path)
            
        # 2. Export ke BibTeX jika path direktori diberikan
        if bibtex_dir and os.path.exists(bibtex_dir):
            generate_bibtex(doc_data, bibtex_dir)
            
        return doc
    except urllib.error.HTTPError as e:
        print(f"❌ Gagal upload metadata: {e.read().decode('utf-8', errors='ignore')}")
        raise e

def upload_file(document_id: str, pdf_path: str):
    file_name = os.path.basename(pdf_path)
    print(f"📤 Melampirkan file PDF ke Mendeley: {file_name}")
    
    headers = {
        "Content-Type": "application/pdf",
        "Content-Disposition": f'attachment; filename="{file_name}"',
        "Link": f'<{DOCUMENTS_URL}/{document_id}>; rel="document"'
    }
    
    with open(pdf_path, "rb") as f:
        file_data = f.read()
        
    try:
        api_request(FILES_URL, method="POST", data=file_data, headers=headers)
        print("✅ File PDF fisik berhasil dilampirkan.")
    except urllib.error.HTTPError as e:
        print(f"❌ Gagal melampirkan PDF: {e.read().decode('utf-8', errors='ignore')}")
        raise e

def generate_bibtex(doc_data: dict, out_dir: str):
    # Buat cite_key misal: Koto2021
    authors = doc_data.get("authors", [])
    first_author_last_name = authors[0].get("last_name", "Unknown") if authors else "Unknown"
    cite_key = f"{first_author_last_name}{doc_data.get('year', '')}"
    
    doc_type = doc_data.get('type', 'article')
    
    lines = [f"@{doc_type}{{{cite_key},"]
    lines.append(f"  title = {{{doc_data.get('title', '')}}},")
    
    author_strs = " and ".join([f"{a.get('last_name', '')}, {a.get('first_name', '')}" for a in authors])
    if author_strs:
        lines.append(f"  author = {{{author_strs}}},")
    if "year" in doc_data:
        lines.append(f"  year = {{{doc_data['year']}}},")
    if "source" in doc_data:
        lines.append(f"  journal = {{{doc_data['source']}}},")
    if "pages" in doc_data:
        lines.append(f"  pages = {{{doc_data['pages']}}},")
    if "volume" in doc_data:
        lines.append(f"  volume = {{{doc_data['volume']}}},")
    
    lines.append("}")
    bib_content = "\n".join(lines) + "\n\n"
    
    bib_path = Path(out_dir) / "references.bib"
    with open(bib_path, "a", encoding="utf-8") as f:
        f.write(bib_content)
    print(f"✅ BibTeX otomatis ditambahkan ke: {bib_path}")
