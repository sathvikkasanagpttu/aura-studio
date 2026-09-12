"""Build the standalone AURA Studio HTML bundle from src/."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"
OUTPUT_FILE = BASE_DIR / "index.html"

FILES = {
    "/* CSS_PLACEHOLDER */": "styles.css",
    "/* AUDIO_JS */": "audio.js",
    "/* PARTICLES_JS */": "particles.js",
    "/* CALIBRATION_JS */": "calibration.js",
    "/* SHAPES_JS */": "shapes.js",
    "/* GESTURES_JS */": "gestures.js",
    "/* APP_JS */": "app.js",
}


def build() -> None:
    template = SRC_DIR / "index.html"
    if not template.exists():
        raise FileNotFoundError(f"Missing template: {template}")

    content = template.read_text(encoding="utf-8")

    for placeholder, filename in FILES.items():
        source = SRC_DIR / filename
        if not source.exists():
            raise FileNotFoundError(f"Missing source file: {source}")
        content = content.replace(placeholder, source.read_text(encoding="utf-8"))

    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"Built production bundle: {OUTPUT_FILE}")
    print(f"Bundle size: {OUTPUT_FILE.stat().st_size:,} bytes")


if __name__ == "__main__":
    build()
