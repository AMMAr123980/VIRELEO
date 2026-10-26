import glob
import re

for f in sorted(glob.glob("*.html")):
    with open(f, encoding="utf-8") as fp:
        txt = fp.read()
    t = re.search(r"<title>(.*?)</title>", txt)
    d = re.search(r'<meta name="description" content="(.*?)"', txt)
    ogt = re.search(r'<meta property="og:title" content="(.*?)"', txt)
    twit = re.search(r'<meta name="twitter:title" content="(.*?)"', txt)
    fav = re.findall(r'<link rel="(?:shortcut )?icon".*?>', txt)
    print("=" * 50)
    print("FILE:", f)
    print("Title:   ", t.group(1) if t else "MISSING")
    print("Desc:    ", d.group(1) if d else "MISSING")
    print("OG Title:", ogt.group(1) if ogt else "MISSING")
    print("TW Title:", twit.group(1) if twit else "MISSING")
    print("Favicons:", len(fav))
