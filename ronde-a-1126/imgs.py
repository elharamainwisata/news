#!/usr/bin/env python3
"""imgs.py slot... -> daftar gambar: slot n file sha256 caption | alt"""
import sys,json,hashlib,os
for s in sys.argv[1:]:
    j=json.load(open(os.path.join(s,'article.json')))
    for n,im in j['images'].items():
        f=im.get('file') or ''
        if f and not f.startswith('/'): f=os.path.abspath(os.path.join(s,f))
        h=hashlib.sha256(open(f,'rb').read()).hexdigest() if f and os.path.exists(f) else 'NOFILE'
        print(s,n,f,h,'|',im.get('caption'),'|',im.get('alt'))
