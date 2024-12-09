# AoC solution. Day: 8; Part 1
import itertools
import copy

with open("./8/inputs.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]
draw = copy.deepcopy(lines)
antinodes = set()
antenas_combinations = set()
locations = {}
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            print(f'{i=}, {j=}, {lines[i][j]=}')
            # save location
            previous = locations.get(lines[i][j])
            locations[lines[i][j]] = previous+ [(i,j)] if previous else [(i,j)]

            # insert antinodes
            all_combinations = list(itertools.combinations(locations[lines[i][j]],r=2))
            for combination in all_combinations:
                # if combination[0] == combination[1]:
                #     print('skip')
                #     continue
                if combination in antenas_combinations:
                    print('combination used up')
                    continue
                x1,y1 = combination[0]
                x2,y2 = combination[1]
                y_dist = y1 - y2
                x_dist = x1 - x2

                for x,y,dir in [(x1,y1,1),(x2,y2,-1)]:
                    anti_x, anti_y = x+x_dist*dir, y+y_dist*dir
                    if 0 <= anti_x < len(lines) and 0<=anti_y < len(lines[0]):
                        if draw[anti_x][anti_y] == '#':
                            print('CLASH')
                        else:
                            print(f'draw:    {combination=}')
                            draw[anti_x][anti_y] = '#'
                        antinodes.add((anti_x, anti_y))
                        antenas_combinations.add(combination)

                # print('*')
                # print('\n'.join(' '.join(map(str,sl)) for sl in lines))
                # print(antinodes)
                # exit()
                # print('comb',combination)

print('\n'.join(' '.join(map(str,sl)) for sl in draw))
print(antinodes)
print(len(antinodes))