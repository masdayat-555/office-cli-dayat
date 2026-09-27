# PEDOMAN PENULISAN ARTIKEL JURNAL NASIONAL TERAKREDITASI SINTA (SINTA 1-6)

Panduan ini mengatur standar baku penyusunan artikel jurnal ilmiah untuk publikasi pada jurnal-jurnal nasional terakreditasi **SINTA (*Science and Technology Index*)** di bawah naungan Kemendikbudristek / BRIN.

---

## 1. HIERARKI & KARAKTERISTIK TINGKATAN SINTA

SINTA mengelompokkan jurnal ilmiah ke dalam enam tingkatan akreditasi (SINTA 1 sampai SINTA 6):

1. **SINTA 1 & SINTA 2 (Akreditasi A / Unggul / Internasional):**
   - Jurnal bereputasi tertinggi di Indonesia.
   - SINTA 1 umumnya terindeks Scopus / Web of Science (WoS) dan mewajibkan penulisan naskah penuh dalam **Bahasa Inggris (*Full English*)**.
   - SINTA 2 menerima Bahasa Indonesia atau Bahasa Inggris, dengan standar metodologi ketat, *peer-review* kritis, dan rujukan mutakhir minimal 20-30 referensi primer.
2. **SINTA 3 & SINTA 4 (Akreditasi B / Baik Sekali):**
   - Tingkat akreditasi yang sangat jamak ditargetkan untuk luaran Skripsi, Tesis, atau hibah riset nasional.
   - Menggunakan Bahasa Indonesia baku dengan Abstrak dwibahasa (Indonesia & Inggris).
   - Mewajibkan struktur IMRaD yang runtut, pembuktian data kuantitatif yang jelas, dan minimal 15-20 referensi.
3. **SINTA 5 & SINTA 6 (Akreditasi C / Pembinaan):**
   - Jurnal nasional terakreditasi peringkat dasar.
   - Standar penulisan tetap mengikuti kaidah IMRaD, format tabel APA, dan sitasi standar.

---

## 2. ANATOMI RESMI NASKAH JURNAL SINTA (STRUKTUR IMRAD)

Format jurnal SINTA berbeda mendasar dari laporan skripsi:
- **DILARANG MENGGUNAKAN KATA 'BAB':** Penomoran seksi menggunakan angka Arab kapital (`1. PENDAHULUAN`, `2. METODE PENELITIAN`, `3. HASIL DAN PEMBAHASAN`, `4. KESIMPULAN`), bukan `BAB I`, `BAB II`.
- **Aliran Berkesinambungan (*Continuous Flow*):** Naskah mengalir bersambung dari seksi 1 sampai seksi terakhir **tanpa jeda pemisah halaman (*no page break*)**. Pergantian seksi hanya dipisahkan spasi vertikal (*space before* 10-12 pt) dan properti *keep with next* agar judul tidak terdampar di baris terbawah.

### 2.1 Judul Artikel (*Title*)
- Panjang ideal: 10 - 15 kata, lugas, spesifik, dan memuat inovasi/objek riset.
- Ditulis dalam dua bahasa: Judul utama Bahasa Indonesia (Times New Roman 12 pt Tebal, Kapital) dan Subjudul Bahasa Inggris (TNR 11 pt, Italic).
- Hindari kata klise seperti *"Rancang Bangun..."*, *"Penerapan..."*, gunakan istilah kontributif seperti *"Adaptasi Domain..."*, *"Analisis Sentimen Temporal..."*, *"Optimasi..."*.

### 2.2 Baris Kepemilikan (*Byline*) & Afiliasi
- Nama lengkap seluruh penulis tanpa gelar akademis (TNR 10 pt Tebal).
- Penulis korespondensi ditandai dengan tanda bintang (`*`).
- Afiliasi memuat: Nama Program Studi/Departemen, Fakultas, Universitas/Institusi, Kota, Negara (TNR 9.5 pt).
- Alamat surel (*corresponding email*) wajib dicantumkan secara aktif dan jelas.

### 2.3 Aturan Mutlak Halaman Pertama (*Page 1 Abstract Fit*)
- Seluruh elemen *front matter* (Judul bilingual, Penulis, Afiliasi, Email, Abstrak Indonesia, Kata Kunci, Abstract Inggris, dan Keywords) **WAJIB SELESAI TUNTAS DI HALAMAN 1**.
- DILARANG membiarkan teks abstrak terpotong atau tumpah (*overflow*) ke Halaman 2. Jika abstrak terlempar ke halaman kedua sebelum teks Pendahuluan dimulai, naskah akan langsung dikembalikan oleh *editorial desk*.
- **Formula IMRaD Mini Abstrak (150 - 200 kata per bahasa):**
  1. *Latar Belakang & Masalah:* 1-2 kalimat urgensi riil lapangan dan batasan solusi sebelumnya.
  2. *Metode yang Diusulkan:* 1-2 kalimat arsitektur, algoritma, atau pipeline beserta validasi *ground truth*.
  3. *Temuan Kuantitatif Konkret:* 2-3 kalimat memuat data metrik riil (akurasi, F1-score, lonjakan performa, reliabilitas Cohen's Kappa, volume dataset).
  4. *Kesimpulan & Implikasi:* 1 kalimat kontribusi ilmiah dan penerapan praktisnya.
- **Tipografi Blok Abstrak:** Font Times New Roman 9.5-10 pt, spasi tunggal (1.0x), indentasi kiri-kanan 0,5 cm, spasi antar-paragraf rapat (after 3-4 pt).
- **Kata Kunci (*Keywords*):** 3 - 5 kata/frasa kunci spesifik, dipisahkan tanda koma atau titik-koma.
- **Pantangan Abstrak:** Dilarang mencantumkan sitasi pustaka, dilarang menyisakan sintaks LaTeX mentah, dan dilarang menuliskan kalimat menggantung.

### 2.4 Pendahuluan (*Introduction*)
- Mengikuti pola segitiga terbalik: fenomena umum -> masalah spesifik -> kajian pustaka terkini (*state-of-the-art*) -> celah penelitian (*research gap*) -> kebaruan (*novelty*) & kontribusi penelitian.
- Minimal merujuk 10-15 artikel jurnal bereputasi 5-10 tahun terakhir.

### 2.5 Metode Penelitian (*Methods*)
- Ditulis secara sistematis, terukur, dan replikatif (*reproducible*).
- Menjelaskan: prosedur pengumpulan data, teknik sampling, prapemrosesan, arsitektur model/algoritma, lingkungan eksperimen (hardware/software), dan metrik evaluasi.
- Seluruh simbol matematika ditulis dalam karakter Unicode murni (`κ`, `Δ`, `×`, `≈`).

### 2.6 Hasil dan Pembahasan (*Results and Discussion*)
- **Penyajian Hasil:** Objektif, runtut, didukung tabel dan grafik visual beresolusi tinggi.
- **Format Tabel APA:** Tabel hanya menggunakan **3 garis horizontal tebal** (garis atas, garis bawah header, garis penutup bawah) dan **DILARANG menggunakan garis vertikal**. Judul tabel diletakkan di **ATAS TABEL**.
- **Format Gambar:** Judul gambar diletakkan di **BAWAH GAMBAR** rata tengah.
- **Pembahasan Mendalam:** Menjawab *mengapa* hasil tersebut tercapai, membandingkan dengan riset-riset terdahulu (apakah mengonfirmasi atau membantah), serta menganalisis galat (*error analysis*).

### 2.7 Kesimpulan (*Conclusion*)
- Sintesis ringkas atas jawaban rumusan masalah berdasarkan bukti empiris.
- Menyampaikan implikasi praktis dan keterbatasan penelitian untuk arah riset selanjutnya.

### 2.8 Ucapan Terima Kasih (*Acknowledgments*) - Opsional
- Ditujukan kepada lembaga penyandang dana hibah (sebutkan nama skema dan nomor kontrak) atau pihak pendukung data.

### 2.9 Daftar Pustaka (*References*)
- Format standar: **APA 7th Edition** (atau IEEE sesuai permintaan spesifik jurnal).
- Minimal 15 - 25 referensi, dengan minimal 80% berupa artikel jurnal ilmiah primer 5-10 tahun terakhir.
- Diurutkan alfabetis (A-Z), menggunakan format paragraf gantung (*hanging indent* 1,27 cm), spasi tunggal, dan wajib menyertakan tautan DOI aktif (`https://doi.org/...`).

---

## 3. MASTER TEMPLATE RESMI JURNAL SINTA (DOCX)

Master template resmi yang telah distandarisasi untuk seluruh penulisan jurnal SINTA tersimpan di:
`templates/template_jurnal_sinta.docx`

**Spesifikasi Master Template:**
- Format: Word (.docx), Ukuran Kertas A4.
- Margin: Normal Simetris 2,54 cm (1 inci) di seluruh sisi (Top, Bottom, Left, Right).
- Alur: Single-column continuous flow dengan blok abstrak berindentasi 0,5 cm.
- Tabel: APA 3 garis horizontal dengan header abu-abu tipis (*#F2F2F2*).
- Style: Bersih dari mojibake, tanpa kode ekonomi JEL, dan siap diisi naskah baru.
