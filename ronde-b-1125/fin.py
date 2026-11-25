#!/usr/bin/env python3
"""fin.py <dir> '{"2":[ID,"URL"],...}'  -> <dir>/final.html + cek gaya.
article.json: content_file, images.N.alt/caption."""
import sys, json, re, os
d = sys.argv[1]; m = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
j = json.load(open(os.path.join(d, 'article.json')))
t = open(os.path.join(d, j.get('content_file', 'content.html'))).read()
for n, (mid, url) in m.items():
    im = j['images'][n]
    alt = im['alt'].replace('"', '&quot;'); cap = im.get('caption') or ''
    fc = f'<figcaption class="wp-element-caption">{cap}</figcaption>' if cap else ''
    blk = (f'<!-- wp:image {{"id":{mid},"sizeSlug":"large","linkDestination":"none","align":"center"}} -->'
           f'<figure class="wp-block-image aligncenter size-large"><img src="{url}" alt="{alt}" class="wp-image-{mid}"/>{fc}</figure><!-- /wp:image -->')
    t = t.replace(f'%%IMG{n}%%', blk)
t = re.sub(r'\n?%%IMG\d+%%\n?', '\n', t)
open(os.path.join(d, 'final.html'), 'w').write(t)
txt = re.sub('<[^>]+>', ' ', t)
print('kata', len(txt.split()), '| excerpt', len(j['excerpt']), '| judul', len(j['title']))
bad = ['Di tengah', 'Dalam era', 'Hal ini menunjukkan', 'Perlu diketahui', 'Penting untuk dicatat', 'Tak hanya itu',
       'Secara keseluruhan', 'Dengan demikian', 'Pada akhirnya', 'bukti nyata', 'luar biasa', 'momen berharga',
       'langkah strategis', 'sangat penting', 'Mari ', 'mari ', '—', 'Tidak hanya']
print('frasa:', [b for b in bad if b in txt])
print('CTA ok' if 'phone=6281287292422' in t else 'CTA HILANG', '| pembuka ok' if t.lstrip().startswith('<!-- wp:paragraph --><p><strong>ELHARAMAIN NEWS</strong> –') else '| PEMBUKA?')
