import re,hashlib,json,sys,itertools
exec(open('/home/khaeruddien/elharamain-news/ronde-a-1112/tools/pemred_apply.py').read().split('def main')[0])
n=lambda s: re.sub(r'-->\n',r'-->',re.sub(r'\n<!--',r'<!--',s))
A=re.compile(r'<a\s[^>]*href="([^"]*)"[^>]*>(.*?)</a>',re.S)
def variants(b):
    ms=[m for m in A.finditer(b) if 'whatsapp' not in m.group(1) and 'elharamainwisata.com' not in m.group(1)]
    out={}
    for k in range(len(ms)+1):
        for sub in itertools.combinations(ms,k):
            s=b
            for m in sorted(sub,key=lambda m:-m.start()):
                s=s[:m.start()]+m.group(2)+s[m.end():]
            out[hashlib.sha1(s.encode()).hexdigest()]=s
    return out
res={}
for d in sys.argv[1:]:
    html=open(d+'/final.html').read()
    blocks=[(nm,n(b)) for nm,b in split_blocks(html)]; rawb=[b for nm,b in split_blocks(html)]
    pj=json.load(open(d+'/pemred.json'))
    eds={}
    for r in pj.get('replacements',[]):
        hit=[i for i,(_,b) in enumerate(blocks) if r['old'] in b]
        if len(hit)!=1: print('MISSING',d,r['old'][:60],hit); continue
        eds.setdefault(hit[0],[]).append(r)
    out=[]
    for i,rs in sorted(eds.items()):
        vs=variants(blocks[i][1]); vs.update(variants(rawb[i]))
        vv={}
        for h,s in vs.items():
            t=s
            for r in rs:
                if r['old'] not in t: print('OLD-NOT-IN-VARIANT',d,i); 
                t=t.replace(r['old'],r['new'],1)
            vv[h]=t
        out.append({'disk_index':i,'type':full(blocks[i][0]),'variants':vv})
    res[d]={'post':pj['post_id'],'nblocks':len(blocks),'edits':out}
json.dump(res,open('/tmp/pr/plan.json','w'),ensure_ascii=False,indent=1)
for d,v in res.items():
    print(d,v['post'],'nblocks',v['nblocks'])
    for e in v['edits']: print('  idx',e['disk_index'],e['type'],[h[:10] for h in e['variants']])
