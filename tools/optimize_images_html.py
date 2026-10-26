import glob
import re

DIMENSIONS = {
    'images/projects/ammar-portfolio.jpg': (1200, 900),
    'images/projects/lean-canvas-model.jpg': (1200, 900),
    'images/projects/ai-employee-os.jpg': (1200, 900),
    'images/projects/mailnexa-ai.jpg': (1200, 900),
    'images/projects/iot-weather.jpg': (1376, 768),
    'images/projects/whatsapp-dm-wide.jpg': (1686, 952),
    'images/projects/instagram-dm-wide.jpg': (1192, 697),
    'images/vireleo-3d-scene.webp': (778, 516),
}

for file in sorted(glob.glob('*.html')):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    for src, (w, h) in DIMENSIONS.items():
        # Match <img ... src="src" ...>
        # Check if width/height is missing or needs decoding="async"
        pattern = re.compile(rf'<img([^>]*?src=["\']{re.escape(src)}["\'][^>]*?)>', re.IGNORECASE)
        
        def replacer(m):
            attrs = m.group(1)
            # Add width if missing
            if 'width=' not in attrs:
                attrs += f' width="{w}"'
            # Add height if missing
            if 'height=' not in attrs:
                attrs += f' height="{h}"'
            # Add loading="lazy" if missing
            if 'loading=' not in attrs:
                attrs += ' loading="lazy"'
            # Add decoding="async" if missing
            if 'decoding=' not in attrs:
                attrs += ' decoding="async"'
            return f'<img{attrs}>'

        new_content = pattern.sub(replacer, content)
        if new_content != content:
            content = new_content
            modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Optimized image tags in {file}')

print('Image optimization complete!')
