import sys,re,html
src=open(sys.argv[1]).read().strip().split('\n\n')
out=[]
for p in src:
    p=p.strip()
    if p.startswith('%%IMG'): out.append(p); continue
    out.append('<!-- wp:paragraph -->\n<p>%s</p>\n<!-- /wp:paragraph -->'%p)
h='\n\n'.join(out)
open(sys.argv[2],'w').write(h+'\n')
t=html.unescape(re.sub('<[^>]+>',' ',h.replace('%%IMG2%%','')))
print('words',len(t.split()), 'emdash','—' in h)
