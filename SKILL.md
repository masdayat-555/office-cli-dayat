---
name: office-cli
description: Unified Document Suite for AI Agents. Fast multi-format extraction to Markdown via Microsoft MarkItDown, and programmatic authoring/manipulation of Microsoft Office documents (Word, Excel, PowerPoint) via OfficeCLI.
---

# Unified Office & Document Suite (MarkItDown + OfficeCLI)

Skill ini merupakan ekosistem terpadu untuk penanganan dokumen digital bagi AI coding agent. Mengintegrasikan kemampuan **ekstraksi cerdas multi-format ke Markdown** menggunakan **Microsoft MarkItDown** dan **pembuatan/manipulasi dokumen Office native** menggunakan **OfficeCLI**, dengan kepatuhan penuh terhadap standar publikasi ilmiah nasional terakreditasi **SINTA (SINTA 1–6)**, jurnal internasional **Scopus (Q1–Q4)**, serta laporan akademik formal (Skripsi, Tesis, Kerja Praktik).

---

## 00. LARANGAN TERTINGGI (SUPREME DIRECTIVE)

> [!CAUTION]
> **DILARANG KERAS MENGGUNAKAN LIBRARY PIHAK KETIGA LAIN (`python-docx`, `openpyxl`, `python-pptx`, dll) UNTUK MENULIS ATAU MEMODIFIKASI DOKUMEN OFFICE.**
> 
> Seluruh operasi pembuatan, mutasi, dan penyuntingan file Office (.docx, .xlsx, .pptx) **WAJIB MUTLAK** menggunakan `officecli` dengan memanfaatkan perintah `batch` atau operasi CLI-nya. Library eksternal hanya boleh digunakan JIKA DAN HANYA JIKA pengguna memberikan izin eksplisit atau `officecli` benar-benar terbukti secara teknis tidak mampu melakukan tugas tersebut.
> 
> Pengecualian hanya berlaku untuk **pembacaan (read-only)**: `markitdown` adalah standar resmi yang diizinkan untuk membaca dokumen.

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
│   └── check_update.py                      # Skrip auto-update berkala dari upstream GitHub
├── templates/
│   ├── template_jurnal_sinta.docx           # Master template OJS SINTA (A4, 1-inch, Page 1 Fit, APA Table)
│   ├── template_laporan_tugas_akhir.docx    # Master template Skripsi / TA (A4, 4-3-3-3 cm, 5 Bab)
│   ├── template_laporan_kerja_praktik.docx  # Master template Laporan KP / Magang Industri
│   └── template_laporan_praktikum.docx      # Master template Laporan Praktikum (Cover luwes, native TOC)
└── references/
    ├── pedoman_jurnal_sinta.md              # Panduan lengkap penulisan jurnal SINTA 1-6 (IMRaD baku)
    ├── pedoman_jurnal_scopus.md             # Panduan jurnal internasional bereputasi Scopus Q1-Q4
    ├── pedoman_skripsi_lengkap.md           # Pedoman penulisan Skripsi / Tesis 5 Bab standar nasional
    ├── pedoman_kerja_praktik.md             # Pedoman penyusunan Laporan Kerja Praktik & Magang
    ├── pedoman_laporan_praktikum.md         # Pedoman Laporan Praktikum (struktur bab, format cover)
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
> 2. Bersifat *non-blocking*: Jika offline atau tidak ada remote git, lewati dan jangan gagalkan tugas utama pengguna.

### Tabel 2. Checklist Alat & Perintah Verifikasi / Instalasi
| Tool | Pengembang & Repositori Resmi | Perintah Pengecekan | Perintah Instalasi (Jika Belum Ada) |
| :--- | :--- | :--- | :--- |
| **Microsoft MarkItDown** | [microsoft/markitdown](https://github.com/microsoft/markitdown) | `markitdown --version`<br>atau `python -m markitdown --version` | `pip install markitdown`<br>*(opsional: `pip install markitdown[all]`)* |
| **OfficeCLI** | [officecli.ai](https://officecli.ai) / [github.com/officecli](https://github.com/officecli) | `officecli --version` | **Windows PowerShell:**<br>`irm https://d.officecli.ai/install.ps1 \| iex`<br>**Linux / macOS (Bash):**<br>`curl -fsSL https://d.officecli.ai/install.sh \| bash` |
| **pypdf** *(On-Demand)* | [py-pdf/pypdf](https://github.com/py-pdf/pypdf) | `python -c "import pypdf; print(pypdf.__version__)"` | `pip install pypdf` *(khusus ekstraksi gambar PDF)* |
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

### 3.4 Konversi Hasil Akhir ke PDF (Trigger: "sudah ok")
- Jika pengguna memberikan instruksi **"sudah ok"** (atau menyatakan laporan sudah final), ini adalah tanda bahwa dokumen DOCX sudah siap dan harus disubmit ke LMS.
- Agen AI **WAJIB** segera mengonversi file DOCX final tersebut menjadi PDF menggunakan library `docx2pdf`.
- **DILARANG** menggunakan library pembaca seperti `pypdf` untuk konversi DOCX.
- Skrip konversi (jalankan dari direktori file, pastikan file DOCX tertutup dari MS Word):
   ```python
   from docx2pdf import convert
   convert("24330030_SalimHidayat_LaporanModul1_PAW.docx")
   ```
- Setelah sukses, laporkan kepada pengguna bahwa file PDF siap diunggah ke LMS.

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
| **TOC (Daftar Isi) Manual** | Menyusun TOC menggunakan ketikan hardcoded spasi/titik dengan `python-docx`. | Dokumen ditolak (*slop*), tidak dinamis, statis dan palsu. | **DILARANG KERAS** mengetik TOC manual. Wajib gunakan `{"type": "toc"}` via OfficeCLI untuk memanggil field native Word. |
| **Pengaturan Posisi Cover** | Mengandalkan nilai `space_before` / `space_after` yang raksasa (mis. 150pt) untuk mendorong teks ke margin bawah. | Teks cover *overflow* ke halaman berikutnya, ukuran sulit diprediksi jika gambar berubah, layout kaku. | **Gunakan spasi (Enter / paragraf kosong)** untuk mendorong blok teks sampul, atau atur ruang sewajarnya tanpa pt ekstrem. |
| **Efek Samping doc.add_page_break**| Memanggil `doc.add_page_break()` di `python-docx` di akhir elemen. | Menghasilkan paragraf kosong *siluman* di halaman sebelum break yang memakan ruang 1 baris vertikal. | Sisipkan break langsung di dalam run terakhir: `p.runs[-1].add_break(WD_BREAK.PAGE)` atau setel properti *Page break before*. |

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
| **Pedoman Skripsi Lengkap** | Panduan penyusunan Skripsi/Tesis 5 Bab standar nasional, preliminary pages, hingga lampiran. | [`references/pedoman_skripsi_lengkap.md`](references/pedoman_skripsi_lengkap.md) |
| **Pedoman Kerja Praktik** | Panduan penyusunan Laporan KP/Magang Industri (profil mitra, SOP, proyek, evaluasi mutu). | [`references/pedoman_kerja_praktik.md`](references/pedoman_kerja_praktik.md) |
| **Pedoman Laporan Praktikum** | Panduan Laporan Praktikum baku (Cover luwes, native TOC, struktur wajib). | [`references/pedoman_laporan_praktikum.md`](references/pedoman_laporan_praktikum.md) |
| **Resep Batch OfficeCLI** | Koleksi batch JSON siap pakai untuk heading 1-3, TOC otomatis, tabel APA, gambar, dan hanging indent. | [`references/resep_officecli_dokumen_ilmiah.md`](references/resep_officecli_dokumen_ilmiah.md) |
| **Master Template Jurnal SINTA** | Berkas Word DOCX resmi OJS SINTA (A4, 2,54 cm simetris, Page 1 Fit, tabel APA, bebas mojibake/JEL). | [`templates/template_jurnal_sinta.docx`](templates/template_jurnal_sinta.docx) |
| **Master Template Skripsi 5 Bab** | Berkas Word DOCX resmi Skripsi/TA (A4, 4-3-3-3 cm, TNR 12 pt spasi 1.25x, preliminary Romawi). | [`templates/template_laporan_tugas_akhir.docx`](templates/template_laporan_tugas_akhir.docx) |
| **Master Template Laporan KP** | Berkas Word DOCX resmi Laporan Kerja Praktik/Magang Industri struktur perusahaan lengkap. | [`templates/template_laporan_kerja_praktik.docx`](templates/template_laporan_kerja_praktik.docx) |
| **Master Template Laporan Praktikum**| Berkas Word DOCX resmi Laporan Praktikum. Dilarang generik, cover proporsional. | [`templates/template_laporan_praktikum.docx`](templates/template_laporan_praktikum.docx) |

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

### 8.8 Template Identitas (python-docx)

```python
# Margin narrow
for attr in ("left_margin","right_margin","top_margin","bottom_margin"):
    setattr(sec, attr, Cm(1.27))

# Judul center bold
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("JUDUL TUGAS"); r.bold = True
r.font.name = "Times New Roman"; r.font.size = Pt(13)

# Identitas — plain paragraph, TIDAK pakai tabel, TIDAK pakai hline
def id_line(label, value):
    p = doc.add_paragraph()
    r1 = p.add_run(f"{label:<16}: "); r1.bold = True
    r1.font.name = "Times New Roman"; r1.font.size = Pt(12)
    r2 = p.add_run(value)
    r2.font.name = "Times New Roman"; r2.font.size = Pt(12)

id_line("Nama", "Salim Hidayat / 24330030")
id_line("Mata Kuliah", "Metode Numerik")
doc.add_paragraph()  # spasi kosong sebelum konten soal
```

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
