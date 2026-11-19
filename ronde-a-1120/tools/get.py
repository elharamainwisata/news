import json,sys
p=json.load(open('/tmp/pr/plan.json'))
d,pre=sys.argv[1],sys.argv[2]
for e in p[d]['edits']:
    for h,s in e['variants'].items():
        if h.startswith(pre): print(s)
