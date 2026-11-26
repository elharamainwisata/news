import sys
from PIL import Image
src,out,ratio,yc=sys.argv[1],sys.argv[2],sys.argv[3],float(sys.argv[4])
im=Image.open(src).convert('RGB'); W,H=im.size
rw,rh=map(int,ratio.split(':'))
if W/H>rw/rh:
    nw=int(H*rw/rh); x=(W-nw)//2; box=(x,0,x+nw,H)
else:
    nh=int(W*rh/rw); y=int(max(0,min(H-nh,yc*H-nh/2))); box=(0,y,W,y+nh)
c=im.crop(box)
tw=1280 if rw>rh else 1024
c=c.resize((tw,int(tw*rh/rw)),Image.LANCZOS)
c.save(out,'JPEG',quality=82); print(out,c.size)
