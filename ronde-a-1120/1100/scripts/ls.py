import re,sys,subprocess,html
fid=sys.argv[1]
h=subprocess.run(["curl","-sL",f"https://drive.google.com/embeddedfolderview?id={fid}"],capture_output=True,text=True).stdout
for m in re.finditer(r'<a href="([^"]+)"[^>]*>.*?<div class="flip-entry-title">(.*?)</div>',h,re.S):
    u=m.group(1); n=html.unescape(m.group(2))
    mm=re.search(r'/folders/([\w-]+)',u) or re.search(r'/file/d/([\w-]+)',u)
    print(('D ' if '/folders/' in u else 'F ')+(mm.group(1) if mm else u)+' | '+n)
