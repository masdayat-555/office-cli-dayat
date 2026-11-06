<div align="center">

# 📄 Unified Office & Document Suite for AI Agents

**Skill Pembuatan & Pengolahan Dokumen untuk AI Coding Assistant.**  
*Membantu penyusunan dokumen Word sesuai pedoman (SINTA, Scopus, IASSSF, Skripsi, Kerja Praktik) serta ekstraksi dokumen multi-format (PDF, Excel, Word, PPT).*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/masdayat-555/office-cli-dayat)
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
* 🎯 **Output Word Asli (`.docx`):** Pembuatan dokumen OpenXML murni yang rapi dan siap pakai menggunakan OfficeCLI.

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
├── SKILL.md                                 # Instruksi utama & pedoman operasional agen AI
├── README.md                                # Dokumentasi publik dwibahasa
├── scripts/
│   ├── check_update.py                      # Skrip pemeriksaan pembaruan otomatis 30 hari
│   ├── clean_word_locks.py                  # Pembersih file lock sementara (~$*.docx) Microsoft Word
│   ├── mendeley_setup.py                    # Otentikasi & inisialisasi API Mendeley Desktop
│   └── mendeley_upload.py                   # Engine sinkronisasi metadata sitasi & PDF ke Mendeley
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
    ├── resep_officecli_dokumen_ilmiah.md    # Resep batch JSON teknis OfficeCLI (Resep 1–12)
    └── aturan_adaptif_pedoman_kampus.md     # Mesin adaptasi & matriks komparatif dokumen institusi
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
* 🎯 **Native Word (`.docx`) Generation:** Clean, production-ready OpenXML document compilation powered by OfficeCLI.

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
