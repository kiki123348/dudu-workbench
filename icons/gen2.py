from PIL import Image, ImageDraw, ImageFont
import os, math

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
OUT_DIR = '/workspace/dudu-workbench/icons'

# 渐变蓝色
for size in SIZES:
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    
    # 画圆角矩形背景
    margin = int(size * 0.06)
    r = int(size * 0.22)
    
    # 渐变背景
    for y in range(size):
        for x in range(size):
            # 圆角裁剪
            dx = 0
            if x < margin + r and y < margin + r:
                dx = ((x - margin - r)**2 + (y - margin - r)**2) - r**2
            elif x > size - margin - r and y < margin + r:
                dx = ((x - (size - margin - r))**2 + (y - margin - r)**2) - r**2
            elif x < margin + r and y > size - margin - r:
                dx = ((x - margin - r)**2 + (y - (size - margin - r))**2) - r**2
            elif x > size - margin - r and y > size - margin - r:
                dx = ((x - (size - margin - r))**2 + (y - (size - margin - r))**2) - r**2
            
            if dx > 0:
                continue
            
            # 渐变
            ratio = y / size
            r_col = int(74 + ratio * (107 - 74))
            g_col = int(95 + ratio * (133 - 95))
            b_col = int(193 + ratio * (214 - 193))
            img.putpixel((x, y), (r_col, g_col, b_col, 255))
    
    draw = ImageDraw.Draw(img)
    
    # 画一个书本图标（用几何图形）
    cx, cy = size // 2, size // 2
    book_w = int(size * 0.42)
    book_h = int(size * 0.32)
    
    # 书本左页
    lx = cx - book_w // 2
    ly = cy - book_h // 2
    draw.rounded_rectangle([lx, ly, cx - 2, ly + book_h], radius=4, fill=(255,255,255,230))
    # 书本右页
    draw.rounded_rectangle([cx + 2, ly, lx + book_w, ly + book_h], radius=4, fill=(255,255,255,230))
    # 书脊
    draw.rectangle([cx - 2, ly, cx + 2, ly + book_h], fill=(255,255,255,255))
    # 书页线条
    line_y1 = ly + int(book_h * 0.35)
    line_y2 = ly + int(book_h * 0.65)
    draw.line([(lx + 6, line_y1), (cx - 6, line_y1)], fill=(74,95,193,120), width=2)
    draw.line([(cx + 6, line_y1), (lx + book_w - 6, line_y1)], fill=(74,95,193,120), width=2)
    draw.line([(lx + 6, line_y2), (cx - 6, line_y2)], fill=(74,95,193,120), width=2)
    draw.line([(cx + 6, line_y2), (lx + book_w - 6, line_y2)], fill=(74,95,193,120), width=2)
    
    # 顶部小叶子装饰
    leaf_y = ly - int(size * 0.08)
    leaf_size = int(size * 0.08)
    draw.ellipse([cx - leaf_size, leaf_y - leaf_size, cx + leaf_size, leaf_y + leaf_size], fill=(76,175,80,230))
    draw.ellipse([cx - leaf_size//2, leaf_y - leaf_size//2, cx + leaf_size//2, leaf_y + leaf_size//2], fill=(74,95,193,255))
    
    path = os.path.join(OUT_DIR, f'icon-{size}x{size}.png')
    img.save(path)
    print(f'Generated {path}')

print('Done!')
