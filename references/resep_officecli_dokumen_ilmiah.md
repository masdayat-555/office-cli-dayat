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

## 9. RESEP 8: BUILDER DOKUMEN ILMIAH PRESISI MENGGUNAKAN OFFICECLI BATCH DOM

Seluruh manipulasi naskah dan penyisipan tabel/elemen wajib dieksekusi melalui `officecli batch` untuk menjamin struktur OpenXML asli dan field codes tidak rusak:

```json
[
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading1",
      "text": "1. PENDAHULUAN"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Penelitian ini menyajikan evaluasi empiris terhadap adaptasi model berbasis transformer pada domain spesifik naskah ilmiah..."
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "table",
    "props": {
      "rows": 4,
      "cols": 4,
      "style": "TableGrid",
      "alignment": "center"
    }
  },
  {
    "command": "set",
    "path": "/body/table[1]",
    "props": {
      "borderTop": "single 1.5pt 000000",
      "borderBottom": "single 1.5pt 000000",
      "borderLeft": "none",
      "borderRight": "none",
      "borderInsideH": "none",
      "borderInsideV": "none"
    }
  },
  {
    "command": "set",
    "path": "/body/table[1]/row[1]",
    "props": {
      "borderBottom": "single 1.0pt 000000",
      "shading": "F2F2F2"
    }
  }
]
```

---

## 10. RESEP 9: QUALITY GATE AUDIT SCRIPT (INSPEKSI XML RAW TANPA DEPENDENSI)

Jalankan script audit ini menggunakan library bawaan Python `zipfile` untuk menginspeksi berkas `word/document.xml` langsung tanpa membutuhkan `python-docx`:

```python
import sys
import zipfile
import re


def audit_cleanliness(docx_path: str) -> bool:
  """Memeriksa kebersihan naskah Word dari kebocoran sintaks LaTeX dan format mentah langsung dari XML."""
  violations = []
  dollar_pattern = re.compile(r'\$[^<>$]+\$')
  latex_command_pattern = re.compile(r'\\(kappa|Delta|times|approx|sum|frac|begin|end)')

  with zipfile.ZipFile(docx_path, "r") as docx:
    if "word/document.xml" not in docx.namelist():
      print("ERROR: Berkas bukan dokumen Word OpenXML yang valid!")
      return False
    xml_content = docx.read("word/document.xml").decode("utf-8")

  # Ekstrak seluruh teks dalam tag w:t
  texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
  full_body_text = " ".join(texts)

  if "$" in full_body_text:
    violations.append("Ditemukan karakter dollar ($) yang mengindikasikan kebocoran LaTeX!")
  if "^{" in full_body_text or "_{" in full_body_text:
    violations.append("Ditemukan tag kurung kurawal LaTeX (^{ atau _{})!")
  if latex_command_pattern.search(full_body_text):
    violations.append("Ditemukan perintah backslash LaTeX mentah (seperti \\Delta atau \\kappa)!")

  if violations:
    print(f"AUDIT GAGAL: Ditemukan {len(violations)} pelanggaran!")
    for v in violations:
      print(" -", v)
    return False
  else:
    print("AUDIT BERHASIL: Dokumen 100% bersih, valid, dan bebas dari kebocoran sintaks LaTeX.")
    return True
```

---

## 11. RESEP 10: AUTOMATED ASSET EXTRACTION (EKSTRAKSI GAMBAR DARI DOCX, PPTX, XLSX, & PDF)

Resep Python untuk mengekstrak seluruh gambar biner asli beresolusi penuh dari dokumen sumber tanpa kompresi atau degradasi kualitas:

```python
import zipfile
from pathlib import Path


def extract_images_from_office(office_path: str, output_folder: str) -> list[str]:
  """Mengekstrak seluruh gambar biner asli dari berkas modern Office (.docx, .pptx, .xlsx)

  menggunakan library standar bawaan Python (zipfile) tanpa dependensi luar.
  """
  out = Path(output_folder)
  out.mkdir(parents=True, exist_ok=True)
  extracted = []

  # Format OpenXML (.docx, .pptx, .xlsx) menyimpan aset media di word/media/, ppt/media/, xl/media/
  with zipfile.ZipFile(office_path, "r") as z:
    for item in z.namelist():
      if "/media/" in item and not item.endswith("/"):
        target_name = Path(item).name
        target = out / target_name
        target.write_bytes(z.read(item))
        extracted.append(str(target))

  print(
      f"Ekstraksi Office selesai: {len(extracted)} aset media tersimpan di"
      f" {out}"
  )
  return extracted


def extract_images_from_pdf(pdf_path: str, output_folder: str) -> list[str]:
  """Mengekstrak seluruh gambar biner asli dari berkas PDF menggunakan pypdf."""
  from pypdf import PdfReader

  out = Path(output_folder)
  out.mkdir(parents=True, exist_ok=True)
  extracted = []

  reader = PdfReader(pdf_path)
  for page_idx, page in enumerate(reader.pages):
    for img_idx, img in enumerate(page.images):
      ext = Path(img.name).suffix or ".png"
      target = out / f"page_{page_idx+1}_img_{img_idx+1}{ext}"
      target.write_bytes(img.data)
      extracted.append(str(target))

  print(f"Ekstraksi PDF selesai: {len(extracted)} gambar tersimpan di {out}")
  return extracted
```

> **Catatan Berkas Format Lawas (`.doc`, `.ppt`, `.xls`):**
> Berkas biner era lama (Office 97–2003) belum berbasis zip container. Konversikan terlebih dahulu ke format modern OpenXML (`.docx`, `.pptx`, `.xlsx`) melalui perintah LibreOffice headless (`soffice --headless --convert-to docx file.doc`) atau buka dan simpan ulang di Word/PowerPoint, lalu jalankan fungsi `extract_images_from_office` di atas.

---

## 12. RESEP 11: BLUEPRINT BATCH OFFICECLI FORMAT DOKUMEN TUGAS AKHIR / SKRIPSI (MONOGRAF 5 BAB)

Blueprint konfigurasi `officecli batch` untuk memformat laporan Tugas Akhir / Skripsi standar perguruan tinggi (Margin 4-3-3-3 cm, Times New Roman 12 pt, 1,25 spasi, Heading bertingkat, dan Intisari 3 alinea):

```json
[
  {
    "command": "set",
    "path": "/section[1]",
    "props": {
      "marginTop": "4.0cm",
      "marginBottom": "3.0cm",
      "marginLeft": "3.0cm",
      "marginRight": "3.0cm",
      "pageWidth": "21.0cm",
      "pageHeight": "29.7cm"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading1",
      "text": "BAB 1. PENDAHULUAN",
      "align": "center",
      "bold": "true",
      "spaceBefore": "0pt",
      "spaceAfter": "12pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading2",
      "text": "1.1. Latar Belakang Masalah",
      "align": "left",
      "bold": "true",
      "spaceBefore": "12pt",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Perkembangan teknologi komputasi dan kecerdasan artifisial telah mendorong transformasi di berbagai sektor...",
      "lineSpacing": "1.25x",
      "indent": "1.27cm",
      "align": "both",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading3",
      "text": "1.1.1. Identifikasi tantangan operasional",
      "align": "left",
      "bold": "true",
      "spaceBefore": "6pt",
      "spaceAfter": "4pt"
    }
  }
]
```

Blueprint untuk menyusun Intisari / Abstrak 3 Alinea presisi:
```json
[
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading1",
      "text": "INTISARI",
      "align": "center",
      "bold": "true",
      "spaceAfter": "12pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Alinea I: Berisi uraian ringkas mengenai latar belakang permasalahan, urgensi penelitian, dan tujuan utama yang ingin dicapai dalam pengembangan sistem ini...",
      "size": "10pt",
      "lineSpacing": "1.0x",
      "align": "both",
      "indent": "1.0cm",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Alinea II: Menjelaskan metodologi penelitian, arsitektur perancangan, tahapan implementasi, alat dan bahan, serta skenario pengujian yang diterapkan...",
      "size": "10pt",
      "lineSpacing": "1.0x",
      "align": "both",
      "indent": "1.0cm",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Alinea III: Menyajikan hasil pengujian performa secara terukur serta kesimpulan kualitatif maupun kuantitatif yang diperoleh dari hasil evaluasi...",
      "size": "10pt",
      "lineSpacing": "1.0x",
      "align": "both",
      "indent": "1.0cm",
      "spaceAfter": "8pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "Kata kunci: Kecerdasan Artifisial, Pengolahan Dokumen, Evaluasi Kinerja, OpenXML.",
      "size": "10pt",
      "lineSpacing": "1.0x",
      "bold": "false",
      "spaceAfter": "18pt"
    }
  }
]
```

---

## 13. RESEP 12: BLUEPRINT BATCH OFFICECLI FORMAT LAPORAN KERJA PRAKTIK (KP) / MAGANG

Blueprint struktur naskah Laporan Kerja Praktik / Magang Industri (Heading Organisasi, Pelaksanaan, dan Pengendalian Mutu Proyek):

```json
[
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading1",
      "text": "BAB 2. GAMBARAN UMUM PERUSAHAAN",
      "align": "center",
      "bold": "true",
      "pageBreakBefore": "true",
      "spaceAfter": "12pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading2",
      "text": "2.1. Profil dan Struktur Organisasi",
      "align": "left",
      "bold": "true",
      "spaceBefore": "12pt",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Normal",
      "text": "PT Inovasi Teknologi Nusantara merupakan perseroan terbatas yang bergerak dalam penyediaan solusi perangkat lunak enterprise...",
      "lineSpacing": "1.25x",
      "indent": "1.0cm",
      "align": "both",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading1",
      "text": "BAB 3. PELAKSANAAN KERJA PRAKTIK",
      "align": "center",
      "bold": "true",
      "pageBreakBefore": "true",
      "spaceAfter": "12pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading2",
      "text": "3.1. Prosedur Kerja dan Perancangan Fitur",
      "align": "left",
      "bold": "true",
      "spaceBefore": "12pt",
      "spaceAfter": "6pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading1",
      "text": "BAB 4. EVALUASI DAN PENGENDALIAN PEKERJAAN",
      "align": "center",
      "bold": "true",
      "pageBreakBefore": "true",
      "spaceAfter": "12pt"
    }
  },
  {
    "command": "add",
    "path": "/body",
    "type": "paragraph",
    "props": {
      "style": "Heading2",
      "text": "4.1. Kendala Teknis dan Solusi Lapangan",
      "align": "left",
      "bold": "true",
      "spaceBefore": "12pt",
      "spaceAfter": "6pt"
    }
  }
]
```

---

## 14. RESEP 13: PROTOKOL ANTI-BURIK DOKUMEN WORD (HIGH FIDELITY INJECTION & 300 DPI CITRA)

Resep Python untuk mengunci dokumen Word agar tidak pernah melakukan kompresi/downsampling gambar otomatis saat disimpan atau diekspor ke PDF:

```python
import zipfile
import re
from pathlib import Path
from PIL import Image

def inject_anti_burik_settings(docx_path: str):
    """
    Menginjeksi flag High Fidelity ke word/settings.xml dalam file .docx.
    Menghentikan kompresi dan downsampling gambar otomatis di Microsoft Word.
    """
    docx_file = Path(docx_path)
    temp_zip = docx_file.with_suffix(".temp.zip")
    
    with zipfile.ZipFile(docx_file, 'r') as zin, zipfile.ZipFile(temp_zip, 'w') as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename == 'word/settings.xml':
                xml_text = content.decode('utf-8')
                
                # 1. Update/Inject defaultImageDpi val="0" (High Fidelity)
                if 'defaultImageDpi' in xml_text:
                    xml_text = re.sub(r'<w14:defaultImageDpi[^>]*/>', '<w14:defaultImageDpi w14:val="0"/>', xml_text)
                else:
                    xml_text = xml_text.replace('</w:settings>', '<w14:defaultImageDpi xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" w14:val="0"/></w:settings>')
                
                # 2. Inject doNotCompressPNG jika belum ada
                if 'doNotCompressPNG' not in xml_text:
                    xml_text = xml_text.replace('</w:settings>', '<w:doNotCompressPNG/></w:settings>')
                
                content = xml_text.encode('utf-8')
            zout.writestr(item, content)
            
    temp_zip.replace(docx_file)
    print(f"Sukses menginjeksi pengaturan Anti-Burik (High Fidelity) ke {docx_path}")

def prepare_image_anti_burik(input_image_path: str, output_image_path: str, target_dpi: int = 300):
    """
    Menyiapkan citra tangkapan layar/grafik dengan format PNG lossless dan metadata 300 DPI.
    """
    img = Image.open(input_image_path)
    img.save(output_image_path, format="PNG", dpi=(target_dpi, target_dpi))
    print(f"Gambar anti-burik tersimpan di {output_image_path} ({target_dpi} DPI)")
```






---

## 15. RESEP 14: PERSAMAAN MATEMATIKA NATIVE WORD EQUATION (OMML / CAMBRIA MATH)

> [!IMPORTANT]
> **Larangan Mutlak LaTeX Mentah:** Dilarang mencetak string LaTeX seperti `\sigma(z) = \frac{1}{1 + e^{-z}}` atau `$...$` sebagai teks biasa di berkas Word. Seluruh persamaan display wajib berwujud objek Native Word Equation (`<m:oMath>`) dalam font *Cambria Math*.

### 15.1 Pola Injeksi OMML Menggunakan Tabel 2 Kolom Borderless
Tata letak persamaan yang paling kokoh di semua platform dan versi Microsoft Word adalah menggunakan tabel 1 baris, 2 kolom tanpa garis batas (*borderless*):
- **Kolom 1 (Lebar ~5.1 inci / 13.0 cm):** Rata tengah (*Center*), memuat elemen matematika `<m:oMath>`.
- **Kolom 2 (Lebar ~0.8 inci / 2.0 cm):** Rata kanan (*Right-aligned*), memuat nomor persamaan `(Eq. 1)`.

```python
import os
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Pt

# Peta string OMML murni (bisa dihasilkan via MathML + XSLT MML2OMML.XSL)
OMML_SIGMOID = (
    '<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">'
    '<m:r><m:t>σ</m:t></m:r>'
    '<m:d><m:dPr><m:begChr m:val="(" /><m:endChr m:val=")" /></m:dPr>'
    '<m:e><m:r><m:t>z</m:t></m:r></m:e></m:d>'
    '<m:r><m:t> = </m:t></m:r>'
    '<m:f><m:num><m:r><m:t>1</m:t></m:r></m:num>'
    '<m:den><m:r><m:t>1 + </m:t></m:r><m:sSup><m:e><m:r><m:t>e</m:t></m:r></m:e>'
    '<m:sup><m:r><m:t>-z</m:t></m:r></m:sup></m:sSup></m:den></m:f>'
    '</m:oMath>'
)

def add_native_equation(doc, omml_xml_string, eq_number_str="(Eq. 1)"):
    """
    Menambahkan persamaan matematika native Word OMML di tengah halaman
    dengan nomor persamaan rata kanan menggunakan tabel borderless 2 kolom.
    """
    tbl = doc.add_table(rows=1, cols=2)
    tbl.autofit = False
    
    # Hilangkan seluruh border tabel
    tblPr = tbl._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/><w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/></w:tblBorders>')
        tblPr[0].append(borders)
        
    cell_eq, cell_num = tbl.rows[0].cells[0], tbl.rows[0].cells[1]
    cell_eq.width = Inches(5.1)
    cell_num.width = Inches(0.8)
    
    # Hapus padding sel agar presisi
    for c in [cell_eq, cell_num]:
        tcPr = c._element.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="0" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:left w:w="0" w:type="dxa"/><w:right w:w="0" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)
        
    # Injeksi OMML ke kolom kiri (Center)
    p_eq = cell_eq.paragraphs[0]
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_eq.paragraph_format.space_before = Pt(4)
    p_eq.paragraph_format.space_after = Pt(4)
    p_eq._element.append(parse_xml(omml_xml_string))
    
    # Nomor persamaan ke kolom kanan (Right)
    p_num = cell_num.paragraphs[0]
    p_num.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_num.paragraph_format.space_before = Pt(4)
    p_num.paragraph_format.space_after = Pt(4)
    r_num = p_num.add_run(eq_number_str)
    r_num.font.name = 'Cambria'
    r_num.font.size = Pt(11)
```

---

## 16. RESEP 15: PROTOKOL SITASI ANTI-HALUSINASI & PENGUNDUHAN REFERENSI TERVERIFIKASI

> [!CAUTION]
> **Prinsip Kejujuran Sitasi Mutlak:**
> 1. Dilarang menyisipkan sitasi fiktif atau karya orang lain secara sepihak ke naskah Word saat jumlah referensi penulis masih kurang dari batas kuota jurnal (misal < 30 judul).
> 2. Seluruh sitasi di naskah wajib 100% nyata dari dokumen/folder asli penulis.
> 3. Kekurangan referensi disajikan sebagai temuan audit, dan naskah rekomendasi diunduh PDF fisiknya ke folder `referensi/rekomendasi_internasional/`.

```python
import os
import requests

def download_verified_recommendations(target_folder, papers_dict):
    """
    Mengunduh berkas PDF Open Access dari daftar rekomendasi jurnal ilmiah
    ke folder lokal agar penulis dapat membaca dan memverifikasi isinya.
    """
    os.makedirs(target_folder, exist_ok=True)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    for filename, url in papers_dict.items():
        fpath = os.path.join(target_folder, filename)
        if os.path.exists(fpath):
            print(f"[SKIP] Berkas sudah ada: {filename}")
            continue
            
        try:
            print(f"[DOWNLOADING] {filename}...")
            r = requests.get(url, headers=headers, timeout=25)
            # Pastikan header berkas adalah PDF valid (%PDF) dan berukuran wajar (>10 KB)
            if r.status_code == 200 and r.content[:4] == b'%PDF' and len(r.content) > 10240:
                with open(fpath, 'wb') as f:
                    f.write(r.content)
                print(f"[SUCCESS] Tersimpan: {filename} ({len(r.content)/1024:.1f} KB)")
            else:
                print(f"[FAILED] Gagal mengunduh {filename}: status {r.status_code}")
        except Exception as e:
            print(f"[ERROR] Kendala jaringan saat mengunduh {filename}: {e}")
```

---

## 17. RESEP 16: RESILIENSI KUNCI BERKAS & PENANGANAN `PermissionError` (SAFE SAVE FALLBACK)

Saat pengguna sedang membuka berkas dokumen Word di komputernya, Windows mengunci file tersebut secara eksklusif. Skrip otomatisasi yang mencoba menimpa berkas akan melempar `PermissionError: [Errno 13] Permission denied`.

```python
import sys
import os

# 1. Konfigurasi UTF-8 pada konsol Windows untuk mencegah UnicodeEncodeError cp1252
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

def safe_save_docx(doc, output_path):
    """
    Menyimpan dokumen Word dengan fallback versioning otomatis jika berkas utama sedang terkunci.
    """
    try:
        doc.save(output_path)
        print(f"[SAVED] Dokumen berhasil disimpan: {output_path}")
        return output_path
    except PermissionError:
        base, ext = os.path.splitext(output_path)
        fallback_path = f"{base}_Rev1{ext}"
        try:
            doc.save(fallback_path)
            print(f"[WARNING] Berkas {output_path} sedang dibuka di Microsoft Word!")
            print(f"[SAVED FALLBACK] Dokumen berhasil disimpan sebagai alternatif: {fallback_path}")
            return fallback_path
        except PermissionError:
            fallback_path2 = f"{base}_Rev2{ext}"
            doc.save(fallback_path2)
            print(f"[SAVED FALLBACK] Dokumen berhasil disimpan sebagai alternatif: {fallback_path2}")
            return fallback_path2
```
