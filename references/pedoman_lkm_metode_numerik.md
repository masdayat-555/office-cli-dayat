# PEDOMAN PENULISAN LKM (LEMBAR / LAPORAN KEGIATAN MAHASISWA) METODE NUMERIK

> [!IMPORTANT]
> **KEDUDUKAN HUKUM DOKUMEN: LAPORAN RESMI PRAKTIKUM METODE NUMERIK**  
> LKM (Lembar / Laporan Kegiatan Mahasiswa) adalah format laporan resmi praktikum Metode Numerik di Program Studi Informatika, Fakultas Teknik, Universitas Janabadra (Dosen Pembina: Ibu Yumarlin MZ, M.Kom.).  
> Dokumen ini **bukan laporan praktikum umum** dan disusun per modul (LKM 1, LKM 2, LKM 3, dst.) yang mengintegrasikan seluruh percobaan laboratorium, pembuktian kode, tangkapan layar, komentar sub-program, serta penyelesaian tugas modul.

---

## 1. DOKTRIN UTAMA & KEJUJURAN AKADEMIK

1. **SELURUH SCREENSHOT MAHASISWA WAJIB DIPASANG 100%**:
   - Semua tangkapan layar (*screenshot*) SciNotes, Scilab Console, maupun Scilab Graphic Window hasil pengerjaan mahasiswa **WAJIB terpasang seluruhnya**.
   - Posisi gambar wajib di tengah (*Center*), proporsional (lebar `11.5cm` s.d. `13.5cm`).
2. **KOMENTAR DAN PENJELASAN SUB-PROGRAM WAJIB LENGKAP**:
   - Dosen mewajibkan adanya ulasan sub-program, fungsi logika, variabel, rumus, dan percabangan/perulangan di bawah setiap nomor praktikum dan tugas.
   - **DILARANG KERAS MENGHAPUS ATAU MEMANGKAS KOMENTAR SUB-PROGRAM**.
3. **ANTI-AI SLOP / ANTI-YAPPING**:
   - Dilarang keras menggunakan gaya bahasa generik AI yang bertele-tele. Gunakan bahasa teknik yang lugas, presisi, faktual, dan mencerminkan pengerjaan langsung di software Scilab.

---

## 2. STRUKTUR BAKU DOKUMEN LKM (4 BAB RESMI)

Setiap berkas LKM mematuhi hierarki 4 Bab resmi berikut (setiap BAB baru **WAJIB Page Break Before**):

```text
HALAMAN JUDUL (COVER RESMI JANABADRA)
DAFTAR ISI (Native Word Automatic Table 1 <w:sdt> - Halaman Tersendiri)
BAB I PENDAHULUAN
  1.1 Latar Belakang (Justified, ringkas, kontekstual materi modul)
  1.2 Tujuan Praktikum (Poin-poin capaian pembelajaran modul)
  1.3 Dasar Teori (Persamaan analitis, fungsi polinomial/biseksi, teorema Bolzano, dsb)
BAB II KEGIATAN PRAKTIKUM
  2.1 Alat dan Bahan
      2.1.1 Perangkat Keras (Laptop Advan Ai Gen Ryzen 7 8845HS, RAM 16GB, SSD 512GB)
      2.1.2 Perangkat Lunak (OS Windows 11, Scilab 2024 / SciNotes, Word 2021)
  2.2 Pelaksanaan Praktikum (Langkah 1..n + 100% Screenshot di tengah + Komentar Sub-Program Wajib)
BAB III PELAKSANAAN TUGAS
  3.1 Tugas 1: [Judul Tugas 1] (Penyelesaian analitis manual + eksekusi Scilab + Komentar)
  3.2 Tugas 2: [Judul Tugas 2] (Langkah SciNotes + Screenshot kode bagian 1..n + Komentar + Analisis Komparatif)
BAB IV PENUTUP
  4.1 Kesimpulan (Rangkuman kuantitatif hasil praktikum & konvergensi nilai akar)
  4.2 Saran (Rekomendasi teknis pemrograman Scilab)
DAFTAR PUSTAKA (Standar sitasi ilmiah IEEE / APA)
```

---

## 3. ATURAN MUTLAK PERLINDUNGAN RUMUS MATEMATIKA & TIPOGRAFI

> [!CAUTION]
> ### 🚨 PERLINDUNGAN RUMUS: ANTI-STRETCHING & ANTI RATA TENGAH RENTAN
> 1. **DILARANG MENYISIPKAN NEWLINE ('\n') DALAM PARAGRAF JUSTIFIED**:
>    - Di Microsoft Word, menyisipkan `\n` (soft line break / Shift+Enter) di dalam *run* teks *justify* akan memicu peregangan spasi kata secara paksa (*forced justified stretch*). Hal ini merusak tampilan rumus dan menghasilkan spasi raksasa antar-simbol (seperti `D   =   b^2   -   4ac`).
> 2. **RUMUS WAJIB MENJADI PARAGRAF MANDIRI PERATAAN KIRI (LEFT) DENGAN INDENTASI**:
>    - Setiap baris rumus analitis, persamaan matematika, matriks, atau kalkulasi numerik ($D = b^2 - 4ac$, $x_{1,2} = \dots$) **WAJIB** dibuat sebagai objek paragraf tersendiri (`<w:p>`) dengan `alignment = WD_ALIGN_PARAGRAPH.LEFT` dan diberi indentasi kiri (`left_indent = Inches(0.4)` atau `1cm`).
>    - **JANGAN MENGANDALKAN RATA TENGAH (CENTER) UNTUK RUMUS BERTAHAP**: Perataan tengah sangat rapuh dan rentan rusak/patah saat enter tidak sengaja tertekan atau margin bergeser. Perataan kiri berindentasi memberikan proteksi $100\%$ stabil dan rapi layaknya buku teks matematika.
> 3. **PEMBERSIHAN SOFT ENTER PADA PARAGRAF NARASI**:
>    - Teks narasi paragraf isi wajib rata kanan-kiri (*justify*), namun **WAJIB** dibersihkan dari `\n` menggunakan:
>      ```python
>      clean_text = " ".join([line.strip() for line in text.split('\n') if line.strip()])
>      ```
>    - Setiap butir langkah, nomor urut, label judul, dan baris rumus harus berupa objek paragraf Word independen (`doc.add_paragraph()`).

---

## 4. STANDAR HEADING & DAFTAR ISI OTOMATIS

1. **Warna Heading Wajib Hitam Pekat (`#000000`)**:
   - `Heading 1` : Warna `#000000`, Tebal, Center (untuk Judul BAB).
   - `Heading 2` : Warna `#000000`, Tebal, Left (untuk Sub-bab `1.1`, `2.1`, `3.1`, `4.1`).
   - `Heading 3` : Warna `#000000`, Tebal, Left (untuk Sub-sub bab `2.1.1`).
   - **HARAM** menggunakan heading berwarna biru default Word.
2. **Pembersihan `w:numPr` pada Heading 2 & 3 Template**:
   - Hapus tag `w:numPr` dari XML gaya Heading 2 dan Heading 3 bawaan template agar tidak terjadi penomoran dobel/tabrakan (seperti `1.4 1.1 Latar Belakang`):
     ```python
     for sname in ['Heading 2', 'Heading 3']:
         st = doc.styles[sname]
         for np in st._element.xpath('.//w:numPr'):
             np.getparent().remove(np)
     ```
3. **Daftar Isi Otomatis Native Word (`<w:sdt>`)**:
   - Wajib menggunakan kontainer Structured Document Tag (`<w:sdt>`) bawaan template (*Automatic Table 1*).
   - Dilarang membuat Daftar Isi teks statis dengan titik-titik tab manual.
   - Perbarui nomor halaman riil via Word COM di belakang layar tanpa memicu dialog pop-up `Normal.dotm`.

---

## 5. FORMAT SPESIFIKASI HALAMAN SAMPUL (COVER RESMI)

- **Judul Atas (Center, Bold 14pt)**:
  - `LAPORAN PRAKTIKUM [NOMOR MODUL]`
  - `METODE NUMERIK`
  - `[JUDUL MODUL PRAKTIKUM SESUAI MATERI]`
- **Logo Kampus**: Logo resmi Universitas Janabadra di tengah (lebar proporsional ~5.5 cm).
- **Blok Identitas Penyusun (Center, 12pt)**:
  - `Disusun Oleh :`
  - `Salim Hidayat`
  - `24330030`
- **Blok Institusi Bawah (Center, Bold 12pt, menempel ke margin bawah)**:
  - `FAKULTAS TEKNIK`
  - `PROGRAM STUDI INFORMATIKA`
  - `UNIVERSITAS JANABADRA`
  - `YOGYAKARTA`
  - `2026`

---

## 6. PROTOKOL PENAMAAN FILE & KEBIJAKAN ZERO PDF

1. **Format Penamaan File**:
   - Format wajib: `[NIM]_[Nama Lengkap]_LKM[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LKM3.docx`).
2. **Format Utama Adalah DOCX**:
   - Berkas diserahkan dalam bentuk DOCX native yang dapat diedit langsung oleh mahasiswa.
   - **DILARANG OTOMATIS** mengonversi atau menghasilkan berkas PDF kecuali diminta secara eksplisit oleh mahasiswa.
3. **Preservasi Resolusi Citra (High Fidelity Minimal 300 DPI)**:
   - Tangkapan layar disimpan dalam format PNG lossless tanpa kompresi agresif.
