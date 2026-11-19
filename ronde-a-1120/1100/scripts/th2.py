import sys,subprocess,os,concurrent.futures as cf
from PIL import Image,ImageDraw
lines=[l.strip() for l in open('raw/list.txt') if l.startswith('F ') and 'jpeg' in l.lower()]
sel=[]
for r in sys.argv[2:]:
    a,b,s=map(int,r.split(':')); sel+=list(range(a,b,s))
def get(i):
    fid=lines[i].split()[1]; p=f'raw/th/{i:03d}.jpg'
    if not os.path.exists(p) or os.path.getsize(p)<1000:
        subprocess.run(['curl','-sL','-o',p,f'https://drive.google.com/thumbnail?id={fid}&sz=w320'])
    return i,p
with cf.ThreadPoolExecutor(12) as ex: res=list(ex.map(get,sel))
C=8;W=240;H=240
rows=(len(res)+C-1)//C
s=Image.new('RGB',(C*W,rows*H),'white'); d=ImageDraw.Draw(s)
for j,(i,p) in enumerate(res):
    try: im=Image.open(p).convert('RGB'); im.thumbnail((W,H-14))
    except Exception: continue
    x=(j%C)*W; y=(j//C)*H; s.paste(im,(x,y+14)); d.text((x+2,y),str(i),fill='red')
s.save(sys.argv[1],quality=80)
