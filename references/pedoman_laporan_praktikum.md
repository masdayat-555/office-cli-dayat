# PEDOMAN PENULISAN LAPORAN PRAKTIKUM

> [!CAUTION]
> ### ⚠️ ATURAN KHUSUS PRAKTIKUM METODE NUMERIK (UNIVERSITAS JANABADRA)
> **JANGAN GUNAKAN FORMAT LAPORAN UMUM DENGAN STRUKTUR BAB UNTUK TUGAS RUTIN METODE NUMERIK!**
> Pada Praktikum Metode Numerik, terdapat 2 jenis dokumen dengan alur wajib:
> 
> 1. **LHP (Laporan Hasil Praktikum) -> DIKERJAKAN DULUAN (RUTIN PER MODUL)**:
>    - Format: **LHP Singkat** menggunakan master template `templates/template_lhp_singkat.docx`.
>    - **DILARANG PAKAI BAB** (Tanpa BAB I, Tanpa BAB II, Tanpa BAB III, Tanpa BAB IV, Tanpa BAB V).
>    - **DILARANG PAKAI KATA PENGANTAR & DAFTAR ISI (TOC)**.
>    - Struktur: **Hanya Cover Page resmi**, lalu halaman berikutnya **LANGSUNG JUDUL `TUGAS LHP`** berisi langkah percobaan, sintaks, output raw console, visualisasi grafik, dan penyelesaian tugas modul.
>    - Penamaan File: `[NIM]_[Nama Lengkap]_LHP[Nomor Modul].docx` (misal: `24330030_Salim Hidayat_LHP2.docx`).
> 
> 2. **LKM (Laporan Keseluruhan Modul) -> DIKERJAKAN BELAKANGAN (AKHIR SEMESTER)**:
>    - Format: Laporan monograf komprehensif menggunakan master template `templates/template_lkm_metode_numerik.docx`.
>    - **WAJIB STRUKTUR LENGKAP**: Cover LKM, Kata Pengantar, Daftar Isi (TOC native Word), BAB I Pendahuluan, BAB II Tinjauan Pustaka, BAB III Pelaksanaan Praktikum, BAB IV Tugas Praktikum, BAB V Penutup, Daftar Pustaka.
>    - **DILARANG MERUSAK ATAU MENDOWNGRADE LKM MENJADI LHP**: Jika pengguna meminta pengerjaan, perbaikan, atau revisi pada dokumen LKM (Laporan Keseluruhan Modul), agen **DILARANG KERAS** mengubah formatnya menjadi LHP, dilarang membuang struktur bab, dan dilarang menghapus Kata Pengantar atau Daftar Isi! Revisi harus tetap mempertahankan integritas dokumen LKM utuh.

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
  - Berkas diserahkan dalam format DOCX. Konversi ke PDF **HANYA** dilakukan bila diminta secara eksplisit oleh mahasiswa.

### 6.2 LKM (Laporan Keseluruhan Modul) — FORMAT LENGKAP (SETELAH SEMUA TUGAS SELESAI)
- **Karakteristik**: LKM adalah laporan gabungan/kompilasi monograf dari seluruh modul praktikum.
- **Waktu Pengerjaan**: **BELAKANGAN** (disusun **SETELAH SELURUH TUGAS PRAKTIKUM SELESAI SEMUA DIKERJAKAN**!).
- **Master Template Wajib**: `templates/template_lkm_metode_numerik.docx`.
- **KONTEN WAJIB PER BAB DI LKM**:
  1. **Cover Page**: Judul LAPORAN KESELURUHAN MODUL, nama, NIM, fakultas, universitas.
  2. **KATA PENGANTAR**: Format monograf rapi dengan first-line indent 1 cm dan blok tanda tangan di kanan bawah (DILARANG newline dalam paragraf justified).
  3. **DAFTAR ISI (WAJIB DAFTAR ISI OTOMATIS ASLI WORD DARI PILIHAN TERSEDIA / AUTOMATIC TABLE 1)**:
     - **DILARANG KERAS** membuat Daftar Isi manual (ketikan teks tab statis `title \t page`) atau menyuntikkan field mentah tanpa kontainer SDT.
     - **Wajib menggunakan Building Block resmi bawaan Word "Automatic Table 1" (Tabel Otomatis 1)** yang terbungkus dalam Structured Document Tag (`<w:sdt>`) galeri Table of Contents. Saat dokumen dibuka dan diklik di Word, muncul tab interaktif resmi Word: `[ Table of Contents v | Update Table... ]`.
     - **DILARANG MENYUNTIKKAN `<w:updateFields w:val="true"/>`**: Tag XML ini memicu pop-up dialog peringatan keamanan Word: *"This document contains fields that may refer to other files. Do you want to update the fields in this document?"*.
     - **Pre-render Nomor Halaman via Word COM / OfficeCLI**: Nomor halaman riil dihitung dan diisi secara otomatis sebelum berkas disimpan. Saat pengguna membuka dokumen di Word, Daftar Isi langsung terisi nomor halaman nyata secara instan, berfungsi normal seperti dokumen Word buatan tangan, dan **BEBAS DARI POP-UP PERINGATAN SAMA SEKALI**.
     - Setiap judul bab (`Heading 1`) dan sub-bab (`Heading 2` / `Heading 3`) ditautkan dengan bookmark (`_Toc...`) atau style heading Word standar sehingga tombol "Update Table" bekerja sempurna.
  4. **BAB I PENDAHULUAN**: Latar Belakang dan Tujuan Praktikum.
  5. **BAB II TINJAUAN PUSTAKA**: Landasan teori lengkap dari modul.
  6. **BAB III PELAKSANAAN PRAKTIKUM (WAJIB COPAS UTUH DARI LHP, DILARANG BIKIN FORMAT BARU)**:
     - Bab ini **MUTLAK MENGAMBIL SELURUH PENYELESAIAN DARI TUGAS LHP** (Praktek 1 s.d. selesai) secara utuh (**COPAS PERSIS** dari naskah LHP yang telah diselesaikan mahasiswa).
     - **DILARANG KERAS MEMBUAT FORMAT BARU**: Dilarang merangkum ulang, dilarang mendesain ulang urutan, dilarang membuat heading baru yang berbeda dari LHP, dan dilarang membuat format acak-acakan baru yang merusak kerapian dokumen!
     - Seluruh tangkapan layar (*screenshot*) konsol laboratorium, cuplikan kode Scilab, kurva grafik visual, serta analisis dan komentarnya dari LHP disalin apa adanya persis sesuai struktur aslinya.
     - **DILARANG MENDUPLIKASI KODE JIKA SUDAH ADA SCREENSHOT**: Jangan membuat box kode teks tambahan di atas atau di bawah gambar jika *screenshot* konsol Scilab sudah ditampilkan. Cukup tampilkan *screenshot* asli dan penjelasannya ("kan udah ada screenshot-an").
     - DILARANG hanya meringkas singkat atau mengosongkan Bab ini!
  7. **BAB IV TUGAS PRAKTIKUM (POLA PENGERJAAN MAHASISWA LOGIS: SOAL -> KODE & OUTPUT KONSOL LANGSUNG -> KOMENTAR DI BAWAHNYA)**:
     - Di LKM inilah seluruh soal dari bagian **'TUGAS PRAKTIKUM'** (halaman akhir modul) resmi dijawab secara lugas, logis, dan tervalidasi.
     - **ALUR WAJIB TIAP NOMOR SOAL/TUGAS (POLA MAHASISWA / HUMAN STUDENT WORKFLOW)**:
       1. **Soal & Matriks/Persoalan**: Sajikan soal dan bentuk matematisnya (persamaan matriks 2D native) dengan jelas.
       2. **Sintaks Perintah & Output Konsol Scilab Langsung Menyatu**: Jawab langsung persoalan menggunakan satu kotak konsol Scilab literal (`--> perintah` diikuti nilai outputnya langsung di bawahnya, persis seperti tampilan command window Scilab mahasiswa). Mahasiswa menjawab soal komputasi langsung dengan kode dan outputnya di situ!
       3. **Komentar dan Penjelasan di Bawahnya**: Penjelasan logis dan matematis diletakkan di bawah kotak kode/output: verifikasi perhitungan aljabar linier manual baris demi baris, penjelasan operator yang dipakai (`*` aljabar linier murni vs `.*` per-elemen), dan sifat/karakteristik matriks (seperti nonsingularitas det != 0 dan jaminan solusi unik SPL).
     - **DILARANG YAPPING / MELEBAR DI AWAL**: Dilarang keras menulis esai teoritis panjang lebar atau analisis bertele-tele sebelum kode/output ditampilkan. Mahasiswa menjawab soal secara langsung (*to the point*), bukan berfilsafat di awal!
     - **DILARANG SUBBAB PEMBAHASAN TERPISAH (SUBBAB 4.3 HARAM)**: Dilarang memecah pembahasan ke dalam subbab terpisah seperti "4.3 Pembahasan dan Analisis Komputasi Numerik" yang mengulang-ulang narasi. Pembahasan dan analisis mutlak melekat langsung sebagai komentar di bawah masing-masing nomor tugas (4.1 dan 4.2).
     - **PERSAMAAN MATRIKS NATIVE 2D WORD (OMML XML)**: Seluruh matriks dan determinan wajib dirender sebagai persamaan matematika 2D native Word (kurung siku `[]` untuk matriks A, B, C dan garis vertikal `||` untuk determinan J). Dilarang menulis matriks dalam bentuk teks flat satu baris.
     - Soal, persamaan matriks, dan perhitungan aljabar linier **WAJIB RATA KIRI (`align=LEFT`)**, dilarang di-justify agar tidak terjadi peregangan spasi rusak (*stretched justify*).
     - **DILARANG ELEMEN VISUAL GIMMICK (GARIS BIRU / WEB CALLOUT)**: Dilarang keras menggunakan border tabel berwarna biru (`#0969DA`), aksen garis tepi warna-warni, atau gaya *callout* web pada naskah ilmiah, LKM, atau LHP. Seluruh dokumen menggunakan format teks hitam standar tanpa kotak berwarna aneh.
  8. **BAB V PENUTUP**: Kesimpulan menyeluruh dan Saran.
  9. **DAFTAR PUSTAKA**: Referensi baku buku dan manual ilmiah.

### 6.3 TOOLCHAIN LIBRARY PYTHON TERPAKAI (DILARANG DIBUANG)
Seluruh library Python berikut telah terpasang, terverifikasi, dan **WAJIB DIPERTAHANKAN** dalam ekosistem skill untuk mendukung automasi dokumen praktikum:
1. **PyMuPDF (`pymupdf`)**:
   - Pustaka utama untuk rendering visual halaman PDF beresolusi tinggi (WAJIB minimal 300 DPI, dilarang 72/96 DPI).
   - Ekstraksi aset media gambar biner dari PDF tanpa degradasi.
   - Pembacaan teks dan layout tabel PDF secara presisi.
2. **Microsoft MarkItDown (`markitdown` / `python -m markitdown`)**:
   - Pustaka resmi pembacaan cepat berkas non-plaintext (PDF, DOCX, XLSX, PPTX) ke Markdown terstruktur.
3. **OfficeCLI (`officecli`)**:
   - Engine mutasi struktur Word OpenXML berbasis batch JSON tanpa merusak template atau field codes.
4. **docx2pdf (`docx2pdf`)**:
   - Utilitas konversi akhir berkas `.docx` ke format `.pdf` (DILARANG dijalankan otomatis; HANYA dijalankan bila diminta secara eksplisit oleh mahasiswa).

### 6.4 PROTOKOL ANTI-BURIK & PRESERVASI RESOLUSI CITRA (HIGH FIDELITY)
Agar dokumen Word dan hasil cetak/ekspor PDF tidak mengalami penurunan resolusi (burik, pecah, atau buram):
1. **Injeksi Pengaturan Anti-Kompresi ke OpenXML (`word/settings.xml`)**:
   Setiap template master dan dokumen `.docx` wajib disematkan tag:
   `<w14:defaultImageDpi w14:val="0"/>` dan `<w:doNotCompressPNG/>`. Nilai `0` mengunci Word pada mode **High Fidelity** sehingga gambar tidak di-downsample otomatis saat dokumen disimpan.
2. **Ekstraksi Aset & Screenshot Minimal 300 DPI**:
   - Saat mengekstrak cuplikan halaman PDF modul atau merender grafik Scilab, selalu gunakan PyMuPDF pada DPI 300 (`page.get_pixmap(dpi=300)`).
   - Seluruh gambar wajib disimpan dalam format **PNG lossless**.
   - Tambahkan metadata resolusi 300 DPI sebelum disisipkan ke Word: `img.save(path, dpi=(300, 300))`.
3. **Penyesuaian Skala Fisik Gambar**:
   - Dilarang meregangkan gambar beresolusi kecil (< 800 piksel) hingga selebar margin kertas (15–16 cm). Letakkan secara proporsional di tengah halaman (*Center*) dengan lebar 6–9 cm.
4. **Instruksi Ekspor PDF di Word GUI bagi Mahasiswa**:
   - Saat mahasiswa menyimpan dokumen Word ke PDF di Microsoft Word:
     - Klik **File > Save As > PDF**.
     - Pastikan memilih opsi **"Standard (publishing online and printing)"** (JANGAN pilih *"Minimum size"*!).
     - Buka menu **File > Options > Advanced > Image Size and Quality**, centang **"Do not compress images in file"** dan set **Default resolution** ke **High fidelity**.

### 6.5 KEBIJAKAN OUTPUT DOKUMEN: DOCX UTAMA, PDF ON-DEMAND
- Agen AI **DILARANG** membuat atau mengonversi berkas PDF secara otomatis pada setiap pengerjaan laporan.
- Mahasiswa membutuhkan berkas DOCX mentah untuk meninjau, mengedit narasi, dan menimpa tangkapan layar langsung dari komputer lab.
- Berkas PDF hanya diproduksi jika mahasiswa memberikan instruksi tegas: *"buatkan pdf-nya"*, *"convert ke pdf"*, dsb.

---

### 🚀 Opsi "Bulldozer Mode" (Mass-Download Otomatis)

Jika Anda memiliki daftar referensi yang panjang dan ingin mencari ketersediaannya secara massal tanpa mengunduh manual satu per satu, Anda bisa memerintahkan agen: **"Aktifkan Bulldozer Mode"**.
Dalam mode ini, agen AI akan:
1. Mengerahkan segala cara (API OpenAlex, CrossRef, dll) untuk menemukan dan mengunduh PDF Open-Access.
2. Memasukkan referensi tersebut secara otomatis ke Mendeley.
3. **Integritas Akademik:** Jika PDF terkunci *paywall* atau tidak ditemukan, agen akan **Jujur Melapor Gagal** dan tidak akan memasukkannya ke Mendeley. Mengutip dokumen tanpa pernah membaca fisiknya adalah pelanggaran akademik.

### 🕵️‍♂️ Otoritas "Visual Browser Agent" (Bypass Blokir API)

Jika *Bulldozer Mode* gagal menembus keamanan repositori (*bot detection* / blokir API) namun Anda yakin PDF tersebut gratis di internet, agen memiliki **otoritas** untuk membangkitkan sub-agen visual. Sub-agen ini akan mengendalikan browser Google Chrome asli Anda untuk mencari dan "menyelamatkan" link PDF rahasia tersebut layaknya penelusuran manusia, lalu menyuntikkannya ke Mendeley Anda secara legal. Perintahkan saja: **"Gunakan browser agent untuk cari PDF ini."**
