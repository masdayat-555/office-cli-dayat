import re
import json

paper_script = r'c:\DISK-D\MOUSEPENELITIAN\build_complete_paper.py'
with open(paper_script, 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_ref = False
raw_refs = []
for l in lines:
    if 'references_list = [' in l:
        in_ref = True
        continue
    if in_ref:
        if l.strip().startswith(']'):
            break
        s = l.strip()
        if s.endswith(','):
            s = s[:-1].strip()
        if (s.startswith("'") and s.endswith("'")) or (s.startswith('"') and s.endswith('"')):
            s = s[1:-1].strip()
        if s:
            raw_refs.append(s)

print(f"Total raw references extracted: {len(raw_refs)}")

structured_papers = []
for line in raw_refs:
    doi_match = re.search(r'https?://(?:dx\.)?doi\.org/([^\s]+)', line)
    doi = doi_match.group(1).rstrip('.') if doi_match else ""
    
    author_year_match = re.match(r'^(.*?)\s*\((\d{4}[a-z]?)\)\.\s*(.*?)$', line)
    if author_year_match:
        authors_raw = author_year_match.group(1)
        year = author_year_match.group(2)
        rest = author_year_match.group(3)
        
        title_match = re.match(r'^(.*?)\.\s*(.*)$', rest)
        if title_match:
            title = title_match.group(1)
            pub = title_match.group(2)
        else:
            title = rest
            pub = ""
            
        first_author = authors_raw.split(',')[0].strip()
        if '&' in authors_raw and len(authors_raw.split(',')) <= 3:
            second_author = authors_raw.split('&')[1].split(',')[0].strip()
            cite_key = f"{first_author} & {second_author}, {year}"
        elif len(authors_raw.split(',')) > 3 or 'et al' in authors_raw:
            cite_key = f"{first_author} et al., {year}"
        else:
            cite_key = f"{first_author}, {year}"
            
        structured_papers.append({
            "cite_key": cite_key,
            "raw_text": line,
            "authors": authors_raw,
            "year": year,
            "title": title,
            "publication": pub,
            "doi": doi
        })
    else:
        structured_papers.append({
            "cite_key": "Unknown",
            "raw_text": line,
            "doi": doi
        })

print(f"Berhasil menyusun {len(structured_papers)} paper terstruktur!")
output_json = r'c:\DISK-D\MOUSEPENELITIAN\references_for_zotero.json'
with open(output_json, 'w', encoding='utf-8') as f:
    json.dump(structured_papers, f, indent=2, ensure_ascii=False)
