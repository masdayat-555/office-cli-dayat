# PANDUAN INTEGRASI & PENGGUNAAN ZOTERO HEADLESS (API + .ENV + WORD)
## Unified Office & Document Suite (OfficeCLI + PyZotero)

> [!IMPORTANT]
> **STANDAR EMAS RISET: ZOTERO HEADLESS UNTUK AI AGENT**  
> Dokumen ini adalah panduan resmi langkah demi langkah bagi pengguna (*user/peneliti*) dan asisten AI untuk mengintegrasikan **Zotero Cloud API** secara senyap (*headless*) menggunakan pustaka `pyzotero`.  
> Pendekatan ini memungkinkan AI mengelola pustaka sitasi, menormalisasi metadata CrossRef kanonikal, mengunggah berkas lampiran PDF fisik ke Cloud, dan menyematkan **OpenXML Field Code Native Word (`ADDIN ZOTERO_ITEM`)** ke dalam dokumen `.docx` tanpa perlu membuka aplikasi Zotero Desktop GUI.

---

## 1. MENGAPA ZOTERO HEADLESS?

Dalam alur kerja penulisan karya ilmiah berbasis AI agent:
1. **Bebas Gesekan GUI (*Zero GUI Friction*):** Pengguna tidak perlu membuka software Zotero Desktop, men-drag file PDF manual, atau mencari tombol di aplikasi saat agen sedang bekerja.
2. **Integritas OpenXML Asli (*Native Word Field Codes*):** Dokumen Word yang disusun AI menghasilkan sitasi interaktif resmi Zotero, bukan sekadar teks mati. Saat dibuka di Microsoft Word, add-in Zotero langsung mengenali seluruh sitasi.
3. **Anti-Halusinasi & Anti-Nama Rusak:** Seluruh metadata disaring melalui pipeline kanonikal **CrossRef API**, memisahkan multi-penulis secara benar, dan menormalisasi kapitalisasi judul (*Title Case*).
4. **Cloud Storage Sinkron:** Berkas fisik PDF Open Access langsung terunggah ke Cloud Zotero pengguna (`attachment_simple`). Saat pengguna membuka Zotero Desktop di laptopnya dan menekan tombol *Sync*, seluruh paper dan PDF otomatis tersedia di perpustakaan lokalnya.

---

## 2. LANGKAH DEMI LANGKAH PENYIAPAN KREDENSIAL ZOTERO API (UNTUK PENGGUNA)

Untuk menghubungkan agen AI dengan akun Zotero Anda, Anda memerlukan dua kunci rahasia: **`ZOTERO_USER_ID`** dan **`ZOTERO_API_KEY`**. Ikuti 5 langkah mudah berikut:

### Langkah 1: Buat atau Masuk ke Akun Zotero
- Kunjungi portal resmi Zotero: [https://www.zotero.org/user/login](https://www.zotero.org/user/login).
- Jika belum memiliki akun, daftar gratis di [https://www.zotero.org/user/register](https://www.zotero.org/user/register).

### Langkah 2: Buka Halaman Pengaturan API Keys
- Setelah login, buka menu pengaturan kunci API:  
  👉 **[https://www.zotero.org/settings/keys](https://www.zotero.org/settings/keys)**
  *(atau klik profil Anda di pojok kanan atas $\rightarrow$ Settings $\rightarrow$ tab Feeds/API)*.

### Langkah 3: Temukan `ZOTERO_USER_ID` Anda
- Di bagian atas halaman tersebut, perhatikan teks tebal:
  ```text
  Your userID for use in API calls is 12345678
  ```
- **Salin angka 7–8 digit tersebut**. Angka inilah yang menjadi nilai variabel `ZOTERO_USER_ID`.

### Langkah 4: Buat Kunci Rahasia `ZOTERO_API_KEY` Baru
1. Pada halaman yang sama, klik tautan / tombol: **`Create new private key`**.
2. **Key Description**: Isi dengan nama bebas yang mudah diingat, misalnya:
   `OfficeCLI AI Assistant` atau `Antigravity Agent`.
3. **Atur Hak Akses (*Key Permissions*) — WAJIB BENAR:**
   - **Personal Library**: Pilih **`Allow library access`** (Read/Write).
   - Centang kotak: **`Allow write access`** (Wajib dicentang agar AI bisa membuat entri jurnal baru dan mengunggah lampiran PDF).
   - *Default Group Permissions*: Opsional (pilih Read/Write jika Anda menggunakan grup kolaborasi).
   - Centang kotak: **`Allow notes access`**.
4. Klik tombol hijau: **`Save Key`**.

### Langkah 5: Salin String Kunci API
- Zotero akan menampilkan deretan karakter string acak panjang (misalnya: `VJqN6N6gWTXEcKVEfFCNBFyH`).
- > [!CAUTION]
  > **SEGERA SALIN KUNCI INI!** Zotero hanya menampilkan kunci ini sekali saja. Jika halaman ditutup atau di-refresh sebelum disalin, Anda harus membuat kunci baru.

---

## 3. PENYIMPANAN KREDENSIAL PADA BERKAS `.env` SKILL

Kredensial disimpan secara aman di berkas `.env` lokal pada direktori root skill `office-cli`.

### 3.1 Lokasi Berkas `.env`
Sesuaikan dengan sistem operasi yang Anda gunakan:
- **Windows:**  
  `C:\Users\<Username>\.gemini\config\skills\office-cli\.env`
- **Linux / macOS:**  
  `~/.gemini/config/skills/office-cli/.env`  
  *(atau `~/.agents/skills/office-cli/.env` tergantung instalasi)*.

### 3.2 Format Isi Berkas `.env`
Buka atau buat berkas `.env` tersebut dengan text editor (Notepad, VS Code, atau nano), lalu masukkan:

```env
# ==============================================================================
# KREDENSIAL ZOTERO HEADLESS CLOUD API (OFFICE-CLI SUITE)
# Dibuat melalui: https://www.zotero.org/settings/keys
# ==============================================================================
ZOTERO_USER_ID="12345678"
ZOTERO_API_KEY="VJqN6N6gWTXEcKVEfFCNBFyH"

# Opsional: Jika Anda juga menggunakan Mendeley
# MENDELEY_CLIENT_ID="12345"
# MENDELEY_CLIENT_SECRET="secret_anda"
```

> [!NOTE]
> **JAMINAN KEAMANAN & PRIVASI:**  
> Berkas `.env` ini secara otomatis diabaikan oleh aturan `.gitignore` repositori. Kredensial Anda **TIDAK AKAN PERNAH** terunggah ke GitHub atau terekspos ke publik saat Anda menjalankan `git push`.

---

## 4. VERIFIKASI KONEKSI (HEALTH CHECK)

Setelah mengisi berkas `.env`, Anda atau agen AI dapat memverifikasi status koneksi dengan menjalankan perintah singkat berikut di terminal:

```bash
python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py
```
*(Di Windows PowerShell: `python C:\Users\<Username>\.gemini\config\skills\office-cli\scripts\zotero_headless_sync.py`)*.

**Keluaran Konsol yang Diharapkan:**
```text
[ZOTERO STATUS] User ID: [TERSEDIA] | API Key: [TERSEDIA]
```
Jika status keduanya adalah `[TERSEDIA]`, integrasi API Zotero Headless Anda sudah aktif 100% dan siap digunakan.

---

## 5. ALUR KERJA OPERASIONAL SEHARI-HARI (WORKFLOWS)

### 5.1 Alur 1: Mendaftarkan & Mengunggah 1 Paper Baru (One-Line CLI)
Jika dalam pengerjaan naskah terdapat referensi baru (misal hasil unduhan PDF di folder `referensi/rekomendasi_internasional/`), cukup jalankan perintah satu baris:

```bash
python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py \
  --upload-pdf "referensi/rekomendasi_internasional/Peffers_2007_JMIS_DSRM.pdf" \
  --doi "10.2753/MIS0742-1222240302" \
  --collection "Pengusir Tikus Pintar" \
  --keys-file "zotero_item_keys.json"
```

**Otomatisasi Latar Belakang yang Terjadi:**
1. **Pengambilan Metadata CrossRef Kanonikal:** Skrip otomatis menembak `api.crossref.org` menggunakan DOI untuk menarik judul murni, daftar penulis lengkap terpisah (*first/last name*), nama jurnal resmi, volume, nomor terbitan, rentang halaman, dan tahun.
2. **Deduplikasi Cerdas:** Memeriksa apakah DOI atau judul artikel sudah ada di koleksi Zotero Cloud pengguna. Jika sudah ada, skrip langsung menggunakan item key lama tanpa membuat entri dobel.
3. **Pembuatan Item Cloud:** Mendaftarkan artikel jurnal ke dalam koleksi spesifik di Zotero Cloud.
4. **Lampiran PDF Fisik (*Attachment Upload*):** Berkas PDF diunggah ke storage Cloud Zotero (`zot.attachment_simple`) dan dikaitkan sebagai lampiran resmi (*child attachment*) di bawah item tersebut.
5. **Pembaruan Peta Kunci Lokal:** File `zotero_item_keys.json` di proyek otomatis diperbarui:
   ```json
   {
     "Peffers et al., 2007": "ZK5HM3UW"
   }
   ```
6. **Keluaran Konsol:** Menampilkan ringkasan Item Key, Attachment Key, dan cuplikan format OpenXML Word siap pakai.

---

### 5.2 Alur 2: Sinkronisasi Massal Seluruh Paper Proyek (Bulk Sync)
Untuk inisialisasi awal proyek yang memiliki puluhan berkas referensi:

```python
import sys
import os
from pathlib import Path

# Impor engine dari direktori skill
sys.path.append(os.path.expanduser('~/.gemini/config/skills/office-cli/scripts'))
from zotero_headless_sync import sync_paper_list_to_zotero

daftar_paper = [
    {
        "cite_key": "Chen & Ran, 2019",
        "doi": "10.1109/JPROC.2019.2921977",
        "title": "Deep Learning With Edge Computing: A Review"
    },
    {
        "cite_key": "Peffers et al., 2007",
        "doi": "10.2753/MIS0742-1222240302",
        "title": "A Design Science Research Methodology for Information Systems Research"
    }
]

# Eksekusi sinkronisasi massal
peta_kunci = sync_paper_list_to_zotero(
    papers_list=daftar_paper,
    collection_name="Pengusir Tikus Pintar",
    pdf_folder="referensi"
)
```

---

### 5.3 Alur 3: Injeksi OpenXML Field Code ke Dokumen Microsoft Word (`.docx`)
Ketika AI menyusun berkas Word menggunakan `python-docx` atau manipulasi OpenXML, AI menyematkan struktur *Field Code* baku Zotero:

```xml
<w:r>
  <w:fldChar w:fldCharType="begin"/>
</w:r>
<w:r>
  <w:instrText xml:space="preserve"> ADDIN ZOTERO_ITEM CSL_CITATION {"citationID":"aRandomID","citationItems":[{"id":123,"uris":["http://zotero.org/users/local/items/ITEM_KEY"]}],"properties":{"formattedCitation":"(Peffers et al., 2007)","plainCitation":"(Peffers et al., 2007)"}} </w:instrText>
</w:r>
<w:r>
  <w:fldChar w:fldCharType="separate"/>
</w:r>
<w:r>
  <w:t>(Peffers et al., 2007)</w:t>
</w:r>
<w:r>
  <w:fldChar w:fldCharType="end"/>
</w:r>
```

**Penjelasan Komponen:**
- `ADDIN ZOTERO_ITEM`: Perintah native Word yang memberi tahu add-in Zotero bahwa teks ini adalah sebuah sitasi interaktif.
- `uris: ["http://zotero.org/users/local/items/ITEM_KEY"]`: Menghubungkan sitasi dengan ID unik item di database Zotero pengguna (misal: `ZK5HM3UW`).
- `<w:fldChar w:fldCharType="separate"/>`: Pemisah antara instruksi kode dan representasi visual teks yang dilihat pembaca.
- `<w:t>(Peffers et al., 2007)</w:t>`: Teks sitasi yang ditampilkan di naskah.

---

### 5.4 Alur 4: Pengalaman Pengguna di Microsoft Word Desktop
Setelah agen selesai membuat berkas `.docx`:
1. Pengguna membuka berkas `.docx` tersebut di laptop menggunakan Microsoft Word.
2. Ketika kursor diarahkan atau diklik pada sitasi (misal `(Peffers et al., 2007)`), blok sitasi akan tersorot abu-abu (*field code shading*). Ini menandakan dokumen terhubung resmi dengan database Zotero.
3. Pengguna dapat mengklik tab **Zotero** di pita menu Word:
   - **Edit Citation**: Pengguna dapat menambahkan nomor halaman (`p. 52`) atau menambah sitasi kedua secara interaktif.
   - **Document Preferences**: Pengguna dapat mengubah gaya sitasi dari *APA 7th Edition* ke *IEEE* atau *Nature* hanya dengan satu klik; seluruh bodynote dan daftar pustaka akan berganti otomatis.
   - **Refresh**: Memperbarui urutan nomor sitasi jika ada paragraf yang digeser.
4. **Di Aplikasi Zotero Desktop Pengguna:**  
   Pengguna cukup mengklik tombol **Sync** (ikon panah hijau melingkar di pojok kanan atas aplikasi Zotero). Seluruh item baru beserta berkas PDF fisiknya akan otomatis terunduh ke komputer pengguna!

---

## 6. PEMECAHAN MASALAH (TROUBLESHOOTING & FAQ)

| Masalah / Pesan Error | Penyebab Utama | Solusi |
| :--- | :--- | :--- |
| **`[ERROR] Kredensial Zotero belum disetel di .env!`** | Berkas `.env` belum dibuat atau path file salah. | Buat berkas `.env` di folder root skill `office-cli/.env` dan pastikan nama variabel adalah `ZOTERO_USER_ID` dan `ZOTERO_API_KEY`. |
| **`HTTP 403 Forbidden` saat upload item** | Kunci API tidak memiliki hak akses tulis (*write permission*). | Buka kembali [zotero.org/settings/keys](https://www.zotero.org/settings/keys), centang opsi **"Allow write access"** pada Personal Library, lalu simpan. |
| **`HTTP 400 Bad Request` saat upload PDF** | Berkas PDF rusak atau path berkas tidak ditemukan di disk lokal. | Pastikan path berkas PDF valid dan berkas tidak sedang terkunci oleh PDF reader lain. |
| **Penyimpanan Zotero Cloud Penuh (*Quota Exceeded*)** | Akun Zotero gratis memiliki kuota cloud 300 MB untuk lampiran PDF. | Hapus file PDF besar yang tidak terpakai di web zotero.org, atau gunakan penyimpanan WebDAV/opsi metadata-only jika kuota habis. |
| **Item dobel di koleksi Zotero** | Skrip dijalankan dua kali dengan parameter judul yang berbeda sedikit. | Skrip `zotero_headless_sync.py` sudah dilengkapi deduplikasi berbasis DOI dan Title. Hapus entri dobel melalui menu *Duplicate Items* di Zotero Desktop. |
| **Field Code di Word tidak aktif / teks biasa** | Berkas Word disusun tanpa kontainer XML `<w:fldChar>`. | Gunakan fungsi injeksi resmi `build_complete_paper.py` atau `zotero_headless_sync.py` yang membungkus sitasi dalam XML Field Code. |

---

## 7. RANGKUMAN CHEAT-SHEET PERINTAH

```bash
# 1. Cek status koneksi API
python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py

# 2. Upload 1 paper baru + PDF + DOI resmi + update mapping keys
python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py \
  --upload-pdf "path/to/paper.pdf" \
  --doi "10.xxxx/yyyy" \
  --collection "Nama Koleksi Riset" \
  --keys-file "zotero_item_keys.json"

# 3. Bantuan argumen CLI
python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py --help
```
