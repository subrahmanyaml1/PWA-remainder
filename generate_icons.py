#!/usr/bin/env python3
"""Generate simple placeholder icons for TaskPulse PWA."""
import struct, zlib, os

def make_png(size, bg=(15,15,15), accent=(200,241,53)):
    """Create a minimal PNG with a colored background and a circle."""
    w = h = size
    raw = []
    for y in range(h):
        row = [0]  # filter type: none
        for x in range(w):
            cx, cy = w // 2, h // 2
            r = w * 0.38
            dot_r = w * 0.14
            dist = ((x - cx)**2 + (y - cy)**2) ** 0.5
            # outer ring
            if abs(dist - r) < w * 0.04:
                row += list(accent) + [255]
            # center dot
            elif dist < dot_r:
                row += list(accent) + [255]
            else:
                row += list(bg) + [255]
        raw.append(bytes(row))

    def chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)

    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
    raw_bytes = b''.join(raw)
    idat = chunk(b'IDAT', zlib.compress(raw_bytes, 9))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

os.makedirs('icons', exist_ok=True)
for size in [192, 512]:
    with open(f'icons/icon-{size}.png', 'wb') as f:
        f.write(make_png(size))
    print(f'Created icons/icon-{size}.png')

print('Icons generated successfully!')
#!/usr/bin/env python3
"""
Generate clean PWA icons for TaskPulse.
Creates:

* icons/icon-192.png
* icons/icon-512.png
  """

import struct
import zlib
import os

def make_png(size, bg=(15, 15, 15), accent=(200, 241, 53)):
"""Create a PNG with a circular accent design."""

```
w = h = size
raw_data = []

for y in range(h):
    row = [0]  # No filter

    for x in range(w):
        cx, cy = w // 2, h // 2
        outer_radius = w * 0.38
        inner_dot = w * 0.14

        dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5

        # Outer ring
        if abs(dist - outer_radius) < w * 0.04:
            row += list(accent) + [255]

        # Center dot
        elif dist < inner_dot:
            row += list(accent) + [255]

        # Background
        else:
            row += list(bg) + [255]

    raw_data.append(bytes(row))

def chunk(tag, data):
    return (
        struct.pack(">I", len(data)) +
        tag +
        data +
        struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)
    )

png_signature = b"\x89PNG\r\n\x1a\n"
ihdr = chunk(b'IHDR', struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
idat = chunk(b'IDAT', zlib.compress(b''.join(raw_data), 9))
iend = chunk(b'IEND', b'')

return png_signature + ihdr + idat + iend
```

def generate_icons():
"""Generate icon files."""

```
output_dir = "icons"
os.makedirs(output_dir, exist_ok=True)

sizes = [192, 512]

for size in sizes:
    file_path = os.path.join(output_dir, f"icon-{size}.png")

    with open(file_path, "wb") as f:
        f.write(make_png(size))

    print(f"✅ Created: {file_path}")

print("\n🎉 All icons generated successfully!")
```

if **name** == "**main**":
generate_icons()
