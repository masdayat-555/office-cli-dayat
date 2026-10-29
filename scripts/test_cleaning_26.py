import json
import sys
from zotero_clean_metadata import clean_and_build_zotero_item

input_json = r'c:\DISK-D\MOUSEPENELITIAN\references_for_zotero.json'
with open(input_json, 'r', encoding='utf-8') as f:
    papers = json.load(f)

print(f"Memulai pembersihan metadata untuk {len(papers)} paper...")
cleaned_results = []
for p in papers:
    cleaned = clean_and_build_zotero_item(p)
    authors_summary = ", ".join([f"{c['lastName']} ({c['firstName']})" for c in cleaned.get('creators', [])[:2]])
    if len(cleaned.get('creators', [])) > 2:
        authors_summary += " et al."
    print(f"[{cleaned.get('extra', 'OK')[:15]}] {cleaned['date']} | {authors_summary[:30]:30} | {cleaned['title'][:50]}...")
    cleaned_results.append(cleaned)

print("\nSeluruh 26 metadata telah dibersihkan secara otomatis!")
