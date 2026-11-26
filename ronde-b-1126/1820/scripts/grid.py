import sys,glob,os
from PIL import Image,ImageDraw
fs=sorted(glob.glob(sys.argv[1]+'/*.jpg')); out=sys.argv[2]; per=30; W=260;H=195
for s in range(0,len(fs),per):
    ch=fs[s:s+per]; g=Image.new('RGB',(W*6,H*5),'white'); d=ImageDraw.Draw(g)
    for k,f in enumerate(ch):
        try: im=Image.open(f).convert('RGB')
        except: continue
        im.thumbnail((W-4,H-4)); x=(k%6)*W; y=(k//6)*H; g.paste(im,(x,y))
        d.rectangle([x,y,x+40,y+16],fill='yellow'); d.text((x+2,y+2),os.path.basename(f)[:-4],fill='black')
    g.save('%s_%d.jpg'%(out,s//per+1),quality=80)
