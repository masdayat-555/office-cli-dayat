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
│   ├── template_laporan_praktikum.docx      # Master template Laporan Praktikum (Cover luwes, native TOC)
│   └── template_lhp_singkat.docx            # Master template Laporan Praktikum Singkat (Hanya Cover, Tanpa Bab/TOC)
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
> 2. **Pembaruan Instan (Prompt Trigger)**: Jika pengguna mengetik perintah seperti *"perbarui office cli"*, *"update officecli"*, atau variasi salah ketik (*typo*) lainnya yang bermaksud memperbarui, agen **WAJIB LANGSUNG** mengeksekusi perintah `git -C "<path_skill>" pull --rebase --autostash origin main` tanpa banyak bertanya.
> 3. Bersifat *non-blocking*: Jika offline atau tidak ada remote git, lewati dan jangan gagalkan tugas utama pengguna.

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
| **Master Template LHP Singkat**| Berkas Word DOCX resmi Laporan Praktikum khusus untuk penugasan singkat (hanya cover, tanpa BAB, tanpa TOC). | [`templates/template_lhp_singkat.docx`](templates/template_lhp_singkat.docx) |

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

### 9.5 Varian "LHP Singkat" (Tugas Praktikum Tanpa BAB)
Beberapa praktikum menghendaki format "LHP Singkat" (hanya *Cover Page* lalu langsung isi penugasan tanpa BAB dan tanpa TOC). Jika pengguna meminta format ini ("halaman judul langsung tugas", "tidak pakai bab"):
- **Gunakan Master Template `template_lhp_singkat.docx`**: Template ini sudah bersih dari Daftar Isi dan siap diinjeksi tugas.
- **Konvensi Penamaan File**: **WAJIB** menggunakan format `[NIM]_[Nama Lengkap]_LHP[Nomor Modul].docx` (Contoh: `24330030_Salim Hidayat_LHP1.docx`).
- **Gaya Penulisan Kode/Console**: Jika tugas meminta reka ulang *console* (tanpa *screenshot*), JANGAN gunakan label kaku seperti "Operator 1:". Gunakan langsung nomor asli dari modul diikuti penjelasannya (perbaiki *typo* modul secara mandiri *kecuali* disuruh patuh mutlak). Setelah teks penjelasan, sisipkan *output raw* dari *console* secara literal.
- **Peringatan Kritis Logo Cover**: Saat membersihkan halaman *cover* dari paragraf kosong untuk menyesuaikan tinggi spasi agar elemen bawah tidak meluap ke halaman dua, **WAJIB** mengecek apakah paragraf tersebut memiliki *runs* (contoh di `python-docx`: `p.text.strip() == "" and len(p.runs) == 0`). JANGAN menghapus paragraf kosong yang berisi logo Universitas (`len(p.runs) > 0`).

---

## 10. MANAJEMEN REFERENSI TERVALIDASI (MENDELEY + FOLDER REFERENSI)

> [!IMPORTANT]
> Bagian ini berlaku untuk **semua proyek penulisan ilmiah (Jurnal SINTA, Skripsi, Tesis)**. Tujuannya adalah memastikan seluruh sitasi dalam naskah berasal dari sumber yang sudah diverifikasi identitasnya — bukan hanya dari ingatan atau copy-paste abstrak.

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
