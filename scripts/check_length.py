#!/usr/bin/env python3
"""Count only the supplied UTF-8 answer; report both common character measures."""
import argparse
import json
from pathlib import Path


def measure(text):
    return {"words": len(text.split()), "characters": len(text),
            "utf16_code_units": len(text.encode("utf-16-le")) // 2}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--max-words", type=int)
    parser.add_argument("--max-characters", type=int)
    args = parser.parse_args()
    for limit in (args.max_words, args.max_characters):
        if limit is not None and limit < 0:
            parser.error("Limits must be non-negative")
    counts = measure(args.file.read_bytes().decode("utf-8"))
    within = ((args.max_words is None or counts["words"] <= args.max_words)
              and (args.max_characters is None or max(counts["characters"], counts["utf16_code_units"]) <= args.max_characters))
    print(json.dumps({**counts, "within_limits": within}, ensure_ascii=False))
    return 0 if within else 1


if __name__ == "__main__":
    raise SystemExit(main())
