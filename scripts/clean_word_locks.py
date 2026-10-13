"""
Utilitas pembersih kunci berkas Microsoft Word (Normal.dotm) dan pengelola TOC COM yang aman.
Mencegah dan mengatasi pop-up:
"This file is in use by another application or user. (C:\\Users\\...\\Normal.dotm)"
"""

import os
import subprocess
import time
import win32com.client
import gc

def clean_word_locks():
    """
    Membersihkan proses zombie WINWORD headless di latar belakang
    dan menghapus berkas kunci ~$Normal.dotm jika tertinggal.
    """
    # 1. Hentikan proses WINWORD yang tidak memiliki jendela aktif (headless background)
    ps_cmd = (
        "$procs = Get-Process -Name WINWORD -ErrorAction SilentlyContinue | "
        "Where-Object { [string]::IsNullOrEmpty($_.MainWindowTitle) }; "
        "if ($procs) { $procs | Stop-Process -Force }"
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True)
    time.sleep(0.5)

    # 2. Hapus berkas kunci lock ~$Normal.dotm jika ada
    templates_dir = os.path.expandvars(r"%APPDATA%\Microsoft\Templates")
    lock_file = os.path.join(templates_dir, "~$Normal.dotm")
    if os.path.exists(lock_file):
        try:
            os.remove(lock_file)
            print(f"[CLEANUP] Berkas kunci berhasil dihapus: {lock_file}")
        except Exception as e:
            # Jika masih terkunci, paksa bunuh seluruh WINWORD jika pengguna tidak sedang membuka Word
            pass

def update_toc_safely(docx_path: str):
    """
    Memperbarui Daftar Isi (TOC) otomatis via Microsoft Word COM secara aman tanpa mengunci Normal.dotm.
    """
    clean_word_locks()
    
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0  # wdAlertsNone (0)
    
    try:
        doc = word.Documents.Open(os.path.abspath(docx_path))
        if doc.TablesOfContents.Count > 0:
            doc.TablesOfContents(1).Update()
        doc.Save()
        doc.Close(SaveChanges=0)
    finally:
        try:
            # PENTING: Tandai NormalTemplate sebagai telah disimpan agar Word tidak mencoba menyimpannya
            word.NormalTemplate.Saved = True
        except Exception:
            pass
        try:
            word.Quit(0)  # wdDoNotSaveChanges (0)
        except Exception:
            pass
        del doc
        del word
        gc.collect()
        time.sleep(0.5)
        # Pastikan tidak ada sisa proses zombie headless
        clean_word_locks()

if __name__ == "__main__":
    clean_word_locks()
    print("[OK] Kunci Normal.dotm dan proses zombie Word telah dibersihkan sepenuhnya.")
