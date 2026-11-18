import re,hashlib,json,sys
exec(open('/home/khaeruddien/elharamain-news/ronde-a-1112/tools/pemred_apply.py').read().split('def main')[0])
def nl(b):
    b=re.sub(r'(<!-- wp:[^>]*-->)\s*',r'\1\n',b,count=1)
    b=re.sub(r'\s*(<!-- /wp:[^>]*-->)$',r'\n\1',b.strip())
    return b
d=sys.argv[1]
html=open(d+'/final.html').read()
blocks=[nl(b) for nm,b in split_blocks(html)]
pj=json.load(open(d+'/pemred.json'))
out=[]
for r in pj.get('replacements',[]):
    hit=[i for i,b in enumerate(blocks) if r['old'] in b]
    if len(hit)!=1: print('MISSING',r['old'][:60],hit); continue
    i=hit[0]; old=blocks[i]; blocks[i]=old.replace(r['old'],r['new'],1)
    out.append((i,hashlib.sha1(old.encode()).hexdigest()))
for i,h in sorted(set(out)):
    print('IDX',i,'oldhash',h); print(blocks[i]); print()
