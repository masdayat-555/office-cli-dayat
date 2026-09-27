#!/usr/bin/env python3
"""
Office-CLI Skill - Periodic & Monthly GitHub Updater
Mengecek dan menarik pembaruan terbaru dari repositori GitHub secara berkala (siklus 30 hari).
"""

import sys
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
TIMESTAMP_FILE = SKILL_DIR / ".last_update_check"
UPDATE_INTERVAL_DAYS = 30


def get_last_check_date() -> datetime | None:
    if not TIMESTAMP_FILE.exists():
        return None
    try:
        content = TIMESTAMP_FILE.read_text(encoding="utf-8").strip()
        return datetime.fromisoformat(content)
    except Exception:
        return None


def save_check_date(date: datetime):
    try:
        TIMESTAMP_FILE.write_text(date.date().isoformat(), encoding="utf-8")
    except Exception as e:
        print(f"[WARN] Gagal mencatat tanggal pembaruan: {e}")


OFFICIAL_REPO_URL = "https://github.com/masdayat-555/office-cli-dayat.git"


def is_git_repo(path: Path) -> bool:
    return (path / ".git").exists()


def check_and_update(force: bool = False) -> bool:
    now = datetime.now()
    last_check = get_last_check_date()

    if not force and last_check is not None:
        elapsed = now - last_check
        if elapsed < timedelta(days=UPDATE_INTERVAL_DAYS):
            days_left = UPDATE_INTERVAL_DAYS - elapsed.days
            print(f"[INFO] Skill 'office-cli' up-to-date (pemeriksaan terakhir: {last_check.date()}, cek berikutnya dalam ~{days_left} hari).")
            return True

    print(f"[SYNC] Memeriksa pembaruan bulanan untuk skill 'office-cli' dari GitHub ({OFFICIAL_REPO_URL})...")

    if not is_git_repo(SKILL_DIR):
        print(f"[NOTICE] Direktori skill belum diinisialisasi sebagai repositori git lokal.")
        print(f"         Menghubungkan ke: {OFFICIAL_REPO_URL}")
        save_check_date(now)
        return False

    # Periksa apakah ada git remote
    remote_check = subprocess.run(
        ["git", "remote"],
        cwd=SKILL_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    if remote_check.returncode != 0 or not remote_check.stdout.strip():
        print(f"[NOTICE] Git remote belum ada. Menambahkan remote origin...")
        subprocess.run(
            ["git", "remote", "add", "origin", OFFICIAL_REPO_URL],
            cwd=SKILL_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8"
        )

    # Tarik update terbaru dengan rebase & autostash agar bebas konflik
    print("[SYNC] Menjalankan git pull --rebase --autostash origin main...")
    pull = subprocess.run(
        ["git", "pull", "--rebase", "--autostash", "origin", "main"],
        cwd=SKILL_DIR,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if pull.returncode == 0:
        output = pull.stdout.strip()
        print(f"[SUCCESS] Sinkronisasi berhasil:\n{output}")
        save_check_date(now)
        return True
    else:
        print(f"[WARN] Gagal menarik pembaruan git: {pull.stderr.strip()}")
        save_check_date(now)
        return False


if __name__ == "__main__":
    force_update = "--force" in sys.argv or "-f" in sys.argv
    check_and_update(force=force_update)
    sys.exit(0)
