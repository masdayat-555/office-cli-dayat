# PEDOMAN PENULISAN LAPORAN PRAKTIKUM

Pedoman ini **wajib ditaati secara mutlak** oleh Agen AI saat menyusun, merevisi, atau memformat dokumen Laporan Praktikum. Laporan Praktikum memiliki tingkat keformalan (formality) yang kaku dan berbeda dari tugas harian biasa.

## 1. ATURAN HALAMAN SAMPUL (COVER)
- **Posisi Judul**: Judul utama ("LAPORAN PRAKTIKUM I", dst.) WAJIB berada di baris paling atas tanpa paragraf kosong sebelumnya.
- **Gambar Logo**: Harus berada di tengah halaman. Lebar standar sekitar 5.5 cm.
- **Blok Identitas Bawah**: ("FAKULTAS TEKNIK", "UNIVERSITAS JANABADRA", "2026") WAJIB mentok sampai mencium batas margin bawah (bottom margin flush).
- **Metode Spacing Cover**: Dilarang keras menggunakan point spacing raksasa (`space_before=150pt`). **Wajib menggunakan Enter/Paragraf kosong biasa** untuk mendorong blok bawah hingga mentok, atau meredistribusi ruang agar luwes.

## 2. ATURAN DAFTAR ISI (TOC)
- **Haram Mengetik Manual**: Dilarang menyusun teks "Daftar Isi" secara manual dengan ketikan titik-titik dan tebakan nomor halaman.
- **Wajib Native Word**: Harus diinjeksi menggunakan `officecli batch` dengan perintah `{"type": "toc"}`.
- **Siklus Wajib**: Modifikasi TOC via `officecli` harus mengikuti siklus: `batch` -> **`save`** -> `refresh` -> `close`. Tanpa `save`, Daftar Isi akan lenyap/rusak saat direfresh.

## 3. ATURAN STRUKTUR BAB & PAGE BREAK
- **Pemisahan Halaman**: Setiap pergantian BAB (misal dari BAB I ke BAB II) **WAJIB** berada di halaman baru.
- **Metode Break**: Gunakan perintah *Page Break* (`Ctrl+Enter` atau `WD_BREAK.PAGE` langsung di `runs[-1]`) atau pastikan heading BAB diset dengan properti *Page break before*. Jangan biarkan BAB menyangkut di tengah atau akhir halaman sebelumnya.

## 4. ATURAN SUMBER KONTEN (ANTI-YAPPING)
- **Dasar Teori Mengikat**: Jangan menggunakan narasi *AI slop* (penjelasan generik AI). Dasar Teori **mutlak harus diekstrak dan diparafrase langsung dari modul/dokumen referensi resmi** (misalnya PDF modul dari dosen).
- **Visualisasi Gambar**: Jika ada gambar tugas, cukup letakkan gambar dan berikan *caption* miring di bawahnya. Jangan buat tabel narasi panjang berulang jika instruksi tidak meminta.

## 5. PENDEKATAN TEKNIS GENERASI
Alih-alih menyusun dari nol menggunakan `python-docx` yang rawan cacat margin, **AGEN SANGAT DISARANKAN** untuk menyalin dari Master Template:
`templates/template_laporan_praktikum.docx`
lalu memutasinya menggunakan `officecli batch` (mengganti judul bab, menyisipkan paragraf teks, memasukkan gambar) untuk menjaga integritas format margin dan properti *Page Break*.

---

### 🚀 Opsi "Bulldozer Mode" (Mass-Download Otomatis)

Jika Anda memiliki daftar referensi yang panjang dan ingin mencari ketersediaannya secara massal tanpa mengunduh manual satu per satu, Anda bisa memerintahkan agen: **"Aktifkan Bulldozer Mode"**.
Dalam mode ini, agen AI akan:
1. Mengerahkan segala cara (API OpenAlex, CrossRef, dll) untuk menemukan dan mengunduh PDF Open-Access.
2. Memasukkan referensi tersebut secara otomatis ke Mendeley.
3. **Integritas Akademik:** Jika PDF terkunci *paywall* atau tidak ditemukan, agen akan **Jujur Melapor Gagal** dan tidak akan memasukkannya ke Mendeley. Mengutip dokumen tanpa pernah membaca fisiknya adalah pelanggaran akademik.

### 🕵️‍♂️ Otoritas "Visual Browser Agent" (Bypass Blokir API)

Jika *Bulldozer Mode* gagal menembus keamanan repositori (*bot detection* / blokir API) namun Anda yakin PDF tersebut gratis di internet, agen memiliki **otoritas** untuk membangkitkan sub-agen visual. Sub-agen ini akan mengendalikan browser Google Chrome asli Anda untuk mencari dan "menyelamatkan" link PDF rahasia tersebut layaknya penelusuran manusia, lalu menyuntikkannya ke Mendeley Anda secara legal. Perintahkan saja: **"Gunakan browser agent untuk cari PDF ini."**
