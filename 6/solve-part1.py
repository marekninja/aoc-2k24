# AoC solution. Day: 6; Part 1

with open("./6/inputs.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

pos_x = 0
pos_y = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "^":
            pos_x, pos_y = i , j

unique_positions = {(pos_x,pos_y)}
is_end = False
# up, down, left, right
direction = 'up'
step_count = 0
while not is_end:
    try:

        if direction == 'up':
            if lines[pos_x-1][pos_y] != "#":
                pos_x -= 1
                unique_positions.add((pos_x,pos_y))
            else:
                direction = 'right'
        if direction == 'down':
            if lines[pos_x+1][pos_y] != "#":
                pos_x += 1
                unique_positions.add((pos_x,pos_y))
            else:
                direction = "left"
        if direction == 'left':
            if lines[pos_x][pos_y-1] != '#':
                pos_y -= 1
                unique_positions.add((pos_x,pos_y))
            else:
                direction = 'up'
        if direction == 'right':
            if lines[pos_x][pos_y+1] != '#':
                pos_y += 1
                unique_positions.add((pos_x,pos_y))
            else:
                direction = 'down'

        lines[pos_x][pos_y] = 'X'
        print(step_count)
        # print('\n'.join(' '.join(map(str,sl)) for sl in lines))
        step_count += 1
    except:
        is_end = True
    # if pos_x == 0 or pos_x == len(lines[0]) or pos_y == 0 or pos_y == len(lines):
    #     is_end = True
            
print(len(unique_positions))