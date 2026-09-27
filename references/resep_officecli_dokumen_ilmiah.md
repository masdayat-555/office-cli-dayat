# RESEP TEKNIS OFFICECLI UNTUK DOKUMEN ILMIAH (SKRIPSI & JURNAL)

Dokumen ini berisi panduan implementasi teknis tingkat lanjut (*cheat sheet*) untuk memanipulasi dan memformat dokumen Word (`.docx`) menggunakan `officecli` berbasis standar akademik.

---

## 1. POLA UTAMA ORCHESTRATION VIA PYTHON (ANTI-MOJIBAKE & SAFE EXECUTION)

Untuk menghindari kerusakan karakter tanda baca (*mojibake*) akibat *piping* terminal PowerShell Windows, pembuatan dan pembaruan dokumen harus selalu dieksekusi melalui *script* Python menggunakan modul `subprocess` dengan encoding `utf-8`.

### Template Eksekusi Standar:
```python
import json
import subprocess
from pathlib import Path


def run_officecli_batch(doc_path: str, commands: list):
  """Mengeksekusi kumpulan perintah batch ke dalam dokumen docx secara aman."""
  cmd_json = json.dumps(commands, ensure_ascii=False)
  proc = subprocess.run(
      ["officecli", "batch", doc_path, "--commands", cmd_json],
      capture_output=True,
      text=True,
      encoding="utf-8",
  )
  if proc.returncode != 0:
    print(f"Error execution: {proc.stderr}")
    raise RuntimeError(proc.stderr)
  print(f"Batch success: {proc.stdout.strip()}")


def refresh_document(doc_path: str):
  """Memperbarui nomor halaman TOC dan cross-references menggunakan engine Word Windows."""
  proc = subprocess.run(
      ["officecli", "refresh", doc_path],
      capture_output=True,
      text=True,
      encoding="utf-8",
  )
  print(f"Refresh status: {proc.stdout.strip()}")
```

---

## 2. RESEP 1: SETUP MARGIN BAKU SKRIPSI (4-4-3-3 CM)

Secara default, margin diatur pada level section:
```json
[
  {
    "command": "set",
    "path": "/section[1]",
    "props": {
      "marginTop": "4.0cm",
      "marginLeft": "4.0cm",
      "marginBottom": "3.0cm",
      "marginRight": "3.0cm",
      "pageWidth": "21.0cm",
      "pageHeight": "29.7cm"
    }
  }
]
```
*(Untuk artikel jurnal umum, gunakan konfigurasi simetris 3.0cm / 2.54cm sesuai template jurnal).*

---

## 3. RESEP 2: STANDARISASI STYLES (HEADING 1, 2, 3 & NORMAL)

Pastikan setiap heading mewarisi font *Times New Roman*, memiliki spasi yang tepat, dan tidak terpisah dari paragraf berikutnya (*keepWithNext*):

```json
[
  {
    "command": "set",
    "path": "/styles/Heading1",
    "props": {
      "font": "Times New Roman",
      "size": "14pt",
      "bold": "true",
      "color": "000000",
      "spaceBefore": "12pt",
      "spaceAfter": "6pt",
      "lineSpacing": "1.5x",
      "align": "center",
      "keepWithNext": "true"
    }
  },
  {
    "command": "set",
    "path": "/styles/Heading2",
    "props": {
      "font": "Times New Roman",
      "size": "12pt",
      "bold": "true",
      "color": "000000",
      "spaceBefore": "12pt",
      "spaceAfter": "4pt",
      "lineSpacing": "1.5x",
      "align": "left",
      "keepWithNext": "true"
    }
  },
  {
    "command": "set",
    "path": "/styles/Heading3",
    "props": {
      "font": "Times New Roman",
      "size": "12pt",
      "bold": "true",
      "italic": "true",
      "color": "000000",
      "spaceBefore": "6pt",
      "spaceAfter": "2pt",
      "lineSpacing": "1.5x",
      "align": "left",
      "keepWithNext": "true"
    }
  },
  {
    "command": "set",
    "path": "/styles/Normal",
    "props": {
      "font": "Times New Roman",
      "size": "12pt",
      "color": "000000",
      "lineSpacing": "1.5x",
      "spaceAfter": "0pt",
      "spaceBefore": "0pt",
      "align": "both"
    }
  }
]
```

---

## 4. RESEP 3: DAFTAR ISI OTOMATIS (TABLE OF CONTENTS / TOC)

Gunakan elemen khusus `toc` bawaan `officecli` agar menghasilkan *field code* resmi Word:
```json
[
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "style": "Heading 1",
      "text": "DAFTAR ISI",
      "align": "center"
    }
  },
  {
    "command": "add",
    "parent": "/",
    "type": "toc",
    "props": {
      "levels": "1-3",
      "hyperlinks": "true",
      "pageNumbers": "true"
    }
  },
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "pageBreakBefore": "true"
    }
  }
]
```
> **Catatan Krusial:** Setelah seluruh naskah selesai disusun, selalu panggil perintah:
> `officecli refresh path/ke/dokumen.docx`
> agar nomor halaman di dalam TOC terhitung secara nyata oleh Word!

---

## 5. RESEP 4: TABEL ILMIAH STANDAR APA (3 GARIS HORIZONTAL)

Kaidah mutlak: **Hanya 3 garis horizontal** (Border Top tabel, Border Bottom header, Border Bottom tabel) dan **TANPA GARIS VERTIKAL**.

### Sintaks Pembuatan Tabel APA:
```json
[
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Tabel 4.1 Hasil Evaluasi Komparatif Model",
      "bold": "true",
      "spaceBefore": "12pt",
      "spaceAfter": "4pt",
      "lineSpacing": "1.0x"
    }
  },
  {
    "command": "add",
    "parent": "/",
    "type": "table",
    "props": {
      "align": "center",
      "borderTop": "single 1.5pt 000000",
      "borderBottom": "single 1.5pt 000000",
      "borderLeft": "none",
      "borderRight": "none",
      "borderInsideH": "none",
      "borderInsideV": "none"
    }
  }
]
```
Pada baris pertama (*header row*):
- Berikan `borderBottom: "single 1.0pt 000000"`.
- Berikan format teks `bold: true`, font 10–11 pt, dan perataan tengah.
- Spasi di dalam sel tabel wajib spasi tunggal (`lineSpacing="1.0x"`).

---

## 6. RESEP 5: JUDUL GAMBAR DAN GRAFIK

Kaidah mutlak: Judul diletakkan di **BAWAH GAMBAR**.
```json
[
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "align": "center",
      "spaceBefore": "12pt",
      "spaceAfter": "4pt"
    }
  },
  {
    "command": "add",
    "parent": "/p[last()]",
    "type": "picture",
    "props": {
      "src": "path/ke/gambar.png",
      "width": "12.0cm",
      "height": "8.0cm"
    }
  },
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "text": "Gambar 3.1 Diagram Arsitektur Pipeline NLP",
      "style": "Normal",
      "align": "center",
      "spaceBefore": "4pt",
      "spaceAfter": "12pt",
      "lineSpacing": "1.0x",
      "size": "10pt"
    }
  }
]
```

---

## 7. RESEP 6: DAFTAR PUSTAKA FORMAT HANGING INDENT

Daftar pustaka menggunakan spasi tunggal dan format baris kedua menjorok (*hanging indent* sejauh 1,27 cm):
```json
[
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "style": "Heading 1",
      "text": "DAFTAR PUSTAKA",
      "align": "center",
      "pageBreakBefore": "true"
    }
  },
  {
    "command": "add",
    "parent": "/",
    "type": "paragraph",
    "props": {
      "text": "Koto, F., Lau, J. H., & Baldwin, T. (2021). IndoBERTweet: A Pretrained Language Model for Indonesian Twitter with Effective Domain-Specific Vocabulary Adaptation. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP), 10123-10134.",
      "indent": "1.27cm",
      "hangingIndent": "1.27cm",
      "lineSpacing": "1.0x",
      "spaceAfter": "6pt",
      "align": "both"
    }
  }
]
```

---

## 8. RESEP 7: PENOMORAN HALAMAN ROMAWI VS ANGKA ARAB (SECTION BREAK)

Untuk menghasilkan halaman awal Romawi (i, ii, iii) di tengah bawah, dan halaman isi Bab Arab (1, 2, 3) di kanan atas:
1. Bagian Awal menggunakan `Section 1`:
   - `pageNumberFormat: "lowerRoman"`
   - `footerAlignment: "center"`
2. Sisipkan *Section Break (Next Page)* sebelum Bab I.
3. Bagian Isi menggunakan `Section 2`:
   - `pageNumberFormat: "decimal"`
   - `pageNumberStart: 1`
   - Aktifkan `differentFirstPage: true` (sehingga halaman pertama bab berada di footer bawah tengah, sedangkan halaman lanjutan berada di header kanan atas).

---

## 9. RESEP 8: BUILDER DOKUMEN ILMIAH PRESISI (PYTHON-DOCX + APA TABLE + SUPERSCRIPT)

Skrip acuan berikut menyusun naskah ilmiah dengan pemisahan metadata terpusat, superskrip asli, dan tabel APA 3 garis horizontal:

```python
import sys
import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Pt, RGBColor

# Wajib untuk Windows: cegah error cp1252 pada simbol Yunani
sys.stdout.reconfigure(encoding="utf-8")


def set_apa_table_borders(table):
  """Menerapkan format APA 3 garis horizontal (Top, Header Bottom, Table Bottom)."""
  tblPr = table._tbl.tblPr
  for child in list(tblPr):
    if child.tag.endswith("tblBorders"):
      tblPr.remove(child)
  borders_xml = parse_xml(
      '<w:tblBorders %s><w:top w:val="single" w:sz="12" w:space="0"'
      ' w:color="000000"/><w:left w:val="none"/><w:bottom w:val="single"'
      ' w:sz="12" w:space="0" w:color="000000"/><w:right w:val="none"/><w:insideH'
      ' w:val="none"/><w:insideV w:val="none"/></w:tblBorders>'
      % nsdecls("w")
  )
  tblPr.append(borders_xml)

  # Beri garis bawah pada baris header (row 0)
  for cell in table.rows[0].cells:
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        '<w:tcBorders %s><w:bottom w:val="single" w:sz="8" w:space="0"'
        ' w:color="000000"/></w:tcBorders>'
        % nsdecls("w")
    )
    tcPr.append(tcBorders)


def add_author_metadata(doc, authors_data):
  """Menambahkan identitas penulis dengan superskrip run asli tanpa kebocoran LaTeX."""
  # authors_data: [("Nama Penulis", "1*"), ("Nama Penulis 2", "2")]
  p = doc.add_paragraph()
  p.alignment = WD_ALIGN_PARAGRAPH.CENTER
  p.paragraph_format.space_before = Pt(6)
  p.paragraph_format.space_after = Pt(2)
  for i, (name, sup) in enumerate(authors_data):
    r_name = p.add_run(name)
    r_name.font.name = "Times New Roman"
    r_name.font.bold = True
    r_name.font.size = Pt(11)
    if sup:
      r_sup = p.add_run(sup)
      r_sup.font.name = "Times New Roman"
      r_sup.font.superscript = True
      r_sup.font.bold = True
    if i < len(authors_data) - 1:
      r_comma = p.add_run(", ")
      r_comma.font.name = "Times New Roman"
```

---

## 10. RESEP 9: QUALITY GATE AUDIT SCRIPT (VERIFIKASI ANTI-KONFLIK PENGKODEAN)

Jalankan script audit ini untuk memastikan dokumen bebas dari kesalahan pengkodean:

```python
import sys
import docx


def audit_cleanliness(docx_path: str):
  doc = docx.Document(docx_path)
  violations = []
  dollar_char = chr(36)  # '$'

  for idx, p in enumerate(doc.paragraphs):
    t = p.text
    if dollar_char in t:
      violations.append(f"Paragraf {idx} memuat karakter dollar: {t[:60]}")
    if "^{" in t or "_{" in t:
      violations.append(f"Paragraf {idx} memuat tag kurung LaTeX: {t[:60]}")
    if "\\kappa" in t or "\\Delta" in t or "\\frac" in t:
      violations.append(f"Paragraf {idx} memuat perintah LaTeX mentah: {t[:60]}")

  for t_idx, table in enumerate(doc.tables):
    for r_idx, row in enumerate(table.rows):
      for c_idx, cell in enumerate(row.cells):
        t = cell.text
        if dollar_char in t or "^{" in t:
          violations.append(
              f"Tabel {t_idx}[{r_idx},{c_idx}] memuat sintaks bocor: {t[:40]}"
          )

  if violations:
    print(f"AUDIT FAILED: Ditemukan {len(violations)} pelanggaran!")
    for v in violations:
      print(" -", v)
      return False
  else:
    print("AUDIT PASSED: Dokumen 100% bersih dari konflik pengkodean & LaTeX.")
    return True
```
