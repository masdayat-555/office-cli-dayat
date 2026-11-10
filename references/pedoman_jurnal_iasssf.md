# PEDOMAN PENULISAN & FORMAT NASKAH ARTIKEL JURNAL IASSSF
## (Institute for Advanced Social, Science, and Sustainable Future)

> [!IMPORTANT]
> **KEDUDUKAN TEMPLATE RESMI & KONSENSUS STANDAR MUTLAK**  
> Dokumen ini adalah standar resmi dan baku penulisan, penyuntingan, dan pemformatan artikel ilmiah untuk **IASSSF (Institute for Advanced Social, Science, and Sustainable Future)**.  
> Seluruh pedoman di bawah ini disusun langsung dari **25 Komentar Editorial Resmi Admin IASSSF** dan analisis forensik OpenXML pada berkas master template.
> - **Master Template Word**: [`templates/Template IASSSF.docx`](file:///c:/Users/masdayat/.gemini/config/skills/office-cli/templates/Template%20IASSSF.docx)  
> - **Lisensi Publikasi**: *Creative Commons Attribution 4.0 International (CC BY 4.0)*.  
> - **Kesadaran Temporal**: Tahun berjalan adalah **2026**. Batasan referensi 5–10 tahun terakhir mencakup terbitan tahun **2016–2026**.

---

## 1. DOKTRIN UTAMA: INTEGRITAS & PROTOKOL "ANTI-SOK TAU"

> [!CAUTION]
> ### 🚨 PROTOKOL "ANTI-SOK TAU" (DILARANG MENGARANG ATAU BERHALUSINASI)
> Penulisan artikel jurnal IASSSF menuntut akurasi empiris dan integritas ilmiah yang ketat.  
> Agen AI yang menyusun atau menyunting naskah IASSSF **DILARANG KERAS**:
> 1. Mengarang data eksperimen, nilai statistik, $p\text{-value}$, atau temuan empiris fiktif.
> 2. Memalsukan atau mengarang nomor protokol Komite Etik (*Ethical Clearance*).
> 3. Mengarang lembaga donor atau nomor kontrak hibah (*Grant Number*).
> 4. Mengarang nomor pengenal peneliti (ORCID iD, Scopus Author ID, Web of Science ResearcherID).
> 5. Memasang gambar atau grafik sembarangan yang resolusinya rendah atau tidak relevan.
> 6. **Mengarang tanggal editorial (*Received Date*, *Revised Date*, *Accepted Date*)**: Tanggal ini merupakan wewenang mutlak dewan redaksi jurnal setelah proses review formal; agen **WAJIB** mengosongkannya sebagai *placeholder* editorial.
> 7. **Menyisipkan sitasi fiktif / halusinasi**: Demi mengejar kuota minimal referensi IASSSF (>30 referensi), agen **DILARANG KERAS** menyisipkan sitasi luar secara sepihak ke dalam teks atau daftar pustaka tanpa persetujuan eksplisit penulis. Naskah artikel **HANYA** boleh memuat referensi 100% riil dari draf asli/folder berkas PDF penulis yang tersinkronisasi di Zotero/Mendeley.
> 8. **Menuliskan rumus matematika sebagai teks raw LaTeX di Word**: Dilarang membiarkan sintaks LaTeX mentah (seperti `\sigma(z) = \frac{1}{1 + e^{-z}}`, `\mathcal{L}_{BCE}`, atau `$...$`) tercetak di dalam paragraf Word. Seluruh persamaan matematika display **WAJIB** berformat objek **Native Word Equation (`<m:oMath>`)** font *Cambria Math*.
>
> **TINDAKAN WAJIB AGEN JIKA DATA / ASSET / REFERENSI BELUM LENGKAP:**  
> Jika dalam pengerjaan naskah terdapat kebutuhan gambar/diagram ilmiah, data numerik, akun identitas penulis, izin etik, atau kuota referensi yang belum mencukupi standar jurnal (>30 judul), agen **WAJIB**:
> 1. Secara transparan menghentikan asumsi dan melaporkannya dalam **Laporan Audit**.
> 2. Menandai bagian yang belum lengkap dengan penanda jelas (`[TODO: USER ACTION REQUIRED]`).
> 3. Untuk kekurangan referensi, agen menyajikan **Daftar Rekomendasi Jurnal Internasional Terindeks Bereputasi (dengan DOI nyata)** dan **MENGUNDUH BERKAS PDF OPEN ACCESS ASLINYA** ke dalam folder khusus (`referensi/rekomendasi_internasional/`) agar penulis dapat membaca dan memverifikasi keasliannya sebelum memutuskan untuk menyitirnya. JANGAN PERNAH menyisipkannya langsung ke naskah sebelum penulis menyetujuinya!

---

## 2. KETENTUAN UMUM & DUA JENIS NASKAH IASSSF

Jurnal IASSSF menerima 2 jenis artikel ilmiah berbahasa Inggris Amerika (*American English*):

| Parameter | Original Research Article | Review Article |
| :--- | :--- | :--- |
| **Fokus Utama** | Riset empiris orisinal dengan kontribusi dan pembahasan komprehensif | Kajian literatur kritis, sistematis, atau bibliometrik / meta-analisis |
| **Batas Kata (*Word Count*)** | **6.000 hingga 7.000 kata** (di luar daftar referensi) | **7.000 hingga 9.000 kata** (di luar daftar referensi) |
| **Struktur Inti** | *Title, Byline, Abstract, 1. Introduction, 2. Methods, 3. Results and Discussion, 4. Conclusions, Back Matter, References, Author Biographies* | *Title, Byline, Abstract, 1. Introduction, 2. Methodology of Review, 3. Synthesis & Discussion, 4. Conclusions, Back Matter, References, Author Biographies* |
| **Jumlah Referensi** | **Lebih dari 30 referensi (> 30)** | **Minimal 50 referensi ($\ge$ 50)** |
| **Proses Review** | *Double-blind peer review* (identitas penulis disamarkan saat proses telaah) | *Double-blind peer review* |

---

## 3. MASTER KONSENSUS: 25 KOMENTAR EDITORIAL ADMIN IASSSF

Berikut adalah 25 pedoman baku yang ditanamkan langsung oleh Dewan Redaksi Admin IASSSF di dalam template resmi, yang wajib ditaati sebagai hukum naskah:

| No. Komentar | Fokus Elemen | Pedoman Baku Editorial Admin IASSSF |
| :---: | :--- | :--- |
| **Comment 0** | **Judul Artikel (*Title*)** | 1. Rumusan isi yang singkat, padat, dan jelas; dapat kreatif untuk menarik pembaca.<br>2. **Dilarang menggunakan singkatan** di dalam judul.<br>3. **Maksimum 25 kata**.<br>4. Wajib ditulis dalam bahasa Inggris Amerika (*American English*). |
| **Comment 1** | **Nama & Afiliasi Penulis** | Cantumkan nama lengkap semua penulis menggunakan **Cambria 11 pt, Proper Case, Bold** (tanpa gelar akademik). Setelah nama, cantumkan afiliasi menggunakan **Cambria 10 pt, Capitalize Each Word, Italics**. Hubungkan penulis dan afiliasi menggunakan huruf/angka superskrip. |
| **Comment 2** | **Korespondensi** | Penulis korespondensi wajib menggunakan **alamat email resmi institusi/afiliasi** (*official affiliation email*). |
| **Comment 3** | **Panjang Abstrak** | Abstrak wajib mencerminkan isi keseluruhan naskah dan **TIDAK BOLEH MELEBIHI 300 KATA** (*not exceed 300 words*). |
| **Comment 4** | **Format Isi Abstrak** | **Tebalkan font untuk setiap judul elemen abstrak** (*Bold the font for each abstract element title*): `Background: `, `Methods: `, `Findings: `, `Conclusion: `, `Novelty/Originality of this article: `. |
| **Comment 5** | **Kata Kunci (*Keywords*)** | Istilah yang digunakan pengindeks dan basis data. Kata kunci terdiri dari **MAKSIMUM 5 KATA/FRASA**, **disusun menurut abjad (alfabetis)**, dan **dipisahkan oleh tanda titik-koma (`;`)**. Font Cambria 11 pt huruf kecil (*lowercase*). Label `KEYWORDS` ukuran 12 pt Bold. |
| **Comment 6** | **Spasi Judul Bab (*Headings*)** | Gunakan **spasi ganda (2 spasi / 2 baris kosong) sebelum heading** dan **satu spasi (1 baris kosong) setelah heading**. |
| **Comment 7** | **Heading Tingkat 1** | Judul bab utama wajib **rata kiri (*left-justified*), tebal (*bold*)**, huruf pertama dikapitalisasi dan dinomori secara berurutan, dimulai dari Pendahuluan (`1. Introduction`, `2. Methods`, `3. Results and Discussion`, `4. Conclusions`). |
| **Comment 8** | **Proporsi Pendahuluan** | Bab Pendahuluan (*Introduction*) harus mencakup sekitar **20% hingga 25% dari total teks naskah**. |
| **Comment 9** | **Higienitas Sitasi** | **Hindari jejak sitasi (*citation trails*)** yang rusak/kotor akibat perangkat lunak pemformat sitasi. Gunakan field kode CSL bersih standar APA 7th Edition. |
| **Comment 10** | **Penempatan Gambar & Tabel** | **Setiap tabel dan gambar WAJIB diletakkan pada halaman yang sama dengan penjelasannya** di dalam naskah (*placed in the same page as its explanation*). Dilarang menumpuk gambar di akhir naskah. |
| **Comment 11** | **Standar Grafik / Bagan (*Charts*)** | Jika menggunakan grafik/bagan: lengkapi keterangan judul sumbu horizontal utama dan sumbu vertikal utama, serta **tampilkan persentase atau nilai utama langsung pada grafik**. |
| **Comment 12** | **Spasi Gambar** | Berikan **satu spasi (1 baris kosong) sebelum gambar** dan **setelah nama atau sumber gambar**. |
| **Comment 13** | **Penomoran & Keterangan Gambar** | Gambar, skema, dan diagram wajib dinomori berurutan. Format: `Fig. 1. Keterangan gambar...` menggunakan font **Cambria 10 pt, rata tengah (*centered*), Sentence case**. |
| **Comment 14 & 21** | **Sumber Gambar & Tabel** | Penulisan sumber acuan: **Cambria 10 pt, rata tengah (*centered*)** diletakkan di bawah gambar/tabel (contoh: `(Author et al., 2026)` atau `(Penulis, 2026)`). |
| **Comment 15** | **Proporsi Metode** | Bab Metode (*Methods*) dibatasi **maksimum sekitar 20% dari total teks naskah**. |
| **Comment 16** | **Peta Lokasi Penelitian** | Jika menyajikan peta lokasi riset, wajib mematuhi aturan ketat:<br>1. Peta wilayah/negara wajib terhubung dengan peta fokus dalam **warna penuh (*full color*)**.<br>2. **Tangkapan layar Google Maps atau citra satelit DILARANG KERAS (TIDAK DITERIMA)**.<br>3. Wajib menyertakan **arah mata angin terpisah (North arrow)** dan **skala grafis terpisah**.<br>4. Tidak perlu menampilkan koordinat garis lintang dan bujur (*latitude/longitude*). |
| **Comment 17** | **Proporsi Hasil & Pembahasan** | Penjelasan pada bab Hasil dan Pembahasan (*Results and Discussion*) merupakan inti naskah, mencakup **minimal 40% hingga 50% dari total naskah**. |
| **Comment 18** | **Sub-Heading Tingkat 2** | Judul subbab menggunakan **Sentence case, huruf miring (*italic*)**, dinomori desimal `1.1`, `1.2`, `2.1`, `3.1`, dan **rata kiri (*left-justified*)** (Cambria 11 pt Italic). |
| **Comment 19** | **Format Penulisan Tabel** | 1. Serahkan tabel sebagai **teks yang dapat diedit (*editable text*)**, bukan gambar raster.<br>2. Nomor tabel diketik di atas tabel ukuran **10 pt rata kiri** (`Table 1.`). Keterangan/deskripsi tabel juga ditulis di atas tabel rata tengah/kiri.<br>3. Seluruh tabel wajib disebut dan dirujuk dalam teks naskah.<br>4. Tabel disajikan dalam **format garis horizontal 3 baris (APA style)**: garis batas atas judul, garis batas bawah kepala kolom (*header*), dan garis penutup paling bawah tabel.<br>5. **DILARANG MENGGUNAKAN GARIS VERTIKAL DAN WARNA ARSIRAN (*SHADING*) DALAM SEL TABEL**. |
| **Comment 20** | **Spasi Tabel** | Berikan **satu spasi (1 baris kosong) sebelum tabel** dan **setelah nama atau sumber tabel**. |
| **Comment 22** | **Batasan Kesimpulan** | Bab Kesimpulan (*Conclusions*) **MAKSIMUM 2 PARAGRAF** (*maximum 2 paragraphs*). |
| **Comment 23** | **Tautan Aktif Referensi** | **Pastikan untuk mengaktifkan tautan hiperlink untuk setiap referensi**. Tautan aktif akan terlihat saat kursor diarahkan ke alamat sumber referensi (DOI/URL) dan warna font berubah menjadi **biru (`#0000FF`)**. |
| **Comment 24** | **Ketentuan Umum Bahasa, Huruf, Pronoun & Nomor Baris** | 1. Gunakan bahasa Inggris Amerika (*American English*).<br>2. Format halaman A4 ($210 \times 297\text{ mm}$), margin $30\text{ mm}$ / template resmi.<br>3. **DILARANG MENGGUNAKAN KATA GANTI PERSONAL** (*personal pronouns*) seperti *We, Our, I, Us*; ganti dengan bentuk pasif orang ketiga (*third-person passive voice*).<br>4. **Sediakan nomor baris kontinu (*line numbers*)** dari judul sampai kesimpulan untuk mempermudah proses penelaahan (*review*). |

---

## 4. TATA LETAK, MARGIN, & TIPOGRAFI PRESISI (CAMBRIA SINGLE-COLUMN)

Tata letak naskah IASSSF menggunakan format **1 Kolom Penuh (*Single-Column*)** dari awal hingga akhir dokumen:

### 4.1 Pengaturan Halaman & Margin
- **Ukuran Kertas:** A4 ($21{,}0\text{ cm} \times 29{,}7\text{ cm}$ / $595{,}3\text{ pt} \times 841{,}9\text{ pt}$).
- **Orientasi:** Portrait.
- **Batas Margin:**
  - **Margin Atas (*Top Margin*):** $2{,}0\text{ cm}$ ($56{,}7\text{ pt}$).
  - **Margin Bawah (*Bottom Margin*):** $2{,}5\text{ cm}$ ($70{,}9\text{ pt}$).
  - **Margin Kiri (*Left Margin*):** $3{,}0\text{ cm}$ ($85{,}05\text{ pt}$).
  - **Margin Kanan (*Right Margin*):** $3{,}0\text{ cm}$ ($85{,}05\text{ pt}$).
- **Jarak Header:** $1{,}3\text{ cm}$ ($36{,}85\text{ pt}$).
- **Jarak Footer:** $0{,}7\text{ cm}$ ($19{,}85\text{ pt}$).

### 4.2 Struktur 3 Seksi (*Three-Section Architecture*)
Dokumen Word IASSSF dibangun di atas 3 seksi OpenXML:
1. **Section 0 (Front Matter):** Halaman judul, nama penulis, afiliasi, korespondensi, Garis Pembatas 1, baris tanggal, abstrak, kata kunci, dan Garis Pembatas 2. Berakhir dengan seksi continuous `sectPr_0`. Tanpa nomor baris.
2. **Section 1 (Main Body):** Batang tubuh naskah dari `1. Introduction`, `2. Methods`, `3. Results and Discussion`, hingga `4. Conclusions`. Memiliki **nomor baris kontinu di margin kiri (`w:lnNumType countBy="1" restart="continuous"`)**.
3. **Section 2 (Back Matter & References):** Bagian akhir tak bernomor (`Acknowledgement`, `Funding`, `References`, dan Kotak Biodata Penulis). Tanpa nomor baris.

---

## 5. DUA GARIS PEMBATAS HORIZONTAL TEBAL (1,5 PT) & BARIS TANGGAL

Berdasarkan analisis forensik template IASSSF, terdapat dua garis pembatas horizontal tegas pada halaman pertama:

### 5.1 Garis Pembatas 1 (Bawah Korespondensi / Atas Tanggal)
- Diterapkan pada paragraf kosong tepat setelah baris `*Correspondence:`.
- **Spesifikasi OpenXML**:
  ```xml
  <w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
    <w:top w:space="0" w:sz="0" w:val="nil"/>
    <w:left w:space="0" w:sz="0" w:val="nil"/>
    <w:bottom w:color="000000" w:space="1" w:sz="12" w:val="single"/>
    <w:right w:space="0" w:sz="0" w:val="nil"/>
    <w:between w:space="0" w:sz="0" w:val="nil"/>
  </w:pBdr>
  ```
  *(Nilai `w:sz="12"` merepresentasikan garis solid tebal 1,5 pt hitam pekat)*.

### 5.2 Garis Pembatas 2 (Bawah Kata Kunci / Pembatas Seksi 0 ke 1)
- Diterapkan pada paragraf pemisah tepat setelah baris `KEYWORDS:` dan menyatu dengan `<w:sectPr>` penutup Seksi 0.
- **Spesifikasi OpenXML**: Memuat elemen `<w:pBdr>` dengan `<w:bottom w:val="single" w:sz="12" w:space="1" w:color="000000"/>` sekaligus menyematkan `<w:sectPr>` halaman pertama.

### 5.3 Pengaturan Baris Tanggal Editorial (*Received / Revised / Accepted Date*)
- Terletak di antara Garis Pembatas 1 dan Abstrak, diapit spasi kosong atas dan bawah.
- **Warna & Ukuran Font**: Cambria 9 pt, warna **Biru `#0000FF`**.
- **Tab Stop Presisi**: Menggunakan 2 tab stop agar teks terdistribusi simetris melintasi kolom:
  - Tab Stop 1: `pos="3402"` (posisi 6,0 cm untuk `Revised Date:`).
  - Tab Stop 2: `pos="6379"` (posisi 11,25 cm untuk `Accepted Date:`).
  - Indentasi Kanan: `w:ind w:right="113"`.
- **Format Teks**:
  ```text
  Received Date: \tRevised Date: \tAccepted Date:
  ```
  *(Tanggal dibiarkan kosong sebagai wewenang redaksi)*.

### 5.4 Penomoran Afiliasi Penulis (Word Native `numId="1"`)
- Baris afiliasi penulis menggunakan fitur penomoran native Word:
  ```xml
  <w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>
  <w:ind w:left="142" w:right="0" w:hanging="151"/>
  ```
- Teks afiliasi ditulis langsung tanpa mengetik angka manual:  
  `Department of Informatics, Faculty of Engineering, Universitas Janabadra, Jl. Tentara Rakyat Mataram No. 55, Yogyakarta 55231, Indonesia;`
- Word otomatis menambahkan angka superskrip $^1$, $^2$, $^3$ dengan lekukan gantung (*hanging indent*) presisi.

---

## 6. FORMAT ABSTRAK BERSTRUKTUR 1 PARAGRAF & KATA KUNCI

> [!IMPORTANT]
> **ATURAN MUTLAK ABSTRAK IASSSF:**
> 1. Abstrak wajib ditulis dalam **satu paragraf tunggal** (*single paragraph*). Dilarang memecahnya menjadi banyak paragraf!
> 2. Ukuran font adalah **Cambria 9 pt Regular**, rata kanan-kiri (*Justified*), spasi 1.0.
> 3. Panjang abstrak **TIDAK BOLEH MELEBIHI 300 KATA** (*maximum 300 words*).
> 4. **DILARANG menyisipkan referensi/sitasi** di dalam abstrak.
> 5. **DILARANG menggunakan singkatan tidak baku** kecuali didefinisikan secara eksplisit saat pertama kali disebut.
> 6. Paragraf abstrak **WAJIB** mengandung 5 sub-unsur terstruktur dengan label tebal (*inline bold labels*):

### Format Baku Isi Abstrak:
```text
ABSTRACT
Background: [Uraikan konteks penelitian, latar belakang permasalahan, dan tujuan penelitian secara ringkas dalam 1–6 kalimat, disertai sintesis singkat kajian literatur yang relevan]. Methods: [Jelaskan prosedur umum atau teknik penelitian, teknik pengumpulan data, serta metode analisis yang digunakan. Jika artikel berupa tinjauan literatur/review, nyatakan komponen teoretis yang dianalisis]. Findings: [Rangkum temuan utama penelitian, termasuk ukuran efek spesifik (effect sizes) dan signifikansi statistiknya (jika relevan). Cantumkan jumlah sampel/partisipan serta jelaskan korelasi nyata antara kerangka teori dan hasil temuan]. Conclusion: [Nyatakan kesimpulan pokok dalam 1–2 kalimat, tekankan aspek baru dan implikasi terpenting dari hasil penelitian]. Novelty/Originality of this article: [Paparkan secara eksplisit elemen baru, inovatif, kontribusi unik, atau metodologi terobosan yang membedakan naskah ini secara fundamental dari penelitian-penelitian terdahulu].
```

### Format Kata Kunci (*Keywords*):
- Format teks: `KEYWORDS:` (Cambria 12 pt Bold) dilanjutkan `: ` (9 pt Bold) lalu daftar kata kunci (Cambria 11 pt Regular).
- **Jumlah**: **Maksimum 5 kata/frasa kunci** (Comment 5 Admin IASSSF).
- **Urutan**: **Wajib berurutan secara alfabetis (A–Z)**.
- **Huruf**: Seluruhnya huruf kecil (*lowercase*), kecuali singkatan teknis baku (misal: CNN, ESP32).
- **Pemisah**: Tanda titik-koma (`;`), diakhiri tanda titik (`.`).
- Contoh:
  ```text
  KEYWORDS: audio classification; convolutional neural network; edge computing; log-mel spectrogram; pest repellent.
  ```

---

## 7. PEDOMAN STRUKTUR BATANG TUBUH (MODIFIED IMRaD)

### 7.1 `1. Introduction` (Pendahuluan) — Proporsi: 20% – 25%
- Jurnal IASSSF **TIDAK MEMILIKI** bab terpisah untuk *Theoretical Background* atau *Literature Review*. Seluruh landasan teoretis, tinjauan pustaka, dan *state of the art* **WAJIB diintegrasikan langsung ke dalam Pendahuluan**.
- **Alur Narasi Logis**:
  1. *Broad Context*: Konteks makro permasalahan yang diangkat.
  2. *Specific Issues & Theoretical Background*: Ulasan teori dan penelitian terkini dari jurnal terindeks bereputasi (5–10 tahun terakhir).
  3. *Research Gap*: Kesenjangan empiris/metodologis yang belum terpecahkan oleh studi terdahulu.
  4. *Objectives of the Study*: Tujuan penelitian yang dinarasikan secara lugas menggunakan kalimat efektif.
  5. *Hypotheses*: Formulasi hipotesis (jika ada) wajib berakar kuat pada kajian teori dan diarahkan satu arah (*one-tailed direction*).

### 7.2 `2. Methods` (Metode Penelitian) — Proporsi: Maksimum 20%
- Uraian metodologis harus sangat rinci agar penelitian dapat direplikasi secara presisi oleh peneliti lain (*reproducible*), namun tetap padat (maksimum 20% dari total naskah).
- **7.2.1 Kerangka Kerja Metodologi Riset Rekayasa (DSRM vs SDLC/Borg&Gall)**:
  - **Larangan Metodologi SDLC / Waterfall**: Dilarang menggunakan Waterfall, Agile, atau SDLC sebagai metodologi penelitian naskah jurnal rekayasa. SDLC adalah alur kerja industri, bukan metodologi riset ilmiah yang memvalidasi kontribusi keilmuan.
  - **Larangan R&D Pendidikan (Borg & Gall / Sugiyono)**: Dilarang menggunakan model Borg & Gall 10 langkah atau ADDIE/Sugiyono untuk riset rekayasa perangkat keras, IoT, atau AI. Model tersebut adalah metodologi riset pendidikan/pedagogik dan dinilai "salah kamar" oleh reviewer Scopus/SINTA.
  - **Standar Emas Wajib: Design Science Research Methodology (DSRM - Peffers et al., 2007)**:
    - Seluruh artikel yang merancang artifak rekayasa (sistem cerdas, perangkat keras IoT, arsitektur AI, algoritma) **WAJIB** merujuk pada pakem DSRM (*Peffers et al., 2007, Journal of Management Information Systems*, https://doi.org/10.2753/MIS0742-1222240302).
    - Batang tubuh metode wajib memetakan secara eksplisit 6 fase DSRM:
      1. *Problem Identification and Motivation*: Menjelaskan rumusan masalah spesifik dan urgensi solusi.
      2. *Objectives of a Solution*: Menetapkan tolok ukur kuantitatif (akurasi, konsumsi daya, latensi).
      3. *Design and Development*: Perancangan arsitektur artifak (skema sirkuit, pipeline audio, model CNN).
      4. *Demonstration*: Demonstrasi operasional artifak dalam pengujian fungsional terintegrasi.
      5. *Evaluation*: Pengujian empiris kuantitatif komparatif (confusion matrix, throughput, perbandingan literatur).
      6. *Communication*: Diseminasi kebaruan dan kontribusi ilmiah melalui publikasi naskah jurnal ini.
- **Pedoman Peta Lokasi Penelitian (Comment 16)**:
  - Peta wilayah/negara wajib terhubung dengan peta fokus dalam warna penuh (*full color*).
  - **Tangkapan layar Google Maps atau citra satelit DILARANG KERAS**.
  - Wajib menyertakan arah mata angin terpisah (North arrow) dan skala grafis terpisah. Tidak perlu garis bujur/lintang.

### 7.3 `3. Results and Discussion` (Hasil dan Pembahasan) — Proporsi: 40% – 50%
- Bab ini merupakan inti naskah dan wajib mengambil porsi **40% hingga 50% dari total naskah** (Comment 17).
- Pembahasan wajib mengaitkan kembali hasil empiris dengan teori dan hipotesis yang diajukan di bab Pendahuluan.
- Pembahasan **WAJIB** membandingkan hasil yang diperoleh dengan artikel jurnal sejenis yang telah terbit sebelumnya untuk membuktikan keunggulan posisi riset (*positioning*).
- Sub-Heading Tingkat 2 menggunakan format: `3.1 Sub-section headings` (Cambria 11 pt Italic, Sentence case).

### 7.4 `4. Conclusions` (Kesimpulan) — Batasan: Maksimum 2 Paragraf
- **Maksimum 2 Paragraf** (Comment 22).
- **DILARANG MENGGUNAKAN BULLET POINTS ATAU NUMBERING!** Wajib berupa alinea naratif mengalir.
- Sintesis temuan orisinal yang menjawab tujuan riset serta kontribusi nyata bagi ilmu pengetahuan.

---

## 8. BAGIAN AKHIR NASKAH WAJIB (*MANDATORY UNNUMBERED BACK MATTER*)

Seluruh subbab bagian belakang menggunakan judul tingkat 1 **tanpa penomoran angka** (*Unnumbered Headings*), berformat **Cambria 12 pt Bold**:

1. `Acknowledgement`: Apresiasi kepada asisten lab, penyedia fasilitas, atau bantuan teknis non-penulis.
2. `Author Contribution`: Uraian pembagian peran penulis menggunakan taksonomi baku **CRediT (*Contributor Roles Taxonomy*)**.
3. `Funding`: Pernyataan sumber pendanaan riset atau APC (contoh: *This research received no external funding*).
4. `Ethical Review Board Statement`: Pernyataan persetujuan komite etik (untuk subjek manusia/hewan) atau *Not applicable*.
5. `Informed Consent Statement`: Persetujuan partisipan riset atau *Not applicable*.
6. `Data Availability Statement`: Tautan repositori data terbuka (Zenodo, Figshare, GitHub) atau *available on request*.
7. `Conflicts of Interest`: Pernyataan ketiadaan konflik (*The authors declare no conflict of interest*).
8. `Declaration of Generative AI Use`: Pernyataan transparan fungsi alat AI generatif yang digunakan selama penulisan.
9. `Open Access`: Pernyataan lisensi resmi CC BY 4.0.
10. `References`: Daftar pustaka lengkap alfabetis APA 7th Edition dengan tautan aktif biru.
11. `Biographies of Author(s)`: Kotak tabel 1 sel tunggal berbingkai tipis hitam (0,5 pt) memuat bio ringkas masing-masing penulis (maksimum 100 kata), email institusi, ORCID, WoS ID, Scopus ID, dan homepage.

---

## 9. STANDAR ILUSTRASI GAMBAR, TABEL, & PERSAMAAN MATEMATIKA

### 9.1 Standar Gambar (*Figures*)
- **Perataan:** Rata tengah (*Center*).
- **Dimensi:** Lebar minimal gambar standar adalah **160 mm** ($16\text{ cm}$), namun disesuaikan dengan rasio aspek gambar.
- **Kaidah Aspek Rasio & Dimensi Gambar 1 Kolom (Anti-Blank Page)**:
  - Jangan memaksakan lebar 16 cm jika gambar berupa diagram alur vertikal yang tinggi, karena tingginya akan melebihi 25 cm dan memaksa Word membuat halaman kosong tak sedap dipandang (*blank orphan page*).
  - **Aturan Dimensi Berdasarkan Rasio Aspek (W/H)**:
    - *Diagram vertikal ramping* (W/H ~ 0.45–0.60): batasi lebar ke **2.1–2.7 inci (5.3–6.8 cm)**, dengan tinggi sekitar **4.5–5.3 inci (11.5–13.5 cm)**.
    - *Plot / grafik horizontal lebar* (W/H ~ 1.6–1.8): gunakan lebar **4.5–5.2 inci (11.5–13.2 cm)**, tinggi sekitar **2.8–3.0 inci (7.0–7.6 cm)**.
    - *Diagram seimbang / bujursangkar* (W/H ~ 0.9–1.2): gunakan lebar **3.2–4.0 inci (8.0–10.0 cm)**.
- **Protokol Citra Asli (Anti-Kompresi Ganda)**:
  - **Wajib menelusuri berkas master gambar asli di repositori**: Gunakan file master beresolusi tinggi (PNG/SVG 2000–5000 px, ekspor matplotlib DPI $\ge 300$, diagram draw.io murni) dari subfolder aset.
  - **Dilarang keras mengekstrak gambar dari PDF draf lama** yang sudah mengalami kompresi lossy berulang (*downsampling*).
- **Pencocokan Gambar Anti-Off-by-One**:
  - Sebelum memasukkan gambar ke dokumen, lakukan *visual inspection* dan susun matriks pemetaan nomor figur (`Fig. 1..n` $\leftrightarrow$ nama berkas asli $\leftrightarrow$ deskripsi visual). Mencegah bug fatal di mana diagram tertukar dengan foto atau plot evaluasi.
- **Kualitas:** Grafik Office diserahkan asli; ilustrasi garis wajib beresolusi minimal **600 DPI**.
- **Keterangan (*Caption*):** Diletakkan di **bawah ilustrasi**, rata tengah, Cambria 10 pt Sentence case: `Fig. 1. Blok diagram arsitektur...`.
- **Sumber:** Diletakkan di bawah keterangan gambar, rata tengah, Cambria 10 pt: `(Penulis, 2026)` atau `(Hanson et al., 2015)`.
- **Spasi:** Berikan **satu spasi sebelum gambar dan setelah sumber gambar** (Comment 12).
- **Bagan/Grafik (*Charts*):** Wajib melengkapi judul sumbu horizontal & vertikal serta menampilkan nilai persentase utama (Comment 11).

### 9.2 Standar Tabel (*Tables*)
- **Format:** Tabel diserahkan sebagai **teks yang dapat diedit (*editable text*)**, bukan gambar raster (Comment 19).
- **Penomoran & Judul:** Diletakkan di **atas tabel**, rata kiri (*Left*), Cambria 10 pt: `Table 1. Spesifikasi komponen perangkat keras...`.
- **Sumber:** Diletakkan di bawah tabel, rata tengah (*Center*), Cambria 10 pt: `(Penulis, 2026)`.
- **Desain Garis (Gaya APA 3-Line):**
  - Hanya 3 garis horizontal: batas atas judul tabel, batas bawah baris kepala kolom (*header*), dan garis penutup paling bawah.
  - **DILARANG MENGGUNAKAN GARIS VERTIKAL DAN WARNA ARSIRAN (*SHADING*)** (Comment 19).
- **Spasi:** Berikan **satu spasi sebelum tabel dan setelah sumber tabel** (Comment 20).

### 9.3 Persamaan Matematika (*Formulae & Equations*)
- **Wajib Native Word Equation (OMML / Cambria Math)**: Dilarang keras teks raw LaTeX mentah (seperti `\sigma(z)` atau `$...$`).
- **Tata Letak Rumus (Borderless 2-Column Table)**:
  - Kolom Kiri (`width=Inches(5.1)`): Rata tengah (*Center*), objek matematika `<m:oMath>`.
  - Kolom Kanan (`width=Inches(0.8)`): Rata kanan (*Right*), nomor persamaan `(Eq. 1)`.

---

## 10. PROTOKOL SITASI & REFERENSI (APA 7th EDITION)

> [!CAUTION]
> ### 🚨 DUA ATURAN LARANGAN MUTLAK SITASI (STRICTLY FORBIDDEN)
> 1. **HARAM MENYITASI ARTIKEL JURNAL IASSSF ITU SENDIRI (*ZERO IASSSF CITATION*)**: Dilarang menyitasi paper terbitan IASSSF untuk mencegah manipulasi metrik sitasi.
> 2. **HARAM MELAKUKAN SITASI-DIRI (*AUTHOR SELF-CITATION*)**: Dilarang menyitasi karya sendiri tanpa urgensi ceruk topik yang mendesak.

### 10.1 Ketentuan Kuantitas & Kualitas Referensi
1. **Jumlah Minimum:**
   - Original Research Article: **Lebih dari 30 referensi (> 30)**.
   - Review Article: **Minimal 50 referensi ($\ge$ 50)**.
2. **Kebaruan (Recency):** Wajib terbit dalam kurun waktu **5–10 tahun terakhir (2016–2026)**.
3. **Komposisi Sumber Primer:** Minimal **80%** dari artikel jurnal ilmiah terindeks **Scopus** dan **Web of Science**.
4. **Tautan Aktif Berwarna Biru (Comment 23):** Setiap referensi wajib memiliki tautan permanen aktif berformat `https://doi.org/...` berwarna font **Biru (`#0000FF`)**.
5. **Indensitas Menggantung (*Hanging Indent*):** Format paragraf daftar pustaka menggunakan hanging indent presisi sebesar **567 twips (28,35 pt)**.
6. **Integrasi Zotero Headless Cloud:** Seluruh sitasi wajib ditanam menggunakan field kode resmi Zotero (`ADDIN ZOTERO_ITEM`) dan kontainer otomatis daftar pustaka (`ADDIN ZOTERO_BIBL`).
7. **Perintah Cepat Registrasi Sitasi Baru (One-Line CLI):**
   - Jika menambah referensi baru yang telah diverifikasi (misal PDF dari `referensi/rekomendasi_internasional/`), jalankan:
     ```bash
     python ~/.gemini/config/skills/office-cli/scripts/zotero_headless_sync.py \
       --upload-pdf "referensi/rekomendasi_internasional/Peffers_2007_JMIS_DSRM.pdf" \
       --doi "10.2753/MIS0742-1222240302" \
       --collection "Pengusir Tikus Pintar" \
       --keys-file "zotero_item_keys.json"
     ```
   - Skrip otomatis menarik CrossRef kanonikal, mengunggah item & PDF ke Zotero Cloud, memperbarui pemetaan item keys, dan menghasilkan XML field code Word native.
8. **Penempatan Bodynote & Pembaruan Bibliografi Sinkron:**
   - Bodynote metodologi (seperti DSRM Peffers et al., 2007) wajib disematkan langsung di kalimat pembuka seksi `2. Methods`.
   - Entri bibliografi di bagian `References` wajib diperbarui secara alfabetis (A–Z) APA 7th Edition dengan tautan aktif biru (`#0000FF`) ke DOI resmi.
