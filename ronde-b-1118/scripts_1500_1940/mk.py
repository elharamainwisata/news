import sys,re,html
src=open(sys.argv[1]).read().strip().split('\n\n')
out=[]
for p in src:
    p=p.strip()
    if p.startswith('%%IMG'): out.append(p); continue
    out.append('<!-- wp:paragraph --><p>%s</p><!-- /wp:paragraph -->'%p)
h='\n\n'.join(out)
open(sys.argv[2],'w').write(h+'\n')
t=html.unescape(re.sub('<[^>]+>',' ',re.sub(r'%%IMG\d+%%','',h)))
print('words',len(t.split()),'emdash','—' in h,'links',re.findall(r'href="([^"]+)"',h))
bad=['Di tengah','Dalam era','Hal ini menunjukkan','Perlu diketahui','Penting untuk dicatat','Tak hanya itu','Secara keseluruhan','Dengan demikian','Pada akhirnya','bukti nyata','luar biasa','momen berharga','langkah strategis','sangat penting','Mari ','mari ','Tidak hanya',' kian ','semakin']
print('frasa',[b for b in bad if b in t])
