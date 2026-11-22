import re,sys,html
t=open(sys.argv[1]).read()
for k in ['article:published_time','datePublished']:
    m=re.search(k+r'"?\s*(?:content=|:)\s*"([^"]+)',t)
    if m: print('DATE',m.group(1)); break
m=re.search(r'<div class="article-content[^"]*"[^>]*>(.*?)</article>',t,re.S) or re.search(r'itemprop="articleBody"[^>]*>(.*?)</div>\s*</div>',t,re.S)
s=m.group(1) if m else t
s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
s=html.unescape(re.sub(r'<[^>]+>',' ',s))
print(re.sub(r'\s+',' ',s)[:int(sys.argv[2]) if len(sys.argv)>2 else 5000])
