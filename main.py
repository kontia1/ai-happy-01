"""Copy entry.png beside this script into the target output directory."""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
MAX_SOURCE_BYTES = 1048576


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SOURCE_NAME)
    size = os.path.getsize(src)
    if size > MAX_SOURCE_BYTES:
        raise SystemExit(
            f"error: {src} is {size} bytes, exceeds limit of {MAX_SOURCE_BYTES} bytes"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, SOURCE_NAME)
    shutil.copyfile(src, dest)
    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
