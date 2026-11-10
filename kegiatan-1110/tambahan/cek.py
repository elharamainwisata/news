import json,re,sys
for k in sys.argv[1:]:
    t=open(k+'.html').read(); j=json.load(open(k+'.json'))
    txt=re.sub(r'<[^>]+>|%%IMG\d%%',' ',t); print(k,'kata',len(txt.split()),'judul',len(j['title']),'excerpt',len(j['excerpt']))
    for w in ['berangkat','bandara','maskapai','pesawat','kepulangan','pulang','Qatar','Makassar','—','kian','semakin','mari ','luar biasa','Tak hanya','check-in','manasik']:
        if w.lower() in t.lower() or w.lower() in j['title'].lower(): print('  CEK:',w)
