import sys
from PIL import Image
fs=sys.argv[2:]; W=640
ims=[Image.open(f).convert('RGB') for f in fs]
rows=[im.resize((W,int(im.height*W/im.width))) for im in ims]
cols=2; heights=[0,0]; pos=[]
for r in rows:
    c=heights.index(min(heights)); pos.append((c*W,heights[c])); heights[c]+=r.height
s=Image.new('RGB',(W*cols,max(heights)),'white')
for r,p in zip(rows,pos): s.paste(r,p)
s.save(sys.argv[1],quality=80)
