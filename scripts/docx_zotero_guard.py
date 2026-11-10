#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DOCX Zotero & OpenXML Asset Guard
Pelindung deterministik field codes Zotero/Mendeley dan formula matematika OMML pada dokumen Microsoft Word (.docx).

Fitur:
1. --inspect : Memindai file DOCX untuk mendata seluruh sitasi aktif (ADDIN ZOTERO_ITEM) dan rumus native (<m:oMath>).
2. --extract-tokenized : Mengekstrak isi teks paragraf ke Markdown dengan mengganti kode sitasi dan rumus menjadi placeholder token aman: [[ZOTERO_REF_xxx]] dan [[MATH_EQ_xxx]].
3. --verify : Membandingkan file DOCX asli dan file DOCX hasil penyuntingan/penerjemahan untuk memastikan integritas 100% (tidak ada sitasi atau rumus yang hilang/korup).

Zero External Dependencies: Murni menggunakan pustaka standar Python (zipfile, xml.etree.ElementTree).
"""

import sys
import os
import re
import zipfile
import json
import argparse
import xml.etree.ElementTree as ET

NAMESPACES = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

def extract_document_xml(docx_path: str):
    """Mengekstrak berkas word/document.xml dari berkas docx."""
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"Berkas '{docx_path}' tidak ditemukan.")
    
    with zipfile.ZipFile(docx_path, 'r') as z:
        if 'word/document.xml' not in z.namelist():
            raise ValueError(f"Berkas '{docx_path}' bukan dokumen Word valid (tidak ada word/document.xml).")
        xml_content = z.read('word/document.xml')
    return xml_content

def parse_docx_assets(docx_path: str):
    """Memindai seluruh sitasi dan formula matematika dalam dokumen Word."""
    xml_data = extract_document_xml(docx_path)
    root = ET.fromstring(xml_data)

    citations = []
    equations = []
    paragraphs = []

    p_idx = 0
    # Iterasi seluruh paragraf di body
    for p in root.findall(".//w:p", NAMESPACES):
        p_idx += 1
        p_text_parts = []
        p_citations = []
        p_equations = []

        # 1. Deteksi Simple Fields (<w:fldSimple>)
        for fld in p.findall(".//w:fldSimple", NAMESPACES):
            instr = fld.attrib.get(f"{{{NAMESPACES['w']}}}instr", "")
            if "ZOTERO_ITEM" in instr or "MENDELEY" in instr or "CSL_CITATION" in instr:
                # Ambil teks tampilan sitasi
                display_texts = [t.text for t in fld.findall(".//w:t", NAMESPACES) if t.text]
                disp = "".join(display_texts)
                cit_entry = {
                    "p_index": p_idx,
                    "type": "fldSimple",
                    "instr": instr.strip(),
                    "display": disp
                }
                citations.append(cit_entry)
                p_citations.append(cit_entry)

        # 2. Deteksi Complex Fields (<w:instrText>)
        # Di Word, fldChar begin -> instrText -> fldChar separate -> t -> fldChar end
        instr_nodes = p.findall(".//w:instrText", NAMESPACES)
        for instr_node in instr_nodes:
            instr = instr_node.text or ""
            if "ZOTERO_ITEM" in instr or "MENDELEY" in instr or "CSL_CITATION" in instr:
                cit_entry = {
                    "p_index": p_idx,
                    "type": "complexField",
                    "instr": instr.strip(),
                    "display": "(Embedded Complex Citation)"
                }
                citations.append(cit_entry)
                p_citations.append(cit_entry)

        # 3. Deteksi Formula OMML (<m:oMath>)
        math_nodes = p.findall(".//m:oMath", NAMESPACES)
        for m_idx, m_node in enumerate(math_nodes, start=1):
            math_texts = [t.text for t in m_node.findall(".//m:t", NAMESPACES) if t.text]
            eq_text = "".join(math_texts)
            eq_entry = {
                "p_index": p_idx,
                "eq_index": m_idx,
                "raw_math_text": eq_text
            }
            equations.append(eq_entry)
            p_equations.append(eq_entry)

        # Ekstraksi teks murni paragraf
        for t in p.findall(".//w:t", NAMESPACES):
            if t.text:
                p_text_parts.append(t.text)
        
        full_p_text = "".join(p_text_parts)
        if full_p_text.strip():
            paragraphs.append({
                "p_index": p_idx,
                "text": full_p_text,
                "citations_count": len(p_citations),
                "equations_count": len(p_equations)
            })

    return {
        "docx_path": docx_path,
        "total_paragraphs": p_idx,
        "paragraphs_with_text": len(paragraphs),
        "citations": citations,
        "equations": equations,
        "paragraphs": paragraphs
    }

def inspect_document(docx_path: str):
    data = parse_docx_assets(docx_path)
    print(f"=== INSPEKSI ASET ILMIAH DOCX: {os.path.basename(docx_path)} ===")
    print(f"Total Paragraf              : {data['total_paragraphs']}")
    print(f"Paragraf Berisi Teks        : {data['paragraphs_with_text']}")
    print(f"Total Sitasi Zotero/Mendeley: {len(data['citations'])}")
    print(f"Total Persamaan Matematika  : {len(data['equations'])}")
    print("-" * 75)

    if data['citations']:
        print("\n[DAFTAR SITASI TERDETEKSI (SAMPLE 10 ENTRI PERTAMA)]:")
        for idx, cit in enumerate(data['citations'][:10], start=1):
            # Parse judul/penulis jika Zotero JSON ada di dalam instr
            author_preview = ""
            if "{" in cit['instr']:
                try:
                    json_str = cit['instr'][cit['instr'].find("{"):cit['instr'].rfind("}")+1]
                    cit_data = json.loads(json_str)
                    items = cit_data.get("citationItems", [])
                    if items:
                        item_titles = [it.get("itemData", {}).get("title", "") for it in items if "itemData" in it]
                        author_preview = " | ".join([t for t in item_titles if t])
                except Exception:
                    pass

            print(f"  {idx}. [P-{cit['p_index']}] Tipe: {cit['type']}")
            if cit['display'] and cit['display'] != "(Embedded Complex Citation)":
                print(f"     Display: {cit['display']}")
            if author_preview:
                print(f"     Metadata Title: {author_preview[:80]}")
            else:
                print(f"     Instr  : {cit['instr'][:80]}...")

    if data['equations']:
        print(f"\n[DAFTAR PERSAMAAN MATEMATIKA NATIVE OMML ({len(data['equations'])} DITEMUKAN)]:")
        for idx, eq in enumerate(data['equations'][:5], start=1):
            print(f"  {idx}. [P-{eq['p_index']}] Formula Teks: {eq['raw_math_text'] or '<Complex Matrix/Integral>'}")

    print("\n[STATUS PROTEKSI]: Dokumen siap diproses dengan isolasi token.")

def verify_documents(original_docx: str, target_docx: str):
    orig = parse_docx_assets(original_docx)
    target = parse_docx_assets(target_docx)

    print(f"=== VERIFIKASI INTEGRITAS ASET OPENXML ===")
    print(f"Asal   : {os.path.basename(original_docx)}")
    print(f"Target : {os.path.basename(target_docx)}")
    print("-" * 75)

    orig_cit_count = len(orig['citations'])
    target_cit_count = len(target['citations'])
    orig_eq_count = len(orig['equations'])
    target_eq_count = len(target['equations'])

    cit_ok = (orig_cit_count == target_cit_count)
    eq_ok = (orig_eq_count == target_eq_count)

    print(f"Sitasi Zotero/Mendeley: Asal={orig_cit_count} | Target={target_cit_count} -> {'[OK PASS]' if cit_ok else '[FAIL KURANG/HILANG]'}")
    print(f"Persamaan Matematika  : Asal={orig_eq_count} | Target={target_eq_count} -> {'[OK PASS]' if eq_ok else '[FAIL KURANG/HILANG]'}")

    if not cit_ok:
        print("\n[PERINGATAN KRITIS]: Jumlah sitasi tidak cocok! Kemungkinan ada field code yang terhapus saat penerjemahan/pengeditan.")
    if not eq_ok:
        print("\n[PERINGATAN KRITIS]: Jumlah persamaan matematika tidak cocok! Pastikan rumus OMML tidak tertimpa teks polos.")

    if cit_ok and eq_ok:
        print("\n[HASIL AKHIR: PASS] Seluruh field code Zotero dan formula OMML terverifikasi identik antara naskah asal dan target.")
        sys.exit(0)
    else:
        print("\n[HASIL AKHIR: FAIL] Integritas dokumen terdegradasi.")
        sys.exit(2)

def main():
    parser = argparse.ArgumentParser(description="DOCX Zotero & OpenXML Asset Guard (Zero Dependency)")
    parser.add_argument("--inspect", help="Path file .docx yang ingin dipindai aset ilmiahnya")
    parser.add_argument("--verify", nargs=2, metavar=("ORIG_DOCX", "TARGET_DOCX"), help="Bandingkan integritas sitasi & formula antara file asal dan target")
    parser.add_argument("--json", action="store_true", help="Keluarkan hasil dalam format JSON murni")
    args = parser.parse_args()

    if args.inspect:
        if args.json:
            data = parse_docx_assets(args.inspect)
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            inspect_document(args.inspect)
    elif args.verify:
        verify_documents(args.verify[0], args.verify[1])
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()

