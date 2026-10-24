"""スクリーンショット（PNG）の矩形の中で、いちばん暗い文字色と背景色を拾って WCAG のコントラスト比を出す。
使い方: python3 png_contrast.py <png> <x0> <y0> <x1> <y1>   （座標は元画像のピクセル）
標準ライブラリだけで動く（8bit・非インターレースの RGB / RGBA の PNG のみ）。"""
import sys, zlib, struct
from collections import Counter

def read_png(path):
    data = open(path, 'rb').read()
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    pos, idat, w = 8, b'', None
    while pos < len(data):
        ln, = struct.unpack('>I', data[pos:pos+4]); typ = data[pos+4:pos+8]; body = data[pos+8:pos+8+ln]; pos += 12 + ln
        if typ == b'IHDR':
            w, h, bd, ct, _, _, il = struct.unpack('>IIBBBBB', body)
            assert bd == 8 and il == 0 and ct in (2, 6), (bd, ct, il)
            bpp = 3 if ct == 2 else 4
        elif typ == b'IDAT':
            idat += body
    raw = zlib.decompress(idat); stride = w * bpp; rows = []; prev = bytearray(stride); i = 0
    for _ in range(h):
        f = raw[i]; line = bytearray(raw[i+1:i+1+stride]); i += 1 + stride
        for x in range(stride):
            a = line[x-bpp] if x >= bpp else 0; b = prev[x]; c = prev[x-bpp] if x >= bpp else 0
            if f == 1: line[x] = (line[x] + a) & 255
            elif f == 2: line[x] = (line[x] + b) & 255
            elif f == 3: line[x] = (line[x] + (a + b) // 2) & 255
            elif f == 4:
                p = a + b - c; pa, pb, pc = abs(p-a), abs(p-b), abs(p-c)
                line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line); prev = line
    return w, h, bpp, rows

def lum(rgb):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

if __name__ == '__main__':
    path, x0, y0, x1, y1 = sys.argv[1], *map(int, sys.argv[2:6])
    w, h, bpp, rows = read_png(path)
    cnt = Counter()
    for y in range(y0, y1):
        r = rows[y]
        for x in range(x0, x1):
            cnt[tuple(r[x*bpp:x*bpp+3])] += 1
    bg = cnt.most_common(1)[0][0]
    # 文字色: 背景からいちばん離れた色のうち、5 画素以上あるもの（アンチエイリアスの中間色を除く）
    fg = max((c for c, n in cnt.items() if n >= 5), key=lambda c: ratio(c, bg))
    print(f'size={w}x{h} bg=#{bytes(bg).hex()} fg=#{bytes(fg).hex()} contrast={ratio(fg, bg):.2f}:1')
