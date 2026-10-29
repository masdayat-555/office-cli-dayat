---
name: office-cli
description: Unified Document Suite for AI Agents. Fast multi-format extraction to Markdown via Microsoft MarkItDown, programmatic authoring/manipulation of Microsoft Office documents (Word, Excel, PowerPoint) via OfficeCLI, and validated reference management via Mendeley Desktop with PDF identity pre-check protocol.
---

# Unified Office & Document Suite (MarkItDown + OfficeCLI + Mendeley)

Skill ini merupakan ekosistem terpadu untuk penanganan dokumen digital bagi AI coding agent. Mengintegrasikan kemampuan **ekstraksi cerdas multi-format ke Markdown** menggunakan **Microsoft MarkItDown**, **pembuatan/manipulasi dokumen Office native** menggunakan **OfficeCLI**, serta **manajemen referensi tervalidasi** menggunakan **Mendeley Desktop**, dengan kepatuhan penuh terhadap standar publikasi ilmiah nasional terakreditasi **SINTA (SINTA 1–6)**, jurnal internasional **Scopus (Q1–Q4)**, serta laporan akademik formal (Skripsi, Tesis, Kerja Praktik).

---

## 00. LARANGAN TERTINGGI (SUPREME DIRECTIVE)

> [!CAUTION]
> **DILARANG KERAS MENGGUNAKAN LIBRARY PIHAK KETIGA LAIN (`python-docx`, `openpyxl`, `python-pptx`, dll) UNTUK MENULIS ATAU MEMODIFIKASI DOKUMEN OFFICE.**
> 
> Seluruh operasi pembuatan, mutasi, dan penyuntingan file Office (.docx, .xlsx, .pptx) **WAJIB MUTLAK** menggunakan `officecli` dengan memanfaatkan perintah `batch` atau operasi CLI-nya. Library eksternal hanya boleh digunakan JIKA DAN HANYA JIKA pengguna memberikan izin eksplisit atau `officecli` benar-benar terbukti secara teknis tidak mampu melakukan tugas tersebut.
> 
> Pengecualian hanya berlaku untuk **pembacaan (read-only)**: `markitdown` adalah standar resmi yang diizinkan untuk membaca dokumen.

> [!CAUTION]
> [!CAUTION]
> **INTEGRITAS SITASI ILMIAH & PROTOKOL "ANTI-HALU":**
> 1. **DILARANG KERAS MENYISIPKAN SITASI FIKTIF ATAU EKSTERNAL SECARA SEPIHAK**: Demi mengejar kuota minimal referensi jurnal (misal >30 referensi), agen **TIDAK BOLEH** menyisipkan sitasi baru ke dalam naskah tanpa izin eksplisit pengguna ("takut kamu halu"). Referensi dalam naskah **HANYA** boleh yang 100% riil dari draf asli/folder `referensi/` pengguna.
> 2. **PENANGANAN DEFISIT REFERENSI**: Laporkan kuota yang kurang dalam Laporan Audit, berikan daftar rekomendasi jurnal bereputasi ber-DOI nyata, dan unduh berkas PDF Open Access aslinya ke `referensi/rekomendasi_internasional/` agar pengguna dapat memverifikasinya sendiri.
> 3. **DILARANG MENGARANG TANGGAL EDITORIAL**: `Received Date`, `Revised Date`, `Accepted Date` wajib dikosongkan sebagai *placeholder* editorial.

> [!CAUTION]
> **STANDAR PERSAMAAN MATEMATIKA NATIVE WORD EQUATION (OMML):**
> 1. **DILARANG MEMBIARKAN RAW LATEX / BACKSLASH**: Persamaan matematika dalam Word **DILARANG** dicetak sebagai teks mentah LaTeX (`\sigma(z)`, `\frac{1}{...}`, `\mathcal{L}`) atau tanda dollar `$...$`.
> 2. **WAJIB NATIVE WORD EQUATION (`<m:oMath>`)**: Seluruh rumus display wajib berwujud objek matematika native Word dengan font *Cambria Math*, diletakkan di tengah (*centered*) menggunakan tabel borderless 2 kolom dengan penomoran `(Eq. X)` rata kanan. Variabel inline wajib Unicode murni italic tanpa backslash.

> [!CAUTION]
> **KEWAJIBAN PENGKODEAN (STRICT UTF-8 ENCODING) & ANTI-MOJIBAKE:**
> Dilarang keras menghasilkan karakter aneh / *mojibake* (seperti `ÔÇ£`, `Ã©`). 
> 1. **WAJIB** menggunakan `encoding="utf-8"` pada **setiap** operasi baca/tulis file (I/O) di dalam script Python.
> 2. **DILARANG** menyalurkan (*piping*) output JSON via terminal (misal: `officecli ... > file.json` atau `| Out-File`) karena PowerShell sering kali merusak *encoding* karakter. Gunakan `subprocess.run` di Python untuk menangkap `stdout` lalu simpan secara aman.

---

## 0. STRUKTUR DIREKTORI SKILL (DIRECTORY TREE)

Struktur hierarki folder dan berkas pada skill ini dirancang secara modular agar mudah dipelihara dan dipublikasikan:

```text
office-cli/
├── SKILL.md                                 # Panduan operasional utama & aturan agen (File ini)
├── README.md                                # Dokumentasi publik repositori GitHub
├── .last_update_check                       # Marker timestamp sinkronisasi pembaruan 30 hari
├── scripts/
│   ├── check_update.py                      # Skrip auto-update berkala dari upstream GitHub
│   ├── clean_word_locks.py                  # Pembersih proses zombie WINWORD & Normal.dotm
│   ├── zotero_clean_metadata.py             # Pipeline pembersih metadata kanonikal CrossRef & normalisasi Title Case
│   ├── zotero_headless_sync.py              # Engine sinkronisasi headless Zotero Cloud via PyZotero (Anti-Halu)
│   ├── mendeley_setup.py                    # Setup otentikasi Mendeley OAuth2
│   └── mendeley_upload.py                   # Pengunggah metadata PDF ke Mendeley
├── templates/
│   ├── template_jurnal_sinta.docx           # Master template OJS SINTA (A4, 1-inch, Page 1 Fit, APA Table)
│   ├── template_laporan_tugas_akhir.docx    # Master template Skripsi / TA (A4, 4-3-3-3 cm, 5 Bab)
│   ├── template_laporan_kerja_praktik.docx  # Master template Laporan KP / Magang Industri
│   ├── template_laporan_praktikum.docx      # Master template Laporan Praktikum (Cover resmi Janabadra, Heading hitam, native SDT TOC)
│   ├── template_lhp_singkat.docx            # Master template Laporan Praktikum Singkat (Hanya Cover, Tanpa Bab/TOC)
│   ├── template_lkm_metode_numerik.docx     # Master template Laporan Keseluruhan Modul (Monograf 5 Bab, TOC native)
│   └── Template IASSSF.docx                 # Master template Artikel Jurnal Internasional IASSSF (Cambria, Single-Column, APA 7th)
└── references/
    ├── pedoman_jurnal_sinta.md              # Panduan lengkap penulisan jurnal SINTA 1-6 (IMRaD baku)
    ├── pedoman_jurnal_scopus.md             # Panduan jurnal internasional bereputasi Scopus Q1-Q4
    ├── pedoman_jurnal_iasssf.md             # Panduan naskah jurnal internasional IASSSF (Cambria, APA 7th >30 refs, CRediT, Anti-Sok Tau)
    ├── pedoman_skripsi_lengkap.md           # Pedoman penulisan Skripsi / Tesis 5 Bab standar nasional
    ├── pedoman_kerja_praktik.md             # Pedoman penyusunan Laporan Kerja Praktik & Magang
    ├── pedoman_laporan_praktikum.md         # Pedoman Laporan Praktikum (struktur bab, format cover)
    ├── pedoman_lkm_metode_numerik.md        # Pedoman LKM Metode Numerik (monograf 5 bab, pola mahasiswa BAB IV)
    ├── resep_officecli_dokumen_ilmiah.md    # Resep batch JSON OfficeCLI siap pakai
    └── aturan_adaptif_pedoman_kampus.md     # Protokol adaptif penyesuaian aturan lokal institusi
```

---

## 1. ARSITEKTUR DUA ENGINE & MATRIKS PEMBAGIAN TUGAS

Untuk mencegah degradasi tata letak dan konflik fungsional, skill ini membagi tanggung jawab penanganan dokumen ke dalam dua engine khusus:

### Tabel 1. Matriks Peran dan Batasan Penggunaan Tool
| Aspek | Microsoft MarkItDown (Reading Engine) | OfficeCLI (Authoring & Manipulation Engine) |
| :--- | :--- | :--- |
| **Fungsi Utama** | Ekstraksi cepat teks, tabel, dan metadata ke Markdown | Pembuatan, penyuntingan, dan mutasi struktur berkas Office |
| **Format yang Didukung** | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.zip`, gambar (OCR), audio | `.docx`, `.xlsx`, `.pptx` (Format OpenXML Microsoft Office) |
| **Tipe Eksekusi** | Pembacaan searah (*Read-Only Ingestion*) | Mutasi dua arah (*Read/Write DOM Batch Manipulation*) |
| **Kekuatan Utama** | Cepat, parsing tabel markdown rapi, ekstraksi metadata EXIF | Presisi visual native, pemutakhiran nomor halaman TOC, field codes |
| **Larangan Mutlak** | **DILARANG** digunakan untuk membuat/mengedit berkas biner | **DILARANG** digunakan untuk membaca cepat isi teks file non-Word |
| **Library Terlarang** | `python-docx` **DILARANG KERAS** digunakan untuk menyusun naskah akhir karena berisiko merusak template OpenXML dan menghapus field codes. |

---

## 2. PEMERIKSAAN KESIAPAN SISTEM & SINKRONISASI (PRE-FLIGHT CHECK)

### 2.0 Sinkronisasi Pembaruan Otomatis Bulanan (30-Day Auto-Update)
> [!IMPORTANT]
> **Instruksi Rutin Agen AI:**  
> Repositori ini didistribusikan untuk publik agar pengguna selalu memperoleh perbaikan bug, penyesuaian aturan SINTA, dan template terbaru langsung dari repositori resmi pengembang: [`masdayat-555/office-cli-dayat`](https://github.com/masdayat-555/office-cli-dayat).
> 1. Periksa file `.last_update_check` di direktori root skill. Jika telah mencapai atau melampaui **30 hari** (atau diminta pengguna):
>    - Jalankan: `python scripts/check_update.py` atau `git -C "<path_skill>" pull --rebase --autostash origin main`.
> 2. **Pembaruan Instan (Prompt Trigger)**: Jika pengguna mengetik perintah seperti *"perbarui office cli"*, *"update officecli"*, atau variasi salah ketik (*typo*) lainnya yang bermaksud memperbarui, agen **WAJIB LANGSUNG** mengeksekusi perintah `git -C "<path_skill>" pull --rebase --autostash origin main` tanpa banyak bertanya.
> 3. Bersifat *non-blocking*: Jika offline atau tidak ada remote git, lewati dan jangan gagalkan tugas utama pengguna.

### Tabel 2. Checklist Alat & Perintah Verifikasi / Instalasi
| Tool | Pengembang & Repositori Resmi | Perintah Pengecekan | Perintah Instalasi (Jika Belum Ada) |
| :--- | :--- | :--- | :--- |
| **Microsoft MarkItDown** | [microsoft/markitdown](https://github.com/microsoft/markitdown) | `markitdown --version`<br>atau `python -m markitdown --version` | `pip install markitdown`<br>*(opsional: `pip install markitdown[all]`)* |
| **OfficeCLI** | [officecli.ai](https://officecli.ai) / [github.com/officecli](https://github.com/officecli) | `officecli --version` | **Windows PowerShell:**<br>`irm https://d.officecli.ai/install.ps1 \| iex`<br>**Linux / macOS (Bash):**<br>`curl -fsSL https://d.officecli.ai/install.sh \| bash` |
| **PyMuPDF (`pymupdf`)** | [pymupdf/PyMuPDF](https://github.com/pymupdf/PyMuPDF) | `python -c "import pymupdf; print(pymupdf.__version__)"` | `pip install pymupdf` *(engine utama rendering PDF & ekstraksi gambar hi-res)* |
| **pypdf** *(On-Demand)* | [py-pdf/pypdf](https://github.com/py-pdf/pypdf) | `python -c "import pypdf; print(pypdf.__version__)"` | `pip install pypdf` *(fallback ekstraksi gambar PDF)* |
| **docx2pdf** *(LMS Export)*| [AlJohri/docx2pdf](https://github.com/AlJohri/docx2pdf) | `python -c "import docx2pdf"` | `pip install docx2pdf` *(khusus konversi akhir DOCX ke PDF)* |

> [!WARNING]
> Jika MarkItDown atau OfficeCLI belum terpasang, agen **WAJIB** menghentikan langkah sementara, melaporkan status kepada pengguna, dan menyajikan perintah instalasi di atas.

---

## 3. PANDUAN PENGGUNAAN ALAT (OPERATIONAL SYNTAX)

### 3.1 Ekstraksi Dokumen Menggunakan MarkItDown
1. Dilarang memanggil `view_file` langsung pada file biner kompleks (`.pdf`, `.docx`, `.xlsx`, `.pptx`).
2. Jalankan perintah ekstraksi ke berkas Markdown sementara di direktori `scratch/`:
   ```powershell
   python -m markitdown "dokumen_sumber.pdf" > "scratch/hasil_ekstraksi.md"
   ```
3. Buka dan pelajari berkas Markdown tersebut menggunakan `view_file`.

### 3.2 Manipulasi Dokumen Menggunakan OfficeCLI
1. **Inspeksi Struktur DOM Dokumen:**
   ```powershell
   officecli info "naskah.docx"
   officecli get "naskah.docx" --path "body/p[0]"
   ```
2. **Eksekusi Mutasi Batch JSON:**
   ```powershell
   officecli batch "naskah.docx" --batch "scratch/batch_mutasi.json"
   ```
3. **Penyegaran Field & Pelepasan File Lock:**
   ```powershell
   officecli refresh "naskah.docx"
   officecli close "naskah.docx"
   ```

### 3.3 Ekstraksi Aset Gambar dari Dokumen
- **Dari Dokumen Office (`.docx`, `.pptx`, `.xlsx`):** Gunakan modul bawaan Python `zipfile` untuk mengekstrak folder internal `word/media/` atau `ppt/media/` tanpa dependensi eksternal.
- **Dari Dokumen PDF (`.pdf`):** Gunakan pustaka `pypdf` untuk membaca `page.images` dan menyimpannya ke folder keluaran resolusi asli.

### 3.4 Aturan Konversi ke PDF: DILARANG Membuat PDF Tanpa Permintaan Eksplisit
- **DILARANG membuat atau mengonversi berkas `.pdf` (docx2pdf / export) jika TIDAK DIMINTA SECARA EKSPLISIT oleh pengguna.**
- Standar keluaran utama dan default selalu berupa dokumen Microsoft Word (`.docx`). Mahasiswa memerlukan berkas `.docx` untuk meninjau tata letak, mengedit naskah, dan menimpa *screenshot* praktikum asli hasil kerja mereka sendiri di laboratorium.
- Agen AI **HANYA** menjalankan konversi ke PDF jika pengguna secara spesifik dan tegas meminta (misal: *"buatkan pdf"*, *"tolong convert ke pdf"*, *"ekspor ke pdf"*, dsb.).
- Skrip konversi (hanya jika diminta, pastikan berkas DOCX tertutup dari MS Word):
   ```python
   from docx2pdf import convert
   convert("24330030_Salim Hidayat_LHP2.docx")
   ```

### 3.5 Protokol Anti-Burik (Preservasi Kualitas Citra & Resolusi Tinggi)

> [!IMPORTANT]
> **MASALAH UTAMA GAMBAR BURIK / BLURRY SAAT EXPORT KE PDF:**
> Secara default, Microsoft Word mengompresi gambar dan saat pengguna mengekspor menggunakan menu *Save As PDF*, Word sering menggunakan preset kompresi rendah (*Minimum size* / 96–150 DPI) atau mendownsample citra yang disisipkan.
> Selain itu, gambar yang diekstrak dari PDF modul sering kali beresolusi rendah jika tidak diekstrak pada DPI tinggi, sehingga saat ditarik di Word gambarnya menjadi pecah dan burik.

**Kaidah Wajib Anti-Burik untuk Dokumen Ilmiah & Laporan:**
1. **Injeksi XML High Fidelity ke Dokumen Word (`word/settings.xml`)**:
   Setiap template master dan dokumen `.docx` yang diproduksi **WAJIB** memiliki flag OpenXML anti-kompresi di dalam `word/settings.xml`:
   ```xml
   <w14:defaultImageDpi xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" w14:val="0"/>
   <w:doNotCompressPNG/>
   ```
   *Catatan:* Nilai `w14:val="0"` secara spesifik mengaktifkan mode **"High Fidelity"** di Microsoft Word, yang melarang Word melakukan *downsampling* atau kompresi otomatis terhadap gambar yang disisipkan.
2. **Standar Resolusi Gambar & Tangkapan Layar (Minimal 300 DPI)**:
   - **Ekstraksi PDF / Rendering Halaman**: Wajib menggunakan PyMuPDF (`pymupdf`) dengan resolusi minimal **300 DPI** (`pix = page.get_pixmap(dpi=300)`). **DILARANG KERAS** mengekstrak atau merender halaman PDF pada DPI 72, 96, atau 150!
   - **Format Gambar**: Wajib format **PNG lossless**. Dilarang menggunakan JPG terkompresi untuk tangkapan layar antarmuka atau kurva grafik.
   - **Injeksi Metadata DPI**: Sebelum gambar disisipkan ke Word, simpan citra dengan metadata resolusi 300 DPI menggunakan Pillow:
     ```python
     img.save(output_path, dpi=(300, 300))
     ```
3. **Proporsi Dimensi Gambar**:
   - Gambar berdimensi kecil (< 800 piksel) **DILARANG ditarik paksa memenuhi lebar halaman** (15–16 cm). Letakkan gambar di tengah (*Center*) dengan ukuran fisik proporsional (lebar 6–9 cm) agar piksel tidak membesar dan buram.
4. **Panduan Pengguna (Save As PDF di Word GUI Tanpa Burik)**:
   Jika mahasiswa menyimpan / mengekspor dokumen Word ke PDF secara mandiri di aplikasi Microsoft Word:
   - Buka **File > Save As > PDF**.
   - Pada bagian optimasi di bawah kotak dialog, **PILIH "Standard (publishing online and printing)"**, **JANGAN PILIH** *"Minimum size"*.
   - Melalui **Word Options > Advanced > Image Size and Quality**:
     - Centang kotak **"Do not compress images in file"** (*Jangan kompres gambar dalam file*).
     - Atur **Default resolution** ke **High fidelity**.

### 3.6 Protokol Hirarki Heading Asli & Daftar Isi Otomatis Word (Pilihan Bawaan: Automatic Table 1)

> [!IMPORTANT]
> **ATURAN EMAS HEADING DAN DAFTAR ISI OTOMATIS (AGAR NORMAL SEPERTI DOKUMEN WORD RESMI):**
> Pengguna Microsoft Word tidak mengetik Daftar Isi manual dan tidak menyuntikkan kode palsu. Word bekerja dengan membaca **Heading Styles resmi** (`Heading 1`, `Heading 2`, `Heading 3`). Jika heading diformat secara benar, fitur Daftar Isi Otomatis bawaan Word (*Automatic Table 1*) langsung mengenali seluruh struktur naskah secara instan dan dapat diperbarui kapan saja oleh pengguna secara natural.

1. **Hirarki Heading Wajib (Style Asli Word, Warna Hitam Pekat `#000000`)**:
   - **`Heading 1`**: Untuk seluruh judul bab utama dan bagian awal monograf:
     `KATA PENGANTAR`, `DAFTAR ISI`, `BAB I PENDAHULUAN`, `BAB II TINJAUAN PUSTAKA`, `BAB III PELAKSANAAN PRAKTIKUM`, `BAB IV TUGAS PRAKTIKUM`, `BAB V PENUTUP`, `DAFTAR PUSTAKA`.
     *Format*: Times New Roman 14 pt, **Bold**, Hitam Pekat (`#000000`), Perataan Tengah (*Center*), Spasi 1.15x, dan **WAJIB `PageBreakBefore = True`** agar setiap bab selalu dimulai di halaman baru tersendiri.
   - **`Heading 2`**: Untuk seluruh sub-bab (misal `1.1 Latar Belakang`, `1.2 Tujuan Praktikum`, `2.1 Dasar Teori`, `4.1 Tugas 1`, `5.1 Kesimpulan`, `5.2 Saran`).
     *Format*: Times New Roman 12 pt, **Bold**, Hitam Pekat (`#000000`), Perataan Kiri (*Left*), Spasi 1.15x.
   - **`Heading 3`**: Untuk sub-sub bab bertingkat (misal `1.1.1`).
2. **Pilihan Daftar Isi Bawaan Word: "Automatic Table 1" (Tabel Otomatis 1)**:
   - Gunakan komponen galeri resmi bawaan Word: `Built-In Building Blocks -> Automatic Table 1` yang dibungkus dalam Structured Document Tag (`<w:sdt>`).
   - Ubah judul wadah TOC menjadi **`DAFTAR ISI`** (TNR 14 pt, Bold, Center, `PageBreakBefore = True`).
   - Saat diklik di Microsoft Word, muncul kontrol/tab interaktif resmi: **`[ Table of Contents ▾ | Update Table... ]`** (atau *Perbarui Tabel...*).
3. **Pemberantasan Pop-Up Peringatan Keamanan (Zero External Pop-Up Policy)**:
   - **DILARANG KERAS MENYUNTIKKAN `<w:updateFields w:val="true"/>`** ke dalam `word/settings.xml`. Tag ini memicu dialog peringatan keamanan Word: *"This document contains fields that may refer to other files. Do you want to update the fields in this document?"*.
   - **Pre-render Nomor Halaman di Belakang Layar**: Selalu panggil `doc.TablesOfContents(1).Update()` via Word COM atau jalankan `officecli refresh` sebelum dokumen diserahkan ke pengguna. Nomor halaman riil sudah terhitung dan tertulis rapi sehingga dokumen terbuka secara instan dan bersih dari pop-up.
4. **Pemisahan Halaman Ketat (Page Break Antar Bagian)**:
   - Dilarang keras menumpuk Daftar Isi di halaman yang sama dengan Kata Pengantar.
   - Urutan halaman monograf baku:
     - Halaman 1: Cover (tanpa header/footer angka)
     - Halaman 2: KATA PENGANTAR (diakhiri blok tanda tangan kanan bawah)
     - Halaman 3: DAFTAR ISI (halaman tersendiri dengan PageBreakBefore)
     - Halaman 4: BAB I PENDAHULUAN (halaman baru tersendiri)
     - Halaman berikutnya: BAB II, BAB III, BAB IV, BAB V, DAFTAR PUSTAKA (masing-masing diawali PageBreakBefore).

---

## 4. STANDAR PENULISAN NASKAH ILMIAH (FOKUS UTAMA: JURNAL SINTA 1–6)

### Tabel 3. Matriks Perbandingan Format Naskah Ilmiah
| Parameter Format | Jurnal SINTA 1–6 (Standar Utama) | Jurnal Internasional Scopus (Q1–Q4) | Skripsi / Tugas Akhir (Monograf) | Laporan Praktikum (Lab) |
| :--- | :--- | :--- | :--- | :--- |
| **Batas Tepi (Margin)** | **2,54 cm (1 inci) Simetris** di seluruh sisi | **2,54 cm (1 inci)** atau format 2 kolom | **4-4-3-3 cm** (Left 4 cm ruang jilid) | **2,54 cm** (Simetris) atau standar institusi |
| **Font & Spasi Isi** | Times New Roman 11–12 pt, spasi **1.15x**, Justified | Times New Roman / Arial 10–11 pt, spasi 1.0–1.15x | Times New Roman 12 pt, spasi **1.5x**, Justified | Times New Roman 12 pt, spasi **1.15x - 1.5x** |
| **Struktur Bab / Seksi** | **DILARANG kata 'BAB'** (`1. PENDAHULUAN`, `2. METODE`) | **DILARANG kata 'BAB'** (`1. Introduction`, `2. Methods`) | **WAJIB kata 'BAB'** (`BAB I PENDAHULUAN`) | **WAJIB kata 'BAB'** (`BAB I`, `BAB II`) |
| **Aliran Halaman** | **Continuous Flow** (Dilarang *Page Break* antar-seksi) | Continuous Flow (1 kolom / 2 kolom) | **Wajib Page Break** di setiap bab baru | **Wajib Page Break** antar BAB |
| **Abstrak & Identitas** | **Wajib Page 1 Fit**, bilingual, 150–200 kata, spasi 1.0x | Structured / Unstructured, 200–250 kata, Full English | Intisari 3 Alinea baku, TNR 10 pt spasi 1.0x | Cover Page Khas (Logo, Identitas Mentok Bawah) |
| **Standar Tabel** | **Format APA (3 Garis Horizontal)**, tanpa garis vertikal | Format APA murni, judul di atas tabel | Format APA / Boxed (sesuai pedoman kampus) | Format Boxed / Grid (Tabel standar) |
| **Gaya Sitasi** | **APA 7th Edition** (atau IEEE), 15–25 rujukan mutakhir | APA 7th / IEEE / Elsevier, 30–50 rujukan Scopus | APA 7th / IEEE, terbagi primer dan sekunder | APA 7th Edition (bila ada tinjauan pustaka) |

---

### Tabel 4. Checklist 10 Bagian Baku Naskah Jurnal SINTA
| No | Bagian Naskah | Kaidah Penulisan Baku | Pantangan Mutlak |
| :---: | :--- | :--- | :--- |
| **1** | **Judul Artikel** | 10–15 kata, lugas, spesifik, memuat metode + objek, bilingual (ID Bold, EN Italic). | Hindari kata klise skripsi (*"Rancang Bangun..."*, *"Penerapan..."*). |
| **2** | **Baris Penulis & Afiliasi** | Nama tanpa gelar, afiliasi lengkap (Prodi, Fakultas, Universitas, Kota, Negara), email bertanda `*`. | Dilarang gelar akademis (ST, MT, Ph.D) dan dilarang tumpuk paragraf rapat. |
| **3** | **Abstrak & Keywords** | 150–200 kata, 1 paragraf, formula IMRaD mini (Masalah, Metode, Hasil Metrik Riil, Kesimpulan). | **Dilarang tumpah ke Halaman 2**, dilarang sitasi, dilarang formula mentah. |
| **4** | **1. PENDAHULUAN** | Pola piramida terbalik: Urgensi riil $\rightarrow$ *State-of-the-Art* $\rightarrow$ *Research Gap* $\rightarrow$ Kebaruan (*Novelty*). | Dilarang menggunakan kata `BAB I` dan dilarang menyisipkan *Page Break*. |
| **5** | **2. METODE PENELITIAN** | Replikatif: sumber data, pra-pemrosesan, arsitektur model, skenario pengujian, rumus matematis Unicode. | Dilarang menyalin diagram pohon terminal ASCII atau kode mentah ke isi teks. |
| **6** | **3. HASIL DAN PEMBAHASAN** | Sajikan temuan kuantitatif via Tabel APA dan grafik tajam. Pembahasan menjawab *mengapa* fenomena terjadi. | Dilarang sekadar membaca ulang angka tabel tanpa konfrontasi literatur. |
| **7** | **4. KESIMPULAN** | Sintesis ringkas jawaban rumusan masalah berdasarkan bukti empiris, implikasi, dan batasan riset. | Dilarang mengulang daftar persentase angka mentah atau membuat ringkasan bab. |
| **8** | **UCAPAN TERIMA KASIH** | Ditujukan kepada penyandang dana hibah (sebutkan nomor kontrak) atau mitra penyedia data. | Opsional; hindari ucapan puitis atau personal non-akademik. |
| **9** | **DAFTAR PUSTAKA** | Format APA 7th Edition, diurutkan A–Z, *hanging indent* 1,27 cm, spasi 1.0x, tautan DOI aktif. | Dilarang menggunakan penomoran numerik `[1]`, `[2]` jika gaya jurnal adalah APA. |
| **10** | **Similaritas Turnitin** | Batas toleransi indeks kesamaan maksimal 15% – 20% (di luar daftar pustaka). | Dilarang plagiarisme teks mentah dari korpus rujukan. |

---

### 4.5 Transformasi Cerdas Elemen Non-Standar (Tree & Raw Code $\rightarrow$ Standar Publikasi SINTA)

Ketika mentransformasikan draf ke dalam naskah jurnal Word resmi, agen **WAJIB** peka terhadap representasi visual dan struktur data:

### Tabel 5. Matriks Konversi Representasi Data Non-Standar ke Format SINTA
| Representasi Mentah di Draf | Kesalahan Fatal Jika Disalin Mentah | Solusi Transformasi Resmi SINTA (Wajib Pilih Salah Satu) |
| :--- | :--- | :--- |
| **Diagram Pohon / Alur Direktori**<br>(`├── folder/`, `└── file`, `│`) | Tampilan terlihat seperti terminal mentah, tidak formal, dan memicu penolakan editor. | **Metode A (Tabel Format APA):** Susun ke dalam tabel terstruktur dengan kolom: *Tahap*, *Modul / Entitas*, *Parameter / Spesifikasi*, dan *Luaran*.<br>**Metode B (Nested Indented List):** Susun ke dalam butir hierarkis bernomor ilmiah (`1.`, `a.`, `1)`).<br>**Metode C (Gambar Diagram Resmi):** Konversi menjadi diagram visual beresolusi tinggi (vektor / PNG 300 DPI) dengan keterangan `Gambar [No]. Judul` di bawah. |
| **Tabel ASCII / Markdown Mentah**<br>(`+---+---+` atau `| col1 | col2 |`) | Huruf monospace Consolas merusak kerapian dokumen dan format tabel tidak dapat dibaca reader. | **Wajib Konversi ke Native Word Table (`w:tbl`):** Tiga garis horizontal tebal (tanpa garis vertikal pembatas kolom), header abu-abu tipis (*#F2F2F2*), teks Justified/Center, font 9.5–10 pt. |
| **Formula Matematika LaTeX**<br>(`$\kappa$`, `\Delta`, `\approx`, `\times`) | Tanda dollar `$` dan tag LaTeX tercetak memalukan di naskah Word. | **Konversi ke Unicode Murni:** `κ` (U+03BA), `Δ` (U+0394), `≈` (U+2248), `×` (U+00D7), `∑` (U+2211). Gunakan run superskrip asli Word (`¹`, `²`, `*`). |
| **Blok Kode Program (````code````)** | Kode terminal yang panjang memboroskan kuota halaman artikel jurnal. | Rangkum logika algoritma ke dalam **Kotak Algoritma / Pseudocode Formal** atau representasikan arsitekturnya dalam diagram pipeline. |

---

## 5. LESSONS LEARNED & ATURAN EMAS ANTI-DEFECT (ZERO-DEFECT MATRIX)

### Tabel 6. Matriks Pelajaran Berharga dari Pengujian Nyata
| Kategori Masalah | Anti-Pola Masa Lalu | Dampak Fatal | Solusi Mutlak (Aturan Emas) |
| :--- | :--- | :--- | :--- |
| **Struktur Gambar** | Mengganti gambar dengan `set src` pada slot yang memiliki rotasi bawaan. | Gambar baru mewarisi rotasi miring 90 derajat sehingga melar menyamping. | Gunakan `remove` pada *run* gambar lama (`r[x]`), lalu `add` (type: picture) di ID paragraf yang sama persis (rotasi 0). |
| **Pemetaan Peran** | Menggunakan *Global String Replace* pada nama kepanitiaan/pengesahan. | Gelar jabatan (Role) tertukar dan menempel pada nama yang salah. | Petakan berdasarkan **JABATAN (Role)**, bukan nama! Ubah nama dan jabatannya secara berpasangan. |
| **Ilusi Markdown** | Mengasumsikan layout visual dari perataan vertikal berkas `.md`. | Kolom tanda tangan sejajar 2x2 runtuh menjadi susunan atas-bawah yang salah. | Wajib merekonstruksi struktur *grid* tabel sejajar 2x2 asli untuk lembar pengesahan. |
| **Batch Mutasi** | Melakukan `remove` beberapa child run secara berurutan maju (`r[2]`, `r[3]`). | Terjadi *index shifting*, memicu error fatal `Path not found`. | **Wajib menghapus dari indeks terbesar ke terkecil (mundur):** `r[4]` $\rightarrow$ `r[3]` $\rightarrow$ `r[2]`. |
| **Encoding Piping** | Mengalirkan keluaran JSON via piping PowerShell (`officecli ... \| Out-File`). | Karakter kutip dan tanda baca rusak menjadi mojibake (`ÔÇ£`). | Gunakan script Python dengan `encoding="utf-8"` untuk seluruh interaksi I/O dokumen. |
| **Kunci Berkas Word** | Menimpa berkas `.docx` saat masih dibuka atau saat ada proses *zombie* Word. | Muncul `PermissionError: [Errno 13] Permission denied`. | Deteksi proses headless: `Get-Process WINWORD \| Where-Object { $_.MainWindowTitle -eq '' }` lalu matikan (`Stop-Process -Force`). Panggil selalu `officecli close`. |
| **Warna Heading Jurnal** | Membiarkan warna bawaan template Word (Steel Blue / Light Blue `#365F91`, `#4F81BD`). | Naskah ditolak editor jurnal karena tidak mematuhi standar monokrom/hitam resmi SINTA/Scopus. | Seluruh gaya *Heading 1–3* dan *Title* **WAJIB diatur ke warna Hitam Pekat** (`#000000` / `RGBColor(0, 0, 0)`). |
| **Kebocoran AI Slop & Asterisk** | Membiarkan karakter markdown (`*`, `**`, `***`, `#`, `` ` ``) bocor ke teks Word (misal `*(Domain Shift)*` atau `**Judul *(Sub)***`). | Teks terlihat seperti salinan mentah bot AI (*AI slop*), memicu penolakan desk review editor jurnal. | **Wajib normalisasi multi-pass & pembersihan asterisk total:** Urai nested format (`**A *(B)***` $\rightarrow$ `**A** *(B)*`), hapus seluruh asterisk delimiter dari teks run, dan ubah murni menjadi properti OpenXML (`bold=True`, `italic=True`). |
| **Audit Pasca-Kompilasi Otomatis** | Mengasumsikan kompilasi berhasil tanpa memvalidasi teks keluaran dokumen. | Asterisk terselubung atau kerusakan XML lolos ke pengguna tanpa terdeteksi. | **Wajib audit terprogram setelah kompilasi:** Jalankan skrip pemeriksa yang menyisir seluruh `paragraph.text` dan `cell.text` guna memastikan **0 kebocoran asterisk** (kecuali footnote penulis `¹*`), 0 tag markdown, dan 0 error skema. |
| **Byline Multi-Penulis & Email** | Hanya mencantumkan email penulis pertama tanpa keterangan pada artikel multi-penulis. | Terjadi kebingungan hak kepengarangan (*authorship dispute*) dan ketidakjelasan korespondensi. | Cantumkan email seluruh penulis (`Email: ¹email1, ²email2`) serta tegaskan tanda bintang untuk penulis korespondensi (`*Penulis Korespondensi: email`). |
| **Tabel Orphan Template** | Hanya membersihkan paragraf template saat inisialisasi tanpa menghapus tabel bawaan. | Tabel contoh dari template tertinggal sebagai tabel hantu (*orphan table*), merusak urutan tabel dan memicu validasi error. | **Wajib membersihkan paragraf DAN tabel bawaan:** `for t in list(doc.tables): t._element.getparent().remove(t._element)`. |
| **Urutan Skema OpenXML tcPr** | Menambahkan `tcBorders`, `shd`, dan `tcMar` tanpa memperhatikan hierarki ketat skema WordML. | Dokumen gagal validasi skema OpenXML (`unexpected child element` atau `attribute val is missing`). | Urutan anak `<w:tcPr>` wajib: `w:tcW` $\rightarrow$ `w:tcBorders` (top, left, bottom, right) $\rightarrow$ `w:shd` (dengan `w:val="clear"`) $\rightarrow$ `w:tcMar` (top, left, bottom, right). |
| **Pemberian Tugas Revisi Naskah** | Mengoreksi redaksional teks kritik/audit pengguna alih-alih merevisi naskah artikel di repositori. | Salah tafsir instruksi pengguna; dokumen jurnal riil tidak tersentuh perbaikan. | Ketika pengguna mengirimkan catatan audit dan meminta koreksi, **AGEN WAJIB LANGSUNG MERIVISI DOKUMEN ARTIKEL ASLI** di repositori (`.md` dan `.docx`). |
| **Kebersihan Repo** | Membuat skrip `fix_xxx.py` atau `dump_xxx.txt` di folder proyek pengguna. | Workspace pengguna kotor oleh berkas sampah sementara. | Seluruh skrip eksekusi sementara **WAJIB** berada di direktori `scratch/` artifact. Timpa (*overwrite*) berkas keluaran tunggal. |
| **Simbol Unicode Fancy di Tugas** | Menggunakan `\u207b\u2074` (⁻⁴), `\u00b2` (²), `\u2192` (→), `\u2013` (–) dsb. dalam script python-docx untuk dokumen tugas kuliah. | Karakter tampil sebagai "angka aneh" atau mojibake di Word karena font tidak mendukung atau encoding bermasalah saat file ditulis via tool. | **Gunakan notasi plain ASCII seperti ketikan mahasiswa:** `10^-4`, `x^2`, `->`, `-`, `x` (untuk perkalian). Tidak ada Unicode escape di string python-docx untuk tugas. |
| **Lebar Gambar Terlalu Besar** | Menyisipkan gambar dengan `width=Cm(16)` atau lebih besar dari lebar teks efektif. | Gambar memaksa halaman baru (blank page) setelah gambar karena tingginya melampaui tinggi halaman setelah margin. | **Gunakan `width=Cm(13)` sebagai batas aman** untuk margin narrow (1,27 cm). Jangan pernah naikkan lebar tanpa mengecek dimensi asli gambar terlebih dahulu. |
| **Siklus Simpan OfficeCLI** | Menjalankan injeksi TOC di `officecli batch`, lalu langsung memanggil `officecli refresh`. | Mesin Word membaca file lama dari disk. Perubahan TOC dari resident RAM lenyap (`resident_died_dirty`). | **WAJIB MENYIMPAN:** `batch` $\rightarrow$ `save` $\rightarrow$ `refresh` $\rightarrow$ `close`. Selalu lakukan `save` sebelum `refresh`. |
| **Hirarki Heading & Daftar Isi Otomatis** | Mengetik TOC manual, menyuntikkan field mentah tanpa kontainer SDT, atau memasang `<w:updateFields>` yang memicu pop-up keamanan (*"fields refer to other files"*). | Dokumen dianggap tidak normal/rusak, muncul peringatan keamanan eksternal saat dibuka, dan fitur otomatis Word tidak bekerja wajar. | **Wajib gunakan hirarki Heading Word asli (`Heading 1` & `Heading 2`) dipadu Building Block resmi bawaan Word "Automatic Table 1" (`<w:sdt>`)**. Setel `PageBreakBefore = True` pada tiap bab, hitung nomor halaman riil di belakang layar via Word COM/`officecli refresh`, dan **DILARANG KERAS menyuntikkan `<w:updateFields>`**. |
| **Page Break Antar Bab & Daftar Isi** | Menumpuk Daftar Isi di halaman yang sama dengan Kata Pengantar, atau membiarkan bab baru bersambung di halaman sebelumnya tanpa pemisah tegas. | Tata letak acak-acakan, format laporan rusak, tidak memenuhi standar monograf akademik. | Setiap bagian utama (`Heading 1`: KATA PENGANTAR, DAFTAR ISI, BAB I s.d. BAB V, DAFTAR PUSTAKA) **WAJIB dimulai pada halaman baru** (`pageBreakBefore = True` pada paragraf heading). |
| **Bab III LKM (Pelaksanaan Praktikum)** | Mendesain format baru yang berbeda dari LHP, merangkum ulang teks, menghilangkan gambar tangkapan layar lab, atau menduplikasi kode dalam box teks tambahan. | Menghilangkan bukti pekerjaan praktikum mahasiswa di lab, format acak-acakan merusak kerapian dokumen. | **Wajib COPAS UTUH (Exact Copy / Verbatim)** dari berkas LHP (`doc_lhp`) paragraf 15 hingga selesai beserta seluruh relasi media gambar resolusi tinggi (300 DPI) asli tanpa mengubah urutan atau membuat format baru. Jangan buat box kode baru jika screenshot sudah ada ("kan udah ada screenshot-an"). |
| **Bab IV LKM (Tugas Praktikum & Matriks)** | Menambahkan border tabel biru `#0969DA`, callout web warna-warni, atau teks persamaan matriks yang di-justify hingga spasi merenggang. | Tampilan seperti *AI slop*, rumus aljabar linier rusak/sulit dibaca. | **Format monokrom hitam formal**, seluruh komputasi matriks dan aljabar linier **WAJIB RATA KIRI (`align=LEFT`)**, font kode monospace Consolas, bersih dari kotak aksen biru. |
| **Pengaturan Posisi Cover** | Mengandalkan nilai `space_before` / `space_after` yang raksasa (mis. 150pt) untuk mendorong teks ke margin bawah. | Teks cover *overflow* ke halaman berikutnya, ukuran sulit diprediksi jika gambar berubah, layout kaku. | **Gunakan spasi (Enter / paragraf kosong)** untuk mendorong blok teks sampul, atau atur ruang sewajarnya tanpa pt ekstrem. |
| **Efek Samping doc.add_page_break**| Memanggil `doc.add_page_break()` di `python-docx` di akhir elemen. | Menghasilkan paragraf kosong *siluman* di halaman sebelum break yang memakan ruang 1 baris vertikal. | Sisipkan break langsung di dalam run terakhir: `p.runs[-1].add_break(WD_BREAK.PAGE)` atau setel properti *Page break before*. |
| **Persamaan Rumus Word (OMML vs LaTeX)** | Menulis rumus display sebagai teks mentah LaTeX (`\sigma(z) = \frac{1}{1 + e^{-z}}`) atau tanda dollar `$...$` di berkas Word. | Naskah terlihat seperti draf mentah AI (*AI slop*), ditolak editor jurnal karena tidak menggunakan Equation native Word. | **Wajib konversi ke Native Word Equation (`<m:oMath>` / Cambria Math)** melalui MathML & `MML2OMML.XSL`. Tempatkan dalam borderless table 2 kolom (`Inches(5.1)` center untuk formula + `Inches(0.8)` right untuk nomor `(Eq. X)`). Variabel inline wajib Unicode murni italic tanpa backslash. |
| **Sitasi & Daftar Pustaka Anti-Halusinasi** | Menambahkan sitasi eksternal/baru secara sepihak ke dalam teks naskah dan daftar pustaka untuk mengejar kuota minimal jurnal (misal >30 referensi). | Integritas riset tercoreng, naskah memuat sitasi halusinasi yang tidak diakui penulis (*"takut kamu halu"*). | **Naskah Word HANYA memuat 100% referensi riil asli penulis**. Kekurangan kuota wajib disajikan dalam Laporan Audit, sodorkan rekomendasi ber-DOI valid, dan **unduh berkas PDF Open Access aslinya ke folder `referensi/rekomendasi_internasional/`** agar penulis dapat memeriksa keasliannya terlebih dahulu. |
| **Tanggal Editorial Naskah Jurnal** | Mengisi tanggal pada baris `Received Date:`, `Revised Date:`, `Accepted Date:` dengan tanggal rekaan saat konversi naskah. | Pelanggaran etika editorial jurnal; tanggal tersebut merupakan wewenang mutlak dewan redaksi jurnal setelah proses telaah formal. | **Wajib mengosongkan tanggal editorial** atau membiarkannya sebagai *placeholder* resmi (`Received Date:                      Revised Date:                      Accepted Date:`). |
| **Skema Pendanaan Kampus (Reimbursement)** | Menganggap penelitian mahasiswa/dosen tanpa hibah eksternal sebagai "tanpa dana" (*no external funding*) atau mengarang nomor kontrak hibah fiktif. | Menghilangkan pengakuan institusi kampus yang mendanai riset melalui skema penggantian biaya (*reimbursement*). | **Format pendanaan kampus internal secara jujur**: Cantumkan pendanaan Fakultas/Universitas melalui skema penggantian biaya (*reimbursement*) riset dan pembinaan kompetisi mahasiswa pada bagian *Funding* dan *Acknowledgment*. |
| **Kunci Berkas Word (File Lock Resiliency)** | Menyimpan file `.docx` langsung tanpa penanganan eksepsi saat file sedang dibuka oleh pengguna di Microsoft Word. | Memicu `PermissionError: [Errno 13] Permission denied`, skrip kompilasi crash dan dokumen gagal tersimpan. | **Bungkus selalu `doc.save()` dalam try-except**: Jika terkena `PermissionError`, otomatis simpan ke nama berkas cadangan (`*_Rev1.docx`, `*_Rev2.docx`), lalu beri tahu pengguna bahwa dokumen utama sedang terkunci di Word. |
| **Encoding Konsol Windows cp1252** | Mencetak karakter Unicode (seperti karakter Yunani `σ`, `ŷ`, atau tanda kutip tipografis) langsung ke konsol Windows cp1252. | Memicu `UnicodeEncodeError: 'charmap' codec can't encode character`, menggagalkan jalannya skrip otomatisasi. | Pasang `sys.stdout.reconfigure(encoding='utf-8')` di bagian atas seluruh skrip Python otomatisasi dokumen. |

---

## 6. MANAJEMEN PRIVASI DATA PENGGUNA & ZERO AI-TRAINING POLICY

### 6.1 Larangan Mutlak Penggunaan Data Pribadi untuk Bahan Training AI (Zero AI-Training Policy)
- **DILARANG KERAS MENGGUNAKAN DATA PRIBADI PENGGUNA SEBAGAI BAHAN TRAINING MODEL AI:** Seluruh identitas pengguna (nama lengkap, NIM, NIP, nomor kontak, surel), data afiliasi kampus/perusahaan mitra, draf naskah karya ilmiah lokal, maupun file template dokumen internal yang dilampirkan pengguna **TIDAK BOLEH** digunakan, disimpan, diekstrak, atau dialirkan sebagai bahan latihan/pelatihan (*training / fine-tuning dataset*) model AI apa pun.
- **Pemrosesan Bersifat Ephemeral & Sepenuhnya Lokal:** Data pribadi dan aset dokumen yang diserahkan pengguna hanya diproses sementara dalam memori sesi aktif (*in-memory*) di lingkungan lokal pengguna semata-mata untuk mengompilasi berkas dokumen Word `.docx`.
- **Larangan Penyimpanan Permanen & Kebocoran Publik:** Dilarang menyimpan data pribadi pengguna ke dalam file kode skill, git commit, skrip publik, atau mengirimkannya ke layanan logging pihak ketiga. File template mentah lokal kampus (`Template_*.docx`) wajib otomatis diabaikan oleh `.gitignore`.

### 6.2 Prinsip Adaptif Pedoman Kampus
Jika pengguna menyertakan pedoman khusus dari institusinya (misalnya format margin, jenis font, atau gaya sitasi kampus tertentu), **ATURAN KAMPUS PENGGUNA 100% MENGALAHKAN ATURAN STANDAR NASIONAL**. Agen wajib langsung menyesuaikan parameter dokumen dengan preferensi tersebut.

---

## 7. DOKUMEN REFERENSI SPESIFIK & MASTER TEMPLATE

### Tabel 7. Katalog Referensi Dokumen & Template Resmi
| Berkas Referensi / Template | Deskripsi & Cakupan Standar | Lokasi Berkas |
| :--- | :--- | :--- |
| **Pedoman Jurnal SINTA** | Panduan lengkap IMRaD baku, kaidah Page 1 Fit, byline afiliasi, dan tabel APA 3 garis. | [`references/pedoman_jurnal_sinta.md`](references/pedoman_jurnal_sinta.md) |
| **Pedoman Jurnal Scopus** | Panduan jurnal internasional Q1–Q4, *Extended IMRaD*, *Ablation Study*, ORCID, dan *Upgrading Pathway*. | [`references/pedoman_jurnal_scopus.md`](references/pedoman_jurnal_scopus.md) |
| **Pedoman Jurnal IASSSF** | Panduan naskah artikel jurnal internasional IASSSF: format Cambria, 1 kolom, abstrak berstruktur 1 paragraf, CRediT, etika AI, APA 7th >30 sitasi, tabel biodata, dan protokol Anti-Sok Tau. | [`references/pedoman_jurnal_iasssf.md`](references/pedoman_jurnal_iasssf.md) |
| **Pedoman Skripsi Lengkap** | Panduan penyusunan Skripsi/Tesis 5 Bab standar nasional, preliminary pages, hingga lampiran. | [`references/pedoman_skripsi_lengkap.md`](references/pedoman_skripsi_lengkap.md) |
| **Pedoman Kerja Praktik** | Panduan penyusunan Laporan KP/Magang Industri (profil mitra, SOP, proyek, evaluasi mutu). | [`references/pedoman_kerja_praktik.md`](references/pedoman_kerja_praktik.md) |
| **Pedoman Laporan Praktikum** | Panduan Laporan Praktikum baku (Cover luwes, native TOC, struktur wajib). | [`references/pedoman_laporan_praktikum.md`](references/pedoman_laporan_praktikum.md) |
| **Resep Batch OfficeCLI** | Koleksi batch JSON siap pakai untuk heading 1-3, TOC otomatis, tabel APA, gambar, dan hanging indent. | [`references/resep_officecli_dokumen_ilmiah.md`](references/resep_officecli_dokumen_ilmiah.md) |
| **Master Template Jurnal SINTA** | Berkas Word DOCX resmi OJS SINTA (A4, 2,54 cm simetris, Page 1 Fit, tabel APA, bebas mojibake/JEL). | [`templates/template_jurnal_sinta.docx`](templates/template_jurnal_sinta.docx) |
| **Master Template Skripsi 5 Bab** | Berkas Word DOCX resmi Skripsi/TA (A4, 4-3-3-3 cm, TNR 12 pt spasi 1.25x, preliminary Romawi). | [`templates/template_laporan_tugas_akhir.docx`](templates/template_laporan_tugas_akhir.docx) |
| **Master Template Laporan KP** | Berkas Word DOCX resmi Laporan Kerja Praktik/Magang Industri struktur perusahaan lengkap. | [`templates/template_laporan_kerja_praktik.docx`](templates/template_laporan_kerja_praktik.docx) |
| **Master Template Laporan Praktikum**| Berkas Word DOCX resmi Laporan Praktikum. Dilarang generik, cover proporsional. | [`templates/template_laporan_praktikum.docx`](templates/template_laporan_praktikum.docx) |
| **Master Template LHP Singkat**| Berkas Word DOCX resmi Laporan Praktikum khusus untuk penugasan singkat (hanya cover, tanpa BAB, tanpa TOC). | [`templates/template_lhp_singkat.docx`](templates/template_lhp_singkat.docx) |
| **Master Template Jurnal IASSSF** | Berkas Word DOCX resmi naskah IASSSF (A4, margin 2-2.5-3-3 cm, banner/logo resmi, footer CC-BY 4.0, format Cambria murni). | [`templates/Template IASSSF.docx`](templates/Template%20IASSSF.docx) |

---

## 8. FORMAT TUGAS KULIAH (LEMBAR JAWABAN MAHASISWA)

> [!IMPORTANT]
> Bagian ini berlaku untuk **tugas kuliah biasa** (lembar jawaban, soal latihan) — bukan jurnal, bukan skripsi. Aturannya berbeda dan lebih sederhana.

### 8.1 Cara Membaca Dokumen Sumber

**WAJIB** gunakan markitdown atau officecli. **DILARANG KERAS** membuka browser untuk membaca isi dokumen Word/PDF/docx.

```powershell
python -m markitdown "file.docx"    # baca isi teks
officecli info "file.docx"          # lihat struktur DOM
```

### 8.2 Header & Identitas

Format identitas adalah **plain paragraf biasa**, bukan tabel, bukan garis:

```
JUDUL TUGAS MATA KULIAH (center, bold, TNR 13pt)

Nama        : [Nama Lengkap] / [NIM]
Nama        : [Nama Lengkap] / [NIM]    ← jika kelompok
Mata Kuliah : [Nama Mata Kuliah]
```

**Larangan mutlak pada bagian identitas:**
| Anti-Pola | Dampak | Solusi |
| :--- | :--- | :--- |
| Tabel borderless 2 kolom untuk Nama & NIM | Tampilan rusak/berantakan di Word | Plain paragraf `Label : Nilai / NIM` |
| Garis horizontal dekoratif (`w:pBdr`) | Terlihat jelek, tidak diminta | Hapus; cukup spasi paragraph kosong |
| NIM di kolom terpisah | Tidak rapi, tabel tak terlihat | Satukan: `Nama Mahasiswa / NIM` dalam 1 run |

### 8.3 Margin & Tipografi

| Parameter | Nilai untuk Tugas Kuliah |
| :--- | :--- |
| **Margin** | **Narrow: 1,27 cm semua sisi** (bukan 4-3-3-3 cm skripsi) |
| **Font** | Times New Roman |
| **Ukuran isi** | 12 pt (10–11 pt untuk isi tabel) |
| **Spasi baris** | 1,15× (`line=276`) |
| **Alignment** | Justify untuk isi, Center untuk judul & caption |

### 8.4 Prinsip Konten: Paste As-Is

Jika user menyediakan file sumber (`.txt`, `.html`, dsb.), **salin persis isinya ke Word tanpa modifikasi**.

**DILARANG menambahkan tanpa perintah eksplisit:**
| Yang Dilarang | Alasan |
| :--- | :--- |
| Tabel langkah-langkah dari teks yang sudah ada | Mengubah "ketikan manusia" jadi AI slop |
| Sub-heading tambahan (2.1, 2.2, 2.3 …) | Tugas bukan jurnal IMRaD |
| Penjelasan/deskripsi ekstra di luar sumber | Tidak diminta |
| Tabel ringkasan yang menduplikasi isi gambar | Gambar sudah cukup sebagai visualisasi |

### 8.5 Gambar sebagai Visualisasi

Jika user melampirkan gambar dan menyebutnya sebagai "visualisasi":
- **Sisipkan gambar langsung** — `width=Cm(13)` maksimal untuk margin narrow, caption italic di bawah
- **DILARANG** menambahkan tabel teks yang mengulang isi gambar
- **DILARANG** memperbesar ke `Cm(16)` atau lebih — bisa memaksa blank page
- Gambar = visualisasi selesai, tidak perlu teks pendukung

### 8.6 Tabel 3 Kolom untuk Sub-soal a / b / c

Jika soal memiliki sub-soal a, b, c dengan panjang konten serupa, buat **tabel 1 baris × 3 kolom** untuk hemat ruang:
- Border: hanya garis vertikal tipis abu-abu (`insideV`) antar kolom, tidak ada top/bottom/left/right
- Isi setiap kolom: teks as-is dari sumber, font 10 pt
- Kolom lebar sama rata

### 8.7 Penulisan Simbol Matematika di Tugas: PLAIN ASCII

> [!IMPORTANT]
> **DILARANG KERAS** menggunakan Unicode escape sequence (`\u207b`, `\u2074`, `\u00b2`, `\u2192`, dsb.) untuk simbol matematika dalam script python-docx tugas kuliah. Simbol ini berpotensi tampil sebagai karakter aneh atau mojibake tergantung encoding file dan dukungan font.

Gunakan **notasi plain ASCII** seperti mahasiswa mengetik di keyboard biasa:

| Simbol | DILARANG | WAJIB Digunakan |
| :--- | :--- | :--- |
| Pangkat/eksponen | `x\u00b2`, `x\u00b3`, `10\u207b\u2074` | `x^2`, `x^3`, `10^-4` |
| Perkalian | `\u00d7`, `\u2715` | `x` atau `*` |
| Minus panjang (em/en dash) | `\u2013`, `\u2014`, `\u2212` | `-` |
| Panah | `\u2192`, `\u2190` | `->`, `<-` |
| Kurang-lebih | `\u2264`, `\u2265` | `<=`, `>=` |
| Derajat | `\u00b0C` | `derajat C` atau `deg C` |
| Tak hingga | `\u221e` | `tak hingga` atau `inf` |

### 8.8 Resep Eksekusi Standar Format Tugas Kuliah (OfficeCLI Native)

Sesuai Supreme Directive 00, penyusunan tugas kuliah **WAJIB menggunakan OfficeCLI batch**, bukan library python-docx:

1. **Section Setup (Margin Narrow 1,27 cm semua sisi):**
   ```json
   {
     "command": "set",
     "path": "/section[1]",
     "props": {
       "marginTop": "1.27cm",
       "marginBottom": "1.27cm",
       "marginLeft": "1.27cm",
       "marginRight": "1.27cm",
       "pageWidth": "21.0cm",
       "pageHeight": "29.7cm"
     }
   }
   ```

2. **Identitas Plain Paragraf (Individu vs Kelompok):**
   - **Tugas Individu:** Hanya satu baris `Nama : [Nama Lengkap] / [NIM]` (Dilarang mencantumkan nama rekan).
   - **Tugas Kelompok:** Baris nama diulang per anggota.
   - Menggunakan paragraf standar Times New Roman 12pt, tanpa tabel borderless dan tanpa garis horizontal dekoratif.

3. **Tipografi & Spasi:**
   - Font: Times New Roman 12 pt.
   - Spasi baris: 1,15x (`lineSpacing: "1.15x"`).
   - Alignment: Justified untuk isi teks, Center untuk Judul Tugas.

## 9. FORMAT LAPORAN PRAKTIKUM SECARA UMUM

Laporan Praktikum memiliki tingkat keformalan di antara tugas biasa dan skripsi. Patuhi konvensi berikut untuk menghindari keluhan pengguna (*user pushback*):

### 9.1 Struktur Bab yang Tersendiri
Berbeda dengan tugas bebas, Laporan Praktikum **WAJIB** dipisahkan per BAB:
- Setiap BAB baru (`BAB I PENDAHULUAN`, `BAB II KEGIATAN PRAKTIKUM`, dll.) **HARUS** berada di halaman baru.
- Sisipkan *Page Break* (`Ctrl+Enter`) tepat sebelum judul Bab atau pada *run* terakhir sebelum bab tersebut.

### 9.2 Dasar Teori Mengikat
- Jangan pernah menyematkan teori klise AI ("yappingan singkat").
- Bagian **Dasar Teori** harus selalu diparafrase/dirangkum **langsung dari Modul Praktikum resmi (PDF/Word)** yang diberikan oleh institusi.

### 9.3 Tampilan Halaman Sampul (Cover Page)
- **Tengah Rapat Atas**: Judul laporan (LAPORAN PRAKTIKUM X) diletakkan di paling atas halaman (tanpa paragraf tersembunyi sebelumnya).
- **Mentok Bawah (Bottom Margin Flush)**: Blok identitas kampus (Fakultas, Universitas, Kota, Tahun) diatur agar benar-benar menempel pada batas margin kertas terbawah.
- **Keseimbangan (Luwes)**: Jangan gunakan *spacing point (pt)* raksasa yang menyiksa layout. Atur secara proporsional dengan kombinasi spasi paragraf atau `space_after` untuk mendorong Logo dan teks "Disusun Oleh" ke area tengah.

### 9.4 Daftar Isi (TOC)
- **Haram** mengetik Daftar Isi secara manual atau memanipulasi *tab leader* di Python.
- Harus murni di-render menggunakan mesin Field Codes dari Word melalui `officecli`. Selalu selesaikan seluruh modifikasi DOM terlebih dahulu, akhiri dengan perintah JSON `toc`, dan mutlak di-*save* sebelum di-*refresh*.

### 9.5 ATURAN KHUSUS PRAKTIKUM METODE NUMERIK: LHP VS LKM (LEMBAR / LAPORAN KEGIATAN MAHASISWA)

> [!CAUTION]
> **ATURAN MUTLAK METODE NUMERIK (UNIVERSITAS JANABADRA - DOSEN IBU YUMARLIN MZ):**
> 1. **LHP (Laporan Hasil Praktikum) → FORMAT TUGAS SINGKAT PER MODUL:**
>    - **Master Template Wajib**: `templates/template_lhp_singkat.docx`.
>    - **DILARANG MENGGUNAKAN BAB** (Tanpa BAB I, Tanpa BAB II, dst.).
>    - **DILARANG MENGGUNAKAN KATA PENGANTAR & DAFTAR ISI (TOC)**.
>    - **Struktur Dokumen LHP**:
>      - Cover Page resmi Universitas Janabadra (Salim Hidayat / 24330030 / Informatika / 2026).
>      - Page Break → Langsung Judul **`TUGAS LHP`** (Centered, Bold 14pt).
>      - Soal-soal Praktek (Praktek 1, Praktek 2, dst.).
>    - **Konvensi Nama File**: `[NIM]_[Nama Lengkap]_LHP[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LHP2.docx`).
> 
> 2. **LKM (Lembar Kegiatan Mahasiswa / Laporan Kegiatan Mahasiswa) → LAPORAN RESMI MODUL METODE NUMERIK:**
>    - **Bukan Laporan Praktikum Umum!** LKM adalah format laporan resmi praktikum Metode Numerik Universitas Janabadra per modul (LKM 1, LKM 2, LKM 3, dst.) yang merangkum seluruh kegiatan laboratorium dan penugasan modul.
>    - **Master Template Wajib**: `templates/template_laporan_praktikum.docx` (Cover resmi Janabadra, heading hitam, `<w:sdt>` native TOC).
>    - **Struktur Baku Dokumen LKM (4 BAB Wajib - Setiap BAB Wajib Page Break Before)**:
>      ```text
>      HALAMAN SAMPUL (Cover Resmi Janabadra: LAPORAN PRAKTIKUM [X] - METODE NUMERIK - [JUDUL MODUL])
>      DAFTAR ISI (Native Word Automatic Table 1 <w:sdt> - Halaman Tersendiri)
>      BAB I PENDAHULUAN
>        1.1 Latar Belakang (Justified, ringkas, kontekstual modul komputasi)
>        1.2 Tujuan Praktikum (Poin-poin capaian modul)
>        1.3 Dasar Teori (Rumus analitis, fungsi polinomial/biseksi, teorema Bolzano, dsb)
>      BAB II KEGIATAN PRAKTIKUM
>        2.1 Alat dan Bahan (Perangkat Keras Advan Ai Gen Ryzen 7, Perangkat Lunak Scilab & Windows 11)
>        2.2 Pelaksanaan Praktikum (Langkah 1..n + 100% Screenshot mahasiswa terpasang di tengah + Komentar Sub-Program Wajib)
>      BAB III PELAKSANAAN TUGAS
>        3.1 Tugas 1: [Judul Tugas 1] (Penyelesaian analitis manual + eksekusi Scilab + Komentar)
>        3.2 Tugas 2: [Judul Tugas 2] (Langkah kode SciNotes + Screenshot kode bagian 1..n + Komentar Sub-Program + Analisis Komparatif)
>      BAB IV PENUTUP
>        4.1 Kesimpulan (Poin keberhasilan komputasi & verifikasi data numerik)
>        4.2 Saran (Rekomendasi teknis pemrograman Scilab)
>      DAFTAR PUSTAKA (Standar sitasi ilmiah IEEE / APA)
>      ```
> 
>    - **ATURAN MUTLAK PERLINDUNGAN RUMUS MATEMATIKA (ANTI-STRETCHING & ANTI RATA TENGAH RENTAN)**:
>      - **DILARANG MENYISIPKAN NEWLINE ('\n') DALAM PARAGRAF JUSTIFIED**: Di Microsoft Word, menyisipkan `\n` di dalam *run* paragraf berformat *justify* akan memicu peregangan spasi paksa (*forced justified stretching*), menghasilkan spasi bolong-bolong raksasa antar-simbol (seperti `D   =   b^2   -   4ac`).
>      - **RUMUS WAJIB MENJADI PARAGRAF MANDIRI DENGAN PERATAAN KIRI (LEFT) & INDENTASI**: Setiap baris rumus analitis, fungsi, matriks, atau kalkulasi matematika ($D = b^2 - 4ac$, $x_{1,2}$, limit, biseksi) **WAJIB** berupa objek paragraf tersendiri (`<w:p>`) dengan `alignment = WD_ALIGN_PARAGRAPH.LEFT` dan diberi `left_indent = Inches(0.4)` atau `1cm`.
>      - **JANGAN MENGANDALKAN RATA TENGAH (CENTER) UNTUK RUMUS BERTAHAP**: Perataan tengah rentan rusak, berantakan, atau patah saat enter tertekan atau terdistorsi margin. Perataan kiri berindentasi memberikan perlindungan $100\%$ stabil dan rapi layaknya buku teks matematika.
> 
>    - **PEMBERSIHAN SOFT ENTER PADA TEKS NARASI NON-RUMUS**:
>      - Paragraf isi non-rumus wajib rata kanan-kiri (*justify*), namun **WAJIB** dibersihkan dari `\n` menggunakan:
>        `clean_text = " ".join([line.strip() for line in text.split('\n') if line.strip()])`.
>      - Setiap butir langkah, nomor, label, dan baris rumus harus berupa objek paragraf Word independen (`doc.add_paragraph()`).
> 
>    - **KOMENTAR DAN PENJELASAN SUB-PROGRAM WAJIB DISAJIKAN LENGKAP**:
>      - Dosen (Ibu Yumarlin MZ) mewajibkan ulasan sub-program / penjelasan setiap baris program pada setiap nomor praktikum dan tugas.
>      - **DILARANG KERAS MENGHAPUS ATAU MEMANGKAS KOMENTAR SUB-PROGRAM**.
> 
>    - **HEADING HITAM PEKAT & PEMBERSIHAN `numPr`**:
>      - Gaya *Heading 1*, *Heading 2*, dan *Heading 3* **WAJIB** disetel ke warna Hitam Pekat (`#000000`).
>      - Tag XML `w:numPr` pada *Heading 2* dan *Heading 3* template **WAJIB DIHAPUS** (`for np in st._element.xpath('.//w:numPr'): np.getparent().remove(np)`) agar penomoran manual (`1.1`, `2.1`, `3.1`) tidak bertabrakan atau dobel (misal `1.4 1.1 Latar Belakang`).
> 
>    - **DAFTAR ISI OTOMATIS NATIVE WORD (`<w:sdt>`)**:
>      - Wajib menggunakan kontainer `<w:sdt>` bawaan template (*Automatic Table 1*).
>      - Hapus elemen body setelah `<w:sdt>` saat membangun ulang dokumen, lalu jalankan sinkronisasi nomor halaman via Word COM (`doc.TablesOfContents(1).Update()`) atau `officecli refresh` tanpa memicu pop-up `Normal.dotm`.
> 
>    - **SELURUH SCREENSHOT MAHASISWA WAJIB DIPASANG 100%**:
>      - Seluruh tangkapan layar praktikum lab mahasiswa wajib dipasang utuh di tengah (*center*), lebar `11.5cm` s.d. `13.5cm`.
> 
>    - **KONVENSI PENAMAAN FILE**:
>      - Format wajib: `[NIM]_[Nama Lengkap]_LKM[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LKM3.docx`). DILARANG membuat PDF otomatis kecuali diminta secara eksplisit.

### 9.6 Varian "LHP Singkat" Umum (Tugas Praktikum Tanpa BAB)
Beberapa praktikum menghendaki format "LHP Singkat" (hanya *Cover Page* lalu langsung isi penugasan tanpa BAB dan tanpa TOC). Jika pengguna meminta format ini ("halaman judul langsung tugas", "tidak pakai bab"):
- **Gunakan Master Template `template_lhp_singkat.docx`**: Template ini sudah bersih dari Daftar Isi dan siap diinjeksi tugas.
- **Konvensi Penamaan File**: **WAJIB** menggunakan format `[NIM]_[Nama Lengkap]_LHP[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LHP1.docx`).
- **Gaya Penulisan Kode/Console**: Jika tugas meminta reka ulang *console* (tanpa *screenshot*), JANGAN gunakan label kaku seperti "Operator 1:". Gunakan langsung nomor asli dari modul diikuti penjelasannya (perbaiki *typo* modul secara mandiri *kecuali* disuruh patuh mutlak). Setelah teks penjelasan, sisipkan *output raw* dari *console* secara literal.
- **Peringatan Kritis Logo Cover**: Saat membersihkan halaman *cover* dari paragraf kosong untuk menyesuaikan tinggi spasi agar elemen bawah tidak meluap ke halaman dua, **WAJIB** mengecek apakah paragraf tersebut memiliki *runs* (contoh di `python-docx`: `p.text.strip() == "" and len(p.runs) == 0`). JANGAN menghapus paragraf kosong yang berisi logo Universitas (`len(p.runs) > 0`).

---

## 10. MANAJEMEN REFERENSI TERVALIDASI (ZOTERO HEADLESS + MENDELEY + FOLDER REFERENSI)

> [!IMPORTANT]
> Bagian ini berlaku untuk **semua proyek penulisan ilmiah (Jurnal SINTA, Skripsi, Tesis)**. Tujuannya adalah memastikan seluruh sitasi dalam naskah berasal dari sumber yang sudah diverifikasi identitasnya — bukan hanya dari ingatan atau copy-paste abstrak.

### 10.1.1 Protokol Penanganan Defisit Referensi & Folder `rekomendasi_internasional`

> [!IMPORTANT]
> **PROTOKOL MUTLAK ANTI-HALU SITASI:**
> Jika sebuah jurnal (seperti IASSSF) mensyaratkan jumlah referensi minimal (misal: **> 30 referensi**), namun naskah asli penulis saat ini hanya memiliki referensi yang lebih sedikit (misalnya 26 judul):
> 1. **DILARANG KERAS MENYISIPKAN SITASI BARU KE DALAM NASKAH WORD**: Naskah artikel dan daftar pustakanya **WAJIB 100% BERSIH** hanya memuat sumber yang telah diverifikasi dari naskah asli penulis dan folder `REFERENSI/`.
> 2. **SAJIKAN KEKURANGAN SEBAGAI TEMUAN AUDIT**: Tuliskan dalam laporan analisis bahwa naskah masih memerlukan $X$ referensi tambahan untuk memenuhi kuota desk review jurnal.
> 3. **SEDIAKAN DAFTAR REKOMENDASI TERVERIFIKASI DENGAN DOI NYATA**: Berikan daftar 6–8 artikel jurnal internasional primer (Scopus/WoS, 5–10 tahun terakhir) yang sangat relevan dengan topik naskah.
> 4. **UNDUH BERKAS PDF OPEN ACCESS KE FOLDER KHUSUS**: Buat subfolder:
>    `REFERENSI/rekomendasi_internasional/`
>    Unduh berkas PDF Open Access asli dari artikel yang direkomendasikan ke folder tersebut. Hal ini membuktikan bahwa artikel tersebut nyata, dapat diakses, dan memungkinkan penulis membaca serta memeriksa metodologi di dalamnya sebelum menyetujui pemakaiannya.

### 10.1 Prinsip Dasar: Folder `REFERENSI` sebagai Sumber Kebenaran Tunggal

Setiap proyek penulisan ilmiah **WAJIB** memiliki satu folder `REFERENSI/` di root workspace proyek.

```text
ROOT_PROYEK/
├── REFERENSI/
│   ├── README.md                         # Tabel pelacak status validasi semua sitasi
│   ├── Koto_2021_IndoBERTweet.pdf
│   ├── Devlin_2019_BERT.pdf
│   └── ...                              # Semua file PDF sitasi
└── naskah_artikel.docx
```

**Konvensi Penamaan File PDF:**
```
[NamaBelakangPenulisPertama]_[Tahun]_[KataKunciJudul].pdf
Contoh: Koto_2021_IndoBERTweet.pdf
        Landis_1977_Kappa.pdf
```

Jika folder `REFERENSI/` belum ada, agen **WAJIB** membuatnya beserta file `README.md` berisi tabel pelacak sitasi sebelum melanjutkan tugas apapun terkait referensi.

---

### 10.1.5 Inisialisasi API Mendeley (Sifat: OPSIONAL / ON-DEMAND)

> [!NOTE]
> **ATURAN WAJIB AGEN:** Integrasi otomatisasi API Mendeley ini **JANGAN DIWAJIBKAN** kepada semua klien. Tawarkan dan pandu klien melakukan setup ini **HANYA JIKA** klien secara eksplisit meminta pembuatan daftar pustaka, integrasi Mendeley otomatis, atau validasi sitasi.

Jika klien membutuhkan daftar pustaka terintegrasi Mendeley secara otomatis, agen AI **WAJIB** memandu klien dengan memberikan panduan setup rahasia (*secrets*) secara **Global di direktori Skill**. Agen harus mem-format panduan tersebut dengan jelas di chat.

**Template Panduan yang Wajib Disampaikan Agen ke Klien:**
1. **Daftar Aplikasi:** Buka portal developer Mendeley di `https://dev.mendeley.com/myapps.html`.
2. **Isi Form:** Buat aplikasi baru dengan mengisi form:
   - *Application Name*: (Bebas, misal: Office CLI AI)
   - *Description*: (Bebas)
   - *Redirect URL*: **WAJIB** diisi persis `http://localhost:12345/callback`
3. **Generate Secret:** Klik *Generate Secret* (atau *Submit*). **PENTING:** Segera *copy* *Secret* yang muncul karena hanya ditampilkan sekali.
4. **Temukan Client ID:** Lihat tabel "My applications" di bagian atas halaman tersebut. *Client ID* Anda adalah angka yang berada tepat di bawah kolom **"ID"**.
5. **Simpan Credentials:** Buka file konfigurasi global skill di:
   `~/.gemini/config/skills/office-cli/.env` (sesuaikan dengan OS Windows/Mac klien)
   Lalu masukkan kredensial Anda:
   ```env
   MENDELEY_CLIENT_ID=masukkan_angka_id_anda
   MENDELEY_CLIENT_SECRET=masukkan_secret_anda
   ```
6. **Otorisasi (Hanya Sekali):** Buka terminal dan jalankan skrip otorisasi berikut:
   ```bash
   python ~/.gemini/config/skills/office-cli/scripts/mendeley_setup.py
   ```
   *(Browser akan terbuka untuk meminta izin login Mendeley. Setelah sukses, token akan tersimpan aman).*

*(Catatan untuk Agen: File `.env` dan token `*.json` sudah otomatis terlindungi oleh `.gitignore` sehingga tidak akan ikut ter-publish ke publik. Skrip integrasi ini dibangun murni menggunakan `urllib` bawaan Python (Zero-Dependency) untuk menembus proteksi Cloudflare Mendeley, sehingga agen **TIDAK PERLU** menyuruh klien melakukan `pip install` apapun. Setelah setup klien selesai, agen siap menggunakan skrip `mendeley_upload.py` untuk menginjeksi metadata PDF).*

---

### 10.1.6 Inisialisasi & Pipeline Zotero Headless (Pilihan Utama / Recommended)

> [!IMPORTANT]
> **STANDAR EMAS RISET: ZOTERO HEADLESS + KOREKSI METADATA KANONIKAL**  
> Zotero adalah reference manager open-source berstandar universal (CSL-JSON). Dalam arsitektur headless, agen AI mengelola Zotero secara senyap di latar belakang menggunakan pustaka resmi `pyzotero` tanpa perlu membuka aplikasi GUI desktop.

#### A. Konfigurasi Kredensial di `.env`
Kredensial disimpan secara aman di berkas lokal `~/.gemini/config/skills/office-cli/.env`:
```env
# Zotero API Credentials (Headless Mode)
# Diperoleh dari: https://www.zotero.org/settings/keys
ZOTERO_USER_ID="12345678"
ZOTERO_API_KEY="aBcDeFgHiJkLmNoPqRsTuVwX"
```
- **`ZOTERO_USER_ID`**: Angka 7–8 digit ID pengguna yang tertera di bagian atas halaman API settings.
- **`ZOTERO_API_KEY`**: String rahasia hasil pembuatan kunci baru (*Create new key*) dengan hak akses baca/tulis library.

#### B. Pipeline 3-Lapis Pembersihan & Koreksi Metadata (`zotero_clean_metadata.py`)
Sebelum paper didaftarkan ke Zotero, seluruh metadata mentah wajib disaring melalui pipeline koreksi otomatis guna mencegah error saat disitir di Word:
1. **Lapisan 1 (Canonical CrossRef Fetcher):**
   - Jika paper memiliki DOI, sistem menembak CrossRef API resmi (`api.crossref.org/works/{doi}`).
   - Menarik data primer penerbit: judul artikel murni, nama lengkap pengarang terpisah, nama resmi jurnal (bukan singkatan rusak), volume, nomor terbitan (*issue*), halaman, dan tahun pasti.
2. **Lapisan 2 (Heuristic Title & Author Normalizer):**
   - **Anti-ALL-CAPS**: Judul huruf besar semua (`DELVING DEEP INTO...`) dinormalisasi otomatis menjadi *Title Case / Sentence Case* akademik dengan tetap mengamankan akronim ilmiah (`CNN`, `ESP32`, `IoT`, `STFT`, `USV`, `AI`).
   - **Pemisahan Penulis Majemuk**: Mengurai format string gabungan (`Chen, J., & Ran, X.`) menjadi entitas resmi Zotero: `[{'creatorType': 'author', 'firstName': 'Jiasi', 'lastName': 'Chen'}, ...]`. Mencegah bug fatal Zotero di mana multi-penulis dianggap satu nama panjang.
   - **Normalisasi Tahun**: Memvalidasi 4 digit tahun kalender publikasi resmi.
3. **Lapisan 3 (Deduplikasi Koleksi):**
   - Mengecek apakah DOI atau judul yang sama sudah ada di koleksi Zotero Cloud pengguna untuk mencegah duplikasi item.

#### C. Alur Sinkronisasi & Peta Item Key (`zotero_headless_sync.py`)
1. Agen menjalankan skrip sinkronisasi headless:
   ```bash
   python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py
   ```
2. Skrip otomatis membuat koleksi baru (misal: `"Pengusir Tikus Pintar"`), mengunggah item yang telah bersih, dan menerbitkan berkas `zotero_item_keys.json`.
3. Berkas JSON ini berisi pemetaan ID nyata: `{"Chen & Ran, 2019": "K9J3X8AZ", ...}`.

#### D. Injeksi Field Code Zotero ke Dokumen Word (`.docx`)
Saat agen menyusun berkas Word, agen menyematkan struktur OpenXML Field Code resmi Zotero:
```xml
<w:r><w:fldChar w:fldCharType="begin"/></w:r>
<w:r><w:instrText xml:space="preserve"> ADDIN ZOTERO_ITEM CSL_CITATION {"citationID":"...","citationItems":[{"id":123,"uris":["http://zotero.org/users/local/items/ITEM_KEY"]}]} </w:instrText></w:r>
<w:r><w:fldChar w:fldCharType="separate"/></w:r>
<w:r><w:t>(Chen &amp; Ran, 2019)</w:t></w:r>
<w:r><w:fldChar w:fldCharType="end"/></w:r>
```
**Hasil Nyata:**
- Dokumen Word yang dihasilkan terhubung 100% secara resmi ke database Zotero pengguna.
- Ketika pengguna membuka Word di laptop yang terpasang Zotero, tab Zotero langsung aktif mengenali seluruh kutipan.
- Pengguna dapat mengutip kembali paper yang sama langsung lewat jendela pencarian Zotero di Word tanpa perlu mengetik ulang data referensi.

---

### 10.2 Protokol Validasi PDF Sebelum Upload ke Mendeley (4 Langkah Wajib)

> [!CAUTION]
> **DILARANG KERAS** mengupload PDF langsung ke Mendeley tanpa menjalankan Langkah 1 (validasi identitas). Mendeley sering salah mengekstrak metadata dari PDF — terutama untuk paper konferensi dan jurnal lokal (SINTA).

#### Langkah 1 — Baca Identitas Paper via `markitdown`

Sebelum menyentuh Mendeley, ekstrak metadata dari file PDF untuk verifikasi:

```powershell
python -m markitdown "REFERENSI/Koto_2021_IndoBERTweet.pdf" > "REFERENSI/_temp_baca.md"
```

Lalu baca output `_temp_baca.md` dan **ekstrak 7 field wajib** berikut:

| Field | Yang Dicari | Contoh Nilai |
| :--- | :--- | :--- |
| **Judul** | Judul lengkap artikel | *IndoBERTweet: A Pretrained Language Model...* |
| **Penulis** | Semua nama penulis (urutan benar) | Fajri Koto, Jey Han Lau, Timothy Baldwin |
| **Tahun** | Tahun publikasi | 2021 |
| **Venue / Jurnal** | Nama jurnal atau prosiding konferensi | EMNLP 2021 |
| **Volume & Issue** | Jika jurnal (bukan prosiding) | Vol. 5, No. 2 |
| **Halaman** | Halaman awal–akhir | 10123–10134 |
| **DOI** | Tautan DOI resmi | https://doi.org/10.18653/v1/2021.emnlp-main.796 |

Jika ada field yang **tidak ditemukan** di PDF (terutama DOI untuk paper lama), agen **WAJIB** mencarinya via web search sebelum lanjut ke Langkah 2.

#### Langkah 2 — Koreksi & Persiapan Data (Oleh Agen AI)
Agen AI **WAJIB** mencocokkan 7 field tersebut dari hasil ekstraksi. Jika ada yang salah/kurang (misal DOI tidak ada, atau nama jurnal disingkat), agen harus mencari kebenaran datanya via *Web Search* dan menyiapkan *dictionary* Python berisi metadata yang benar.

#### Langkah 3 — Upload Otomatis via API (Metadata + PDF + BibTeX)
Setelah data dipastikan 100% akurat, agen menggunakan skrip global `mendeley_upload.py` untuk melakukan 3 tugas sekaligus secara otomatis: mengunggah metadata, melampirkan PDF fisik, dan membuat ekspor lokal `references.bib`.

**Contoh kode eksekusi bagi agen:**
```python
import sys
import os
sys.path.append(os.path.expanduser('~/.gemini/config/skills/office-cli/scripts'))
from mendeley_upload import create_document

doc_data = {
    "title": "IndoBERTweet: A Pretrained Language Model...",
    "type": "journal",
    "authors": [
        {"first_name": "Fajri", "last_name": "Koto"},
        {"first_name": "Jey Han", "last_name": "Lau"}
    ],
    "year": 2021,
    "source": "Proceedings of EMNLP",
    "identifiers": {"doi": "10.18653/v1/2021.emnlp-main.796"}
}

# Upload metadata, attach PDF, dan append ke BibTeX
create_document(
    doc_data=doc_data, 
    pdf_path="c:/path/ke/proyek/REFERENSI/Koto_2021_IndoBERTweet.pdf",
    bibtex_dir="c:/path/ke/proyek/REFERENSI/"
)
```

#### Langkah 4 — Konfirmasi Final
Tandai status entry di `REFERENSI/README.md` proyek klien menjadi ✅. Klien sekarang bisa melihat referensi beserta PDF fisiknya langsung di aplikasi Mendeley.

---

### 10.3 Konvensi Penulisan Sitasi Sementara (Placeholder)

Karena agen tidak dapat menyisipkan *field* Mendeley Cite secara interaktif ke dalam Microsoft Word, agen **WAJIB** meninggalkan jejak penanda (*placeholder*) yang sangat jelas di dalam draf teks yang ditulisnya. Tujuannya agar klien dapat dengan mudah mencari paper tersebut di panel Mendeley Cite tanpa takut tertukar dengan paper bersampul/penulis mirip.

**Format Penanda Wajib:**
`[CITE: NamaBelakang Tahun, 3-Kata-Pertama-Judul]`

**Contoh Penulisan oleh Agen di Naskah:**
> Penggunaan model bahasa pra-latih sangat efektif untuk klasifikasi teks di media sosial `[CITE: Koto 2021, IndoBERTweet A Pretrained]`. Hal ini mendukung arsitektur *transformer* dasar yang telah diusulkan sebelumnya `[CITE: Devlin 2019, BERT Pre-training of]`.

Dengan format yang detail ini, klien cukup mengetik/menyalin kata kunci tersebut ke kolom pencarian *Mendeley Cite* di Word, lalu menimpa *placeholder* tersebut dengan sitasi interaktif yang asli.

---

### 10.4 Aturan Sinkronisasi Daftar Pustaka SINTA dari Mendeley

Karena metadata dan file PDF sudah terinjeksi sempurna ke Mendeley klien, sinkronisasi ke naskah Word menjadi sangat mudah:

#### Format Export untuk Jurnal SINTA (APA 7th Edition)
1. **Opsi 1 (Otomatis & Interaktif):** Klien tinggal membuka Microsoft Word, mengaktifkan **Mendeley Cite add-in**, cari penanda `[CITE: ...]` di naskah, lalu pilih *Insert Citation* dengan style **APA 7th Edition**. Daftar pustaka otomatis akan ter-generate di akhir naskah.
2. **Opsi 2 (Fallback / Auto Cite Lokal):** Jika Mendeley Cite klien bermasalah, klien bisa langsung menggunakan file `REFERENSI/references.bib` yang digenerate otomatis oleh agen. File `.bib` ini bisa dibuka di LaTeX, Zotero, atau alat Word bibliografi pihak ketiga tanpa bergantung pada internet.

#### Checklist Final Daftar Pustaka SINTA

> [!IMPORTANT]
> **TEMPORAL AWARENESS (KESADARAN WAKTU):** Agen AI **WAJIB** menyadari bahwa tahun saat ini adalah **2026** setiap kali mem-filter atau mencari referensi. Jangan merekomendasikan literatur usang yang melanggar batas usia SINTA.

| Syarat | Keterangan |
| :--- | :--- |
| ✅ Urutan A–Z | Berdasarkan nama belakang penulis pertama |
| ✅ Format APA 7th | `Penulis. (Tahun). Judul. *Jurnal*, *Vol*(Issue), halaman. DOI` |
| ✅ *Hanging Indent* 1,27 cm | Baris kedua dan seterusnya menjorok ke kanan |
| ✅ Spasi 1.0x (single) | Antar baris dalam satu entri |
| ✅ Spasi setelah entri | Tambahkan spasi 6–10pt antar entri |
| ✅ DOI aktif & dapat diklik | Format `https://doi.org/xxx` dalam hyperlink biru |
| ✅ Minimal 15 sitasi | Jurnal SINTA umumnya mensyaratkan ≥ 15 referensi primari |
| ✅ **80% Literatur Terkini** | **Minimal 80% referensi WAJIB berusia maksimal 10 tahun terakhir (Batas minimal tahun terbit = 2016 karena saat ini adalah 2026).** |
| ❌ Dilarang `[1], [2]` | APA bukan IEEE; jangan pakai penomoran dalam kurung siku |

---

### 10.5 Tabel Masalah Umum Mendeley & Solusinya

| Masalah | Penyebab | Solusi |
| :--- | :--- | :--- |
| Judul terpotong atau salah kapital | OCR PDF gagal ekstrak teks bersih | Edit manual di panel detail |
| Semua penulis tercampur jadi satu nama | Mendeley gagal parse separator | Pisahkan manual: `Koto, F.` kemudian `Lau, J. H.` dst |
| Tahun kosong atau salah | PDF metadata tidak terisi | Cek halaman cover PDF, isi manual |
| DOI kosong untuk paper konferensi | PDF tidak menyematkan DOI di metadata | Cari DOI via `doi.org` atau `semanticscholar.org` |
| Nama jurnal dalam bahasa Inggris singkat | Mendeley tidak tahu nama lengkap | Isi dengan nama lengkap resmi prosiding |
| Duplikat entri | Drag & drop dua kali | Hapus duplikat via `Edit > Select Duplicates > Delete` |
| Plugin Word tidak muncul | Mendeley belum terinstal Add-in | Buka Mendeley → `Tools > Install MS Word Plugin` |

---

### 10.6 "BULLDOZER MODE" (FULL-AUTO ROBUST SCRIPTING)

Jika klien memerintahkan untuk mengunduh dan menyinkronkan seluruh referensi secara massal (misalnya: *"download semua sitasi dan jalanin mendeley auto full"* atau *"pakai bulldozer mode"*), agen **WAJIB** mengeksekusi otomatisasi tangguh dengan spesifikasi berikut:

1. **Pembuatan Skrip Unduhan & Unggahan Gabungan (`scratch/auto_download_robust.py`):**
   Agen menulis skrip Python yang memproses daftar referensi dalam loop panjang.
2. **Fallback API Ganda:**
   Skrip mencari metadata dan URL PDF Open Access dengan mencoba **OpenAlex API** terlebih dahulu (tanpa key). Jika gagal, jatuh kembali (*fallback*) ke **CrossRef API**.
3. **Integritas Akademik Mutlak (No PDF = No Cite):**
   Jika PDF fisik gagal diunduh atau terkunci *paywall*, skrip **DILARANG KERAS** melakukan "Force Upload" metadata ke Mendeley. Mengutip referensi tanpa memiliki dan membaca dokumen aslinya adalah pelanggaran integritas akademik. Skrip wajib jujur mencatat status *Gagal/Paywalled* di log, dan **TIDAK** mendaftarkan paper tersebut ke Mendeley. Klien harus tahu paper mana yang gagal didapat agar tidak dikutip.
4. **Timer Berkala (`schedule`):**
   Agen wajib membungkus proses eksekusi latar belakang dengan `manage_task` dan `schedule` (contoh: Timer 60 detik) untuk memantau kemajuan log secara reguler dan terus memberikan laporan (*progress update*) kepada klien, tanpa memaksa klien menunggu dalam diam.

---

### 10.7 "VISUAL BROWSER AGENT" (OTORITAS BYPASS BLOKIR API)

Jika skrip *Bulldozer Mode* (berbasis API Python) gagal mengunduh PDF Open-Access karena diblokir oleh anti-bot atau captcha (seperti pada Semantic Scholar, Elsevier, atau ArXiv timeout), agen memiliki **Otoritas** penuh untuk membangkitkan sub-agen peramban visual (`browser_subagent`).

1. **Simulasi Manusia:** Sub-agen ini akan mengendalikan Google Chrome asli, mengetikkan kata kunci layaknya manusia (contoh: *'Attention Is All You Need arxiv pdf'*), dan menelusuri halaman web untuk mencari *Direct Link* PDF yang gagal dijangkau oleh skrip statis.
2. **Penyedotan Pasca-Pencarian:** Setelah sub-agen kembali dengan URL PDF murni, agen utama akan menggunakan Python untuk menarik file tersebut ke dalam folder `REFERENSI/` dan menyuntikkannya ke Mendeley secara legal, mematuhi prinsip Integritas Akademik.
3. **Pemicu:** Mode ini bisa ditawarkan oleh agen jika API gagal berulang kali, atau dipicu klien dengan perintah seperti *"Gunakan browser agent"*, *"Cari pakai Chrome"*, atau *"Akali pakai headless browser"*.

### 10.8 GOLDEN RULE: ITERASI = BULLDOZER MODE
Setiap tugas yang membutuhkan iterasi berulang (seperti mencoba mengunduh puluhan file, merevisi skrip pencarian berkali-kali, atau memecahkan masalah API yang terus gagal) **WAJIB menggunakan pendekatan Bulldozer Mode**. Agen tidak boleh melakukan iterasi panjang secara sinkron. Agen harus mendelegasikan iterasi ke latar belakang (`run_command` dengan timer, skrip Python `while/for` yang tangguh, atau `browser_subagent`) dan melaporkan hasilnya secara asinkron kepada klien. Jangan menahan interaksi (*block*) untuk tugas iteratif!

### Referensi Dokumen Spesifik
- Jika tugas melibatkan **Surat Permohonan Insentif**, **WAJIB** merujuk ke pedoman detail di [pedoman_surat_insentif.md](file:///C:/Users/masdayat/.gemini/config/skills/office-cli/references/pedoman_surat_insentif.md) untuk menghindari *error formatting* berulang.
- Jika tugas melibatkan **Laporan Praktikum Umum / LHP Singkat**, **WAJIB** merujuk ke [pedoman_laporan_praktikum.md](file:///C:/Users/masdayat/.gemini/config/skills/office-cli/references/pedoman_laporan_praktikum.md).
- Jika tugas melibatkan **LKM (Laporan Keseluruhan Modul) Metode Numerik**, **WAJIB MUTLAK** merujuk ke pedoman spesifik di [pedoman_lkm_metode_numerik.md](file:///C:/Users/masdayat/.gemini/config/skills/office-cli/references/pedoman_lkm_metode_numerik.md).
  - **Pembedaan Hirarki**: LHP (singkat, tanpa bab/TOC, hanya tugas praktek lab) vs LKM (monograf lengkap 5 bab, template `template_lkm_metode_numerik.docx`, cover, kata pengantar, TOC native Word Automatic Table 1, Bab I-V, daftar pustaka).
  - **Dilarang Merusak LKM**: Jangan pernah mengubah atau merusak dokumen LKM menjadi LHP saat pengguna meminta perbaikan atau revisi tugas!
  - **Pola Mahasiswa Logis di BAB IV (Anti-Yapping)**: Wajib ikuti alur mahasiswa: Soal & Matriks -> Kode & Output Konsol Scilab Langsung di Satu Box -> Komentar & Penjelasan di Bawahnya. Dilarang yapping/esai bertele-tele di depan dan dilarang membuat subbab 4.3 pembahasan terpisah yang redundan.
  - **Persamaan Matriks Native 2D (OMML XML)**: Matriks dan determinan wajib dirender sebagai persamaan matematika 2D native Word (kurung siku `[]` untuk matriks, garis tegak vertikal `||` untuk determinan).
  - **Zero PDF**: Berkas diserahkan dalam format DOCX mentah; dilarang otomatis membuat PDF kecuali diminta secara eksplisit.
- Jika tugas melibatkan **Artikel Jurnal IASSSF (Institute for Advanced Social, Science, and Sustainable Future)**, **WAJIB MUTLAK** merujuk ke pedoman spesifik di [pedoman_jurnal_iasssf.md](file:///c:/Users/masdayat/.gemini/config/skills/office-cli/references/pedoman_jurnal_iasssf.md).
  - **Master Template Wajib**: Gunakan [`templates/Template IASSSF.docx`](file:///c:/Users/masdayat/.gemini/config/skills/office-cli/templates/Template%20IASSSF.docx) sebagai basis dokumen resmi (A4, 1 kolom penuh, margin 2.0-2.5-3.0-3.0 cm, banner/logo resmi, footer CC-BY 4.0).
  - **Tipografi 100% Cambria**: Seluruh teks menggunakan font Cambria (Judul 16pt Bold, Penulis 11pt Bold, Afiliasi 10pt Italic, Abstrak 9pt, Heading Utama 12pt Bold, Sub-heading 11pt Italic, Isi 11pt Justified, Keterangan 10pt, Running Header/Footer 8-10pt).
  - **Abstrak Wajib 1 Paragraf Tunggal**: Abstrak ditulis dalam satu paragraf mengalir (Cambria 9pt Justified, 200–250 kata, bebas sitasi) dengan 5 label tebal inline: **Background:**, **Methods:**, **Findings:**, **Conclusion:**, dan **Novelty/Originality of this article:**. Format kata kunci: `KEYWORDS:` (12pt Bold) `: ` (9pt Bold) `keyword 1; keyword 2; keyword 3.` (11pt Regular).
  - **Batas Kata & Kuantitas Referensi**:
    - *Original Research Article*: 6.000–7.000 kata (di luar referensi), jumlah referensi **> 30**.
    - *Review Article*: 7.000–9.000 kata (di luar referensi), jumlah referensi **>= 50**.
    - Minimal 80% sumber primer jurnal Scopus/WoS 5–10 tahun terakhir (2016–2026), format APA 7th via Mendeley, tautan DOI aktif wajib.
  - **Standar Persamaan Native OMML**: Rumus matematika display wajib berupa Native Word Equation (`<m:oMath>` / Cambria Math) dalam borderless 2-column table (`Inches(5.1)` center untuk formula, `Inches(0.8)` right untuk `(Eq. X)`). Dilarang teks raw LaTeX!
  - **Larangan Mengarang Tanggal Editorial**: Baris `Received Date:`, `Revised Date:`, `Accepted Date:` wajib dikosongkan sebagai placeholder editorial.
  - **Integritas Referensi 100% Real (Anti-Halu)**: Dilarang menyisipkan referensi eksternal secara sepihak untuk memenuhi kuota >30 refs. Sajikan sebagai audit, sodorkan rekomendasi ber-DOI, dan unduh PDF Open Access ke `referensi/rekomendasi_internasional/`.
  - **Dua Larangan Mutlak Sitasi (Strictly Forbidden)**:
    1. **HARAM** menyitasi artikel yang pernah terbit di jurnal IASSSF itu sendiri (*Zero IASSSF self-citation*).
    2. **HARAM** melakukan sitasi-diri (*author self-citation*) tanpa justifikasi ceruk topik yang mendesak.
  - **Bagian Belakang Wajib (*Mandatory Unnumbered Back Matter*)**: Acknowledgement, Author Contribution (CRediT formal), Funding, Ethical Review Board Statement, Informed Consent Statement, Data Availability Statement, Conflicts of Interest, Declaration of Generative AI Use, Open Access (CC-BY 4.0), References, dan Kotak Tabel `Biographies of Author(s)` (1 sel berbingkai, foto/narasi max 100 kata, Email, ORCID, WoS ID, Scopus ID, Homepage).
  - **Pembersihan Bagian Panduan**: Teks `PAPER TEMPLATE` dan instruksi persiapan di akhir berkas template wajib dihapus saat menerbitkan naskah final.
  - **🚨 PROTOKOL "ANTI-SOK TAU" (VERIFIKASI ASSET & METADATA)**: Agen **DILARANG KERAS MENGARANG ATAU BERHALUSINASI** terkait gambar eksperimen, data kuantitatif, nomor protokol etik, nomor kontrak hibah, ID peneliti (ORCID, Scopus, WoS), maupun link repositori data. Jika ada asset atau metadata yang belum tersedia, agen **WAJIB** menandai `[TODO: USER ACTION REQUIRED]` dan menyajikan rekap checklist kekurangan secara eksplisit agar pengguna dapat menyiapkannya.
