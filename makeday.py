import os
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Make day structure for AoC')
parser.add_argument('-d', '--day', help='Day number to create directory for', required=True,type=int)
args = parser.parse_args()

if __name__ == "__main__":
    dir = Path("./") / str(args.day)
    contents = f"# AoC solution. Day: {args.day}"

    os.mkdir(dir)
    with open(dir / "inputs.txt", "w") as f:
        f.write("")

    for i in [1,2]:
        with open(dir / f"solve-part{i}.py", "w") as f:
            f.write(contents + f"; Part {i}")