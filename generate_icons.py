"""Run once to generate PNG icons from icon.svg for PWA support."""
import subprocess, sys, pathlib

def try_cairosvg():
    try:
        import cairosvg
        svg = pathlib.Path("static/icon.svg").read_bytes()
        for size in (192, 512):
            cairosvg.svg2png(bytestring=svg, write_to=f"static/icon-{size}.png",
                             output_width=size, output_height=size)
            print(f"Generated static/icon-{size}.png")
        return True
    except ImportError:
        return False

def try_inkscape():
    svg = "static/icon.svg"
    for size in (192, 512):
        out = f"static/icon-{size}.png"
        r = subprocess.run(["inkscape", "--export-type=png",
                            f"--export-width={size}", f"--export-height={size}",
                            f"--export-filename={out}", svg], capture_output=True)
        if r.returncode != 0:
            return False
        print(f"Generated {out}")
    return True

if not try_cairosvg() and not try_inkscape():
    print("Install cairosvg (pip install cairosvg) or Inkscape, then re-run.")
    sys.exit(1)
