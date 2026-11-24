#!/usr/bin/env python3
"""Two Lines of Morning Light — make.fun entry.
Writes the two-line micro poem to /output/entry.txt.
"""
import os

ENTRY = "Morning light through the blinds\ndrew stripes on the floor, and the room was a tiger for a minute."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
