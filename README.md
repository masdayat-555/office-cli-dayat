<div align="center">

# 📄 Unified Document, Academic & Translation Suite for AI Agents
### (MarkItDown + OfficeCLI + Zotero Headless + Academic Translation Engine)

**Skill Pembuatan Dokumen, Manajemen Sitasi, & Penerjemahan Akademik Standar Scopus/EYD V untuk AI Coding Assistant.**  
*Membantu ekstraksi multi-format (PDF, DOCX, XLSX, PPTX), penyusunan dokumen Word sesuai pedoman (SINTA, Scopus, IASSSF, Skripsi, KP), integrasi sitasi otomatis via Zotero Headless, serta penerjemahan & penulisan ulang akademik Scopus Q1 bebas AI slop.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/masdayat-555/office-cli-dayat)
[![Zotero: Headless](https://img.shields.io/badge/Zotero-Headless%20API-red.svg)](https://www.zotero.org/)
[![Translation: Academic Rewriting](https://img.shields.io/badge/Translation-Scopus%20%7C%20EYD%20V-green.svg)]()
[![Manchester Phrasebank](https://img.shields.io/badge/Phrasebank-Manchester%2018%20Modules-blue.svg)]()
[![Standard](https://img.shields.io/badge/Standard-SINTA%201--6%20%7C%20Scopus%20Q1--Q4%20%7C%20IASSSF%20%7C%20APA%207th-purple.svg)]()

[🇮🇩 Bahasa Indonesia](#-bahasa-indonesia) • [🇬🇧 English](#-english-version)

---

</div>

<a name="-bahasa-indonesia"></a>
## 🇮🇩 Bahasa Indonesia

### ✨ Fitur Utama
Skill ini membekali asisten koding AI Anda (Antigravity, Cursor, Claude Code, Windsurf, VS Code, Roo Code, dll.) dengan kapabilitas native untuk **membaca**, **mengekstrak**, dan **menyusun** dokumen perkantoran profesional:

* 🎓 **Jurnal Terakreditasi SINTA 1–6:** Penyusunan naskah IMRaD baku, abstrak bilingual rapi, serta tabel ilmiah standar APA.
* 🌐 **Jurnal Bereputasi Scopus Q1–Q4 & WoS:** Struktur extended IMRaD, analisis perbandingan state-of-the-art, dan kepatuhan standar publikasi global.
* 🌿 **Jurnal Internasional IASSSF:** Format naskah resmi 1 kolom (Cambria), abstrak berstruktur, taksonomi peran CRediT, serta kelengkapan etika publikasi.
* 📚 **Skripsi & Tugas Akhir:** Hierarki 5 bab standar perguruan tinggi, daftar isi otomatis, serta penataan tipografi dan sitasi yang konsisten.
* 💼 **Laporan Kerja Praktik & Magang:** Format komprehensif profil mitra, alur kerja/SOP, logbook aktivitas mingguan, dan laporan teknis.
* 🔬 **Laporan Praktikum & LKM:** Laporan kegiatan laboratorium, monograf modul praktikum, dan penyajian data eksperimen terstruktur.
* 📑 **Ekstraksi Multi-Format:** Konversi cerdas berkas PDF, DOCX, XLSX, dan PPTX menjadi Markdown via Microsoft MarkItDown.
* 🖼️ **Ekstraksi Aset Visual:** Pengambilan gambar, bagan, dan diagram asli dari berbagai format dokumen dalam resolusi penuh.
* 🏷️ **Zotero Headless (Tool Sitasi & Referensi Otomatis):** Manajemen referensi dan sitasi otomatis secara senyap (*headless*) menggunakan pustaka `pyzotero`, verifikasi metadata kanonikal CrossRef, pengunggahan berkas PDF fisik ke cloud library, serta injeksi *field code* Word native (`ADDIN ZOTERO_ITEM` dan `ADDIN ZOTERO_BIBL`) tanpa membuka GUI Zotero.
* 🌐 **Academic Translation & Rewriting Engine (Scopus Q1 & EYD V):** Doktrin *Translation as Rewriting* untuk artikel jurnal dan buku teks akademik. Mengintegrasikan 18 modul fungsional *Manchester Academic Phrasebank*, pemotongan semantik buku panjang (1.500–2.500 kata & `GLOSSARY.json`), eliminasi kata klise bot AI (*delve*, *pivotal*, *tapestry*, dll.), serta linter deterministik otomatis (`linter_akademis_en.py` & `linter_tata_bahasa_id.py`).
* 🛡️ **DOCX OpenXML & Zotero Guard:** Skrip verifikasi zero-dependency (`docx_zotero_guard.py`) yang menjamin keutuhan 100% field code sitasi Zotero/Mendeley (`ADDIN ZOTERO_ITEM`) dan rumus native Word Equation (`<m:oMath>`) saat teks dialihbahasakan atau disunting.
* 🎯 **Output Word Asli (`.docx`):** Pembuatan dokumen OpenXML murni yang rapi dan siap pakai menggunakan OfficeCLI.

---

### 🌐 Academic Translation & Rewriting Engine (Scopus Q1 & EYD V)

Skill ini menghadirkan engine penerjemahan dan penulisan ulang akademik berbasis doktrin **"Translation as Academic Rewriting"**:
* ✍️ **Bukan Alih-Kata Harfiah:** Mencegah *"translationese"* (bahasa Inggris rasa struktur Indonesia) dengan mendekonstruksi anak kalimat bertingkat menjadi alur penalaran linier deduktif dengan kepadatan leksikal tinggi.
* 🏛️ **Manchester Academic Phrasebank:** Mengintegrasikan 18 modul fungsional resmi The University of Manchester untuk manuver retorika ilmiah (*Introducing Work, Describing Methods, Reporting Results, Discussing Findings, Cautious Language/Hedging*, dll.).
* 🛡️ **Proteksi Aset OpenXML (`docx_zotero_guard.py`):** Isolasi token otomatis sebelum teks dialihbahasakan sehingga field code Zotero (`ADDIN ZOTERO_ITEM`) dan rumus native Word Equation (`<m:oMath>`) **dijamin 100% utuh tanpa rusak/korup**.
* 📖 **Penerjemahan Dokumen Panjang & Buku (`translate-book`):** Didukung protokol pemotongan semantik (*semantic chunking* 1.500–2.500 kata) tepat pada batas sub-bab dan penguncian istilah teknis lintas bab via `GLOSSARY.json`.
* 🤖 **Linter Deterministik Non-LLM:**
  * `linter_akademis_en.py`: Memindai naskah bahasa Inggris secara kaku untuk membasmi kata klise AI (*delve, pivotal, tapestry, realm, foster, underscore, leverage*), personal pronouns (*we/our*), dan kesalahan koma desimal (*95,5%*).
  * `linter_tata_bahasa_id.py`: Memindai naskah bahasa Indonesia dari kata tidak baku KBBI (*merubah, analisa, sistim, efektifitas*), pleonasme, kalke kaku (*di mana, yang mana*), dan basa-basi robotik AI.

---

### 🚀 Cara Pemasangan (Instalasi)

#### 💬 Opsi 1: Salin & Tempel Prompt ke AI Agent Anda (Praktis)
Cukup salin dan tempel prompt di bawah ini langsung ke obrolan AI Assistant Anda (Antigravity, Cursor, Claude Code, Windsurf, dll.):

```text
Tolong pasang skill office-cli ini ke folder skills kamu:
git clone https://github.com/masdayat-555/office-cli-dayat.git ~/.agents/skills/office-cli
```

---

#### 💻 Opsi 2: Jalankan Langsung di Terminal
Jika Anda lebih suka menjalankan perintah terminal secara manual:

```bash
git clone https://github.com/masdayat-555/office-cli-dayat.git ~/.agents/skills/office-cli
```

---

### 💡 Cara Penggunaan
Setelah terpasang, Anda tidak perlu menghafal perintah yang rumit. Cukup berikan instruksi dengan bahasa alami ke AI Agent Anda:

```text
"Buatkan draf artikel jurnal ilmiah standar SINTA 2 tentang analisis sentimen IndoBERT..."
```

```text
"Susun draf naskah artikel jurnal internasional untuk template IASSSF lengkap dengan abstrak berstruktur dan tabel biodata penulis..."
```

```text
"Format dokumen skripsi ini ke standar baku (margin 4-3-3-3 cm, Times New Roman 12 pt, 1.25 spasi)..."
```

```text
"Susun Laporan Kerja Praktik 5 bab berdasarkan catatan logbook dan profil perusahaan ini..."
```

```text
"Ekstrak seluruh bagan arsitektur dan gambar dari berkas laporan.docx ini..."
```

```text
"Ekstrak dan analisis tabel data dari laporan.pdf ini..."
```

```text
"Sinkronkan daftar referensi dan berkas PDF ke Zotero Cloud, lalu susun naskah dengan sitasi native Word..."
```

```text
"Terjemahkan naskah artikel_indonesia.docx ke bahasa Inggris ilmiah standar Scopus Q1, hilangkan kata klise AI, terapkan kaidah tenses IMRaD, dan pastikan seluruh field code sitasi Zotero serta rumus OMML tetap utuh..."
```

```text
"Audit dan bersihkan naskah draf skripsi ini dari kesalahan ejaan EYD V, kata tidak baku KBBI, dan kalke bahasa Inggris..."
```

```text
"Terjemahkan draf buku akademik ini bab demi bab dengan semantic chunking (2.000 kata per segmen) dan buatkan berkas GLOSSARY.json untuk mengunci padanan istilah teknis..."
```

```text
"Jalankan linter akademis otomatis pada naskah bahasa Inggris ini untuk memastikan tidak ada kata terlarang AI seperti delve, pivotal, atau tapestry..."
```

AI Agent akan otomatis mengaktifkan skill ini, mengonfirmasi preferensi template Anda, dan menghasilkan berkas `.docx` resmi.

---

### ⚙️ Kebutuhan Sistem (Prasyarat)
Skill ini memanfaatkan mesin *open-source* yang terpasang di terminal sistem Anda:

1. **Microsoft MarkItDown (Mesin Pembaca Dokumen):**
   ```bash
   pip install markitdown
   # Opsional: untuk dukungan OCR gambar & Audio Speech-to-Text:
   pip install markitdown[all]
   ```

2. **OfficeCLI (Mesin Penyusun Dokumen Word):**
   - **Windows (PowerShell):**
     ```powershell
     irm https://d.officecli.ai/install.ps1 | iex
     ```
   - **Linux / macOS (Bash):**
     ```bash
     curl -fsSL https://d.officecli.ai/install.sh | bash
     ```

3. **PyZotero & Requests (Tool Manajemen Referensi & Sitasi Zotero Headless):**
   ```bash
   pip install pyzotero requests
   ```
   *Konfigurasi Kredensial Zotero (`.env`)*: Buat berkas `.env` di direktori skill (`office-cli/.env`) dan cantumkan:
   ```env
   ZOTERO_USER_ID="12345678"
   ZOTERO_API_KEY="kunci_rahasia_api_zotero_anda"
   ```
   *(Kunci API dapat diperoleh gratis melalui [zotero.org/settings/keys](https://www.zotero.org/settings/keys))*.

4. **docx2pdf (Ekspor Akhir ke LMS):**
   ```bash
   pip install docx2pdf
   ```

---

### 🔄 Sinkronisasi Pembaruan Otomatis
Skill ini dilengkapi skrip sinkronisasi otomatis setiap **30 hari**. Namun, Anda dapat memaksa pembaruan kapan saja cukup dengan memberikan instruksi santai ke AI Agent (meskipun sedikit *typo*):

```text
"perbarui office cli"
```
Agen akan otomatis mendeteksi permintaan Anda dan mengeksekusi sinkronisasi dari repositori utama:
```bash
git pull --rebase --autostash origin main
```

---

### 📁 Struktur Direktori Repositori

```text
office-cli/
├── SKILL.md                                 # Instruksi utama & pedoman operasional agen AI
├── README.md                                # Dokumentasi publik dwibahasa
├── scripts/
│   ├── check_update.py                      # Skrip pemeriksaan pembaruan otomatis 30 hari
│   ├── clean_word_locks.py                  # Pembersih file lock sementara (~$*.docx) Microsoft Word
│   ├── zotero_headless_sync.py              # CLI & Engine sinkronisasi Zotero Cloud Headless & field code Word
│   ├── zotero_clean_metadata.py             # Pipeline pembersihan metadata CrossRef kanonikal & normalisasi
│   ├── mendeley_setup.py                    # Otentikasi & inisialisasi API Mendeley Desktop
│   ├── mendeley_upload.py                   # Engine sinkronisasi metadata sitasi & PDF ke Mendeley
│   ├── linter_akademis_en.py                # Linter deterministik bahasa Inggris ilmiah & eliminasi AI slop (delve, etc.)
│   ├── linter_tata_bahasa_id.py             # Linter deterministik tata bahasa Indonesia baku EYD V & pleonasme
│   └── docx_zotero_guard.py                 # Pelindung tokenisasi field codes Zotero & OMML formula pada DOCX
├── templates/
│   ├── template_jurnal_sinta.docx           # Master template universal Jurnal OJS SINTA
│   ├── Template IASSSF.docx                 # Master template resmi Jurnal Internasional IASSSF (Cambria, 1-Kolom)
│   ├── template_laporan_tugas_akhir.docx    # Master template universal Skripsi / Tugas Akhir (5 Bab)
│   ├── template_laporan_kerja_praktik.docx  # Master template universal Kerja Praktik / Magang Industri
│   ├── template_laporan_praktikum.docx      # Master template Laporan Praktikum (Cover resmi Janabadra)
│   ├── template_lhp_singkat.docx            # Master template Laporan Praktikum Singkat (Hanya cover tugas)
│   └── template_lkm_metode_numerik.docx     # Master template Monograf LKM Metode Numerik (5 Bab, TOC native)
└── references/
    ├── pedoman_jurnal_sinta.md              # Panduan publikasi jurnal terakreditasi SINTA 1–6 (IMRaD baku)
    ├── pedoman_jurnal_scopus.md             # Panduan publikasi jurnal bereputasi Scopus Q1–Q4 & WoS
    ├── pedoman_jurnal_iasssf.md             # Panduan naskah jurnal internasional IASSSF & verifikasi data
    ├── pedoman_skripsi_lengkap.md           # Panduan lengkap skripsi & tugas akhir 5 bab standar nasional
    ├── pedoman_kerja_praktik.md             # Panduan laporan kerja praktik & magang industri lengkap
    ├── pedoman_laporan_praktikum.md         # Pedoman Laporan Praktikum (struktur bab, format cover)
    ├── pedoman_lkm_metode_numerik.md        # Pedoman LKM Metode Numerik (monograf & kode Scilab)
    ├── pedoman_surat_insentif.md            # Pedoman penyusunan surat permohonan insentif resmi
    ├── panduan_integrasi_zotero_headless.md # Panduan setup API Zotero, .env, CLI satu baris, dan injeksi Word
    ├── resep_officecli_dokumen_ilmiah.md    # Resep batch JSON teknis OfficeCLI (Resep 1–12)
    ├── aturan_adaptif_pedoman_kampus.md     # Mesin adaptasi & matriks komparatif dokumen institusi
    ├── pedoman_bahasa_indonesia.md          # Dokumen induk EYD V, kalimat efektif, eliminasi kata mubazir/slop ID
    ├── pedoman_bahasa_inggris.md            # Dokumen induk Scopus Q1 register, tenses IMRaD, blacklist AI buzzwords
    ├── phrasebank_manchester.md             # Rangkuman indeks & panduan navigasi 18 modul Manchester Phrasebank
    ├── phrasebank/                          # Direktori 18 modul frasa fungsional lengkap Manchester Academic Phrasebank
    └── metodologi_penerjemahan.md           # Doktrin Translation as Rewriting, chunking buku, dan glossary locking
```

---

<a name="-english-version"></a>
## 🇬🇧 English Version

### ✨ Overview
**Unified Office & Document Suite** empowers your AI coding assistants (Antigravity, Cursor, Claude Code, Windsurf, VS Code, Roo Code, etc.) with native capabilities to **ingest**, **extract**, and **author** professional office documents:

* 🎓 **SINTA 1–6 Accredited Journals:** Standard IMRaD structure, polished bilingual abstracts, and APA-compliant scientific tables.
* 🌐 **Scopus Q1–Q4 & WoS Journals:** Extended IMRaD workflows, comparative state-of-the-art analysis, and international publication standards.
* 🌿 **IASSSF International Journals:** Official single-column layout (Cambria), structured abstracts, CRediT author roles, and complete publication ethics declarations.
* 📚 **Theses & Academic Dissertations:** Standard university chapter hierarchy, automated dynamic TOC, and consistent typography & citation formatting.
* 💼 **Internship & Industrial Reports:** Comprehensive partner profiles, standard operating procedures, weekly logs, and technical outcomes.
* 🔬 **Lab Reports & Practicum Modules:** Structured laboratory reports, academic module workbooks, and scientific data presentation.
* 📑 **Multi-Format Document Ingestion:** Intelligent extraction of PDF, DOCX, XLSX, and PPTX to structured Markdown via Microsoft MarkItDown.
* 🖼️ **Visual Asset Extraction:** Lossless extraction of embedded diagrams, figures, and charts across document formats in full resolution.
* 🏷️ **Zotero Headless Citation Engine:** Automated, background reference and citation management via `pyzotero`, canonical CrossRef metadata normalization, cloud PDF attachment uploads, and native Word OpenXML field code injection (`ADDIN ZOTERO_ITEM` and `ADDIN ZOTERO_BIBL`) without opening the Zotero GUI.
* 🌐 **Academic Translation & Rewriting Engine (Scopus Q1 & EYD V):** "Translation as Rewriting" doctrine for academic papers and textbooks. Integrates 18 functional modules from the *Manchester Academic Phrasebank*, book-length semantic chunking (1,500–2,500 words with persistent `GLOSSARY.json`), strict AI buzzword elimination (*delve*, *pivotal*, *tapestry*, *realm*), and automated deterministic linters (`linter_akademis_en.py` & `linter_tata_bahasa_id.py`).
* 🛡️ **DOCX OpenXML & Zotero Asset Guard:** Zero-dependency OpenXML inspector and verifier (`docx_zotero_guard.py`) ensuring 100% preservation of active Zotero/Mendeley citation field codes (`ADDIN ZOTERO_ITEM`) and native Word OMML math equations (`<m:oMath>`) during editing and translation.
* 🎯 **Native Word (`.docx`) Generation:** Clean, production-ready OpenXML document compilation powered by OfficeCLI.

---

### 🌐 Academic Translation & Rewriting Engine (Scopus Q1 & Indonesian EYD V)

Built-in scholarly translation and stylistic refinement based on the **"Translation as Academic Rewriting"** doctrine:
* ✍️ **Beyond Word-for-Word Translation:** Eliminates "translationese" by deconstructing complex compound sentences into deductive, linear paragraphs with high lexical density and precise academic cadence.
* 🏛️ **Manchester Academic Phrasebank:** Integrates 18 official functional rhetorical modules (*Introducing Work, Referring to Sources, Describing Methods, Reporting Results, Discussing Findings, Cautious Language/Hedging*, etc.).
* 🛡️ **DOCX OpenXML & Zotero Guard (`docx_zotero_guard.py`):** Automated pre-translation tokenization ensuring 100% integrity of active Zotero/Mendeley citations (`ADDIN ZOTERO_ITEM`) and native Word equations (`<m:oMath>`) with zero corruption.
* 📖 **Book-Length Translation Architecture (`translate-book`):** Semantic chunking (1,500–2,500 words) strictly aligned to heading boundaries with cross-chapter terminology locking via `GLOSSARY.json`.
* 🤖 **Deterministic Non-LLM Linters:**
  * `linter_akademis_en.py`: Hardcoded regex scanner to detect and eradicate AI buzzwords (*delve, pivotal, tapestry, realm, foster, underscore, leverage*), personal pronouns (*we/our*), and decimal formatting errors.
  * `linter_tata_bahasa_id.py`: Scans Indonesian manuscripts for non-standard KBBI spelling, pleonasms, English calques (*di mana, yang mana*), and robotic AI openings.

---

### 🚀 Installation

#### 💬 Option 1: Copy-Paste Prompt to Your AI Agent (Quick)
Paste this prompt into your AI Assistant chat:

```text
Tolong pasang skill office-cli ini ke folder skills kamu:
git clone https://github.com/masdayat-555/office-cli-dayat.git ~/.agents/skills/office-cli
```

#### 💻 Option 2: Terminal Command
```bash
git clone https://github.com/masdayat-555/office-cli-dayat.git ~/.agents/skills/office-cli
```

---

### 💡 Example Prompts
```text
"Draft an international manuscript for the IASSSF journal template with a structured abstract and author biography boxes..."
```

```text
"Format this thesis document to university standards (4-3-3-3 cm margin, Times New Roman 12 pt, 1.25 line spacing)..."
```

```text
"Sync reference PDFs in this directory to Zotero Cloud and format the manuscript with active Word citations..."
```

```text
"Translate this Indonesian research paper to Scopus Q1 academic English using the 'Translation as Rewriting' doctrine, eliminate AI clichés, and preserve all active Zotero citations and OMML formulas..."
```

```text
"Audit my translated manuscript using the deterministic linter to ensure zero AI buzzwords (delve, pivotal, tapestry) and verified IMRaD tenses..."
```

```text
"Translate this academic textbook chapter by chapter with semantic chunking (2,000 words per chunk) and maintain consistent terminology via GLOSSARY.json..."
```

```text
"Audit this Indonesian thesis draft against EYD V spelling rules and clean all pleonasms and robotic AI filler..."
```

---

### ⚙️ Prerequisites
1. **Microsoft MarkItDown:** `pip install markitdown`
2. **OfficeCLI:**
   - Windows: `irm https://d.officecli.ai/install.ps1 | iex`
   - Linux/macOS: `curl -fsSL https://d.officecli.ai/install.sh | bash`
3. **PyZotero & Requests (Zotero Headless Reference Engine):**
   ```bash
   pip install pyzotero requests
   ```
   *Credential Configuration (`.env`)*: Create `.env` in the skill folder (`office-cli/.env`) with:
   ```env
   ZOTERO_USER_ID="12345678"
   ZOTERO_API_KEY="your_zotero_api_key"
   ```
4. **docx2pdf:** `pip install docx2pdf`

---

## 📄 Lisensi & Hak Cipta (License)

Skill ini dilisensikan di bawah [MIT License](LICENSE).

### Perangkat Lunak Pihak Ketiga (Third-Party Notices)
* **[Microsoft MarkItDown](https://github.com/microsoft/markitdown):** Dilisensikan di bawah **MIT License** oleh Microsoft Corporation. Hak Cipta (c) Microsoft Corporation.
* **[OfficeCLI](https://officecli.ai):** OpenXML CLI engine. Hak Cipta (c) OfficeCLI Contributors.
* **[PyZotero](https://github.com/urschrei/pyzotero):** Zotero API client by Stephan Speicher and contributors.

### Penafian Merek Dagang (Trademark Disclaimer)
*Microsoft, Microsoft Office, Word, Excel, PowerPoint, dan MarkItDown adalah merek dagang atau merek dagang terdaftar milik Microsoft Corporation di Amerika Serikat dan/atau negara lainnya.*  
*Proyek ini adalah skill komunitas independen dan tidak berafiliasi dengan, disponsori oleh, atau didukung oleh Microsoft Corporation.*
