"""ai-happy-01 entry: copies the image beside it to /output/entry.png."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(OUTPUT_DIR, "entry.png")
SIZE_CAP = 1048576


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    size = os.path.getsize(SOURCE)
    if size > SIZE_CAP:
        raise SystemExit(f"entry image is {size} bytes, over the cap")
    shutil.copyfile(SOURCE, TARGET)
    print(f"wrote {TARGET} ({size} bytes)")


if __name__ == "__main__":
    main()
