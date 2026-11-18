import re,hashlib,json,sys
exec(open('/home/khaeruddien/elharamain-news/ronde-a-1112/tools/pemred_apply.py').read().split('def main')[0])
n=lambda s: re.sub(r'-->\n',r'-->',re.sub(r'\n<!--',r'<!--',s))
for d in sys.argv[1:]:
    html=open(d+'/final.html').read()
    blocks=[(nm,n(b)) for nm,b in split_blocks(html)]
    pj=json.load(open(d+'/pemred.json'))
    print('#####',d,'content_hash',hashlib.sha1('\n\n'.join(b for _,b in blocks).strip().encode()).hexdigest())
    new={i:b for i,(_,b) in enumerate(blocks)}
    ed=set()
    for r in pj.get('replacements',[]):
        hit=[i for i in new if r['old'] in new[i]]
        if len(hit)!=1: print('MISSING',r['old'][:60],hit); continue
        new[hit[0]]=new[hit[0]].replace(r['old'],r['new'],1); ed.add(hit[0])
    for i in sorted(ed):
        print('IDX',i,full(blocks[i][0]),hashlib.sha1(blocks[i][1].encode()).hexdigest())
        print(new[i])
