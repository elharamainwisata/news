import re,sys,html
t=open(sys.argv[1]).read()
d=re.search(r'article:published_time" content="([^"]+)',t)
print('DATE',d.group(1) if d else '?')
i=t.find('(ANTARA) -'); 
if i<0: i=t.find('ANTARA) -')
j=t.find('Pewarta:',i)
s=t[i-200:j]
s=re.sub(r'<script.*?</script>','',s,flags=re.S)
s=html.unescape(re.sub(r'<[^>]+>',' ',s))
print(re.sub(r'\s+',' ',s)[:int(sys.argv[2]) if len(sys.argv)>2 else 4000])
