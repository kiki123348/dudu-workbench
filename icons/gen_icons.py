from PIL import Image, ImageDraw, ImageFont
import os

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
OUT_DIR = '/workspace/dudu-workbench/icons'

for size in SIZES:
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 圆角矩形背景
    margin = int(size * 0.05)
    r = int(size * 0.18)

    # 渐变蓝色背景
    for y in range(margin, size - margin):
        ratio = (y - margin) / (size - 2 * margin)
        r_col = int(74 + ratio * (107 - 74))
        g_col = int(95 + ratio * (133 - 95))
        b_col = int(193 + ratio * (214 - 193))
        for x in range(margin, size - margin):
            # 简单圆角判断
            cx, cy = x, y
            in_corner = False
            if cx < margin + r and cy < margin + r:
                in_corner = ((cx - margin - r)**2 + (cy - margin - r)**2) > r**2
            elif cx > size - margin - r and cy < margin + r:
                in_corner = ((cx - (size - margin - r))**2 + (cy - margin - r)**2) > r**2
            elif cx < margin + r and cy > size - margin - r:
                in_corner = ((cx - margin - r)**2 + (cy - (size - margin - r))**2) > r**2
            elif cx > size - margin - r and cy > size - margin - r:
                in_corner = ((cx - (size - margin - r))**2 + (cy - (size - margin - r))**2) > r**2
            if not in_corner:
                img.putpixel((x, y), (r_col, g_col, b_col, 255))

    # 文字
    try:
        font_size = int(size * 0.45)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    text = "📚"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text(((size - tw) / 2, (size - th) / 2 - int(size * 0.02)), text, font=font, embedded_color=True)

    path = os.path.join(OUT_DIR, f'icon-{size}x{size}.png')
    img.save(path)
    print(f'Generated {path}')

print('All icons generated.')
