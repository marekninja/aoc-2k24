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
    for i in ["","_small"]:
        with open(dir / f"inputs{i}.txt", "w") as f:
            f.write("")

    solve_content =f"""

with open("./{args.day}/inputs.txt", "r") as f:
    lines = f.readlines()
"""
    for i in [1,2]:
        with open(dir / f"solve-part{i}.py", "w") as f:
            f.write(contents + f"; Part {i}" + solve_content)