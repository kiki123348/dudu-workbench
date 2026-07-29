from PIL import Image, ImageDraw
import os

SIZES = [72, 96, 128, 144, 152, 192, 384, 512]
OUT_DIR = '/workspace/dudu-workbench/icons'

for size in SIZES:
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 圆角半径 (iOS 标准)
    r = int(size * 0.2237)  # iOS 圆角比例
    
    # 渐变背景 - 从左上到右下的蓝色渐变
    for y in range(size):
        for x in range(size):
            # 圆角裁剪
            dx = 0
            if x < r and y < r:
                dx = (x - r)**2 + (y - r)**2 - r**2
            elif x > size - 1 - r and y < r:
                dx = (x - (size - 1 - r))**2 + (y - r)**2 - r**2
            elif x < r and y > size - 1 - r:
                dx = (x - r)**2 + (y - (size - 1 - r))**2 - r**2
            elif x > size - 1 - r and y > size - 1 - r:
                dx = (x - (size - 1 - r))**2 + (y - (size - 1 - r))**2 - r**2
            
            if dx > 0:
                continue
            
            # 对角线渐变
            t = (x + y) / (2 * size)
            r_col = int(58 + t * (30))
            g_col = int(81 + t * (40))
            b_col = int(181 + t * (25))
            img.putpixel((x, y), (r_col, g_col, b_col, 255))
    
    # 书本图标
    cx, cy = size // 2, size // 2
    
    # 书本尺寸
    bw = int(size * 0.38)
    bh = int(size * 0.30)
    
    # 左页（白色半透明）
    lx = cx - bw // 2
    ly = cy - bh // 2
    rx = cx - 1
    
    # 左页
    draw.rounded_rectangle([lx, ly, rx, ly + bh], radius=max(2, size//40), fill=(255,255,255,245))
    # 右页
    draw.rounded_rectangle([cx + 1, ly, lx + bw, ly + bh], radius=max(2, size//40), fill=(255,255,255,245))
    # 书脊
    draw.rectangle([cx - 1, ly, cx + 1, ly + bh], fill=(255,255,255,255))
    
    # 书页横线
    line_w = int(bw * 0.28)
    line_y1 = ly + int(bh * 0.38)
    line_y2 = ly + int(bh * 0.62)
    line_thick = max(1, size // 80)
    
    # 左页线条
    draw.line([(lx + 5, line_y1), (rx - 5, line_y1)], fill=(74,95,193,100), width=line_thick)
    draw.line([(lx + 5, line_y2), (rx - 5, line_y2)], fill=(74,95,193,100), width=line_thick)
    # 右页线条
    draw.line([(cx + 6, line_y1), (lx + bw - 5, line_y1)], fill=(74,95,193,100), width=line_thick)
    draw.line([(cx + 6, line_y2), (lx + bw - 5, line_y2)], fill=(74,95,193,100), width=line_thick)
    
    # 顶部小绿叶装饰
    leaf_r = int(size * 0.06)
    leaf_cx = cx
    leaf_cy = ly - int(size * 0.06)
    draw.ellipse([leaf_cx - leaf_r, leaf_cy - leaf_r, leaf_cx + leaf_r, leaf_cy + leaf_r], fill=(76,175,80,240))
    
    path = os.path.join(OUT_DIR, f'icon-{size}x{size}.png')
    img.save(path)
    print(f'Generated {path}')

print('All icons done!')
