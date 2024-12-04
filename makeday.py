import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Make day structure for AoC')
parser.add_argument('-d', '--day', help='Day number to create directory for', required=True,type=int)
args = parser.parse_args()

if __name__ == "__main__":
    dir = Path("./") / str(args.day)
    os.mkdir(dir)
    with open(dir / "inputs.py", "w") as f:
        f.write("")

    with open(dir / "solve.py", "w") as f:
        contents = """#AoC solution. Day: {args.day}
from __future__ import absolute_import
from inputs import
"""
        f.write(contents)