#!/usr/bin/env python3
"""Isi placeholder %%IMGn%% di <x>.html dengan blok wp:image.
Pakai: python3 isi.py a '{"2":[17400,"https://news.elharamainwisata.com/wp-content/uploads/2026/11/xxx.jpg"],"3":[..],"4":[..]}'
Hasil: a.final.html (siap jadi content posts.create). Gambar 1 = featured_media (tidak masuk badan).
Alt diambil dari a.json; caption "Foto: Dokumentasi Elharamain Wisata"."""
import sys,json
k=sys.argv[1]; m=json.loads(sys.argv[2]); j=json.load(open(k+'.json')); t=open(k+'.html').read()
for n,(mid,url) in m.items():
    alt=j['images'][n]['alt'].replace('"','&quot;')
    blk=(f'<!-- wp:image {{"id":{mid},"sizeSlug":"large","linkDestination":"none","align":"center"}} -->'
         f'<figure class="wp-block-image aligncenter size-large"><img src="{url}" alt="{alt}" class="wp-image-{mid}"/>'
         f'<figcaption class="wp-element-caption">Foto: Dokumentasi Elharamain Wisata</figcaption></figure><!-- /wp:image -->')
    t=t.replace(f'%%IMG{n}%%',blk)
assert '%%IMG' not in t, 'masih ada placeholder'
open(k+'.final.html','w').write(t); print('ok',k+'.final.html')
