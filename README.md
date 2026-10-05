<div align="center">

# 📄 Unified Office & Document Suite for AI Agents

**Skill Pembuatan & Kecerdasan Dokumen Terlengkap untuk AI Coding Assistant.**  
*Menyusun dokumen Word siap publikasi (SINTA, Scopus, Skripsi, Kerja Praktik) dan mengekstrak dokumen multi-format (PDF, Excel, Word, PPT) dengan format 100% presisi.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/masdayat-555/office-cli-dayat)
[![Standard](https://img.shields.io/badge/Standard-SINTA%201--6%20%7C%20Scopus%20Q1--Q4%20%7C%20APA%207th-purple.svg)]()

[🇮🇩 Bahasa Indonesia](#-bahasa-indonesia) • [🇬🇧 English](#-english-version)

---

</div>

<a name="-bahasa-indonesia"></a>
## 🇮🇩 Bahasa Indonesia

### ✨ Fitur Utama
Skill ini membekali asisten koding AI Anda (Antigravity, Cursor, Claude Code, Windsurf, VS Code, Roo Code, dll.) dengan kapabilitas native untuk **membaca**, **mengekstrak**, dan **menyusun** dokumen perkantoran profesional:

* 🎓 **Jurnal Terakreditasi SINTA 1–6:** Struktur IMRaD baku, garansi *Page 1 Fit* (seluruh abstrak bilingual tuntas di halaman 1), alur kontinu tanpa jeda halaman palsu, dan tabel ilmiah APA 3 garis horizontal.
* 🌐 **Jurnal Internasional Bereputasi Scopus Q1–Q4 & WoS:** Extended IMRaD, matriks perbandingan penelitian terdahulu (*State-of-the-Art*), validasi statistik, integrasi ORCID, serta pernyataan etika data.
* 📚 **Skripsi & Tugas Akhir Standar Perguruan Tinggi:** Format margin 4-4-3-3 cm dan variasi teknik 4-3-3-3 cm, spasi 1.25x / 1.5x, penomoran formal BAB (Heading 1-3), daftar isi otomatis (*dynamic TOC*), Intisari 3 alinea presisi, dan daftar pustaka *hanging indent*.
* 💼 **Laporan Kerja Praktik (KP), PKL, & Magang Industri:** Profil & struktur organisasi mitra, uraian SOP kerja, pelaksanaan fitur sistem, pengendalian mutu (*quality control*), dan logbook mingguan.
* 📑 **Ekstraksi Dokumen Multi-Format:** Mengonversi PDF, DOCX, XLSX, dan PPTX menjadi Markdown terstruktur untuk penalaran AI via Microsoft MarkItDown.
* 🖼️ **Ekstraksi Aset Gambar & Bagan:** Mengambil seluruh gambar asli dari Word (DOCX), slide PowerPoint (PPTX), tabel Excel (XLSX), dan PDF dalam resolusi 100% asli tanpa kompresi.
* 🎯 **Garansi Output Word Asli (`.docx`):** Menghasilkan deliverable berkas Word murni menggunakan OfficeCLI secara rapi, bukan sekadar file teks Markdown.

---

### 🚀 Cara Pemasangan (Instalasi)

#### 💬 Opsi 1: Salin & Tempel Prompt ke AI Agent Anda (Paling Mudah)
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

AI Agent akan otomatis mengaktifkan skill ini, mengonfirmasi preferensi template Anda, dan menghasilkan berkas `.docx` resmi.

---

### ⚙️ Kebutuhan Sistem (Prasyarat)
Skill ini memanfaatkan dua mesin *open-source* yang terpasang di terminal sistem Anda:

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

3. **docx2pdf (Ekspor Akhir ke LMS):**
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
├── SKILL.md                                 # Instruksi utama & pedoman agen AI
├── README.md                                # Dokumentasi publik dwibahasa
├── scripts/
│   └── check_update.py                      # Skrip pemeriksaan pembaruan otomatis 30 hari
├── templates/
│   ├── template_jurnal_sinta.docx           # Master template universal Jurnal OJS SINTA
│   ├── template_laporan_tugas_akhir.docx    # Master template universal Skripsi / Tugas Akhir
│   ├── template_laporan_kerja_praktik.docx  # Master template universal Kerja Praktik / Magang
│   └── template_laporan_praktikum.docx      # Master template Laporan Praktikum
└── references/
    ├── pedoman_jurnal_sinta.md              # Panduan publikasi jurnal SINTA 1–6
    ├── pedoman_jurnal_scopus.md             # Panduan publikasi jurnal Scopus Q1–Q4
    ├── pedoman_skripsi_lengkap.md           # Panduan lengkap skripsi & tugas akhir 5 bab
    ├── pedoman_kerja_praktik.md             # Panduan laporan kerja praktik & magang industri
    ├── pedoman_laporan_praktikum.md         # Pedoman Laporan Praktikum (struktur bab, format cover)
    ├── resep_officecli_dokumen_ilmiah.md    # Resep batch JSON teknis OfficeCLI (Resep 1–12)
    └── aturan_adaptif_pedoman_kampus.md     # Mesin adaptasi & matriks komparatif dokumen
```

---

<a name="-english-version"></a>
## 🇬🇧 English Version

### ✨ Overview
**Unified Office & Document Suite** empowers your AI coding assistants (Antigravity, Cursor, Claude Code, Windsurf, VS Code, Roo Code, etc.) with native capabilities to **ingest**, **extract**, and **author** professional office documents:

* 🎓 **SINTA 1–6 & Scopus Journals:** Fully compliant IMRaD workflows, Page 1 Fit abstracts, continuous flow sections, and APA 3-line tables.
* 📚 **Undergraduate Theses & Dissertations (Skripsi):** 4-4-3-3 cm and 4-3-3-3 cm margins, formal chapter hierarchy, automated Table of Contents (TOC), and hanging indent bibliographies.
* 💼 **Internship & Industrial Reports (Kerja Praktik / PKL):** Organizational hierarchies, SOPs, system implementation, and weekly activity records.
* 📑 **Deep Multi-Format Document Ingestion:** Extracts text, tables, and structure from PDF, DOCX, XLSX, and PPTX via Microsoft MarkItDown.
* 🖼️ **Asset Extraction:** Losslessly extracts embedded images and diagrams from Word, PowerPoint, Excel, and PDF files.
* 🎯 **Guaranteed Word (`.docx`) Deliverables:** Compiles pristine OpenXML Word documents directly without manual formatting overhead.

---

### 🚀 Installation

#### 💬 Option 1: Copy-Paste Prompt to Your AI Agent (Easiest)
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

### ⚙️ Prerequisites
1. **Microsoft MarkItDown:** `pip install markitdown`
2. **OfficeCLI:**
   - Windows: `irm https://d.officecli.ai/install.ps1 | iex`
   - Linux/macOS: `curl -fsSL https://d.officecli.ai/install.sh | bash`
3. **docx2pdf:** `pip install docx2pdf`

---

## 📄 Lisensi & Hak Cipta (License)

Skill ini dilisensikan di bawah [MIT License](LICENSE).

### Perangkat Lunak Pihak Ketiga (Third-Party Notices)
* **[Microsoft MarkItDown](https://github.com/microsoft/markitdown):** Dilisensikan di bawah **MIT License** oleh Microsoft Corporation. Hak Cipta (c) Microsoft Corporation.
* **[OfficeCLI](https://officecli.ai):** OpenXML CLI engine. Hak Cipta (c) OfficeCLI Contributors.

### Penafian Merek Dagang (Trademark Disclaimer)
*Microsoft, Microsoft Office, Word, Excel, PowerPoint, dan MarkItDown adalah merek dagang atau merek dagang terdaftar milik Microsoft Corporation di Amerika Serikat dan/atau negara lainnya.*  
*Proyek ini adalah skill komunitas independen dan tidak berafiliasi dengan, disponsori oleh, atau didukung oleh Microsoft Corporation.*
