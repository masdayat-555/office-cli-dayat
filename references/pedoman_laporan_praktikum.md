# PEDOMAN PENULISAN LAPORAN PRAKTIKUM

> [!CAUTION]
> ### ⚠️ ATURAN KHUSUS PRAKTIKUM METODE NUMERIK (UNIVERSITAS JANABADRA)
> **JANGAN GUNAKAN FORMAT LAPORAN UMUM DENGAN STRUKTUR BAB UNTUK TUGAS RUTIN METODE NUMERIK!**
> Pada Praktikum Metode Numerik, terdapat 2 jenis dokumen dengan alur wajib:
> 
> 1. **LHP (Laporan Hasil Praktikum) $
ightarrow$ DIKERJAKAN DULUAN (RUTIN PER MODUL)**:
>    - Format: **LHP Singkat** menggunakan master template `templates/template_lhp_singkat.docx`.
>    - **DILARANG PAKAI BAB** (Tanpa BAB I, Tanpa BAB II, Tanpa BAB III, Tanpa BAB IV, Tanpa BAB V).
>    - **DILARANG PAKAI KATA PENGANTAR & DAFTAR ISI (TOC)**.
>    - Struktur: **Hanya Cover Page resmi**, lalu halaman berikutnya **LANGSUNG JUDUL `TUGAS LHP`** berisi langkah percobaan, sintaks, output raw console, visualisasi grafik, dan penyelesaian tugas modul.
>    - Penamaan File: `[NIM]_[Nama Lengkap]_LHP[Nomor Modul].docx` (misal: `24330030_Salim Hidayat_LHP2.docx`).
> 
> 2. **LKM (Laporan Keseluruhan Modul) $
ightarrow$ DIKERJAKAN BELAKANGAN (AKHIR SEMESTER)**:
>    - Format: Laporan monograf komprehensif menggunakan master template `templates/template_lkm_metode_numerik.docx`.
>    - **WAJIB STRUKTUR LENGKAP**: Cover LKM, Kata Pengantar, Daftar Isi (TOC native Word), BAB I Pendahuluan, BAB II Tinjauan Pustaka, BAB III Pelaksanaan Praktikum, BAB IV Tugas Praktikum, BAB V Penutup, Daftar Pustaka.

Pedoman ini **wajib ditaati secara mutlak** oleh Agen AI saat menyusun, merevisi, atau memformat dokumen Laporan Praktikum. Laporan Praktikum memiliki tingkat keformalan (formality) yang kaku dan berbeda dari tugas harian biasa.

## 1. ATURAN HALAMAN SAMPUL (COVER)
- **Posisi Judul**: Judul utama ("LAPORAN PRAKTIKUM I", dst.) WAJIB berada di baris paling atas tanpa paragraf kosong sebelumnya.
- **Gambar Logo**: Harus berada di tengah halaman. Lebar standar sekitar 5.5 cm.
- **Blok Identitas Bawah**: ("FAKULTAS TEKNIK", "UNIVERSITAS JANABADRA", "2026") WAJIB mentok sampai mencium batas margin bawah (bottom margin flush).
- **Metode Spacing Cover**: Dilarang keras menggunakan point spacing raksasa (`space_before=150pt`). **Wajib menggunakan Enter/Paragraf kosong biasa** untuk mendorong blok bawah hingga mentok, atau meredistribusi ruang agar luwes.

## 2. ATURAN DAFTAR ISI (TOC)
- **Haram Mengetik Manual**: Dilarang menyusun teks "Daftar Isi" secara manual dengan ketikan titik-titik dan tebakan nomor halaman.
- **Wajib Native Word**: Harus diinjeksi menggunakan `officecli batch` dengan perintah `{"type": "toc"}`.
- **Siklus Wajib**: Modifikasi TOC via `officecli` harus mengikuti siklus: `batch` -> **`save`** -> `refresh` -> `close`. Tanpa `save`, Daftar Isi akan lenyap/rusak saat direfresh.

## 3. ATURAN STRUKTUR BAB & PAGE BREAK
- **Pemisahan Halaman**: Setiap pergantian BAB (misal dari BAB I ke BAB II) **WAJIB** berada di halaman baru.
- **Metode Break**: Gunakan perintah *Page Break* (`Ctrl+Enter` atau `WD_BREAK.PAGE` langsung di `runs[-1]`) atau pastikan heading BAB diset dengan properti *Page break before*. Jangan biarkan BAB menyangkut di tengah atau akhir halaman sebelumnya.

## 4. ATURAN SUMBER KONTEN (ANTI-YAPPING)
- **Dasar Teori Mengikat**: Jangan menggunakan narasi *AI slop* (penjelasan generik AI). Dasar Teori **mutlak harus diekstrak dan diparafrase langsung dari modul/dokumen referensi resmi** (misalnya PDF modul dari dosen).
- **Visualisasi Gambar**: Jika ada gambar tugas, cukup letakkan gambar dan berikan *caption* miring di bawahnya. Jangan buat tabel narasi panjang berulang jika instruksi tidak meminta.

## 5. PENDEKATAN TEKNIS GENERASI
Alih-alih menyusun dari nol menggunakan `python-docx` yang rawan cacat margin, **AGEN SANGAT DISARANKAN** untuk menyalin dari Master Template:
- Untuk LHP Singkat / Tugas Per Modul: `templates/template_lhp_singkat.docx`
- Untuk Laporan Praktikum Umum: `templates/template_laporan_praktikum.docx`
- Untuk LKM (Laporan Keseluruhan Modul) Metode Numerik: `templates/template_lkm_metode_numerik.docx`
lalu memutasinya menggunakan `officecli batch` (mengganti judul modul, menyisipkan paragraf teks, memasukkan gambar) untuk menjaga integritas format margin dan properti *Page Break*.

---

## 6. STANDAR MUTLAK PRAKTIKUM METODE NUMERIK: LHP VS LKM

> [!IMPORTANT]
> **ATURAN HIRARKI PENGERJAAN: LHP DULUAN, LKM BELAKANGAN!**
> Pada mata kuliah Praktikum Metode Numerik (Fakultas Teknik - Prodi Informatika Universitas Janabadra), terdapat pembedaan mutlak antara **LHP** dan **LKM**:

### 6.1 LHP (Laporan Hasil Praktikum) — FORMAT SINGKAT (HANYA BAGIAN PRAKTEK)
- **Karakteristik**: LHP adalah laporan pengerjaan rutin per modul (Modul 1, Modul 2, dst.) yang dikerjakan langsung setelah sesi praktikum lab.
- **Waktu Pengerjaan**: **DULUAN** (dikerjakan segera setelah praktikum lab modul tersebut).
- **Master Template Wajib**: `templates/template_lhp_singkat.docx`.
- **ATURAN MUTLAK PENGERJAAN SCILAB (DILARANG JALANKAN CLI SCILAB SENDIRI)**:
  - **Scilab adalah praktikum langsung yang wajib dijalankan oleh mahasiswa sendiri di lab.**
  - **Agen DILARANG menjalankan perintah/CLI Scilab secara otomatis di background/terminal.**
  - **Agen WAJIB menyediakan kode perintah Scilab dalam bentuk blok teks salin (code box / copyable block) yang rapi di respon chat dan laporan Markdown, agar mahasiswa dapat menyalin dan menjalankannya sendiri di Scilab Command Window mereka.**
- **ATURAN MUTLAK KONTEN LHP (HANYA BAGIAN 'PRAKTEK', BUKAN SEMUANYA)**:
  - **HANYA KERJAKAN SOAL-SOAL BAGIAN 'PRAKTEK'** (contoh di Modul 2: Praktek 1 di hal 3, dan Praktek 2 di hal 7). Inilah yang menjadi tugas resmi LHP!
  - **DILARANG MEMASUKKAN LANGKAH PRAKTIKUM / PERCOBAAN**: Seluruh langkah percobaan dasar di Scilab (misal bagian 1 pembentukan, 2 pengalamatan, 3 matematika array, 4 matriks/SPL, 5 ukuran array, 6 grafik) adalah praktikum mandiri yang dilakukan oleh mahasiswa di lab, BUKAN tugas LHP!
  - **DILARANG MEMASUKKAN 'TUGAS PRAKTIKUM' (Halaman 8)**: Bagian 'Tugas Praktikum' di akhir modul BELUM TERMASUK di LHP! Itu disimpan dan baru dimasukkan ke LKM nanti jika sudah dikerjakan dan diminta oleh mahasiswa!
  - **DILARANG PAKAI BAB** (Tanpa BAB I, Tanpa BAB II, Tanpa BAB III, Tanpa BAB IV, Tanpa BAB V).
  - **DILARANG PAKAI KATA PENGANTAR & DAFTAR ISI (TOC)**.
- **Struktur Dokumen LHP**:
  1. **Halaman Sampul (Cover Page)**:
     - Judul: `LAPORAN HASIL PRAKTIKUM`
     - Mata Kuliah: `METODE NUMERIK`
     - Modul: `MODUL [X]: [JUDUL MODUL]` (Contoh: `MODUL II: ARRAY DAN MATRIKS`)
     - Logo: Logo Universitas Janabadra resmi (posisi tengah)
     - Identitas Penyusun: `Disusun Oleh :` diikuti baris `Salim Hidayat` dan `24330030`
     - Footer Institusi: `FAKULTAS TEKNIK`, `PROGRAM STUDI INFORMATIKA`, `UNIVERSITAS JANABADRA`, `YOGYAKARTA`, `2026`.
  2. **Halaman Isi (Langsung Tugas LHP)**:
     - Judul Isi: **TUGAS LHP** (Centered, Bold, Page Break).
     - **Praktek 1**: Soal-soal Praktek 1 beserta sintaks perintah Scilab, output console, dan penjelasan.
     - **Praktek 2**: Kasus visualisasi grafik perbandingan data (misal: grafik perbandingan suhu dua kota di hal 7) beserta kode plot Scilab, screenshot grafik asli, dan analisis datanya.
- **Konvensi Penamaan Berkas LHP**:
  - Format Wajib: `[NIM]_[Nama Lengkap]_LHP[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LHP2.docx`).
  - Setelah final, dikonversi ke PDF dengan nama sama: `24330030_Salim Hidayat_LHP2.pdf`.

### 6.2 LKM (Laporan Keseluruhan Modul) — FORMAT LENGKAP (SETELAH SEMUA TUGAS SELESAI)
- **Karakteristik**: LKM adalah laporan gabungan/kompilasi monograf dari seluruh modul praktikum.
- **Waktu Pengerjaan**: **BELAKANGAN** (disusun **SETELAH SELURUH TUGAS PRAKTIKUM SELESAI SEMUA DIKERJAKAN**!).
- **Master Template Wajib**: `templates/template_lkm_metode_numerik.docx`.
- **Peran Bagian 'TUGAS PRAKTIKUM' di LKM**:
  - Di LKM inilah seluruh soal dari bagian **'TUGAS PRAKTIKUM'** resmi dimasukkan, dihitung manual, dibuktikan secara aljabar linier, dan dibahas secara komprehensif pada **BAB IV TUGAS PRAKTIKUM**.
- **Struktur Dokumen LKM**:
  - Halaman Sampul: `LAPORAN KESELURUHAN MODUL METODE NUMERIK`
  - KATA PENGANTAR
  - DAFTAR ISI (Native TOC Word)
  - BAB I PENDAHULUAN
  - BAB II TINJAUAN PUSTAKA (Teori Lengkap)
  - BAB III PELAKSANAAN PRAKTIKUM (Langkah & Praktek seluruh modul)
  - BAB IV TUGAS PRAKTIKUM (Pembahasan lengkap seluruh Tugas Praktikum)
  - BAB V PENUTUP (Kesimpulan & Saran)
  - DAFTAR PUSTAKA

### 6.3 TOOLCHAIN LIBRARY PYTHON TERPAKAI (DILARANG DIBUANG)
Seluruh library Python berikut telah terpasang, terverifikasi, dan **WAJIB DIPERTAHANKAN** dalam ekosistem skill untuk mendukung automasi dokumen praktikum:
1. **PyMuPDF (`pymupdf`)**:
   - Pustaka utama untuk rendering visual halaman PDF beresolusi tinggi (DPI 150-300).
   - Ekstraksi aset media gambar biner dari PDF tanpa degradasi.
   - Pembacaan teks dan layout tabel PDF secara presisi.
2. **Microsoft MarkItDown (`markitdown` / `python -m markitdown`)**:
   - Pustaka resmi pembacaan cepat berkas non-plaintext (PDF, DOCX, XLSX, PPTX) ke Markdown terstruktur.
3. **OfficeCLI (`officecli`)**:
   - Engine mutasi struktur Word OpenXML berbasis batch JSON tanpa merusak template atau field codes.
4. **docx2pdf (`docx2pdf`)**:
   - Utilitas konversi final berkas `.docx` ke format `.pdf` secara otomatis memanfaatkan Microsoft Word headless, siap diserahkan ke sistem LMS kampus.

---

### 🚀 Opsi "Bulldozer Mode" (Mass-Download Otomatis)

Jika Anda memiliki daftar referensi yang panjang dan ingin mencari ketersediaannya secara massal tanpa mengunduh manual satu per satu, Anda bisa memerintahkan agen: **"Aktifkan Bulldozer Mode"**.
Dalam mode ini, agen AI akan:
1. Mengerahkan segala cara (API OpenAlex, CrossRef, dll) untuk menemukan dan mengunduh PDF Open-Access.
2. Memasukkan referensi tersebut secara otomatis ke Mendeley.
3. **Integritas Akademik:** Jika PDF terkunci *paywall* atau tidak ditemukan, agen akan **Jujur Melapor Gagal** dan tidak akan memasukkannya ke Mendeley. Mengutip dokumen tanpa pernah membaca fisiknya adalah pelanggaran akademik.

### 🕵️‍♂️ Otoritas "Visual Browser Agent" (Bypass Blokir API)

Jika *Bulldozer Mode* gagal menembus keamanan repositori (*bot detection* / blokir API) namun Anda yakin PDF tersebut gratis di internet, agen memiliki **otoritas** untuk membangkitkan sub-agen visual. Sub-agen ini akan mengendalikan browser Google Chrome asli Anda untuk mencari dan "menyelamatkan" link PDF rahasia tersebut layaknya penelusuran manusia, lalu menyuntikkannya ke Mendeley Anda secara legal. Perintahkan saja: **"Gunakan browser agent untuk cari PDF ini."**
