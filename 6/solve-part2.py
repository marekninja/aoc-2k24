# AoC solution. Day: 6; Part 2

with open("./6/inputs.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

pos_x = 0
pos_y = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "^":
            pos_x, pos_y = i , j


# up, right, down, left
# (move x, move y, character, next direction)
directions = [(-1,0,'|',1),(0,1,'-',2),(1,0,'|',3),(0,-1,'-',0)]

def draw_map(pref, mymap):
        print(pref)
        print('\n'.join(' '.join(map(str,sl)) for sl in mymap))

def make_move(lines, posx, posy, direction):
    # is within bounds
    if 0 <= posx + direction[0] < len(lines) and 0 <= posy + direction[1]< len(lines[0]):
        if lines[posx + direction[0]][posy + direction[1]] != '#':
            posx += direction[0]
            posy += direction[1]
        else:
            direction = directions[direction[3]]
        return lines, posx, posy, direction, False
    else:
        return lines, posx, posy, direction, True
    

def solve_map(lines, posx, posy, direction, reference_positions=None):
    # get unique positions
    positions = set()
    end = False
    similar_path = True
    while not end:
        # draw_map("*",lines)
        lines, posx, posy, direction, end = make_move(lines, posx, posy, direction)
        position = (posx,posy,direction)
        
        if position in positions and not end:
            print("LOOP DETECTED")
            return set(), True
        else:
            positions.add(position)

    return positions, False

print(f'start {pos_x=},{pos_y=}')
# 1. solve basic map
positions, _ = solve_map(lines.copy(),pos_x, pos_y, directions[0])
unique_positions = { (one[0], one[1]) for one in positions}
print(len(unique_positions))

# 2. search for loops
# approach by placing obstacles on empty blocks in route and detect if loop happens
loop_count = 0
marks = [[el for el in line]for line in lines]
for idx, pos in enumerate(unique_positions):
    i = pos[0]
    j = pos[1]
    if lines[i][j] == '.':
            lines_c = [[el for el in line]for line in lines]
            lines_c[i][j] = '#'
            _,loop_found = solve_map(lines_c, pos_x, pos_y, directions[0], positions)
            if loop_found:
                print('FOUND IT', pos)
                loop_count += 1
                marks[i][j] = "O"

draw_map("LOOP MARKS:",marks)
print('is loop:', loop_count)