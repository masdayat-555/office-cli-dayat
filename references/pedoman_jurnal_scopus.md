# PEDOMAN PENULISAN & STANDAR ARTIKEL JURNAL INTERNASIONAL BEREPUTASI (SCOPUS Q1-Q4)

Dokumen ini merupakan panduan komprehensif bagi agen AI dan peneliti dalam mempersiapkan, menulis, dan memformat artikel ilmiah berstandar internasional yang ditargetkan untuk jurnal terindeks **Scopus** (Elsevier) dan **Web of Science (WoS / Clarivate Analytics)**.

---

## 1. MENGENAL EKOSISTEM SCOPUS & SISTEM KUARIL (Q1-Q4)

Scopus adalah basis data rujukan ilmiah terkurasi terbesar di dunia yang dikelola oleh Elsevier. Jurnal yang terindeks Scopus diklasifikasikan ke dalam empat kuartil (*Quartiles*) berdasarkan metrik pengaruh saintifik seperti **SJR (*SCImago Journal Rank*)** dan **CiteScore**:

| Kuartil | Persentil Pengaruh | Karakteristik & Tingkat Keketatan Seleksi |
| :--- | :--- | :--- |
| **Q1** | Top 25% (75 - 99%) | Jurnal teratas di bidangnya (contoh: IEEE TPAMI, Nature, Elsevier Applied Soft Computing). *Desk reject* 70-80%, *acceptance rate* < 15-20%, *peer-review* sangat mendalam dan kritis. Menuntut kebaruan teoretis atau terobosan metodologis fundamental. |
| **Q2** | 50% - 74% | Jurnal bereputasi tinggi dengan dampak sitasi konsisten. Menuntut eksperimen empiris berskala besar, pembanding SOTA (*State of the Art*) yang adil, dan analisis galat mendalam. |
| **Q3** | 25% - 49% | Jurnal internasional terindeks bereputasi menengah. Cocok untuk penerapan metodologi mutakhir pada korpus/studi kasus regional atau optimasi arsitektur spesifik. |
| **Q4** | Bawah 25% (0 - 24%) | Peringkat kuartil awal pada Scopus. Standar format internasional tetap wajib dipatuhi secara ketat. |

---

## 2. PERSYARATAN UTAMA NASKAH STANDAR SCOPUS

### 2.1 Bahasa & Kualitas Penulisan
- **100% Bahasa Inggris Akademik (*Academic English*):** Menggunakan bahasa Inggris formal, baku, dan konsisten (pilih salah satu: *American English* atau *British English*, dilarang mencampuradukkan ejaan).
- Disarankan melewati pemeriksaan keterbacaan (*readability*) dan *professional proofreading* untuk menghindari penolakan karena alasan linguistik (*poor linguistic quality*).

### 2.2 Struktur Naskah Lengkap (Extended IMRaD)
Sebagian besar penerbit besar (Elsevier, Springer Nature, IEEE, Wiley, MDPI) menerapkan struktur IMRaD yang diperluas:
1. **Title:** 10 - 14 kata, padat, lugas, tidak bertele-tele, menonjolkan metode dan dampak utama.
2. **Authors & Affiliations:** Nama lengkap tanpa gelar, afiliasi lengkap dengan nama negara dan kode pos, email institusional, serta **tautan wajib ORCID iD** untuk setiap penulis (`https://orcid.org/0000-000...`).
3. **Structured / Unstructured Abstract:** 200 - 250 kata, memuat konteks masalah, metodologi, pembuktian kuantitatif dengan metrik statistik, dan signifikansi dampak.
4. **Keywords:** 4 - 6 istilah teknis baku terindeks (contoh: IEEE Thesaurus, ACM Computing Classification System, atau MeSH).
5. **Section 1: Introduction:** Latar belakang, *State-of-the-Art* komprehensif (minimal 15-20 sitasi terkini), formulasi celah riset (*Research Gap*), rumusan pertanyaan penelitian (*Research Questions*), dan 3-4 butir kontribusi utama (*Key Contributions*).
6. **Section 2: Related Work:** Mengulas penelitian terdahulu yang relevan secara kritis, menyajikan tabel perbandingan fitur/metode riset terdahulu vs penelitian saat ini.
7. **Section 3: Proposed Methodology:**
   - Formalisasi matematis yang ketat untuk setiap persamaan.
   - Diagram arsitektur sistem resolusi tinggi (vektor SVG atau minimal 300-600 DPI).
   - Kotak Algoritma / Pseudocode (menggunakan notasi standar IEEE/ACM).
   - Rincian replikabilitas: spesifikasi hardware (tipe GPU, CPU, RAM), versi pustaka/framework, hyperparameter lengkap, dan prosedur validasi.
8. **Section 4: Experiments and Results:**
   - Deskripsi dataset, partisi data (Train/Validation/Test split), dan metrik evaluasi.
   - Perbandingan *apples-to-apples* terhadap beberapa model *baseline* dan SOTA.
   - Pengujian signifikansi statistik (misal: *p-value* < 0.05 via paired t-test / Wilcoxon signed-rank test).
   - Studi Ablasi (*Ablation Study*): membuktikan dampak masing-masing komponen atau modul yang diusulkan.
9. **Section 5: Discussion:**
   - Menjelaskan wawasan ilmiah di balik keberhasilan metode (*why it works*).
   - Analisis Galat (*Error Analysis & Failure Cases*): jujur memaparkan kasus ketika model gagal memprediksi.
   - Ancaman Validitas (*Threats to Validity*): membagi batasan ke dalam validitas internal, eksternal, dan konstruksi.
10. **Section 6: Conclusion and Future Work:** Sintesis temuan dan peta jalan penelitian lanjutan.
11. **Pernyataan Wajib (*Mandatory Statements*):**
    - *Data Availability Statement* (di mana data dapat diakses, misal: Zenodo, Figshare, GitHub).
    - *Code Availability Statement* (tautan repositori kode yang dapat direplikasi).
    - *Conflict of Interest Declaration*.
    - *Author Contributions Statement* (menggunakan taksonomi CRediT: *Conceptualization, Methodology, Software, Validation, Writing - Original Draft*, dll.).
12. **References:** Minimal 30 - 50 referensi, 85%+ berasal dari jurnal Scopus/WoS 3-5 tahun terakhir, dilengkapi nomor DOI aktif.

---

## 3. PANDUAN PENYIAPAN TATA LETAK & DOKUMEN WORD / LATEX

Penerbit jurnal Scopus umumnya menyediakan template resmi dalam dua varian:
1. **Microsoft Word (.docx):**
   - Format 2 kolom (*Two-Column Layout*): Umum pada IEEE Transactions/Conferences, Elsevier procedia, Springer LNCS.
   - Format 1 kolom (*Single-Column Layout*): Umum pada jurnal Elsevier standar, MDPI, Emerald, Sage.
   - Tipografi: Times New Roman atau Arial 10 pt untuk teks utama, 8-9 pt untuk tabel dan keterangan gambar.
   - Tabel APA murni tanpa garis vertikal.
2. **LaTeX (Overleaf):**
   - Sangat disukai di rumpun Ilmu Komputer / Artificial Intelligence. Menggunakan template resmi seperti `IEEEtran.cls`, `elsarticle.cls`, atau `springer-nature.cls`.

---

## 4. JEMBATAN DARI SINTA KE SCOPUS (UPGRADING PATHWAY)

Jika sebuah naskah yang awalnya dirancang untuk jurnal SINTA (misal SINTA 2) ingin ditingkatkan untuk menembus jurnal Scopus (Q2/Q3):
1. **Terjemahan & Polishing:** Alihkan naskah ke Bahasa Inggris akademik penuh dengan alur kohesif.
2. **Perluasan Literatur:** Tambahkan 15-20 referensi jurnal internasional Scopus terkini pada bagian Pendahuluan dan Pembahasan.
3. **Tambahkan Studi Ablasi (*Ablation Study*):** Buktikan secara matematis kontribusi setiap modul (misalnya: buktikan performa model dengan vs tanpa *Emotional Seeding*, dengan vs tanpa *Domain Adaptation*).
4. **Sertakan Data & Code Repositori:** Unggah draf dataset teranotasi dan kode inferensi ke repositori terbuka dengan lisensi open-source (MIT/Apache 2.0).
5. **Tambahkan Pernyataan Etika & CRediT:** Lengkapi naskah dengan *Data Availability* dan pembagian peran penulis formal.



## 5. MANAJEMEN REFERENSI TERVALIDASI (FULL AUTO MENDELEY)

> [!IMPORTANT]
> **TEMPORAL AWARENESS (KESADARAN WAKTU):** Penulis dan Agen AI **WAJIB** menyadari bahwa tahun saat ini adalah **2026** setiap kali mem-filter atau mencari referensi.
>
> **Yang Agen AI lakukan secara Otomatis (Full Auto):**
> 1. Membaca PDF via `markitdown` dan memverifikasi metadata.
> 2. Mengunggah metadata & file fisik PDF langsung ke akun Mendeley klien via API.
> 3. Membuat file cadangan `references.bib` di komputer lokal.
> 4. Menyisipkan *placeholder* sitasi di draf naskah Word.
>
> **Yang Pengguna lakukan secara Manual (Semi-Auto):**
> Membuka Word, mencari teks *placeholder* di naskah, lalu mengeklik "Insert Citation" dari panel Mendeley Cite.

### 5.1 Folder `REFERENSI/` — Repositori PDF Sitasi

Setiap proyek penulisan **WAJIB** memiliki satu folder `REFERENSI/` di root workspace proyek.
**Konvensi Penamaan File PDF (wajib dipatuhi):**
`[NamaBelakangPenulisPertama]_[Tahun]_[KataKunciJudul].pdf`

### 5.2 Alur Otomatisasi (PDF → Mendeley)

1. **Ekstrak Teks:** Agen membaca isi PDF menggunakan `markitdown`.
2. **Koreksi Data:** Agen mengoreksi 7 field wajib (Judul, Penulis, Tahun, Venue, Vol/Issue, Halaman, DOI).
3. **Upload via API:** Agen menggunakan skrip internal (`mendeley_upload.py`) untuk mem-POST metadata dan PDF langsung ke Mendeley.

### 5.3 Konvensi Penulisan Sitasi Sementara (Placeholder)

**Format Penanda Wajib:**
`[CITE: NamaBelakang Tahun, 3-Kata-Pertama-Judul]`

Pengguna tinggal menyalin `Koto 2021, IndoBERTweet` ke kolom pencarian Mendeley Cite di Word.

### 5.4 Checklist Final Daftar Pustaka

Gunakan checklist ini sebelum naskah dikirim:

| # | Syarat | Detail |
| :--: | :--- | :--- |
| 1 | ✅ **85% Literatur Mutakhir (Krusial)** | **Minimal 85% referensi WAJIB dari 5 tahun terakhir (Tahun terbit ≥ 2021, karena saat ini adalah 2026).** |
| 2 | ✅ Semua sitasi punya PDF | Ada di folder `REFERENSI/` dan terunggah ke Mendeley. |
| 3 | ✅ Kualitas Referensi | Wajib bersumber dari jurnal internasional bereputasi (Scopus/WoS), bukan web sembarangan. |
| 4 | ✅ Format Sitasi | Sesuai pedoman Author Guidelines jurnal tujuan (Bisa APA 7th, IEEE, atau Elsevier Harvard). |
| 5 | ✅ DOI aktif & dapat diklik | Wajib format `https://doi.org/xxx`. |
| 6 | ✅ Minimal 30-50 referensi | Jurnal Scopus menuntut tinjauan literatur yang ekstensif dan komprehensif. |

---

### 5.5 Tabel Masalah Umum Mendeley

| Masalah | Solusi |
| :--- | :--- |
| Plugin Mendeley Cite tidak muncul di Word | Di Word, klik Insert > Get Add-ins > Cari "Mendeley Cite". |
| Sitasi baru tidak muncul di panel Word | Klik "Update From Library" di opsi Mendeley Cite. |
| Agen gagal upload | Script agen sudah mendukung *Auto-Refresh*, jika gagal periksa koneksi internet. |

---

### 🚀 Opsi "Bulldozer Mode" (Mass-Download Otomatis)

Jika Anda memiliki daftar referensi yang panjang dan ingin mencari ketersediaannya secara massal tanpa mengunduh manual satu per satu, Anda bisa memerintahkan agen: **"Aktifkan Bulldozer Mode"**.
Dalam mode ini, agen AI akan:
1. Mengerahkan segala cara (API OpenAlex, CrossRef, dll) untuk menemukan dan mengunduh PDF Open-Access.
2. Memasukkan referensi tersebut secara otomatis ke Mendeley.
3. **Integritas Akademik:** Jika PDF terkunci *paywall* atau tidak ditemukan, agen akan **Jujur Melapor Gagal** dan tidak akan memasukkannya ke Mendeley. Mengutip dokumen tanpa pernah membaca fisiknya adalah pelanggaran akademik.

### 🕵️‍♂️ Otoritas "Visual Browser Agent" (Bypass Blokir API)

Jika *Bulldozer Mode* gagal menembus keamanan repositori (*bot detection* / blokir API) namun Anda yakin PDF tersebut gratis di internet, agen memiliki **otoritas** untuk membangkitkan sub-agen visual. Sub-agen ini akan mengendalikan browser Google Chrome asli Anda untuk mencari dan "menyelamatkan" link PDF rahasia tersebut layaknya penelusuran manusia, lalu menyuntikkannya ke Mendeley Anda secara legal. Perintahkan saja: **"Gunakan browser agent untuk cari PDF ini."**
