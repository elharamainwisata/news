#!/usr/bin/env python3
"""Hitung edit per blok dari pemred.json terhadap final.html.
Pakai: pemred_apply.py <final.html> <pemred.json>
Cetak JSON: content_hash, blocks [{index,type,hash}], edits [{index,type,old_hash,new_markup}], missing [...]"""
import hashlib, json, re, sys

def split_blocks(s):
    tok = re.compile(r'<!--\s+(/)?wp:([a-z0-9\-/]+)(\s+\{.*?\})?\s*(/)?-->', re.S)
    blocks, depth, start, name = [], 0, None, None
    for m in tok.finditer(s):
        closing, nm, selfclose = m.group(1), m.group(2), m.group(4)
        if not closing:
            if depth == 0:
                start, name = m.start(), nm
                if selfclose:
                    blocks.append((name, s[start:m.end()]))
                    continue
            if not selfclose:
                depth += 1
        else:
            depth -= 1
            if depth == 0:
                blocks.append((name, s[start:m.end()]))
    return blocks

def full(n):
    return n if '/' in n else 'core/' + n

def main():
    html = open(sys.argv[1]).read()
    pj = json.load(open(sys.argv[2]))
    blocks = split_blocks(html)
    out = {"content_hash": hashlib.sha1(html.strip().encode()).hexdigest(),
           "blocks": [{"index": i, "type": full(n), "hash": hashlib.sha1(b.encode()).hexdigest()} for i, (n, b) in enumerate(blocks)],
           "edits": {}, "missing": []}
    new = {i: b for i, (n, b) in enumerate(blocks)}
    for r in pj.get("replacements", []):
        hit = [i for i in new if r["old"] in new[i]]
        if len(hit) != 1:
            out["missing"].append({"old": r["old"][:80], "hits": hit}); continue
        i = hit[0]; new[i] = new[i].replace(r["old"], r["new"], 1)
        out["edits"][i] = {"index": i, "type": full(blocks[i][0]), "old_hash": out["blocks"][i]["hash"], "new_markup": new[i]}
    out["edits"] = list(out["edits"].values())
    print(json.dumps(out, ensure_ascii=False, indent=1))

main()
