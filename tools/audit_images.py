import glob
import re
from html.parser import HTMLParser

class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.images.append(dict(attrs))

for f in sorted(glob.glob("*.html")):
    with open(f, encoding="utf-8") as fp:
        txt = fp.read()

    parser = ImgParser()
    parser.feed(txt)

    missing_alt = [img for img in parser.images if not img.get("alt")]
    missing_loading = [img for img in parser.images if not img.get("loading")]
    missing_dims = [img for img in parser.images if not (img.get("width") and img.get("height"))]

    print(f"{f}: {len(parser.images)} images")
    if missing_alt:
        print(f"  Missing alt ({len(missing_alt)}):", [img.get("src") for img in missing_alt])
    if missing_loading:
        print(f"  Missing loading attribute ({len(missing_loading)}):", [img.get("src") for img in missing_loading])
    if missing_dims:
        print(f"  Missing width/height ({len(missing_dims)}):", [img.get("src") for img in missing_dims])
