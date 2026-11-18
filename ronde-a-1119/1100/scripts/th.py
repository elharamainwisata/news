import sys,subprocess,os,concurrent.futures as cf
from PIL import Image,ImageDraw
lines=[l.strip() for l in open('raw/list.txt') if l.startswith('F ') and 'jpeg' in l.lower()]
step=int(sys.argv[1]); start=int(sys.argv[2]) if len(sys.argv)>2 else 0
sel=list(range(start,len(lines),step))
def get(i):
    fid=lines[i].split()[1]; p=f'raw/th/{i:03d}.jpg'
    if not os.path.exists(p) or os.path.getsize(p)<1000:
        subprocess.run(['curl','-sL','-o',p,f'https://drive.google.com/thumbnail?id={fid}&sz=w320'])
    return i,p
with cf.ThreadPoolExecutor(12) as ex: res=list(ex.map(get,sel))
C=8;W=240;H=240
for k in range(0,len(res),40):
    ch=res[k:k+40]; rows=(len(ch)+C-1)//C
    s=Image.new('RGB',(C*W,rows*H),'white'); d=ImageDraw.Draw(s)
    for j,(i,p) in enumerate(ch):
        try: im=Image.open(p).convert('RGB'); im.thumbnail((W,H-14))
        except Exception: continue
        x=(j%C)*W; y=(j//C)*H; s.paste(im,(x,y+14)); d.text((x+2,y),f'{i} {lines[i].split("at ")[-1][:8] if "at " in lines[i] else ""} {lines[i].split("Image ")[-1][5:10]}',fill='red')
    s.save(f'raw/sheet_{start}_{k//40}.jpg',quality=80); print(f'raw/sheet_{start}_{k//40}.jpg')
