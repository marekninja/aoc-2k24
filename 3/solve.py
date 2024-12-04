#AoC solution. Day: {args.day}
from __future__ import absolute_import

with open("./3/inputs.txt", "r") as f:
    inputs = f.read()

import re
sum_all = 0
discard = False
for one in re.finditer(r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))",inputs):
    # print(one.groups())
    do, dont, mul, first, second = one.groups()
    if dont:
        discard = True
        continue
    elif do:
        discard = False
        continue
    
    if not discard:
        print("accept:  ", mul)
        sum_all += int(first) * int(second)
    else:
        print("discarding:  ", mul)
    # break

print("RESULT:", sum_all)

