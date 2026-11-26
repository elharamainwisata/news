import sys,re,html,urllib.request
fid=sys.argv[1]
h=urllib.request.urlopen("https://drive.google.com/embeddedfolderview?id="+fid).read().decode()
for m in re.finditer(r'<a href="([^"]+)"[^>]*>.*?<div class="flip-entry-title">(.*?)</div>',h,re.S):
    u,n=m.group(1),html.unescape(m.group(2))
    k='D' if '/folders/' in u else 'F'
    i=re.search(r'/(?:folders|d)/([\w-]+)',u)
    print(k,i.group(1) if i else u,n)
