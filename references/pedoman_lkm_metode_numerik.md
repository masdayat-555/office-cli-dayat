# PEDOMAN PENULISAN LKM (LAPORAN KESELURUHAN MODUL) METODE NUMERIK

> [!IMPORTANT]
> **KEDUDUKAN HUKUM DOKUMEN: MONOGRAF LENGKAP AKHIR SEMESTER**  
> LKM (Laporan Keseluruhan Modul) adalah laporan monograf ilmiah komprehensif yang merangkum seluruh pelaksanaan praktikum Metode Numerik (Fakultas Teknik - Program Studi Informatika, Universitas Janabadra).  
> Dokumen ini **berbeda mutlak** dengan LHP (Laporan Hasil Praktikum yang berformat singkat per modul).

---

## 1. ATURAN INTEGRITAS DOKUMEN (ANTI-DOWNGRADE)

> [!CAUTION]
> **DILARANG KERAS MENGUBAH / MERUSAK LKM MENJADI LHP!**  
> Jika pengguna meminta pembuatan, penyusunan, atau revisi pada dokumen LKM:
> 1. **Dilarang membuang struktur bab**: Dokumen LKM **WAJIB** memiliki 5 BAB lengkap (BAB I s.d. BAB V), Kata Pengantar, Daftar Isi, dan Daftar Pustaka.
> 2. **Revisi Parsial yang Presisi**: Jika pengguna meminta perbaikan pada bagian tertentu (contoh: *"perbaiki bagian tugas"*), agen **HANYA** memodifikasi bagian tersebut (BAB IV) tanpa menghapus Kata Pengantar, Daftar Isi, atau bab-bab lainnya.
> 3. **Master Template Wajib**: Seluruh generasi dokumen LKM wajib berbasis `templates/template_lkm_metode_numerik.docx`.

---

## 2. STRUKTUR BAKU DOKUMEN LKM (5 BAB LENGKAP)

Setiap berkas LKM wajib mematuhi susunan hierarki halaman berikut secara berurutan:

```text
HALAMAN JUDUL (COVER LKM)
├── KATA PENGANTAR
├── DAFTAR ISI (Native Word Automatic Table 1)
├── BAB I PENDAHULUAN
│   ├── 1.1 Latar Belakang
│   └── 1.2 Tujuan Praktikum
├── BAB II TINJAUAN PUSTAKA
│   ├── 2.1 Konsep Dasar Array dan Matriks
│   ├── 2.2 Pengalamatan dan Operasi Element-Wise
│   ├── 2.3 Sistem Persamaan Linier dan Determinan
│   └── 2.4 Visualisasi Grafik Dua Dimensi
├── BAB III PELAKSANAAN PRAKTIKUM
│   └── (Copas utuh dari pengerjaan LHP: screenshot lab, kode, grafik, dan analisis)
├── BAB IV TUGAS PRAKTIKUM
│   ├── 4.1 Tugas 1 (Pola Mahasiswa: Soal -> Kode & Output Konsol -> Komentar)
│   └── 4.2 Tugas 2 (Pola Mahasiswa: Soal -> Kode & Output Konsol -> Komentar)
├── BAB V PENUTUP
│   ├── 5.1 Kesimpulan
│   └── 5.2 Saran
└── DAFTAR PUSTAKA
```

---

## 3. ATURAN KHUSUS TIAP BAGIAN

### 3.1 Halaman Sampul (Cover LKM)
- **Judul Utama**: `LAPORAN KESELURUHAN MODUL METODE NUMERIK` (Huruf kapital, Arial 14pt, tebal, rata tengah).
- **Logo Kampus**: Logo resmi Universitas Janabadra diletakkan di tengah dengan lebar proporsional (~5.5 cm).
- **Blok Identitas Penyusun**: Rata tengah:
  - `Disusun Oleh :`
  - `Nama: Salim Hidayat`
  - `NIM: 24330030`
- **Blok Institusi Bawah**: Rata tengah di batas bawah halaman (flush to bottom):
  - `PROGRAM STUDI INFORMATIKA`
  - `FAKULTAS TEKNIK`
  - `UNIVERSITAS JANABADRA`
  - `YOGYAKARTA`
  - `2026`

### 3.2 Kata Pengantar
- Paragraf isi menggunakan *First-Line Indent* 1 cm dan rata kiri-kanan (*justify*).
- Dilarang menyisipkan karakter *newline* (`\n`) manual di dalam run teks agar spasi justify tidak renggang/rusak.
- Blok tanda tangan penyusun (Yogyakarta, 2026 & Salim Hidayat) berada di kanan bawah.

### 3.3 Daftar Isi (Wajib Native Word Automatic Table 1)
- **Haram Mengetik Manual**: Dilarang mengetik titik-titik tab statis (`... 4`).
- **Wajib Building Block Word**: Dibungkus dalam Structured Document Tag (`<w:sdt>`) bawaan Word (Automatic Table 1). Saat diklik di Word, muncul tab interaktif resmi Word: `[ Table of Contents v | Update Table... ]`.
- **Dilarang Tag XML updateFields**: Dilarang menyisipkan `<w:updateFields w:val="true"/>` karena memicu pop-up peringatan keamanan Word saat berkas dibuka mahasiswa.
- **Wajib Refresh Nomor Halaman Riil**: Jalankan `officecli refresh <nama_file.docx>` untuk menghitung dan mencetak nomor halaman riil secara otomatis ke dalam XML TOC sebelum diserahkan ke mahasiswa.

### 3.4 BAB III Pelaksanaan Praktikum (Preservasi Penuh dari LHP)
- Bab ini berisi seluruh modul praktikum yang telah dikerjakan di lab.
- **Wajib Copas Persis**: Seluruh tangkapan layar (*screenshot*) konsol laboratorium, cuplikan kode Scilab, kurva grafik visual, serta analisis dan komentarnya disalin apa adanya persis sesuai struktur aslinya dari LHP.
- **Dilarang Menduplikasi Kode**: Jika *screenshot* konsol Scilab sudah ditampilkan, jangan membuat box teks kode tambahan yang mengulang isi screenshot.

---

## 4. STANDAR EMAS BAB IV TUGAS PRAKTIKUM (POLA LOGIS MAHASISWA)

> [!IMPORTANT]
> **POLA MAHASISWA: SOAL -> KODE & OUTPUT KONSOL LANGSUNG -> KOMENTAR DI BAWAHNYA**  
> Mahasiswa mengerjakan soal komputasi secara *to the point*, logis, dan terstruktur. Dilarang berfilsafat atau menulis esai teoritis panjang lebar di awal soal!

### 4.1 Alur Wajib Tiap Nomor Tugas
Setiap butir tugas praktikum di BAB IV wajib disusun dengan urutan mutlak berikut:

1. **Penyajian Soal & Matriks/Persoalan**:
   - Tuliskan instruksi soal secara lugas.
   - Sajikan matriks atau formula numerik menggunakan **Persamaan Matematika 2D Native Word (OMML XML)**:
     - Matriks menggunakan kurung siku 2D (`[...]`).
     - Determinan menggunakan garis tegak vertikal 2D (`|...|`).
     - Dilarang menuliskan matriks sebagai teks datar satu baris (`[3 5 2 10; ...]`).

2. **Sintaks Perintah & Output Konsol Scilab Langsung di Satu Box**:
   - Jawab langsung pertanyaan menggunakan **satu blok konsol Scilab literal**.
   - Format blok konsol menggabungkan baris perintah (`--> perintah`) dan hasil kalkulasi Scilab di bawahnya, persis seperti rekaman nyata pada Scilab Command Window:
     ```text
     --> A = [3 5 2 10; 2 1 6 9; 4 2 1 12; 9 3 2 4];

     --> B = [3; 5; 3; 9];

     --> C = A * B
      C  = 

        130.
        110.
        133.
        84.
     ```

3. **Komentar dan Penjelasan di Bawahnya**:
   - Tempatkan uraian analitis dan matematis tepat **di bawah** kotak kode/output:
     - **Verifikasi Perhitungan Manual**: Uraikan perkalian aljabar linier baris demi baris secara rinci (misal: *Baris 1: (3×3) + (5×5) + ... = 130*).
     - **Analisis Operator**: Jelaskan perbedaan operator yang digunakan (misal: operator `*` untuk aljabar matriks murni vs operator `.*` untuk operasi *element-wise*).
     - **Karakteristik Matematis**: Jelaskan sifat matriks dari hasil yang didapat (misal: nilai determinan $\det(J) = -27 \neq 0$ membuktikan bahwa matriks bersifat **nonsingular**, memiliki balikan $J^{-1}$, dan sistem persamaan linier $J \cdot x = b$ dijamin memiliki solusi unik dan tunggal).

### 4.2 Larangan Keras pada BAB IV
- **Dilarang Yapping di Awal**: Dilarang menulis narasi panjang, ulasan teori, atau penjelasan sebelum kode dan output disajikan.
- **Dilarang Subbab 4.3 Pembahasan Terpisah**: Dilarang memecah alur pengerjaan dengan membuat subbab terpisah seperti *"4.3 Pembahasan dan Analisis Komputasi Numerik"*. Seluruh analisis, evaluasi, dan pembahasan wajib melekat langsung di bawah masing-masing nomor tugas (subbab 4.1 dan 4.2).
- **Dilarang Gimmick Visual Garis Biru / Web Callout**: Seluruh naskah ilmiah formal dilarang menggunakan tabel callout berbingkai biru (`#0969DA`) atau aksen warna-warni. Gunakan format paragraf berindentasi rapi dan kotak kode abu-abu standar.

---

## 5. FORMAT TIPOGRAFI, PARAGRAF, DAN MARGIN

- **Ukuran Kertas**: A4 (21,0 cm $\times$ 29,7 cm).
- **Batas Margin**:
  - Kiri (*Left*): 4,0 cm
  - Atas (*Top*): 3,0 cm
  - Kanan (*Right*): 3,0 cm
  - Bawah (*Bottom*): 3,0 cm
- **Tipografi**:
  - Judul Bab & Subbab: Font Arial, tebal (*bold*).
  - Teks Isi: Font Calibri, ukuran 11 pt.
  - Spasi Antar Baris: 1.15 line spacing, spasi setelah paragraf (*space after*) 0 pt atau 4 pt.
  - Perataan Persamaan & Hitungan: **Rata Kiri (`align=LEFT`)**, dilarang di-justify agar tidak terjadi peregangan spasi rusak (*stretched justify*).
- **Page Break**: Setiap BAB baru (BAB I, BAB II, BAB III, BAB IV, BAB V) **WAJIB** dimulai pada halaman baru (*Page break before*).

---

## 6. PROTOKOL EKSPOR & KEBIJAKAN ZERO PDF

1. **Format Utama Adalah DOCX Mentah**:
   - Berkas wajib diserahkan dalam format `.docx` berbasis template `template_lkm_metode_numerik.docx`.
   - Nama Berkas: `[NIM]_[Nama Lengkap]_LKM[Nomor Modul].docx` (contoh: `24330030_Salim Hidayat_LKM2.docx`).
2. **Kebijakan Zero PDF (Kecuali Diminta Eksplisit)**:
   - Agen **DILARANG OTOMATIS** mengonversi atau menghasilkan file PDF.
   - File PDF hanya diproduksi jika pengguna secara tegas memerintahkan: *"buatkan pdf"*, *"export ke pdf"*, dsb.
3. **Preservasi Resolusi Citra (High Fidelity Minimal 300 DPI)**:
   - Setiap tangkapan layar praktikum wajib disimpan dalam format PNG lossless dengan resolusi minimal 300 DPI.
   - Jangan melakukan downsampling atau kompresi agresif pada gambar lab.
