#!/usr/bin/env python3
"""Pengganti tool WordPress-com (MCP) untuk mode cadangan API.

Pemakaian (meniru operasi wpcom-mcp-content-authoring):
    python3 backup/wp.py <operasi> '<params JSON>'

Operasi: posts.list, posts.get, posts.create, posts.update,
         media.create, media.get, tags.list, tags.create, categories.list

media.create menerima {"file": "/path/lokal.jpg"} ATAU {"source_url": "https://..."}
plus title, alt_text, caption. Tidak perlu media.upload / upload_command.

Kredensial dibaca dari ~/.config/elharamain-news/api-backup.env:
    WP_NEWS_USER, WP_NEWS_PASS (Application Password WordPress)
"""
import json
import mimetypes
import os
import sys
import tempfile
import urllib.parse

import requests

BASE = "https://news.elharamainwisata.com/wp-json/wp/v2"
ENV_FILE = os.path.expanduser("~/.config/elharamain-news/api-backup.env")


def load_env():
    if os.path.exists(ENV_FILE):
        for line in open(ENV_FILE, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
    user, pw = os.environ.get("WP_NEWS_USER"), os.environ.get("WP_NEWS_PASS")
    if not user or not pw:
        sys.exit("WP_NEWS_USER / WP_NEWS_PASS belum diisi di " + ENV_FILE)
    return (user, pw)


AUTH = None


def req(method, path, **kw):
    r = requests.request(method, BASE + path, auth=AUTH, timeout=120, **kw)
    if r.status_code >= 400:
        sys.exit(f"HTTP {r.status_code}: {r.text[:800]}")
    return r


def pick(obj, fields):
    if not fields:
        return obj
    return {k: obj.get(k) for k in fields}


def simplify(obj):
    # samakan bentuk dengan MCP: title/content/excerpt sebagai string bila bisa
    for k in ("title", "excerpt", "caption"):
        v = obj.get(k)
        if isinstance(v, dict):
            obj[k] = v.get("raw", v.get("rendered"))
    c = obj.get("content")
    if isinstance(c, dict):
        obj["content"] = c.get("raw", c.get("rendered"))
    return obj


def list_params(p):
    q = {}
    for k, v in p.items():
        if k in ("include_fields",):
            continue
        if isinstance(v, list):
            v = ",".join(str(x) for x in v)
        q[k] = v
    if "status" in q:
        q["status"] = q["status"].replace(" ", "")
    return q


def posts_list(p):
    fields = p.get("include_fields")
    q = list_params(p)
    q.setdefault("context", "edit")
    q.setdefault("per_page", 20)
    r = req("GET", "/posts", params=q)
    data = [pick(simplify(x), fields) for x in r.json()]
    return {"data": data, "total": int(r.headers.get("X-WP-Total", len(data)))}


def posts_get(p):
    fields = p.get("include_fields")
    r = req("GET", f"/posts/{p['id']}", params={"context": p.get("context", "edit")})
    return {"data": pick(simplify(r.json()), fields)}


def post_body(p):
    body = {k: v for k, v in p.items() if k not in ("id", "user_confirmed", "include_fields")}
    return body


def posts_create(p):
    r = req("POST", "/posts", json=post_body(p))
    x = r.json()
    return {"data": {"id": x["id"], "status": x["status"], "date": x["date"], "link": x["link"]}}


def posts_update(p):
    r = req("POST", f"/posts/{p['id']}", json=post_body(p))
    x = r.json()
    return {"data": {"id": x["id"], "status": x["status"], "date": x["date"], "link": x["link"]}}


def media_create(p):
    path = p.get("file")
    tmp = None
    if not path:
        url = p.get("source_url")
        if not url:
            sys.exit("media.create butuh 'file' atau 'source_url'")
        r = requests.get(url, timeout=120, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        name = os.path.basename(urllib.parse.urlparse(url).path) or "gambar.jpg"
        if "." not in name:
            name += ".jpg"
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(name)[1])
        tmp.write(r.content)
        tmp.close()
        path = tmp.name
    filename = p.get("filename") or os.path.basename(path)
    mime = mimetypes.guess_type(filename)[0] or "image/jpeg"
    with open(path, "rb") as fh:
        r = req("POST", "/media", data=fh.read(), headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Content-Type": mime})
    mid = r.json()["id"]
    meta = {k: p[k] for k in ("title", "alt_text", "caption", "description") if k in p}
    if meta:
        r = req("POST", f"/media/{mid}", json=meta)
    if tmp:
        os.unlink(tmp.name)
    x = r.json()
    sizes = {k: v.get("source_url") for k, v in x.get("media_details", {}).get("sizes", {}).items()}
    return {"data": {"id": x["id"], "source_url": x["source_url"], "sizes": sizes}}


def media_get(p):
    x = req("GET", f"/media/{p['id']}").json()
    sizes = {k: v.get("source_url") for k, v in x.get("media_details", {}).get("sizes", {}).items()}
    return {"data": {"id": x["id"], "source_url": x["source_url"], "alt_text": x.get("alt_text"), "sizes": sizes}}


def tags_list(p):
    q = list_params(p)
    q.setdefault("per_page", 20)
    return {"data": [{"id": t["id"], "name": t["name"], "slug": t["slug"]} for t in req("GET", "/tags", params=q).json()]}


def tags_create(p):
    t = req("POST", "/tags", json={"name": p["name"]}).json()
    return {"data": {"id": t["id"], "name": t["name"]}}


def categories_list(p):
    q = list_params(p)
    q.setdefault("per_page", 50)
    return {"data": [{"id": c["id"], "name": c["name"]} for c in req("GET", "/categories", params=q).json()]}


OPS = {
    "posts.list": posts_list, "posts.get": posts_get, "posts.create": posts_create,
    "posts.update": posts_update, "media.create": media_create, "media.get": media_get,
    "tags.list": tags_list, "tags.create": tags_create, "categories.list": categories_list,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in OPS:
        sys.exit("Operasi: " + ", ".join(OPS))
    AUTH = load_env()
    params = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    print(json.dumps(OPS[sys.argv[1]](params), ensure_ascii=False, indent=1))
