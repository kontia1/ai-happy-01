"""ai-happy-01 entry.

The image beside this program is the entry: one picture made to make the
judge happy. This program copies those exact bytes to /output/entry.png,
and does nothing else, so both of the grader's runs write the same file.

Run it outside the grader with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUTPUT_DIR, "entry.png")
SIZE_CAP = 1048576


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    size = os.path.getsize(SOURCE)
    if size > SIZE_CAP:
        raise SystemExit(f"entry image is {size} bytes, over the {SIZE_CAP} cap")
    shutil.copyfile(SOURCE, TARGET)
    print(f"wrote {TARGET} ({size} bytes)")


if __name__ == "__main__":
    main()
