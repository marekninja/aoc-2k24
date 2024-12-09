# AoC solution. Day: 7; Part 1
import re
import itertools

with open("./7/inputs.txt", "r") as f:
    pattern = re.compile(r"(\d+)")
    lines = [ pattern.findall(line) for line in f.readlines()]

found_results = []
for line in lines:
    result = int(line[0])
    found = False
    num_spaces = len(line[1:])-1
    all_combinations = list(itertools.product([0,1,2],repeat=num_spaces))

    for comb in all_combinations:
        equation = int(line[1])
        for idx, op in enumerate(comb):
            if op == 0:
                equation += int(line[idx+2])
            elif op == 1:
                equation *= int(line[idx+2])
            else:
                equation = int(str(equation) + line[idx+2])

        if equation == result:
            print('found', comb)
            found_results.append(equation)
            break

print('RESULT', sum(found_results))