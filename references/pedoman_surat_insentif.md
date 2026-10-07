# ?? Pedoman Komprehensif Surat Permohonan Insentif (Office-CLI & Python-Docx)

File ini adalah pedoman lengkap dan baku untuk agen saat berhadapan dengan manipulasi, perbaikan, atau pembuatan **Surat Permohonan Insentif Kejuaraan/Lomba** berbasis Microsoft Word .docx. Pedoman ini digagas dari hasil *post-mortem* ekstensif untuk menghindari kerusakan tata letak (*layout*) dan memastikan dokumen 100% siap cetak.

---

## 1. Konteks dan Struktur Anatomi Surat
Surat permohonan insentif mahasiswa memiliki struktur rigid yang saling terhubung. Jangan mengubah urutannya:
- **Halaman 1 (Isi Surat & Tanda Tangan)**: Berisi permohonan dana, rincian prestasi, dan daftar lampiran. Diakhiri dengan tanda tangan kelompok mahasiswa.
- **Halaman 2 (Lampiran 1)**: Berisi gambar/fotokopi Sertifikat Kejuaraan atau Medali.
- **Halaman Sisipan Fisik (Lampiran 2)**: Berisi lembar *Official Result* (Pengumuman Resmi). Bagian ini umumnya dicetak terpisah oleh klien, sehingga agen hanya perlu memberikan *placeholder* atau melewati penomorannya di dalam .docx.
- **Halaman 3 (Lampiran 3)**: Berisi dokumentasi kegiatan/foto saat lomba.

---

## 2. Prosedur Kerja Teknis (Golden Workflow)
Setiap agen yang ditugaskan membuat/memodifikasi surat ini **WAJIB** mengikuti alur berikut:

### 2.1 Menggunakan Golden Template
Alih-alih memformat dokumen mentah dari nol, agen **WAJIB** memulai pekerjaan dengan menyalin kerangka emas yang sudah kebal dari bug layout.
- **Lokasi Template**: C:\Users\masdayat\.gemini\config\skills\office-cli\templates\template_surat_insentif.docx
- Template ini sudah memiliki pemisahan *Section Breaks* yang sempurna dan pengaturan *Header* lampiran statis yang tidak akan tembus ke halaman lain.

### 2.2 Injeksi Data (Teks dan Tabel)
- Gunakan officecli batch untuk mengganti *placeholder* teks sederhana (seperti nama lomba, tanggal, dan prodi).
- Untuk manipulasi struktur kolom **Tanda Tangan**, WAJIB menggunakan modul python-docx. Tabel tanda tangan (doc.tables[0]) harus menggunakan tabel *Borderless* (tanpa garis tepi) agar penyelarasan Nama, NIM, dan ruang kosong tanda tangan basah presisi tanpa perlu bantuan karakter *Enter* (\n) manual.

### 2.3 Aturan Keselamatan Eksekusi (File Locking)
- Sebelum mengeksekusi skrip Python yang memodifikasi dokumen, agen WAJIB mengonfirmasi bahwa klien telah **menutup aplikasi Microsoft Word**. Jika muncul PermissionError: [Errno 13], itu berarti *file lock* sedang aktif.

---

## 3. Manajemen Lanjutan: Header & Section Breaks
Penomoran lampiran (Lampiran 1, Lampiran 3) tidak boleh ditulis di dalam *body text*, melainkan wajib berada di sudut atas kertas melalui fitur *Header* MS Word. Namun, konfigurasi *Header* Word sangat berisiko merusak seluruh halaman jika tidak diisolasi.

### Aturan Ketat Isolasi Section:
1. **Gunakan Section Breaks, Bukan Page Breaks**: Pisahkan Surat, Lampiran 1, dan Lampiran 3 menggunakan *Section Break (Next Page)*, bukan enter panjang atau pemisah halaman biasa.
2. **Putus Rantai Pewarisan (Unlink to Previous)**: Setiap memanipulasi *header* lampiran, agen wajib menjalankan pemutusan ganda:
   `python
   sec.header.is_linked_to_previous = False
   sec.first_page_header.is_linked_to_previous = False
   `
3. **Mencegah Teks Berulang (Header Carry-Over)**: Agar tulisan "Lampiran 1" hanya muncul di lembar pertama sertifikat dan tidak terbawa ("kebawa") ke lembar sertifikat kedua/ketiga, pastikan:
   - Aktifkan sec.different_first_page_header_footer = True.
   - Tulis teks "Lampiran 1" **HANYA** di dalam objek irst_page_header.
   - Kosongkan seluruh *paragraph* yang ada di dalam objek header biasa.

---

## 4. Kesadaran Visual: Jebakan Ekstraktor OCR
Saat menggunakan alat analisis Markdown (markitdown) untuk membaca isi file Word yang diberikan klien, berhati-hatilah terhadap **Ilusi Teks OCR**:
- Alat OCR mesin seringkali secara diam-diam membaca teks di dalam *gambar* (seperti tulisan "MEDALI DAN SERTIFIKAT KEJUARAAN" yang ada di dalam gambar/hasil *scan* piagam) lalu menyajikannya seolah-olah itu adalah paragraf teks asli (<w:p>) di dokumen.
- **Akibatnya**: Skrip Python yang mencoba mencari teks tersebut menggunakan if 'MEDALI' in paragraph.text: akan selalu gagal dan *error*.
- **Solusi**: Dilarang keras menjadikan teks tebal yang dicurigai sebagai gambar (sertifikat, piagam, foto brosur) sebagai penanda/jangkar struktural. Selalu gunakan elemen absolut seperti navigasi tabel (doc.tables[x]) untuk mengetahui lokasi penyisipan komponen.
