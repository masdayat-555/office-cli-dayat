# MEKANISME ADAPTASI PEDOMAN KAMPUS & JURNAL (DYNAMIC OVERRIDE ENGINE)

Dokumen ini merupakan pusat routing dan mesin adaptasi dinamis bagi agen AI dalam menyesuaikan aturan penulisan dokumen ilmiah dan laporan profesional secara presisi.

---

## 1. HIERARKI PRIORITAS & PROTOKOL INQUIRY TEMPLATE PENGGUNA

Ketika memulai tugas penulisan dokumen Word, agen **WAJIB** menerapkan hierarki prioritas berikut:

### 1.1 Protokol Tanya Pengguna di Awal (Pre-Generation Inquiry)
Sebelum membuat berkas `.docx` apa pun, agen wajib mengajukan pertanyaan klarifikasi:
> *"Apakah Anda memiliki file template `.docx` resmi dari kampus/instansi atau pedoman penulisan khusus yang ingin digunakan? Jika ada, silakan lampirkan agar naskah 100% mengikuti template tersebut. Jika tidak ada, saya akan menggunakan template dan format standar nasional (general academic standard)."*

### 1.2 Hierarki Prioritas
1. **PRIORITAS 1: Template Resmi & Instruksi Eksplisit Pengguna (100% Override)**
   - Jika pengguna melampirkan template `.docx`, buku pedoman kampus, atau instruksi spesifik (misal: margin 4-3-3-3, font Arial 11 pt, spasi 2.0x, atau sitasi IEEE), **aturan pengguna MUTLAK mengesampingkan standar bawaan**. Agen wajib sepenuhnya patuh pada template tersebut.
   - Pengguna berhak menyertakan logo institusi, nama kampus/mitra, nomor induk mahasiswa (NIM), dll., yang akan langsung diintegrasikan secara lokal ke dokumen.
2. **PRIORITAS 2: Master Template Standar Nasional (Default Engine)**
   - Jika pengguna tidak memiliki template khusus, agen secara otomatis menggunakan master template bawaan skill (`templates/template_jurnal_sinta.docx`, `templates/template_laporan_tugas_akhir.docx`, atau `templates/template_laporan_kerja_praktik.docx`).

---

## 2. JAMINAN PRIVASI PENGGUNA: ZERO AI-TRAINING RETENTION

Demi melindungi integritas data pengguna dan rahasia institusi:
1. **DILARANG KERAS MENGGUNAKAN DATA PRIBADI UNTUK TRAINING MODEL AI:**
   Seluruh data pribadi pengguna (nama lengkap, NIM, NIP, nomor kontak, surel, draf naskah penelitian, file template internal kampus, dan logo institusi) **TIDAK BOLEH** digunakan sebagai bahan latihan (*training/fine-tuning dataset*) model AI.
2. **Pemrosesan Lokal & Ephemeral:**
   Data yang diberikan pengguna hanya diproses sementara dalam memori sesi aktif untuk mengompilasi berkas `.docx` milik pengguna.
3. **Pencegahan Kebocoran Git:**
   Seluruh berkas mentah kampus (`Template_*.docx`) wajib otomatis diabaikan oleh `.gitignore` agar tidak pernah terunggah ke repositori publik GitHub.

---

## 3. MATRIKS KOMPARATIF 4 ARKETIPE DOKUMEN ILMIAH & LAPORAN

Tabel ini membantu agen mengenali secara cepat perbedaan mendasar antar jenis dokumen sehingga tidak terjadi kerancuan format:

| Parameter | Artikel Jurnal SINTA | Artikel Jurnal Scopus | Laporan Tugas Akhir / Skripsi | Laporan Kerja Praktik (KP / Magang) |
| :--- | :--- | :--- | :--- | :--- |
| **Tujuan Utama** | Diseminasi riset nasional terakreditasi | Publikasi bereputasi global berdampak sitasi tinggi | Ujian kelulusan sarjana (monograf komprehensif) | Pelaporan pengalaman industri & solusi praktis |
| **Struktur Inti** | IMRaD (Pendahuluan, Metode, Hasil & Pembahasan, Kesimpulan) | Extended IMRaD (+ Related Work, Ablation, Error Analysis, Validity) | Monograf 5 Bab (Pendahuluan, Pustaka, Teori/Metode, Hasil, Penutup) | 5 Bab Praktis (Pendahuluan, Profil Mitra, Pelaksanaan, Evaluasi Mutu, Penutup) |
| **Penomoran Bab/Seksi** | Angka Arab (`1. PENDAHULUAN`). **Dilarang kata 'BAB'** | Angka Arab / Huruf Kapital. **Dilarang kata 'BAB'** | **Wajib kata 'BAB'** (`BAB 1. PENDAHULUAN` / `BAB I`) | **Wajib kata 'BAB'** (`BAB 1. PENDAHULUAN` / `BAB I`) |
| **Aliran Halaman** | **Continuous Flow** (tanpa page break antar-seksi) | **Continuous Flow** (tanpa page break antar-seksi) | **Wajib Page Break** setiap bab baru (`pageBreakBefore: true`) | **Wajib Page Break** setiap bab baru (`pageBreakBefore: true`) |
| **Aturan Abstrak** | Formula IMRaD mini (150-200 kata), **Wajib tuntas di Halaman 1** | Structured/Unstructured (200-250 kata), Full English | Intisari 3 Alinea presisi (Latar belakang, Metode, Hasil), 10 pt spasi 1.0x | Ringkasan Eksekutif (1-2 alinea ringkas profil mitra & kontribusi penugasan) |
| **Pengesahan** | Tidak ada lembar pengesahan (cukup *Byline & Affiliations*) | Tidak ada lembar pengesahan (*Byline, Affiliations, ORCID iD*) | Pembimbing I/II, Penguji, Kaprodi, Dekan Fakultas | Pembimbing Kampus **DAN Pembimbing Lapangan Industri** |
| **Lampiran Kunci** | Biasanya tidak ada lampiran (semua terintegrasi di naskah) | *Supplementary Materials* (repositori online / OSF / GitHub) | Bukti pengujian empiris, instrumen, data mentah | **Surat selesai magang, lembar nilai industri, logbook mingguan** |
| **Panduan Detail** | [pedoman_jurnal_sinta.md](pedoman_jurnal_sinta.md) | [pedoman_jurnal_scopus.md](pedoman_jurnal_scopus.md) | [pedoman_skripsi_lengkap.md](pedoman_skripsi_lengkap.md) | [pedoman_kerja_praktik.md](pedoman_kerja_praktik.md) |

---

## 4. DAFTAR PARAMETER MODULAR YANG DAPAT DI-OVERRIDE

| Parameter | Nilai Baku Bawaan (Skripsi/Laporan) | Variasi Pedoman Kampus Lain | Implementasi di `officecli` |
| :--- | :--- | :--- | :--- |
| **Margin** | 4-4-3-3 cm (Umum) atau 4-3-3-3 cm (Teknik) | 3-3-3-3 cm atau 1,5-1-1-1 inci | Set atribut `marginTop`, `marginLeft`, `marginBottom`, `marginRight` |
| **Jenis Font** | *Times New Roman* | *Arial*, *Calibri*, *Georgia*, *Book Antiqua* | Set properti `font` pada `/styles/Normal` dan Headings |
| **Ukuran Font Isi** | 12 pt (Regular) | 11 pt (biasa pada font Arial/Calibri) | Set properti `size` pada `/styles/Normal` |
| **Spasi Teks Utama** | 1,25x atau 1,5x | 2,0x atau 1,15x | Set atribut `lineSpacing` pada paragraf body |
| **Format Sitasi** | APA Style 7th Edition (Nama, Tahun) | IEEE Style `[1]`, Harvard, Vancouver | Sesuaikan kurung sitasi di teks & format Daftar Pustaka |
| **Garis Tabel** | 3 garis horizontal standar APA (tanpa garis vertikal) | Tabel bergaris kotak penuh (*Full Grid*) jika diminta | Atur properti `borderTop`, `borderBottom`, `borderInsideH/V` |

---

## 5. TRANSFORMASI ADAPTIF ELEMEN SEMANTIK (ANTI-RAW COPY)

1. **Deteksi Tabel Semantik:**
   - Draf masukan: Tabel Markdown (`| col1 | col2 |`), tabel ASCII (`+---+---+`), atau teks data berkolom.
   - Perilaku: Wajib diubah menjadi **Native Word Table (`w:tbl`)** berstandar APA 3 garis horizontal. Dilarang menyalinnya sebagai blok teks monospace.
2. **Deteksi Struktur Pohon / Hierarki (Tree):**
   - Draf masukan: ASCII tree direktori (`├── folder/`, `└── file.py`), hierarki modul, atau struktur organisasi.
   - Perilaku: Wajib diubah menjadi **Nested Indented Bullet List** resmi Word atau **Tabel Hierarkis Bertingkat**. Dilarang menyalin simbol ASCII `├──` secara mentah.

---

## 6. PROTOKOL WAJIB: DRAF PROPOSAL MARKDOWN SEBELUM EKSEKUSI DOCX

1. **Peka Konteks Proyek Lokal:**
   Baca berkas penting di workspace pengguna (`README.md`, `doc.md`, `PLAN.md`) untuk menyerap nama arsitektur, parameter riset, dan tujuan proyek.
2. **Verifikasi Persetujuan Pengguna:**
   Sajikan rancangan draf struktur naskah (Judul, Outline Bab, Poin Utama Narasi, Rancangan Tabel/Gambar) dalam format Markdown.
3. **Persetujuan Pengguna:**
   Hanya setelah pengguna memberikan persetujuan (*"Lanjut"*, *"Oke"*), barulah berkas Word `.docx` dikompilasi secara penuh menggunakan `officecli`.
