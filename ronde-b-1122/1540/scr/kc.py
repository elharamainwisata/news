import re,sys,html
t=open(sys.argv[1]).read()
d=re.search(r'content_PublishedDate" content="([^"]+)',t) or re.search(r'datePublished"\s*:\s*"([^"]+)',t); print('DATE',d.group(1) if d else '?')
m=re.search(r'<div class="read__content">(.*?)<div class="(?:read__tag|tag__article)',t,re.S)
s=m.group(1) if m else t
s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
s=re.sub(r'<p>\s*<strong>Baca juga.*?</p>','',s,flags=re.S)
print(re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s)))[:int(sys.argv[2]) if len(sys.argv)>2 else 5000])
