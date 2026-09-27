# PEDOMAN PENULISAN ARTIKEL JURNAL ILMIAH (STANDAR SINTA 1–4 & SCOPUS)

Dokumen ini merupakan panduan spesifik penulisan artikel ilmiah dengan struktur internasional **IMRaD** (*Introduction, Methods, Results, and Discussion*) yang dirancang untuk menembus seleksi editor dan mitra bestari (*peer-review*) pada jurnal ilmiah terakreditasi SINTA dan terindeks Scopus.

---

## 1. ATURAN UMUM & STRUKTUR IMRAD

Artikel jurnal berbeda fundamental dengan skripsi. Artikel jurnal menekankan pada **keringkasan, kebaruan (*novelty*), ketajaman metodologis, dan signifikansi hasil**. Jumlah kata umumnya dibatasi antara 4.000 hingga 8.000 kata (atau 8 hingga 15 halaman).

### Struktur Standar:
1. **Judul (*Title*)**
2. **Identitas Penulis & Afiliasi (*Authors, Affiliations, Corresponding Email*)**
3. **Abstrak (*Abstract*) & Kata Kunci (*Keywords*)**
4. **Pendahuluan (*Introduction*)**
5. **Metode Penelitian (*Methods / Proposed Methodology*)**
6. **Hasil (*Results*)**
7. **Pembahasan (*Discussion*)** — *sering digabung menjadi Results and Discussion*
8. **Kesimpulan (*Conclusion*)**
9. **Ucapan Terima Kasih (*Acknowledgment*)** — *opsional*
10. **Daftar Pustaka (*References*)**

### Karakteristik Tata Letak Khusus Jurnal:
- **Aliran Teks Kontinu (*Continuous Flow / No Page Break*):** Berbeda dengan skripsi di mana setiap bab baru wajib dimulai pada halaman baru (*page break*), pada artikel jurnal seluruh bagian (1. Pendahuluan s.d. 5. Kesimpulan dan Daftar Pustaka) **mengalir bersambung secara kontinu tanpa page break**. Hal ini demi efisiensi kuota halaman publikasi. Pergantian seksi hanya ditandai dengan jeda spasi vertikal (*space before* 12–14 pt) dan properti *keep with next* agar judul seksi tidak tertinggal sendirian di baris terbawah halaman (*anti-orphan*).

---

## 2. PANDUAN RINCI SETIAP KOMPONEN ARTIKEL

### 2.1 Judul (*Title*)
- **Panjang Ideal:** 10 – 15 kata.
- **Kaidah:**
  - Padat, spesifik, dan memuat kata kunci utama (variabel/metode + objek riset).
  - Hindari kata klise skripsi: *"Rancang Bangun..."*, *"Penerapan..."*, *"Implementasi..."*, *"Sistem Informasi Berbasis Web..."*.
  - Gunakan istilah ilmiah kontributif: *"Adaptasi Domain..."*, *"Optimasi..."*, *"Pendekatan Hibrida..."*, *"Evaluasi Komparatif..."*.
  - Jika target SINTA 1, SINTA 2, atau Scopus, judul **wajib ditulis dalam Bahasa Inggris**.

### 2.2 Abstrak (*Abstract*) & Aturan Mutlak Halaman Pertama (*Page 1 Fit*)
- **Format:** 1 paragraf tunggal, panjang **150 – 200 kata** (ideal: ~150–175 kata untuk jurnal dengan abstrak dwibahasa), spasi tunggal (1,0), font 9.5–10 pt Times New Roman.
- **Aturan Mutlak Halaman Pertama (*Page 1 Fit*):**
  - Pada format artikel jurnal standar SINTA dan Scopus, seluruh bagian *Front Matter* (Judul bilingual, Penulis, Afiliasi, Email Korespondensi, Abstrak Indonesia, Kata Kunci, Abstract Inggris, dan Keywords) **WAJIB TUNTAS SEPENUHNYA DI HALAMAN 1**.
  - DILARANG KERAS membiarkan abstrak tumpah (*overflow*) ke Halaman 2. Jika abstrak terpotong dan sebagian teks abstrak berada di halaman kedua, naskah akan langsung dikembalikan oleh *editorial desk* karena cacat tata letak (*layout flaw*).
  - Untuk menjaga agar muat di Halaman 1: gunakan spasi tunggal (1.0x), margin paragraf rapat (*space after* 3–4 pt), dan kompresi panjang teks ke kisaran 150–180 kata per bahasa.
- **Struktur Wajib 4 Elemen (IMRaD Mini):**
  1. *Background & Objective (1–2 kalimat):* Masalah utama di lapangan dan tujuan penelitian.
  2. *Proposed Method (2–3 kalimat):* Algoritma, arsitektur, atau metodologi spesifik yang diusulkan beserta kebaruannya.
  3. *Key Empirical Results (2–3 kalimat):* Temuan kuantitatif utama dengan angka metrik yang jelas (seperti skor akurasi, F1-score, delta peningkatan, perbandingan dengan baseline). **Wajib mencantumkan data numerik riil!**
  4. *Conclusion & Significance (1 kalimat):* Kesimpulan utama dan dampak praktis atau teoretisnya.
- **Pantangan Abstrak:**
  - DILARANG mencantumkan sitasi pustaka (contoh: [1] atau Smith (2020)).
  - DILARANG menggunakan singkatan tanpa penjelasan awal.
  - DILARANG menuliskan kalimat menggantung seperti *"hasil akan dibahas lebih lanjut pada artikel ini"*.
  - DILARANG menyisakan karakter format mentah LaTeX (`$`, `\times`, dll). Gunakan simbol Unicode murni (`κ`, `Δ`, `×`).

### 2.3 Kata Kunci (*Keywords*)
- Berisi **3 – 5 kata atau frasa spesifik**.
- Dipisahkan dengan koma (`,`) atau titik-koma (`;`).
- Tidak mengulang kata yang sudah tertera secara persis di judul untuk memperluas jangkauan mesin pengindeks (*indexing engine*).

### 2.4 Pendahuluan (*Introduction*)
Pendahuluan artikel jurnal harus mengikuti pola segitiga terbalik (*inverted pyramid*) yang padat (maksimal 1,5 – 2 halaman):
1. **Latar Belakang & Urgensi:** Menjelaskan fenomena riil dan mengapa domain ini penting diteliti.
2. **Kajian Literatur Terkini (*State-of-the-Art*):** Mengulas penelitian-penelitian terdahulu yang relevan (minimal 10–15 referensi primer jurnal 5 tahun terakhir).
3. **Kesenjangan Riset (*Research Gap*):** Menjelaskan secara tegas kelemahan, celah, atau keterbatasan metode sebelumnya yang belum terpecahkan.
4. **Kebaruan & Solusi yang Diusulkan (*Novelty & Contribution*):** Menjelaskan solusi yang ditawarkan penulis untuk mengisi celah tersebut.
5. **Tujuan Penelitian:** Pernyataan lugas tujuan eksperimen yang dilakukan.

### 2.5 Metode Penelitian (*Methods*)
Metode harus ditulis dengan tingkat ketelitian tinggi agar dapat **direplikasi (*reproducible*)** oleh peneliti lain:
- **Dataset:** Sumber data, ukuran sampel, distribusi kelas, dan prosedur pengumpulan.
- **Prapemrosesan (*Preprocessing*):** Rincian pembersihan data dan pertimbangan ilmiah di baliknya.
- **Arsitektur Model:** Diagram pipeline sistem, spesifikasi model (nama model base, tokenizer, embedding dimension).
- **Hyperparameter & Lingkungan Eksperimen:** Learning rate, batch size, epochs, optimizer, hardware (GPU/CPU), dan pustaka perangkat lunak.
- **Metrik Evaluasi:** Rumus matematis akurasi, presisi, recall, F1-score, atau skor reliabilitas inter-rater (Cohen's Kappa).

### 2.6 Hasil (*Results*)
- Menampilkan data eksperimen secara objektif dan sistematis.
- Menggunakan **Tabel Format APA (3 garis horizontal)** dan grafik visual beresolusi tinggi.
- Narasi hasil harus menyoroti angka-angka kunci di tabel tanpa menduplikasi seluruh isi tabel ke dalam teks.

### 2.7 Pembahasan (*Discussion*)
Ini adalah bagian penentu apakah artikel diterima (*accepted*) atau ditolak (*rejected*):
- **Bukan Sekadar Mengulang Hasil:** Pembahasan tidak boleh hanya menceritakan kembali angka-angka di tabel.
- **Menjawab "Mengapa":** Mengapa model yang diusulkan menghasilkan performa lebih baik? Mengapa baseline gagal?
- **Konfrontasi Literatur:** Membandingkan temuan penelitian saat ini dengan klaim penelitian terdahulu yang dikutip di Pendahuluan (apakah sejalan atau membantah temuan peneliti lain?).
- **Analisis Galat (*Error Analysis*):** Menguraikan kasus-kasus di mana model salah memprediksi (*false positive / false negative*).
- **Keterbatasan (*Threats to Validity*):** Secara jujur menyebutkan batasan metodologi yang dihadapi.

### 2.8 Kesimpulan (*Conclusion*)
- Ditulis dalam bentuk narasi (hindari penggunaan *bullet points* jika template jurnal melarangnya).
- Menyajikan sintesis ringkas jawaban atas pertanyaan riset berdasarkan bukti empiris.
- Memuat implikasi praktis dan rekomendasi arah penelitian masa depan (*future works*).

### 2.9 Referensi (*References*)
- **Kualitas Sumber:** Minimal 80% berasal dari **artikel jurnal ilmiah primer bereputasi** yang terbit dalam **5 tahun terakhir**. Hindari mengutip buku teks umum, modul kuliah, skripsi lama, atau blog/website tanpa reputasi ilmiah.
- **Gaya Sitasi:**
  - **IEEE Style (Numerik):** `[1]`, `[2]`, `[3]` — jamak digunakan di bidang Ilmu Komputer / Informatika.
  - **APA Style 7th Edition (Nama-Tahun):** `(Koto et al., 2021)` — jamak digunakan di bidang Sistem Informasi / Interdisipliner.
- Gunakan *reference manager* (Mendeley, Zotero) untuk memastikan keselarasan antara kutipan di dalam teks dengan daftar di bagian akhir.

---

## 3. MASTER TEMPLATE RESMI JURNAL SINTA (.DOCX) SIAP PAKAI

Untuk memudahkan penulisan dan memastikan kepatuhan 100% tanpa mengotori workspace proyek pengguna:
- **Lokasi Master Template di Skill:**
  `templates/template_jurnal_sinta.docx`
- **Karakteristik Template:**
  1. Standar OJS Jurnal Terakreditasi SINTA (Ukuran A4, Margin Normal Simetris 2,54 cm).
  2. Typografi Header: Judul TNR 12 pt Tebal, Identitas Penulis 10 pt, Abstrak 9.5–10 pt Spasi Tunggal.
  3. Continuous Flow Section: Format penomoran seksi `1. PENDAHULUAN`, `2. METODE`, `3. HASIL DAN PEMBAHASAN`, `4. KESIMPULAN` tanpa Page Break buatan.
  4. Template tabel standar APA 3 garis horizontal.
- **Cara Penggunaan yang Bersih:**
  Agen menyalin template ini dari folder skill langsung ke target output naskah pengguna atau membaca format dasarnya saat membangun file `.docx` baru, sehingga workspace proyek tetap bersih dan bebas dari file template sampah.

