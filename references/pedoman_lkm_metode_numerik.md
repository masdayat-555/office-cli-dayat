# PEDOMAN PENULISAN LKM (LEMBAR / LAPORAN KEGIATAN MAHASISWA) METODE NUMERIK

> [!IMPORTANT]
> **KEDUDUKAN HUKUM DOKUMEN: LAPORAN RESMI PRAKTIKUM METODE NUMERIK**  
> LKM (Lembar / Laporan Kegiatan Mahasiswa) adalah format laporan resmi praktikum Metode Numerik di Program Studi Informatika, Fakultas Teknik, Universitas Janabadra (Dosen Pembina: Ibu Yumarlin MZ, M.Kom.).  
> Dokumen ini **bukan laporan praktikum umum** dan disusun per modul (LKM 1, LKM 2, LKM 3, dst.) yang mengintegrasikan seluruh percobaan laboratorium, pembuktian kode, tangkapan layar, penjelasan program, serta penyelesaian tugas modul.

---

## 1. DOKTRIN UTAMA & INTEGRITAS AKADEMIK

1. **SELURUH SCREENSHOT MAHASISWA WAJIB DIPASANG 100%**:
   - Semua tangkapan layar (*screenshot*) SciNotes, Scilab Console, maupun Scilab Graphic Window hasil pengerjaan mahasiswa **WAJIB terpasang seluruhnya**.
   - Posisi gambar wajib di tengah (*Center*), proporsional (lebar `11.5cm` s.d. `13.5cm`).

2. **SUDUT PANDANG INDEPENDEN & LARANGAN KOSAKATA PERCAKAPAN ("ANDA" / "MENURUT ANDA")**:
   - Laporan adalah karya mandiri mahasiswa yang menjawab soal dan tugas praktikum, **BUKAN ruang obrolan/percakapan antara AI dan pengguna, dan BUKAN percakapan tanya-jawab dengan dosen**.
   - Dosen pada naskah modul praktikum sering kali menulis kalimat perintah/tanya:
     - *"Jelaskan perbedaan untuk Praktek -1 dan Praktek -2 dari hasil Output nya (menurut Anda)"*
     - *"Berikan Penjelasan menurut anda hasil output yang diberikan coding program 1 dan 2"*
     - *"Berikan Penjelasan menurut anda hasil output yang diberikan coding 3"*
   - **DILARANG KERAS MENYALIN KATA "ANDA" ATAU "(MENURUT ANDA)" KE DALAM LAPORAN!** (Jika laporan menulis kata "Anda", itu adalah kesalahan fatal; pembaca akan bertanya siapa yang sebenarnya mengerjakan laporan tersebut).
   - Ubah seluruh kalimat tanya/perintah tersebut menjadi **Judul/Label Jawaban Tugas yang Independen, Objektif, dan Baku**:
     - Gunakan: `2. Perbedaan Output Praktek 1 dan Praktek 2:` (BUKAN `Soal 2: Jelaskan perbedaan... (menurut Anda)`).
     - Gunakan: `c. Penjelasan Hasil Output Coding 1 dan Coding 2:` (BUKAN `Poin c: Penjelasan menurut Anda...`).
     - Gunakan: `b. Penjelasan Hasil Output Coding 3:` (BUKAN `Poin b: Berikan Penjelasan menurut Anda...`).
   - Seluruh teks narasi wajib menggunakan sudut pandang orang ketiga formal/akademis atau langsung menjawab substansi masalah tanpa embel-embel gaya percakapan.

3. **GAYA JAWABAN: TO-THE-POINT, SEDERHANA, JAWAB SOAL (ANTI-AI YAPPING)**:
   - Jawablah persoalan tugas praktikum layaknya mahasiswa yang sedang menjawab soal ujian/laporan: **langsung ke inti masalah (*straight to the point*), sederhana, padat, dan akurat secara matematis**.
   - Dilarang menggunakan gaya bahasa AI yang bertele-tele, paragraf pembuka/penutup klise, atau kosakata dramatis/bombastis (seperti *"Hal ini memberikan konfirmasi geometris yang tidak terbantahkan"*, *"Membuktikan superioritas laju konvergensi"*, *"Sistem otomasi batch yang terprogram"*).
   - Jawaban evaluasi cukup disajikan dalam poin-poin sederhana yang lugas:
     1. Nilai solusi numerik yang diperoleh dan nomor iterasi berhentinya.
     2. Perilaku konvergensi (misal: galat turun cepat hingga memenuhi toleransi).
     3. Perbedaan teknis antar program (misal: parameter input statis vs interaktif runtime, atau adanya header identitas mahasiswa).

4. **PENJELASAN KODE PROGRAM: RINGKASAN FUNGSIONAL, BUKAN DEKONSTRUKSI BARIS KODE ROBOTIK**:
   - **DILARANG KERAS** membuat daftar bullet point berulang ala robot seperti:
     - *"- Sub-program Inisialisasi Lingkungan: Perintah clc membersihkan riwayat teks konsol..."*
     - *"- Sub-program Definisi Fungsi: deff('y=f(x)'..."*
     - *"- Sub-program Header Tabel: mprintf()..."*
   - Dosen di laboratorium tidak memerlukan penjelasan baris kode sepele (`clc`, `clear`, `mprintf`) yang diulang-ulang di setiap praktikum.
   - Penjelasan kode di bawah screenshot cukup disajikan dalam **1 paragraf ringkas (2–4 kalimat)** yang menjelaskan:
     - Persamaan fungsi yang diselesaikan dan metode numerik yang diterapkan.
     - Parameter masukan yang digunakan (nilai awal dan toleransi galat).
     - Hasil akhir konvergensi atau penanganan kondisi khusus (misal: pengaman turunan mendekati nol pada Newton-Raphson).

5. **STANDAR DIAGRAM ALIR (FLOWCHART): RAMPING & TIDAK MAKAN BARIS VERTIKAL**:
   - Alur diagram tetap top-down vertikal (`flowchart TD`).
   - Kotak proses dan input-output **WAJIB ramping secara vertikal dan memanjang secara horizontal** (gunakan teks single-line dan konfigurasi Mermaid `wrappingWidth: 600`, tanpa tag `<br/>` di dalam kotak proses) agar kotak tidak "gemuk" atau boros baris vertikal (*tidak makan baris*).
   - Bentuk belah ketupat keputusan (*decision diamond*) wajib proporsional: gunakan teks kondisi singkat (2 baris pendek) agar belah ketupat tidak mengembang raksasa yang memakan ruang vertikal.
   - Jalur terminasi, error, dan kondisi selesai diarahkan keluar ke sisi kanan (*side-branching*) untuk membagi lebar halaman secara seimbang dan menjaga diagram muat proporsional dalam 1 halaman.
   - Diagram wajib diekspor dengan resolusi tinggi minimal 300 DPI dan format PNG lossless.

6. **KEBIJAKAN ZERO PDF (MUTLAK FORMAT DOCX)**:
   - Format akhir penyerahan berkas adalah **DOCX native murni**.
   - Agen **DILARANG KERAS OTOMATIS** mengonversi atau menghasilkan berkas PDF. Mahasiswa akan meninjau, mengoreksi, dan mengekspor dokumen Word tersebut ke PDF secara mandiri.

7. **PROTEKSI ANTI-BURIK & ANTI-KOMPRESI CITRA (HIGH FIDELITY)**:
   - Gambar tangkapan layar dan flowchart wajib dipertahankan pada resolusi 300 DPI.
   - Berkas Word wajib diinjeksi tag XML Anti-Kompresi pada `word/settings.xml`:
     `<w14:defaultImageDpi xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" w14:val="0"/><w:doNotCompressPNG/>`
     agar Word tidak mendegradasi kualitas gambar saat disimpan.

---

## 2. STRUKTUR BAKU DOKUMEN LKM (4 BAB RESMI)

Setiap berkas LKM mematuhi hierarki 4 Bab resmi berikut (setiap BAB baru **WAJIB Page Break Before**):

```text
HALAMAN JUDUL (COVER RESMI JANABADRA)
DAFTAR ISI (Native Word Automatic Table 1 <w:sdt> - Halaman Tersendiri)
BAB I PENDAHULUAN
  1.1 Latar Belakang (Justified, ringkas, kontekstual materi modul)
  1.2 Tujuan Praktikum (Poin-poin capaian pembelajaran modul)
  1.3 Dasar Teori (Persamaan analitis, formula metode, kriteria konvergensi)
BAB II KEGIATAN PRAKTIKUM
  2.1 Alat dan Bahan
      2.1.1 Perangkat Keras (Laptop Advan Ai Gen Ryzen 7 8845HS, RAM 16GB, SSD 512GB)
      2.1.2 Perangkat Lunak (OS Windows 11, Scilab 2026 / SciNotes, Word 2021)
  2.2 Pelaksanaan Praktikum (Praktek 1..n + 100% Screenshot di tengah + Penjelasan ringkas program)
  2.3 Evaluasi Hasil Praktikum (Jawaban independen soal modul: tabel nilai numerik & perbedaan output)
BAB III PELAKSANAAN TUGAS
  3.1 Tugas Coding 1: [Nama Metode/Tugas] (Screenshot kode + output console + Penjelasan ringkas)
  3.2 Tugas Coding 2: [Nama Metode/Tugas] (Screenshot kode + output console + Penjelasan ringkas)
  3.3 Evaluasi Tugas Coding 1 dan 2 (Tabel hasil, Flowchart ramping 300 DPI, Analisis perbedaan)
  3.4 Tugas Coding 3: [Nama Metode/Tugas] (Screenshot kode + output console + screenshot grafik 2D)
  3.5 Evaluasi Tugas Coding 3 (Tabel hasil & Penjelasan hasil komputasi dan grafik)
BAB IV PENUTUP
  4.1 Kesimpulan (Rangkuman poin-poin capaian nilai akar, jumlah iterasi, dan komparasi metode)
  4.2 Saran (Rekomendasi teknis komputasi Scilab)
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
   - Format wajib: `[NIM]_[Nama Lengkap]_LKM[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LKM4.docx`).
2. **Format Utama Adalah DOCX**:
   - Berkas diserahkan dalam bentuk DOCX native yang dapat diedit langsung oleh mahasiswa.
   - **DILARANG OTOMATIS** mengonversi atau menghasilkan berkas PDF kecuali diminta secara eksplisit oleh mahasiswa.
3. **Preservasi Resolusi Citra (High Fidelity Minimal 300 DPI)**:
   - Tangkapan layar dan flowchart disimpan dalam format PNG lossless tanpa kompresi agresif.
