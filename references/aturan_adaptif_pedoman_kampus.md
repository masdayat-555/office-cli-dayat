# MEKANISME ADAPTASI PEDOMAN KAMPUS & JURNAL (DYNAMIC OVERRIDE ENGINE)

Dokumen ini memandu agen AI dalam mengadaptasi aturan penulisan secara fleksibel berdasarkan instruksi pengguna, buku pedoman skripsi perguruan tinggi tertentu, atau *Author Guidelines* jurnal yang dituju.

---

## 1. HIERARKI PRIORITAS ATURAN PENULISAN

Ketika memformat atau menyusun dokumen ilmiah, agen AI **WAJIB** menerapkan hierarki prioritas berikut (aturan di nomor lebih kecil mengalahkan aturan di nomor lebih besar):

1. **PRIORITAS 1: Instruksi Eksplisit Pengguna & Template Resmi Kampus / Jurnal**
   - Jika pengguna memberikan *template* `.docx`, buku pedoman skripsi kampus (PDF/Docx), atau koreksi spesifik (contoh: *"Di kampusku marginnya 4-3-3-3 dan font-nya Arial"* atau *"Gunakan spasi 2.0 dan format sitasi IEEE"*), **aturan ini 100% MUTLAK mengesampingkan aturan standar default!**
2. **PRIORITAS 2: Standar Baku Nasional / Internasional (Default Engine)**
   - Jika pengguna TIDAK memberikan pedoman kampus khusus, agen secara otomatis menerapkan **Standar Baku Pendidikan Tinggi Indonesia** (Kertas A4, Margin 4-4-3-3, Font Times New Roman 12, Spasi 1,5, Indent 1,27 cm, Tabel APA 3 garis, Sitasi APA 7th).
   - Untuk artikel jurnal: Menerapkan struktur internasional **IMRaD** dan template dua kolom atau satu kolom sesuai target SINTA.

---

## 2. DAFTAR PARAMETER YANG DAPAT DI-OVERRIDE

Agen AI harus mampu menyesuaikan variabel-variabel berikut secara modular:

| Parameter | Nilai Baku Default (Skripsi) | Variasi Umum Kampus Lain | Cara Penyesuaian di `officecli` |
| :--- | :--- | :--- | :--- |
| **Batas Tepi (Margin)** | Kiri: 4cm, Atas: 4cm, Bawah: 3cm, Kanan: 3cm (4-4-3-3) | 4-3-3-3 cm, 3-3-3-3 cm, atau 1,5-1-1-1 inci | Mengubah nilai `marginTop`, `marginLeft`, dll. pada `/section[1]` |
| **Jenis Huruf (Font)** | *Times New Roman* | *Arial*, *Calibri*, *Georgia*, *Book Antiqua* | Mengubah atribut `font` pada `/styles/Normal` dan `/styles/HeadingX` |
| **Ukuran Font Isi** | 12 pt | 11 pt (biasa pada Arial/Calibri) | Mengubah atribut `size` pada `/styles/Normal` |
| **Spasi Teks Utama** | 1,5 spasi (`lineSpacing="1.5x"`) | 2,0 spasi (`lineSpacing="2.0x"`) atau 1,15 spasi | Mengubah atribut `lineSpacing` pada `/styles/Normal` |
| **Struktur Bab** | Bab I s.d. Bab V (Format Skripsi Monograf) | Format Makalah Kompilasi / Format Jurnal IMRaD | Menyesuaikan daftar Heading 1 dan nomor bab |
| **Format Sitasi** | APA Style 7th Edition (Nama, Tahun) | IEEE Style `[1]`, Harvard, Vancouver | Menyesuaikan struktur kurung sitasi di teks dan urutan alfabetis vs numerik di Daftar Pustaka |
| **Posisi Judul Tabel** | Di ATAS tabel, rata tengah/kiri | Ada kampus yang meminta cetak tebal huruf kapital | Menyesuaikan paragraf sebelum elemen `table` |
| **Posisi Judul Gambar** | Di BAWAH gambar, rata tengah | Di bawah gambar, cetak miring | Menyesuaikan paragraf setelah elemen `picture` |

---

## 3. PROTOKOL KOREKSI & CONTINUOUS IMPROVEMENT

Jika pengguna menyampaikan koreksi atau pedoman baru:
1. **Catat Perubahan:** Identifikasi parameter mana yang dikoreksi (misal margin, font, format daftar isi).
2. **Revisi Langsung:** Terapkan koreksi tersebut pada dokumen yang sedang dikerjakan tanpa berdebat.
3. **Konfirmasi Cakupan:** Pastikan apakah perubahan ini berlaku untuk dokumen saat ini saja atau untuk seluruh draf masa depan di proyek ini.
4. **Perbarui Memori:** Jika perubahan ini adalah aturan institusional permanen bagi pengguna, catat aturan tersebut ke dalam dokumentasi proyek agar agen di sesi berikutnya tidak mengulangi kesalahan format yang sama.

---

## 4. TRANSFORMASI ADAPTIF ELEMEN SEMANTIK (ANTI-RAW COPY)

Agen AI tidak boleh hanya bertindak sebagai "tukang salin teks mentah", melainkan harus mampu mengenali maksud semantik dari draf Markdown:

1. **Deteksi Tabel Semantik:**
   - Bentuk masukan: tabel pipa markdown, tabel garis putus-putus ASCII (`+---+`, `--|--`), atau teks berkolom dengan field & record terstruktur.
   - Perilaku adaptif: Wajib diubah menjadi **tabel native Word berformat APA** (3 garis horizontal: atas, pemisah header, dan penutup bawah). Dilarang menyalinnya sebagai blok teks monospace.
2. **Deteksi Struktur Pohon / Hierarki (Tree):**
   - Bentuk masukan: ASCII tree folder (`├── src/`, `└── main.py`), pohon keputusan, atau taksonomi hierarkis.
   - Perilaku adaptif: Wajib diubah menjadi **daftar butir bertingkat (nested indented bullet list)** formal Word atau **tabel hierarki multi-level**, bukan teks karakter ASCII `├──` mentah di paragraf ilmiah.

---

## 5. PROTOKOL WAJIB: DRAF PROPOSAL MARKDOWN SEBELUM EKSEKUSI DOCX

1. **Peka Terhadap File Markdown Proyek:**
   Sebelum menyusun dokumen, agen wajib membaca berkas `.md` kunci di repositori pengguna (`README.md`, `doc.md`, `PLAN.md`, draf naskah). Serap nama sistem, arsitektur, dan tujuan agar isi naskah akurat.
2. **Verifikasi Persetujuan Pengguna:**
   Susun draf rencana struktur naskah dalam format Markdown terlebih dahulu. Paparkan usulan judul, kerangka bab, dan poin inti ke pengguna untuk disetujui. Setelah pengguna memberikan persetujuan (*"Oke"*, *"Setuju"*), barulah file `.docx` resmi dibuat.

