---
name: office-cli
description: Unified Document Suite for AI Agents. Fast multi-format extraction to Markdown via Microsoft MarkItDown, and programmatic authoring/manipulation of Microsoft Office documents (Word, Excel, PowerPoint) via OfficeCLI.
---

# Unified Office & Document Suite (MarkItDown + OfficeCLI)

Skill ini merupakan ekosistem terpadu untuk penanganan dokumen digital bagi AI coding agent. Mengintegrasikan kemampuan **ekstraksi cerdas multi-format ke Markdown** menggunakan **Microsoft MarkItDown** dan **pembuatan/manipulasi dokumen Office native** menggunakan **OfficeCLI**, dengan kepatuhan penuh terhadap standar publikasi ilmiah nasional terakreditasi **SINTA (SINTA 1–6)**, jurnal internasional **Scopus (Q1–Q4)**, serta laporan akademik formal (Skripsi, Tesis, Kerja Praktik).

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
│   └── template_laporan_kerja_praktik.docx  # Master template Laporan KP / Magang Industri
└── references/
    ├── pedoman_jurnal_sinta.md              # Panduan lengkap penulisan jurnal SINTA 1-6 (IMRaD baku)
    ├── pedoman_jurnal_scopus.md             # Panduan jurnal internasional bereputasi Scopus Q1-Q4
    ├── pedoman_skripsi_lengkap.md           # Pedoman penulisan Skripsi / Tesis 5 Bab standar nasional
    ├── pedoman_kerja_praktik.md             # Pedoman penyusunan Laporan Kerja Praktik & Magang
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

---

## 4. STANDAR PENULISAN NASKAH ILMIAH (FOKUS UTAMA: JURNAL SINTA 1–6)

### Tabel 3. Matriks Perbandingan Format Naskah Ilmiah
| Parameter Format | Jurnal SINTA 1–6 (Standar Utama) | Jurnal Internasional Scopus (Q1–Q4) | Skripsi / Tugas Akhir (Monograf) |
| :--- | :--- | :--- | :--- |
| **Batas Tepi (Margin)** | **2,54 cm (1 inci) Simetris** di seluruh sisi | **2,54 cm (1 inci)** atau format 2 kolom | **4-4-3-3 cm** (Left 4 cm ruang jilid) |
| **Font & Spasi Isi** | Times New Roman 11–12 pt, spasi **1.15x**, Justified | Times New Roman / Arial 10–11 pt, spasi 1.0–1.15x | Times New Roman 12 pt, spasi **1.5x**, Justified |
| **Struktur Bab / Seksi** | **DILARANG kata 'BAB'** (`1. PENDAHULUAN`, `2. METODE`) | **DILARANG kata 'BAB'** (`1. Introduction`, `2. Methods`) | **WAJIB kata 'BAB'** (`BAB I PENDAHULUAN`) |
| **Aliran Halaman** | **Continuous Flow** (Dilarang *Page Break* antar-seksi) | Continuous Flow (1 kolom / 2 kolom) | **Wajib Page Break** di setiap bab baru |
| **Abstrak & Identitas** | **Wajib Page 1 Fit**, bilingual, 150–200 kata, spasi 1.0x | Structured / Unstructured, 200–250 kata, Full English | Intisari 3 Alinea baku, TNR 10 pt spasi 1.0x |
| **Standar Tabel** | **Format APA (3 Garis Horizontal)**, tanpa garis vertikal | Format APA murni, judul di atas tabel | Format APA / Boxed (sesuai pedoman kampus) |
| **Gaya Sitasi** | **APA 7th Edition** (atau IEEE), 15–25 rujukan mutakhir | APA 7th / IEEE / Elsevier, 30–50 rujukan Scopus | APA 7th / IEEE, terbagi primer dan sekunder |

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
| **Resep Batch OfficeCLI** | Koleksi batch JSON siap pakai untuk heading 1-3, TOC otomatis, tabel APA, gambar, dan hanging indent. | [`references/resep_officecli_dokumen_ilmiah.md`](references/resep_officecli_dokumen_ilmiah.md) |
| **Master Template Jurnal SINTA** | Berkas Word DOCX resmi OJS SINTA (A4, 2,54 cm simetris, Page 1 Fit, tabel APA, bebas mojibake/JEL). | [`templates/template_jurnal_sinta.docx`](templates/template_jurnal_sinta.docx) |
| **Master Template Skripsi 5 Bab** | Berkas Word DOCX resmi Skripsi/TA (A4, 4-3-3-3 cm, TNR 12 pt spasi 1.25x, preliminary Romawi). | [`templates/template_laporan_tugas_akhir.docx`](templates/template_laporan_tugas_akhir.docx) |
| **Master Template Laporan KP** | Berkas Word DOCX resmi Laporan Kerja Praktik/Magang Industri struktur perusahaan lengkap. | [`templates/template_laporan_kerja_praktik.docx`](templates/template_laporan_kerja_praktik.docx) |
