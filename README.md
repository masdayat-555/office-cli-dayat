<div align="center">

# 📄 Unified Office & Document Suite for AI Agents

**The definitive document authoring & intelligence skill for AI coding assistants.**  
*Generate publication-ready Word documents (SINTA, Scopus, Skripsi) and extract multi-format documents (PDF, Excel, Word, PPT) with zero formatting defects.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/masdayat-555/office-cli-dayat)
[![Standard](https://img.shields.io/badge/Standard-SINTA%201--6%20%7C%20Scopus%20Q1--Q4%20%7C%20APA%207th-purple.svg)]()

---

</div>

## ✨ What This Skill Does

This skill equips your AI coding agent (Antigravity, Cursor, Claude Code, VS Code, Windsurf) with native capabilities to **read**, **author**, and **format** professional office documents:

* 🎓 **SINTA 1–6 Accredited Journals:** Strict IMRaD structure, Page 1 Fit abstract layout, bilingual front matter, continuous flow (no artificial page breaks), and APA 3-line tables.
* 🌐 **Scopus & WoS International Standards:** Extended IMRaD, related work matrices, statistical validation, and academic ethics declarations.
* 📚 **Indonesian Standard Thesis & Skripsi:** 4-4-3-3 cm and 4-3-3-3 cm margins, formal Chapter/BAB structure, dynamic Table of Contents (TOC), and hanging indent APA bibliographies.
* 💼 **Internship & Industrial Reports (Kerja Praktik / PKL / MBKM):** Company profile, organizational hierarchy, project implementation, quality control evaluations, and weekly logbooks.
* 📑 **Deep Multi-Format Document Ingestion:** Extracts text, tables, and metadata from PDF, DOCX, XLSX, and PPTX into clean Markdown for AI reasoning.
* 🖼️ **Image & Figure Asset Extraction:** Losslessly extracts embedded photos, diagrams, and charts from Word DOCX, PPTX, XLSX, and PDF documents.
* 🎯 **Guaranteed Native Word Output (`.docx`):** Produces pristine Microsoft Word deliverables instead of stopping at plain Markdown.


---

## 🚀 Installation

### 💬 Copy & Paste to Your AI Agent (Easiest)
Copy and paste this prompt directly into your AI Assistant (Antigravity, Cursor, Claude Code, Windsurf, etc.):

```text
Tolong pasang skill office-cli ini ke folder skills kamu:
git clone https://github.com/masdayat-555/office-cli-dayat.git ~/.agents/skills/office-cli
```

---

### 💻 Or Run Directly in Terminal
```bash
git clone https://github.com/masdayat-555/office-cli-dayat.git ~/.agents/skills/office-cli
```



---

## 💡 How to Use

Once installed, you don't need to learn any complex commands. Just prompt your AI assistant naturally:

```text
"Buatkan draf artikel jurnal ilmiah standar SINTA 2 dengan topik evaluasi IndoBERT..."
```

```text
"Format dokumen skripsi ini ke standar baku nasional (margin 4-4-3-3, font TNR 12 pt, 1.5 spasi)..."
```

```text
"Ekstrak seluruh bagan arsitektur dan gambar dari berkas laporan.docx ini..."
```

```text
"Ekstrak dan analisis tabel data keuangan dari laporan.pdf ini..."
```

Your AI assistant will automatically activate this skill, orchestrate the document engines, and deliver a publication-ready `.docx` file.

---

## ⚙️ Prerequisites

This skill leverages two open-source CLI engines installed on your system:

### 1. Microsoft MarkItDown (Document Ingestion Engine)
```bash
pip install markitdown
# Optional: for OCR & Audio Speech-to-Text:
pip install markitdown[all]
```

### 2. OfficeCLI (Document Authoring Engine)
- **Windows (PowerShell):**
  ```powershell
  irm https://d.officecli.ai/install.ps1 | iex
  ```
- **Linux / macOS (Bash):**
  ```bash
  curl -fsSL https://d.officecli.ai/install.sh | bash
  ```

---

## 🔄 Updates & Maintenance

The skill automatically checks and updates itself every **30 days** via:
```bash
git pull --rebase --autostash origin main
```
You can also trigger an update at any time by asking your agent (*"perbarui skill office-cli"*).

---

## 📁 Repository Structure

```text
office-cli/
├── SKILL.md                                 # Core agent instructions & guidelines
├── README.md                                # Public overview & documentation
├── scripts/
│   └── check_update.py                      # 30-day automated update checker
├── templates/
│   ├── template_jurnal_sinta.docx           # Master universal SINTA OJS template
│   ├── template_laporan_tugas_akhir.docx    # Master universal Thesis / Skripsi template
│   └── template_laporan_kerja_praktik.docx  # Master universal Internship / KP template
└── references/
    ├── pedoman_jurnal_sinta.md              # SINTA 1-6 comprehensive publication guide
    ├── pedoman_jurnal_scopus.md             # Scopus Q1-Q4 international journal guide
    ├── pedoman_skripsi_lengkap.md           # Indonesian standard thesis & skripsi guide
    ├── pedoman_kerja_praktik.md             # Internship & industrial report guide
    ├── resep_officecli_dokumen_ilmiah.md    # Scientific document formatting recipes
    └── aturan_adaptif_pedoman_kampus.md     # Dynamic override engine & routing hub
```

---

## 📄 License & Third-Party Notices

This skill is open-sourced under the [MIT License](LICENSE).

### Third-Party Software & Acknowledgments
* **[Microsoft MarkItDown](https://github.com/microsoft/markitdown):** Released under the **MIT License** by Microsoft Corporation. Copyright (c) Microsoft Corporation.
* **[OfficeCLI](https://officecli.ai):** OpenXML CLI manipulation engine. Copyright (c) OfficeCLI Contributors.

### Disclaimer & Trademarks
*Microsoft, Microsoft Office, Word, Excel, PowerPoint, and MarkItDown are trademarks or registered trademarks of Microsoft Corporation in the United States and/or other countries.*  
*This project is an independent community skill and is not affiliated with, sponsored by, or endorsed by Microsoft Corporation.*
