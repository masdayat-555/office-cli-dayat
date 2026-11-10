#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linter Tata Bahasa Indonesia Akademik & EYD Edisi V
Pemeriksa deterministik ejaan baku KBBI, struktur kalimat efektif, eliminasi pleonasme, dan AI Slop ID.

Fitur:
- Deteksi kata tidak baku populer (merubah, efektifitas, analisa, praktek, sistim, standarisasi, dsb.)
- Deteksi pleonasme/kemubaziran kata (adalah merupakan, agar supaya, sangat ... sekali, demi untuk)
- Deteksi pembuka dan basa-basi robotik AI ("Di era digital yang dinamis ini", "Tidak dapat dimungkiri bahwa")
- Deteksi kalke kaku bahasa Inggris ("di mana" di tengah kalimat sambung, "yang mana", "memainkan peran penting")
- Laporan baris per baris dengan rujukan baku KBBI/EYD V.
"""

import sys
import re
import os
import json
import argparse

# 1. Katalog Kata Tidak Baku vs Bentuk Baku EYD V / KBBI
KATA_TIDAK_BAKU = {
    r"\bmerubah\b": ("mengubah", "Bentuk baku berawalan 'me-' dari kata dasar 'ubah' adalah 'mengubah'."),
    r"\brubah\b": ("ubah", "Kata dasar yang baku adalah 'ubah'."),
    r"\befektifitas\b": ("efektivitas", "Serapan akhiran '-ity' menjadi '-itas', bukan '-ifitas'."),
    r"\baktip\b": ("aktif", "Bentuk baku berakhiran '-f'."),
    r"\baktifitas\b": ("aktivitas", "Bentuk kata turunan serapan yang baku adalah 'aktivitas'."),
    r"\banalisa\b": ("analisis", "Serapan '-ysis' menjadi '-isis', bukan '-isa'."),
    r"\bpraktek\b": ("praktik", "Bentuk baku menggunakan vokal 'i'."),
    r"\bpraktisi\b": ("praktisi", "Sudah baku."),
    r"\bsistim\b": ("sistem", "Bentuk baku menggunakan vokal 'e'."),
    r"\bsistematik\b": ("sistematika / sistematis", "Gunakan 'sistematis' untuk adjektiva."),
    r"\bstandarisasi\b": ("standardisasi", "Serapan dari 'standardization' mempertahankan huruf 'd'."),
    r"\bhakekat\b": ("hakikat", "Bentuk baku menggunakan huruf 'i'."),
    r"\brespon\b": ("respons", "Bentuk baku berakhiran 's'."),
    r"\bresiko\b": ("risiko", "Bentuk baku menggunakan vokal 'i'."),
    r"\bijin\b": ("izin", "Bentuk baku menggunakan huruf 'z'."),
    r"\bobyek\b": ("objek", "Bentuk baku menggunakan huruf 'j'."),
    r"\bsubyek\b": ("subjek", "Bentuk baku menggunakan huruf 'j'."),
    r"\btehnik\b": ("teknik", "Bentuk baku tanpa huruf 'h'."),
    r"\btehnologi\b": ("teknologi", "Bentuk baku tanpa huruf 'h'."),
    r"\bjadual\b": ("jadwal", "Bentuk baku menggunakan huruf 'w'."),
    r"\bnomer\b": ("nomor", "Bentuk baku menggunakan vokal 'o'."),
    r"\bjaman\b": ("zaman", "Bentuk baku menggunakan huruf 'z'."),
    r"\bberfikir\b": ("berpikir", "Bentuk baku menggunakan huruf 'p'."),
    r"\bnegri\b": ("negeri", "Bentuk baku menggunakan vokal 'e'."),
    r"\bsilahkan\b": ("silakan", "Bentuk baku tanpa huruf 'h'."),
    r"\bantri\b": ("antre", "Bentuk baku menggunakan huruf 'e'."),
    r"\bantrian\b": ("antrean", "Bentuk baku menggunakan huruf 'e'."),
    r"\bprosentase\b": ("persentase", "Bentuk baku diawali 'per-', bukan 'pro-'."),
    r"\botentik\b": ("autentik", "Bentuk baku menggunakan diftong 'au'."),
    r"\bkomplit\b": ("lengkap", "Gunakan kata baku bahasa Indonesia 'lengkap'."),
    r"\bkarakteristik\b": ("karakteristik", "Sudah baku."),
    r"\bmetodologi\b": ("metode", "Jika merujuk pada prosedur/tahapan kerja, gunakan 'metode'. 'Metodologi' adalah ilmu tentang metode."),
}

# 2. Pleonasme / Kemubaziran Kata
PLEONASME_PATTERNS = [
    (r"\badalah merupakan\b", "Pleonasme", "Gunakan salah satu: 'adalah' atau 'merupakan'."),
    (r"\bagar supaya\b", "Pleonasme", "Gunakan salah satu: 'agar' atau 'supaya'."),
    (r"\bsangat\s+\w+\s+sekali\b", "Pleonasme", "Pilih salah satu: 'sangat [kata]' atau '[kata] sekali'."),
    (r"\bdemi untuk\b", "Pleonasme", "Gunakan salah satu: 'demi' atau 'untuk'."),
    (r"\bberbagai\s+macam\s+\w+-+\w+\b", "Pleonasme", "Bentuk jamak berulang (contoh: 'berbagai macam faktor-faktor'). Gunakan 'berbagai faktor'."),
    (r"\bbertujuan untuk\b", "Pemborosan Kata", "Cukup gunakan 'bertujuan [kata kerja]' (misal 'bertujuan menguji')."),
]

# 3. AI Slop & Basa-Basi Robotik
AI_SLOP_ID = [
    (r"\bdi era digital (?:yang )?(?:dinamis|pesat|modern)\b", "AI Slop Pembuka", "Hapus pembuka kosmik klise ini! Langsung masuk ke subjek dan masalah riil riset."),
    (r"\bseiring dengan perkembangan teknologi\b", "AI Slop Pembuka", "Hapus basa-basi pengantar! Nyatakan latar belakang empiris secara spesifik."),
    (r"\btidak dapat dipungkiri bahwa\b|\btidak dapat dimungkiri bahwa\b", "AI Slop Penegas Kosong", "Hapus frasa penegas tanpa bukti ini. Nyatakan fakta langsung dan sertakan rujukan sitasi."),
    (r"\bsudah menjadi rahasia umum bahwa\b", "AI Slop Bahasa Santai", "Gaya bahasa non-akademis. Ganti dengan rujukan literatur ilmiah."),
    (r"\bmari kita (?:bahas|lihat|tinjau)\b", "Gaya Ceramah / Percakapan", "Hindari mengajak pembaca berbicara langsung. Gunakan sudut pandang objektif orang ketiga."),
    (r"\bperlu diingat bahwa\b", "AI Slop", "Gunakan formulasi objektif, contoh: 'Keterbatasan penelitian ini terletak pada...'"),
]

# 4. Kalke Kaku Bahasa Inggris
KALKE_INGGRIS = [
    (r"\s+di mana\s+", "Kalke Inggris ('where/in which')", "'Di mana' adalah kata tanya tempat. Gunakan 'tempat', 'saat', 'ketika', 'sehingga', atau pecah kalimat."),
    (r"\s+yang mana\s+", "Kalke Inggris ('which')", "Bahasa Indonesia tidak mengenal kata sambung 'yang mana'. Gunakan 'yang' atau jadikan kalimat baru."),
    (r"\bmemainkan peran penting\b", "Kalke Inggris ('play an important role')", "Gunakan verba asli bahasa Indonesia: 'berperan penting'."),
    (r"\bmengambil tempat\b", "Kalke Inggris ('take place')", "Gunakan: 'berlangsung', 'diadakan', atau 'bertempat'."),
    (r"\bmelakukan perbandingan\b", "Nominalisasi Kalke ('make a comparison')", "Gunakan verba aktif yang lugas: 'membandingkan'."),
    (r"\bmemberikan kontribusi\b", "Nominalisasi Kalke ('make a contribution')", "Gunakan verba aktif: 'berkontribusi' atau 'menyumbang'."),
]

def lint_text(text: str):
    lines = text.splitlines()
    findings = []
    
    for line_idx, line in enumerate(lines, start=1):
        # Abaikan baris heading atau komentar markdown
        if line.strip().startswith("<!--") or line.strip().startswith("```"):
            continue

        # 1. Cek Kata Tidak Baku
        for pat, (baku, desc) in KATA_TIDAK_BAKU.items():
            matches = list(re.finditer(pat, line, re.IGNORECASE))
            for m in matches:
                # Lewati jika sudah baku (misal praktisi)
                if m.group(0).lower() == baku.lower():
                    continue
                findings.append({
                    "line": line_idx,
                    "col": m.start() + 1,
                    "category": "KATA_TIDAK_BAKU",
                    "matched": m.group(0),
                    "rule": f"Bentuk tidak baku menurut KBBI/EYD V.",
                    "suggestion": f"Ganti dengan bentuk baku: '{baku}'. {desc}",
                    "snippet": line.strip()
                })

        # 2. Cek Pleonasme
        for pat, rule_name, desc in PLEONASME_PATTERNS:
            matches = list(re.finditer(pat, line, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "line": line_idx,
                    "col": m.start() + 1,
                    "category": "PLEONASME",
                    "matched": m.group(0),
                    "rule": rule_name,
                    "suggestion": desc,
                    "snippet": line.strip()
                })

        # 3. Cek AI Slop
        for pat, rule_name, desc in AI_SLOP_ID:
            matches = list(re.finditer(pat, line, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "line": line_idx,
                    "col": m.start() + 1,
                    "category": "AI_SLOP_ID",
                    "matched": m.group(0),
                    "rule": rule_name,
                    "suggestion": desc,
                    "snippet": line.strip()
                })

        # 4. Cek Kalke Bahasa Inggris
        for pat, rule_name, desc in KALKE_INGGRIS:
            matches = list(re.finditer(pat, line, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "line": line_idx,
                    "col": m.start() + 1,
                    "category": "KALKE_INGGRIS",
                    "matched": m.group(0),
                    "rule": rule_name,
                    "suggestion": desc,
                    "snippet": line.strip()
                })

    return findings

def format_report_text(findings, total_lines):
    if not findings:
        return "[PASS] Bersih. Tidak terdeteksi kata tidak baku dalam daftar pantauan KBBI/EYD V, pleonasme, kalke, atau pola klise bahasa Indonesia."
    
    report = []
    report.append(f"=== LAPORAN LINTER TATA BAHASA INDONESIA AKADEMIK ({len(findings)} TEMUAN DARI {total_lines} BARIS) ===")
    
    categories = {}
    for f in findings:
        cat = f["category"]
        categories[cat] = categories.get(cat, 0) + 1

    report.append(f"Ringkasan Masalah: " + ", ".join([f"{k}: {v}" for k, v in categories.items()]))
    report.append("-" * 75)

    for f in findings:
        report.append(f"[Baris {f['line']}:{f['col']}] [{f['category']}] '{f['matched']}'")
        report.append(f"  Aturan    : {f['rule']}")
        report.append(f"  Saran     : {f['suggestion']}")
        report.append(f"  Kutipan   : \"{f['snippet'][:90]}\"")
        report.append("")

    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Linter Tata Bahasa Indonesia Akademik & EYD Edisi V")
    parser.add_argument("--file", "-f", help="Path file teks atau markdown yang akan diperiksa")
    parser.add_argument("--text", "-t", help="String teks langsung untuk diperiksa")
    parser.add_argument("--json", action="store_true", help="Output dalam format JSON murni")
    args = parser.parse_args()

    content = ""
    if args.file:
        if not os.path.exists(args.file):
            print(f"Error: File '{args.file}' tidak ditemukan.", file=sys.stderr)
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.text:
        content = args.text
    else:
        if not sys.stdin.isatty():
            content = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)

    findings = lint_text(content)
    total_lines = len(content.splitlines())

    if args.json:
        print(json.dumps({
            "status": "PASS" if not findings else "WARN",
            "total_findings": len(findings),
            "total_lines": total_lines,
            "findings": findings
        }, indent=2, ensure_ascii=False))
    else:
        print(format_report_text(findings, total_lines))

    if findings:
        sys.exit(2)
    sys.exit(0)

if __name__ == "__main__":
    main()

