# PEDOMAN METODOLOGI & ENGINE PENERJEMAHAN AKADEMIK (PAPER & BUKU)
## Sintesis Komprehensif: English-Paper-Translator + Translate-Book + Baoyu-Skills

> [!IMPORTANT]
> **DOKUMEN INDUK METODOLOGI & ARSITEKTUR PENERJEMAHAN**  
> Dokumen ini menyatukan doktrin ilmiah **"Translation as Rewriting"** (Penerjemahan sebagai Penulisan Ulang), eliminasi cacat terjemahan kaku (*anti-translationese*), arsitektur pemotongan dokumen panjang dan buku (*book-length semantic chunking*), retensi memori lintas bab, serta penguncian glosarium terminologi khusus (*glossary locking*).  
> Dokumen ini adalah panduan operasional AI Agent dan penerjemah manusia untuk mentransformasikan draf karya ilmiah dan buku berbahasa Indonesia ke dalam Bahasa Inggris akademik formal berstandar internasional.

---

## 1. DOKTRIN UTAMA: TRANSLATION AS ACADEMIC REWRITING

Penerjemahan karya ilmiah dan buku teks akademik **BUKAN** sekadar mengalihkan kata per kata (*word-by-word substitution*). Terjemahan harfiah selalu menghasilkan *"translationese"*—yaitu teks bahasa Inggris yang secara gramatikal benar tetapi terasa janggal, kaku, dan mempertahankan struktur kalimat bahasa sumber.

### 1.1 Perbedaan Pola Pikir Naskah (Indonesian vs English Academic Discourse)
| Parameter Diskursus | Pola Naskah Bahasa Indonesia | Pola Naskah Bahasa Inggris Akademik |
| :--- | :--- | :--- |
| **Alur Logika** | Kontekstual, sirkular, mendalam di latar belakang sebelum ke inti masalah. | **Linier, deduktif, langsung ke sasaran (*direct & concise*)**. |
| **Beban Kalimat** | Banyak anak kalimat bertingkat yang dihubungkan koma dan kata sambung. | **Satu gagasan utama per kalimat**; klausa majemuk dibatasi maksimal 2 tingkat. |
| **Struktur Verba vs Nomina** | Cenderung verbal (*"Untuk mengetahui bagaimana pengaruh..."*). | **Padat nomina (*high nominalization*)** (*"To evaluate the influence of..."*). |
| **Transisi Kalimat** | Mengandalkan penghubung longgar (*"Dalam hal ini...", "Adapun..."*). | Mengandalkan kata kait retorika presisi (*"Consequently", "Conversely"*, atau klausa partisipial). |

---

## 2. PIPELINE 3 TAHAP PENERJEMAHAN BERMUTU TINGGI (*MULTI-ROLE PIPELINE*)

Sesuai standar `english-paper-translator`, penerjemahan dilakukan melalui tiga peran virtual terstruktur:

```
[Draf Teks Sumber Bahasa Indonesia]
               │
               ▼
┌────────────────────────────────────────────────────────┐
│ TAHAP 1: LEAD REWRITING TRANSLATOR (TRANSFER SEMANTIK) │
│ - Menangkap inti argumen, fakta, dan data numerik.     │
│ - Membongkar urutan klausa yang berbelit-belit.        │
│ - Mengubah kata kerja bertingkat menjadi nomina padat. │
└───────────────────────┬────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────┐
│ TAHAP 2: CRITICAL REVIEWER (DIAGNOSIS & ANTI-SLOP)     │
│ - Mendeteksi residu terjemahan kaku (*translationese*).│
│ - Memeriksa kesesuaian tenses IMRaD (Past vs Present). │
│ - Menghapus kata klise AI (delve, crucial, landscape). │
│ - Memvalidasi keutuhan sitasi, tabel, dan persamaan.   │
└───────────────────────┬────────────────────────────────┘
                        │
                        ▼
┌────────────────────────────────────────────────────────┐
│ TAHAP 3: FINAL POLISH EDITOR (PEMOLESAN SCOPUS/WOS)    │
│ - Menyelaraskan diksi dengan Manchester Phrasebank.    │
│ - Memastikan ritme kalimat mengalir alami (*cadence*). │
│ - Menghasilkan naskah final siap publikasi / cetak.    │
└────────────────────────────────────────────────────────┘
```

---

## 3. ARSITEKTUR PENERJEMAHAN BUKU UTUH & DOKUMEN PANJANG (`translate-book`)

Menerjemahkan dokumen berukuran besar (buku 5–10 bab, monograf tesis, atau laporan $50+$ halaman) menghadapi kendala batas konteks memori AI dan pergeseran istilah (*terminology drift*). Solusinya mengadopsi arsitektur `translate-book`:

### 3.1 Strategi Pemotongan Semantik (*Semantic Chunking*)
1. **Ukuran Chunk Ideal:** Potong naskah menjadi segmen berukuran **1.500 hingga 2.500 kata**.
2. **Larangan Memotong Elemen Kritis:**
   - **DILARANG** memotong di tengah-tengah paragraf.
   - **DILARANG** memotong di antara baris tabel atau di tengah blok persamaan matematika (`<m:oMath>` / LaTeX).
   - Pemotongan **WAJIB** dilakukan tepat pada batas Sub-Bab (*Heading 2 / Heading 3*) atau batas bab.

### 3.2 Penguncian Glosarium & Memori Lintas Bab (*Glossary Locking*)
Sebelum menerjemahkan Bab 1, agen dan penerjemah wajib menyusun berkas `GLOSSARY.json` yang memetakan istilah kunci.
- Sekali istilah ditetapkan (misal: *rancang bangun $\rightarrow$ design and implementation*, *catu daya $\rightarrow$ power supply*, *habituasi $\rightarrow$ habituation*), AI **DILARANG MENGGANTI** istilah tersebut di Bab 2, 3, atau bab berikutnya.
- **Format Peta Glosarium (`GLOSSARY.json`):**
  ```json
  {
    "pengusir tikus": "rat repellent",
    "komputasi tepi": "edge computing",
    "luring": "offline / on-device",
    "spektrogram suara": "audio spectrogram",
    "gelombang ultrasonik adaptif": "adaptive ultrasonic waveform",
    "frekuensi sapuan": "sweep frequency",
    "himpunan data": "dataset",
    "galat": "error / discrepancy"
  }
  ```

### 3.3 Penanganan Format Dokumen (DOCX, PDF, EPUB)
- **Ekstraksi Bersih ke Markdown:** Selalu konversi dokumen sumber ke Markdown murni terlebih dahulu (menggunakan Microsoft MarkItDown).
- **Pertahankan Tag XML & Markdown:** Seluruh heading (`#`, `##`), bullet points, bold/italic, tautan hyperlink, dan anchor tag harus tetap berada di posisi yang identik setelah diterjemahkan.

---

## 4. PROTOKOL TRANSFORMASI KHUSUS: INDONESIA $\rightarrow$ INGGRIS AKADEMIK

Berikut adalah panduan transformasi konkret untuk kasus-kasus sintaksis yang paling sering dijumpai:

### 4.1 Transformasi Pasif Impersonal Indonesia ke Inggris Akademik
Bahasa Indonesia sangat sering menggunakan awalan pasif *di-kan* yang tidak memiliki padanan subjek aktif langsung.
- **Teks Indonesia:**  
  *"Dalam penelitian ini dilakukan pengujian terhadap modul sensor untuk mengetahui tingkat kepekaannya."*
- **Terjemahan Kaku (Translationese):**  
  *❌ "In this research, testing is done on the sensor module to know its sensitivity level."*
- **Transformasi Akademik Luwes (Translation as Rewriting):**  
  *✅ "The sensor module was tested to evaluate its sensitivity threshold."*

### 4.2 Menangani Frasa Transisi Khas Indonesia
| Frasa Transisi Indonesia | Kesalahan Kalke (Hindari) | Transformasi Baku Bahasa Inggris |
| :--- | :--- | :--- |
| **Adapun mengenai...** | *As for... / As regarding...* | Langsung sebutkan subjeknya: **"Regarding the...", "With respect to..."** |
| **Dalam hal ini...** | *In this case... (diulang terus)* | Gunakan klausa partisipial atau: **"In this context, ...", "Specifically, ..."** |
| **Berdasarkan hal tersebut...** | *Based on that thing...* | **"Consequently, ...", "Accordingly, ...", "Based on these observations, ..."** |
| **Dapat dilihat bahwa...** | *Can be seen that...* | **"As indicated by...", "It is apparent that...", "Fig. 2 reveals that..."** |
| **Perlu diketahui bahwa...** | *Need to be known that...* | Hapus! Langsung nyatakan faktanya: **"Notably, ...", "It is worth noting that..."** |

### 4.3 Padanan Istilah Institusional & Pendidikan Indonesia
| Konsep Pendidikan Indonesia | Padanan Resmi Bahasa Inggris Akademik |
| :--- | :--- |
| **Skripsi (S-1)** | **Undergraduate Thesis / Bachelor's Thesis** |
| **Tesis (S-2)** | **Master's Thesis** |
| **Disertasi (S-3)** | **Doctoral Dissertation** |
| **Kerja Praktik / Magang Industri** | **Industrial Internship Report / Practical Work** |
| **Dosen Pembimbing** | **Academic Advisor / Thesis Supervisor** |
| **Dosen Penguji** | **Thesis Examiner / Committee Member** |
| **Program Studi / Jurusan** | **Department of [Informatics] / Study Program** |
| **Fakultas Teknik** | **Faculty of Engineering** |

---

## 5. PROTOKOL PERLINDUNGAN ASET & FORMULA

Saat menerjemahkan teks naskah akademik atau buku ilmiah, **DILARANG KERAS MENGUBAH**:
1. **Persamaan Rumus:** Blok Native Word Equation (`<m:oMath>`) dan ekspresi matematika ($D = b^2 - 4ac$, $\sigma(z)$) harus tetap utuh 100%.
2. **Kutipan Field Code Zotero:** Tag OpenXML `<w:instrText> ADDIN ZOTERO_ITEM ... </w:instrText>` tidak boleh diubah strukturnya; hanya teks representasi visual di dalam `<w:t>` yang diselaraskan (misal `(Hanson dkk., 2015)` menjadi `(Hanson et al., 2015)`).
3. **Data Numerik:** Angka, persentase, koordinat, dan nilai statistik tidak boleh berubah nilai atau dibulatkan secara sepihak.

---

## 6. AUDIT KUALITAS HASIL TERJEMAHAN (10-POINT QA CHECKLIST)

Sebelum hasil terjemahan diserahkan atau dikompilasi kembali ke berkas Word/Buku final:
- [ ] **1. Bebas Translationese:** Kalimat tidak lagi terdengar seperti terjemahan harfiah struktur bahasa Indonesia.
- [ ] **2. Alur Deduktif:** Inti kalimat diletakkan di awal klausa, bukan berputar-putar di anak kalimat.
- [ ] **3. Konsistensi Glosarium:** Seluruh istilah teknis di `GLOSSARY.json` konsisten 100% dari bab awal hingga akhir.
- [ ] **4. 0 Kata Klise AI:** Bebas dari kata *delve, crucial, notably, landscape, leverage, realm, tapestry*.
- [ ] **5. Tenses Sesuai Seksi:** Metode memakai *Past Passive*, Pengantar memakai *Present/Present Perfect*, Hasil memakai *Past*.
- [ ] **6. Pronomina Personal Bersih:** 0 kemunculan kata *We, Our, I, Us*.
- [ ] **7. Pungtuasi Baku:** Rentang angka memakai en-dash (`–`), desimal memakai titik (`.`), minus memakai `−`.
- [ ] **8. Angka Numerik Akurat:** 100% nilai statistik dan angka sama persis dengan naskah sumber.
- [ ] **9. Label Tabel & Figur Valid:** `Table 1`, `Fig. 1` dipanggil runtut sesuai urutan di teks.
- [ ] **10. Kerapian Format:** Heading Markdown atau XML Word terpelihara tanpa paragraf menggantung (*orphan*).

