"""
mendeley_setup.py
=================
Script SEKALI PAKAI untuk setup OAuth2 Mendeley API.
Jalankan ini satu kali, dan token yang dihasilkan akan disimpan ke .mendeley_token.json
di dalam folder skill global, sehingga bisa direuse untuk semua proyek.

CARA PAKAI:
1. Isi file .env di folder skill (office-cli/.env) dengan Client ID & Secret
2. Jalankan script ini: python mendeley_setup.py
3. Browser akan terbuka → login Mendeley → izinkan akses → SELESAI
"""

import os
import json
import webbrowser
import urllib.parse
import urllib.request
import urllib.error
import base64
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
ENV_FILE = SKILL_ROOT / ".env"
TOKEN_FILE = SKILL_ROOT / ".mendeley_token.json"
REDIRECT_URI = "http://localhost:12345/callback"
AUTH_URL = "https://api.mendeley.com/oauth/authorize"
TOKEN_URL = "https://api.mendeley.com/oauth/token"
SCOPE = "all"

def load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    return env

def save_token(token_data: dict):
    TOKEN_FILE.write_text(json.dumps(token_data, indent=2), encoding="utf-8")
    print(f"\n✅ Token berhasil disimpan ke: {TOKEN_FILE}")

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    auth_code = None
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            OAuthCallbackHandler.auth_code = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"<html><body style='font-family:sans-serif;text-align:center;padding:60px'><h2>&#10003; Otorisasi Berhasil!</h2><p>Anda bisa menutup tab ini dan kembali ke terminal.</p></body></html>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Error: tidak ada authorization code.")

    def log_message(self, format, *args):
        pass 

def main():
    env = load_env()
    client_id = env.get("MENDELEY_CLIENT_ID")
    client_secret = env.get("MENDELEY_CLIENT_SECRET")

    if not client_id or not client_secret:
        print("=" * 60)
        print("SETUP AWAL: Isi file .env di folder skill global terlebih dahulu!")
        print(f"File: {ENV_FILE}")
        return

    auth_params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE,
    }
    full_auth_url = AUTH_URL + "?" + urllib.parse.urlencode(auth_params)

    print("\n🌐 Membuka browser untuk otorisasi Mendeley...")
    webbrowser.open(full_auth_url)

    print("⏳ Menunggu callback OAuth2 di http://localhost:12345 ...")
    server = HTTPServer(("localhost", 12345), OAuthCallbackHandler)
    server.handle_request() 

    auth_code = OAuthCallbackHandler.auth_code
    if not auth_code:
        print("❌ Gagal mendapatkan authorization code.")
        return

    print("🔄 Menukar kode dengan access token...")
    
    # Gunakan urllib native untuk menghindari blokir Cloudflare pada library 'requests'
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
    }).encode("utf-8")
    
    req = urllib.request.Request(TOKEN_URL, data=data)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
    req.add_header("Accept", "application/json")
    
    # HTTP Basic Auth
    auth_b64 = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("ascii")
    req.add_header("Authorization", f"Basic {auth_b64}")

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            token_data = json.loads(response.read().decode("utf-8"))
            save_token(token_data)
            print("\n✅ SETUP SELESAI! Token tersimpan secara global untuk semua proyek Anda.")
    except urllib.error.HTTPError as e:
        print(f"❌ Gagal mendapatkan token. Response: {e.code}")
        print(f"   Detail Error: {e.read().decode('utf-8', errors='ignore')}")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
