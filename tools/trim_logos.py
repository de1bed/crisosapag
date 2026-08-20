#!/usr/bin/env python3
"""
Trim the dead margin around each logo.

The logos were extracted from the presentation and every one carries a
different amount of empty canvas around the artwork. On a logo wall that
reads as random sizing — one wordmark tiny, the next enormous — no matter
what CSS does, because CSS can only fit the canvas, not the ink.

This crops each PNG to its actual ink and leaves a small even margin, so
`object-fit: contain` then gives every logo the same optical weight.

    python3 tools/trim_logos.py            # trims assets/logos/*.png

Idempotent: an already-trimmed logo is left alone.
"""
import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGOS = ROOT / "assets" / "logos"
MARGIN = 0.02          # breathing room, as a fraction of the cropped side
ALPHA_MIN = 12         # below this a pixel counts as empty
WHITE_MIN = 246        # for logos with no transparency, near-white counts as empty


def ink_box(im):
    """Bounding box of the artwork, by alpha when present and by ink when not."""
    alpha = im.getchannel("A")
    if alpha.getextrema()[0] < 255:                    # real transparency
        return alpha.point(lambda v: 255 if v > ALPHA_MIN else 0).getbbox()
    grey = im.convert("L")
    return grey.point(lambda v: 0 if v >= WHITE_MIN else 255).getbbox()


def main():
    changed = 0
    for p in sorted(LOGOS.glob("*.png")):
        im = Image.open(p).convert("RGBA")
        box = ink_box(im)
        if not box:
            print(f"  skip  {p.name} (empty)")
            continue
        l, t, r, b = box
        if (l, t, r, b) == (0, 0, im.width, im.height):
            print(f"  ok    {p.name} (already tight)")
            continue
        pad = round(max(r - l, b - t) * MARGIN)
        crop = im.crop((max(0, l - pad), max(0, t - pad),
                        min(im.width, r + pad), min(im.height, b + pad)))
        crop.save(p, optimize=True)
        print(f"  trim  {p.name}  {im.width}x{im.height} → {crop.width}x{crop.height}")
        changed += 1
    print(f"\n{changed} logos trimmed.")


if __name__ == "__main__":
    sys.exit(main())
