# AoC solution. Day: 4; Part 1
import re
import numpy as np

with open("./4/inputs.txt", "r") as f:
    lines = np.array([list(line.strip()) for line in f.readlines()])

xmas = "XMAS"

def search_in_line(line: str, pattern: str) -> int:
    groups = re.findall(pattern,line)
    return len(groups)

found_c = 0

for processed_lines in [lines, lines.T]:
    for idx, line in enumerate(processed_lines):
        line = "".join(line)
        # in line
        found_c += search_in_line(line,xmas)
        found_c += search_in_line(line,xmas[::-1])

print('in lines and cols', found_c)

for master in [lines, np.fliplr(lines)]:
    processed_lines = master
    min_offset = -processed_lines.shape[1]
    max_offset = processed_lines.shape[1]
    for offset in range(min_offset, max_offset):
        line = "".join(processed_lines.diagonal(offset))
        found_c += search_in_line(line,xmas)
        found_c += search_in_line(line,xmas[::-1])


print("RESULT:",found_c)