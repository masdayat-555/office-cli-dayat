#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linter Akademis Bahasa Inggris (Scopus / WoS / IEEE)
Pemeriksa deterministik kepatuhan standar bahasa Inggris ilmiah dan eliminasi kata klise AI.

Fitur:
- Deteksi kata dan frasa klise AI (AI vocabulary blacklist: delve, pivotal, tapestry, realm, dsb.)
- Deteksi pronomina personal (I, We, Our) dalam naskah yang mewajibkan third-person passive.
- Deteksi format angka dan desimal (koma sebagai desimal, spasi sebelum satuan unit SI, minus vs hyphen).
- Laporan baris per baris dengan kode kesalahan dan rekomendasi perbaikan.
"""

import sys
import re
import os
import json
import argparse

# 1. Katalog Kata Klise AI Terlarang & Saran Pengganti Baku
AI_BUZZWORDS = {
    r"\bdelve\b|\bdelves\b|\bdelving\b|\bdelved\b": (
        "Delve (Klise AI Terbesar)",
        "Gunakan: 'examine', 'investigate', 'analyze', 'explore'"
    ),
    r"\bpivotal\b": (
        "Pivotal (Klise AI Hiperbolis)",
        "Gunakan: 'critical', 'crucial', 'essential', 'significant'"
    ),
    r"\btapestry\b": (
        "Tapestry (Metafora puitis non-ilmiah)",
        "Gunakan: 'framework', 'spectrum', 'diversity', 'network'"
    ),
    r"\brealm\b": (
        "Realm (Gaya bahasa sastra)",
        "Gunakan: 'domain', 'field', 'area', 'context'"
    ),
    r"\bleverage\b|\bleverages\b|\bleveraging\b|\bleveraged\b": (
        "Leverage (Jargon bisnis korporat)",
        "Gunakan: 'utilize', 'apply', 'employ', 'exploit', 'adopt'"
    ),
    r"\bmultifaceted\b": (
        "Multifaceted (Diksi dramatis AI)",
        "Gunakan: 'complex', 'comprehensive', 'multi-component'"
    ),
    r"\btestament\b": (
        "Testament ('a testament to...')",
        "Gunakan: 'evidence of', 'indication of', 'demonstrates'"
    ),
    r"\bfoster\b|\bfosters\b|\bfostering\b|\bfostered\b": (
        "Foster (Metafora persuasif)",
        "Gunakan: 'promote', 'facilitate', 'enable', 'improve'"
    ),
    r"\bseamless\b|\bseamlessly\b": (
        "Seamless (Gaya bahasa promosi produk)",
        "Gunakan: 'integrated', 'continuous', 'automated'"
    ),
    r"\bcutting-edge\b|\bstate-of-the-art\b": (
        "Cutting-edge / State-of-the-art (Klaim berlebihan jika tanpa bukti)",
        "Gunakan: 'modern', 'advanced', 'recent' atau sebutkan spesifikasi teknisnya"
    ),
    r"\bgame-changer\b|\bparadigm shift\b": (
        "Game-changer / Paradigm shift (Slogan pemasaran)",
        "Gunakan: 'substantial advancement', 'notable improvement'"
    ),
    r"\bbeacon\b": (
        "Beacon (Bahasa puitis)",
        "Gunakan: 'benchmark', 'model', 'reference'"
    ),
    r"\bunderscore\b|\bunderscores\b|\bunderscoring\b": (
        "Underscore (Penegas mekanis AI berulang)",
        "Gunakan: 'highlight', 'emphasize', 'demonstrate', 'indicate'"
    ),
    r"\bin the .* landscape\b": (
        "Landscape ('in the technological landscape')",
        "Gunakan: 'in the field of...', 'in current applications'"
    ),
}

# 2. Pronomina Personal (Jika jurnal mewajibkan gaya impersonal)
PERSONAL_PRONOUNS = {
    r"\bwe\b": "Pronomina personal 'we' (Gunakan pasif orang ketiga atau 'This study...')",
    r"\bour\b": "Pronomina kepemilikan 'our' (Gunakan 'the proposed...', 'this...')",
    r"\bi\b": "Pronomina personal 'I' (Dilarang keras dalam naskah ilmiah)",
    r"\bmy\b": "Pronomina kepemilikan 'my' (Dilarang)",
    r"\bus\b": "Pronomina personal 'us'",
    r"\byou\b|\byour\b": "Pronomina orang kedua 'you/your' (Dilarang bernada mengajak bicara)",
}

# 3. Masalah Tipografi & Angka
TYPO_PATTERNS = [
    (r"\b\d+,\d+\s*%", "Koma desimal pada persentase (Gunakan titik desimal, misal '96.8%')"),
    (r"\b\d+,\d+\b(?!\s*%)", "Kemungkinan koma desimal bahasa Indonesia (Gunakan titik desimal dalam bahasa Inggris)"),
    (r"(?<![,\.\d])\b\d+\s*%", "Spasi sebelum simbol persentase (Tulis rapat: '95%')"),
    (r"\b\d+(?:kHz|MHz|GHz|ms|min|h|cm|mm|kg|g|V|mA|W|dB)\b", "Kurang spasi antara angka dan satuan SI (misal '44.1 kHz', '5 V')"),
    (r"-\d+\s*(?:dB|°C|C|V|mA)", "Tanda minus keyboard '-' digunakan untuk nilai negatif (Gunakan Unicode minus '−' U+2212)"),
]

def lint_text(text: str, check_pronouns: bool = True):
    lines = text.splitlines()
    findings = []
    
    for line_idx, line in enumerate(lines, start=1):
        # Abaikan baris heading atau komentar markdown
        if line.strip().startswith("<!--") or line.strip().startswith("```"):
            continue

        # 1. Cek AI Buzzwords
        for pat, (name, suggestion) in AI_BUZZWORDS.items():
            matches = list(re.finditer(pat, line, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "line": line_idx,
                    "col": m.start() + 1,
                    "category": "AI_SLOP",
                    "matched": m.group(0),
                    "rule": name,
                    "suggestion": suggestion,
                    "snippet": line.strip()
                })

        # 2. Cek Personal Pronouns
        if check_pronouns:
            for pat, desc in PERSONAL_PRONOUNS.items():
                matches = list(re.finditer(pat, line, re.IGNORECASE))
                for m in matches:
                    findings.append({
                        "line": line_idx,
                        "col": m.start() + 1,
                        "category": "PERSONAL_PRONOUN",
                        "matched": m.group(0),
                        "rule": desc,
                        "suggestion": "Ubah ke bentuk pasif impersonil (third-person passive).",
                        "snippet": line.strip()
                    })

        # 3. Cek Tipografi Ilmiah & Angka
        for pat, desc in TYPO_PATTERNS:
            matches = list(re.finditer(pat, line))
            for m in matches:
                findings.append({
                    "line": line_idx,
                    "col": m.start() + 1,
                    "category": "TYPOGRAPHY",
                    "matched": m.group(0),
                    "rule": desc,
                    "suggestion": "Sesuaikan format angka/satuan dengan standar internasional.",
                    "snippet": line.strip()
                })

    return findings

def format_report_text(findings, total_lines):
    if not findings:
        return "[PASS] Bersih. Tidak terdeteksi kata klise AI dalam daftar pantauan, pronomina personal, atau kesalahan tipografi umum."
    
    report = []
    report.append(f"=== LAPORAN LINTER AKADEMIS BAHASA INGGRIS ({len(findings)} TEMUAN DARI {total_lines} BARIS) ===")
    
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
    parser = argparse.ArgumentParser(description="Linter Akademis Bahasa Inggris (Scopus Q1 Standards)")
    parser.add_argument("--file", "-f", help="Path file teks atau markdown yang akan diperiksa")
    parser.add_argument("--text", "-t", help="String teks langsung untuk diperiksa")
    parser.add_argument("--json", action="store_true", help="Output dalam format JSON murni")
    parser.add_argument("--allow-pronouns", action="store_true", help="Izinkan kata ganti orang pertama (We/Our)")
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
        # Baca dari stdin jika ada pipe
        if not sys.stdin.isatty():
            content = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)

    findings = lint_text(content, check_pronouns=(not args.allow_pronouns))
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

    # Exit code: 0 jika bersih, 2 jika ada temuan AI slop/personal pronoun
    if findings:
        sys.exit(2)
    sys.exit(0)

if __name__ == "__main__":
    main()
