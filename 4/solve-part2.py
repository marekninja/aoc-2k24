# AoC solution. Day: 4; Part 2
import numpy as np

example = [
        ['M','*','M'],
        ['*','A','*'],
        ['S','*','S'],
    ]
mask = np.ones_like(example,dtype=bool).flatten()
mask[1::2] = False

combinations = [np.rot90(example,i) for i in range(0,4)]

with open("./4/inputs.txt",'r') as f:
    lines = np.array([list(line.strip()) for line in f.readlines()])

found_c = 0
for i in range(lines.shape[0]-2):
    for j in range(lines.shape[0]-2):
        cut = lines[i:i+3,j:j+3]
        for one_pattern in combinations:
            comparison = np.array(cut == one_pattern)
            check = comparison.flatten()[mask].all()
            found_c += 1 if check else 0 

print('RESULT:',found_c)