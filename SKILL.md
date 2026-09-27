---
name: office-cli
description: Unified Document Suite for AI Agents. Fast multi-format extraction to Markdown via Microsoft MarkItDown, and programmatic authoring/manipulation of Microsoft Office documents (Word, Excel, PowerPoint) via OfficeCLI.
---

# Unified Office & Document Suite (MarkItDown + OfficeCLI)

Skill ini merupakan ekosistem terpadu untuk penanganan dokumen digital bagi AI coding agent. Mengintegrasikan kemampuan **ekstraksi cerdas multi-format ke Markdown** menggunakan **Microsoft MarkItDown** dan **pembuatan/manipulasi dokumen Office native** menggunakan **OfficeCLI**.

---

## 0. STRATEGI PEMBAGIAN TUGAS (ARSITEKTUR KERJA)

Untuk mencegah benturan fungsional dan degradasi format file:
*   **Gunakan `markitdown` (Reading & Extraction Engine):**
    MUTLAK digunakan untuk tugas **MEMBACA CEPAT, EKSTRAKSI TEKS, TABEL, DAN METADATA** dari format biner kompleks (`.pdf`, `.docx`, `.xlsx`, `.pptx`, `.zip`, gambar/audio) menjadi teks Markdown bersih.
*   **Gunakan `officecli` (Creation & Editing Engine):**
    MUTLAK digunakan untuk tugas **MENGEDIT, MEMODIFIKASI, ATAU MEMBUAT DOKUMEN BARU** (`.docx`, `.xlsx`, `.pptx`). Mempertahankan struktur DOM OpenXML asli, nomor halaman, TOC, dan formatting visual.

---

## 1. PEMERIKSAAN KESIAPAN SISTEM & SINKRONISASI PEMBARUAN (PRE-FLIGHT CHECK)

### 1.0 Sinkronisasi Pembaruan Otomatis Bulanan (Monthly Auto-Update from GitHub)
> [!IMPORTANT]
> **Instruksi Mutlak bagi Agen AI (Untuk Seluruh Pengguna Publik):**  
> Repositori ini didistribusikan untuk publik agar setiap pengguna selalu mendapatkan perbaikan bug, pemutakhiran standar SINTA/Scopus, dan template resmi terbaru langsung dari repositori GitHub pengembang.
>
> 1. **Pemeriksaan Rutin Setiap 30 Hari (1 Bulan):**  
>    Setiap kali skill ini aktif untuk menangani tugas dokumen, agen **WAJIB** memeriksa kapan sinkronisasi terakhir dilakukan (via file `.last_update_check` di direktori skill).
> 2. **Prosedur Update Otomatis:**  
>    Jika waktu telah mencapai atau melampaui **30 hari** (atau pengguna meminta update/perbarui skill):
>    - Jalankan skrip pembaruan di direktori skill:
>      ```powershell
>      python scripts/check_update.py
>      ```
>    - Atau lakukan penarikan git secara langsung:
>      ```powershell
>      git -C "<path_ke_folder_skill>" pull origin main
>      ```
>      *(Upstream GitHub: `https://github.com/<OWNER>/<REPO>.git` — detail URL repositori resmi menyusul).*
> 3. **Non-Blocking Fallback:**  
>    Jika pengguna berada dalam kondisi offline atau remote git belum terhubung, lewati pembaruan dan jangan sampai menggagalkan pekerjaan dokumen pengguna.
> 4. **Pelaporan Singkat:** Jika terdapat file yang diperbarui (misalnya template atau resep baru), informasikan secara ringkas kepada pengguna.

Sebelum menjalankan tugas dokumen, agen juga **WAJIB** memverifikasi ketersediaan perangkat lunak pendukung di terminal:

### 1.1 Tool 1: Microsoft MarkItDown (Reading Engine)
- **Pengembang:** Microsoft Corporation (Lisensi MIT)
- **Repositori Resmi:** [GitHub - microsoft/markitdown](https://github.com/microsoft/markitdown)
- **Perintah Pengecekan:**
  ```powershell
  # Cek perintah biner langsung atau via modul python
  markitdown --version
  # Alternatif jika PATH belum terdaftar:
  python -m markitdown --version
  ```
- **Perintah Instalasi (Jika Belum Terpasang):**
  ```powershell
  pip install markitdown
  # Untuk dukungan penuh (audio STT & OCR gambar):
  pip install markitdown[all]
  ```

### 1.2 Tool 2: OfficeCLI (Manipulation Engine)
- **Pengembang:** OfficeCLI Contributors
- **Situs Resmi & Repositori:** [officecli.ai](https://officecli.ai) / [GitHub - officecli](https://github.com/officecli)
- **Perintah Pengecekan:**
  ```powershell
  officecli --version
  ```
- **Perintah Instalasi (Jika Belum Terpasang):**
  - **Windows (PowerShell Run as Admin/User):**
    ```powershell
    irm https://d.officecli.ai/install.ps1 | iex
    ```
  - **Linux / macOS (Bash):**
    ```bash
    curl -fsSL https://d.officecli.ai/install.sh | bash
    ```

> [!IMPORTANT]
> Jika salah satu atau kedua tool di atas belum terpasang di sistem pengguna, agen **WAJIB** menghentikan langkah sementara, menginformasikan status ketersediaan alat, dan menyajikan perintah instalasi di atas beserta tautan repositori resminya.

---

## 2. CARA PENGGUNAAN ALAT

### 2.1 Ekstraksi Dokumen Menggunakan MarkItDown
1. **Dilarang langsung membaca file biner:** Jangan memanggil `view_file` langsung pada file `.pdf`, `.docx`, `.xlsx`, atau `.pptx`.
2. **Jalankan Perintah Ekstraksi:**
   ```powershell
   # Ekstraksi ke file markdown sementara di scratch
   python -m markitdown "path/ke/dokumen.pdf" > "output.md"
   ```
3. **Baca Hasilnya:** Buka file Markdown hasil ekstraksi menggunakan `view_file` untuk analisis teks dan tabel.

### 2.2 Manipulasi Dokumen Menggunakan OfficeCLI
1. **Inspeksi Struktur DOM:**
   ```powershell
   officecli info "dokumen.docx"
   officecli get "dokumen.docx" --path "body/p[0]"
   ```
2. **Manipulasi Batch:** Susun berkas batch JSON yang memuat operasi atomik (`add`, `set`, `remove`) dan eksekusi:
   ```powershell
   officecli batch "dokumen.docx" --batch "batch.json"
   ```
3. **Refresh Field & Tutup Handle:**
   ```powershell
   officecli refresh "dokumen.docx"
   officecli close "dokumen.docx"
   ```

---

## 3. LESSONS LEARNED & ATURAN EMAS (ANTI-PATTERNS TO AVOID)

Patuhi aturan mutlak berikut berdasarkan evaluasi komprehensif kesalahan masa lalu:

### 3.1 Logika Dokumen & Mapping Template
1. **DILARANG MEMALSUKAN DOKUMEN FISIK KE DALAM TEKS:** Jika dokumen (seperti Daftar Hadir/Presensi, Nota) aslinya harus ditandatangani/dibubuhi cap manual, **DILARANG KERAS** mengetik ulang nama-namanya menjadi tabel teks kosong di Word! Selalu masukkan/mapping foto/scan bukti aslinya (`.jpeg`, `.png`) ke slot template. Jaga keaslian bukti fisik.
2. **DILARANG MEMBUAT LAMPIRAN/BAB BARU TANPA IZIN:** Jangan pernah menyisipkan gambar/paragraf baru di luar hirarki bab dokumen. Jika template memiliki slot gambar lama, ganti isi gambar di ID paragraf yang sama persis.
3. **AWAS ROTASI TERSEMBUNYI SAAT REPLACE GAMBAR:** Jangan gunakan `set` untuk mengganti gambar jika orientasinya bermasalah (bisa mewarisi rotasi 90 derajat template lama). Gunakan `remove` pada *run* gambar lama (`r[x]`), dan gunakan `add` (type: picture) di ID paragraf yang sama untuk posisi tegak lurus sempurna.
4. **AWAS TABRAKAN JABATAN (ROLES) AKIBAT GLOBAL REPLACE:** Jangan gunakan *Global String Replace* pada nama orang. Selalu petakan berdasarkan **JABATAN (Role)**, ubah teks nama beserta teks jabatannya secara berpasangan agar logika tidak rancu.
5. **BAHAYA ILUSI MARKDOWN (FLATTENING):** File `.md` hasil ekstraksi sering meratakan tabel/elemen sejajar (kiri-kanan) menjadi susunan vertikal (atas-bawah). Jangan mengasumsikan layout fisik semata dari markdown. Untuk lembar pengesahan tanda tangan, pertahankan struktur grid sejajar 2x2.
6. **AUTO-CORRECTION (OBLIGASI MEMPERBAIKI DIRI):** Jika pengguna mengoreksi kesalahan logika atau format, agen wajib memperbarui dokumentasi skill ini secara otomatis tanpa perlu disuruh berulang kali.
7. **KEBERSIHAN WORKSPACE (ARTIFACT ONLY):** Dilarang membuat script manipulasi sementara (`fix_xxx.py`), dump teks, atau file batch di folder proyek pengguna. Gunakan folder `scratch/` di direktori artifact. Timpa (*overwrite*) file keluaran tunggal dan hindari membuat rentetan file versi berlebihan (`Final1`, `Final2`, dst).

### 3.2 Kesalahan Teknis OfficeCLI & Python
8. **HATI-HATI SHIFTING INDEX SAAT BATCH REMOVE:** Jika menghapus beberapa *child/run* di dalam satu elemen, **WAJIB MENGHAPUS DARI INDEKS TERBESAR KE TERKECIL (MUNDUR)**, misalnya `r[4]` lalu `r[3]` lalu `r[2]`. Menghapus maju akan memicu error `Path not found`.
9. **AWAS MOJIBAKE KARENA POWERSHELL PIPING:** Dilarang menggunakan piping PowerShell (`officecli ... | Out-File`) tanpa penanganan encoding UTF-8 yang benar karena akan merusak tanda baca. Gunakan skrip Python dengan `encoding="utf-8"` untuk menjaga integritas Unicode 100%.
10. **WASPADAI FILE LOCK (IO_ERROR):** Jangan menimpa file DOCX yang sedang dibuka oleh pengguna di Microsoft Word. Selalu panggil `officecli close <path>` setelah proses selesai.
11. **MENGATASI ZOMBIE WINWORD PROCESS:** Jika muncul error `Permission denied`, periksa proses zombie di latar belakang via PowerShell: `Get-Process WINWORD | Where-Object { $_.MainWindowTitle -eq '' }` dan hentikan proses tersebut (`Stop-Process -Id <pid> -Force`) agar kunci berkas terlepas.
12. **DILARANG MEMBIARKAN SINTAKS LATEX/MARKDOWN BOCOR KE DOKUMEN WORD:**
    - Parser CommonMark pada OfficeCLI tidak mendukung matematika LaTeX (`$...$`, `$$...$$`).
    - **Solusi Mutlak:** Seluruh simbol Yunani dan operator matematika wajib ditulis dalam karakter **Unicode murni**: `$\kappa$` $\rightarrow$ `κ` (U+03BA), `$\Delta$` $\rightarrow$ `Δ` (U+0394), `$\approx$` $\rightarrow$ `≈`, `$\sum$` $\rightarrow$ `∑`, `$\times$` $\rightarrow$ `×`. Dilarang menyisakan karakter `$` di dokumen Word!
    - **Superskrip Bersih:** Gunakan run superskrip asli Word (`run.font.superscript = True`) atau karakter superskrip Unicode (`¹`, `²`, `³`, `*`). Dilarang meninggalkan tag `^{...}`.
    - **Metadata Mandiri:** Judul, Penulis, Afiliasi, dan Email wajib menjadi paragraf-paragraf mandiri terpisah rata tengah (anti-collapsing).

---

## 4. STANDAR PENULISAN KARYA ILMIAH & DOKUMEN RESMI

### 4.0 Kewajiban Deliverable File Akhir (.DOCX)
Ketika pengguna meminta penulisan karya ilmiah, tugas akhir, atau artikel jurnal, **OUTPUT UTAMA YANG WAJIB DIBERIKAN ADALAH FILE WORD BERFORMAT `.DOCX` MENGGUNAKAN `officecli` / `python-docx`**. Agen DILARANG KERAS hanya berhenti pada file Markdown (`.md`)!

### 4.1 Spesifikasi Tata Letak & Tipografi Baku
1. **Batas Tepi (Margin):**
   - Artikel Jurnal SINTA / Scopus: Normal simetris **2,54 cm (1 inci)** di seluruh sisi (Top, Bottom, Left, Right).
   - Skripsi / Tesis Standar Indonesia: Format **4-4-3-3 cm** (Left 4 cm ruang jilid, Top 4 cm, Bottom 3 cm, Right 3 cm).
2. **Font & Spasi:**
   - Teks Utama: *Times New Roman* 11–12 pt, spasi 1.15x (Jurnal) atau 1.5x (Skripsi), perataan *Justified*, indentasi alinea 1,27 cm.
   - Spasi Tunggal (1.0x): Khusus untuk Abstrak, isi sel tabel, judul tabel/gambar, dan Daftar Pustaka.
3. **Abstrak Ilmiah & Aturan Mutlak Halaman Pertama (*Page 1 Fit*):**
   - Format: 1 paragraf padat (150–200 kata), memuat formula IMRaD mini (Masalah, Metode, Hasil Kuantitatif Riil dengan Angka Metrik, dan Kesimpulan).
   - Wajib mencantumkan 3–6 Kata Kunci (*Keywords*). Bebas sitasi dan bebas sintaks LaTeX.
   - **Aturan Mutlak Halaman Pertama (*Page 1 Fit*):** Seluruh elemen *front matter* (Judul bilingual, Penulis, Afiliasi, Email, Abstrak Indonesia, Kata Kunci, Abstract Inggris, dan Keywords) **WAJIB TUNTAS SEPENUHNYA DI HALAMAN 1**. Dilarang membiarkan teks abstrak terpotong ke Halaman 2.
4. **Perbedaan Mendasar Struktur Artikel Jurnal vs. Skripsi:**
   - **Artikel Jurnal (SINTA & Scopus):** Menggunakan angka Arab kapital (`1. PENDAHULUAN`, `2. METODE PENELITIAN`, `3. HASIL DAN PEMBAHASAN`, `4. KESIMPULAN`). **DILARANG MENGGUNAKAN KATA 'BAB'**. Alur naskah mengalir kontinu (*Continuous Flow*) **tanpa Page Break antar-seksi**.
   - **Skripsi / Tesis:** **WAJIB MENGGUNAKAN KATA 'BAB'** (`BAB I PENDAHULUAN`, `BAB II TINJAUAN PUSTAKA`, dst.), dan setiap bab baru **MUTLAK MENGGUNAKAN PAGE BREAK** (`pageBreakBefore: true`).

### 4.2 Format Elemen Khusus
1. **Tabel Format APA:** Wajib menggunakan **3 garis horizontal tebal** (garis atas tabel, garis pemisah header, dan garis penutup bawah) dan **DILARANG menggunakan garis vertikal**. Judul diletakkan di **ATAS TABEL**.
2. **Gambar:** Judul diletakkan di **BAWAH GAMBAR**, rata tengah, resolusi minimal 300 DPI.
3. **Daftar Pustaka APA 7th Edition:**
   - Diurutkan secara alfabetis (A–Z), menggunakan paragraf gantung (*hanging indent* 1,27 cm), spasi tunggal, dan wajib memuat tautan DOI aktif (`https://doi.org/...`).
   - Minimal 80% berasal dari jurnal bereputasi 5–10 tahun terakhir.

---

## 5. MANAJEMEN PRIVASI DATA PENULIS & ADAPTASI PEDOMAN KAMPUS

### 5.1 Privasi Data Pribadi Penulis (Author Privacy Guidelines)
- **Aturan Mutlak:** File skill ini ditujukan untuk dapat dipublikasikan secara umum (open-source / GitHub). Oleh karena itu, **DILARANG KERAS MENYIMPAN INFORMASI PRIBADI (PII - Personally Identifiable Information)** seperti nama lengkap pengguna, nomor kontak, NIK/NIM, atau alamat surel pribadi secara *hardcoded* di dalam berkas skill.
- **Injeksi Data Dinamis:** Identitas penulis, afiliasi lembaga, dan email korespondensi wajib diambil secara dinamis dari konteks proyek yang sedang dikerjakan pengguna atau dari draf naskah lokal di workspace aktif.

### 5.2 Prinsip Adaptif Pedoman Kampus
Jika pengguna menyertakan pedoman khusus dari institusinya (misalnya format margin, jenis font, atau gaya sitasi kampus tertentu), **ATURAN KAMPUS PENGGUNA 100% MENGALAHKAN ATURAN STANDAR NASIONAL**. Agen wajib langsung menyesuaikan parameter dokumen dengan preferensi tersebut.

---

## 6. DOKUMEN REFERENSI SPESIFIK

Saat menangani penyusunan dokumen mendalam, agen dapat berkonsultasi pada dokumen referensi di folder `references/`:
- [Pedoman Jurnal SINTA Lengkap (SINTA 1-6)](references/pedoman_jurnal_sinta.md): Standar resmi naskah jurnal nasional terakreditasi SINTA (IMRaD baku, Page 1 Fit, Byline, Tabel APA, tanpa kata BAB).
- [Pedoman Jurnal Internasional Scopus (Q1-Q4)](references/pedoman_jurnal_scopus.md): Panduan penulisan jurnal bereputasi global Scopus/WoS, sistem kuartil Q1-Q4, extended IMRaD, pengujian statistik, etika data, dan jalur peningkatan (*upgrading pathway*) dari SINTA ke Scopus.
- [Pedoman Skripsi Lengkap](references/pedoman_skripsi_lengkap.md): Anatomi lengkap Skripsi/Tesis dari Bab I sampai Bab V, preliminary pages, hingga lampiran.
- [Resep Teknis OfficeCLI Dokumen Ilmiah](references/resep_officecli_dokumen_ilmiah.md): Kumpulan batch JSON siap pakai untuk pembuatan margin, style heading 1-3, TOC otomatis, tabel APA, gambar, hanging indent, dan refresh.
- [Aturan Adaptif Pedoman Kampus](references/aturan_adaptif_pedoman_kampus.md): Panduan penyesuaian dinamis terhadap variasi aturan kampus dan penulisan.

---

## 7. TEMPLATE DOKUMEN ILMIAH RESMI SIAP PAKAI (REUSABLE TEMPLATES)

Untuk memastikan konsistensi tata letak tanpa mengotori workspace aktif pengguna:
- **Lokasi Master Template Jurnal SINTA:**  
  `templates/template_jurnal_sinta.docx` (relatif terhadap direktori root skill)
- **Karakteristik Master Template:**
  1. Format resmi Jurnal OJS SINTA (A4, Margin Normal Simetris 2,54 cm / 1 Inci).
  2. Garansi *Page 1 Fit* untuk judul dwibahasa, afiliasi, email, dan abstrak bilingual (Indonesia & Inggris).
  3. Alur IMRaD kontinu tanpa jeda halaman (*no page break*).
  4. Contoh tabel format APA 3 garis horizontal.
  5. 100% bebas mojibake dan bebas dari elemen ekonomi non-relevan (seperti kode JEL).
