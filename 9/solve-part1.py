# AoC solution. Day: 9; Part 1

with open("./9/inputs.txt", "r") as f:
    line = list(f.read().strip())

def create_mem(line:list[str]) -> list[str]:
    memory = []
    disk_size = 0
    is_empty = False
    for val,count in enumerate(line):
        
        for i in range(int(count)):
            if not is_empty:
                disk_size +=1
            memory.append(str(val//2) if not is_empty else '.')
        
        is_empty = False if is_empty else True

    return memory, disk_size

def find_non_empty_idx(memory: list[str], last_idx) -> int:
    for idx in range(last_idx,-1,-1):
        if memory[idx] != '.':
            return idx


memory, disk_size = create_mem(line)
last_idx = len(memory)-1
for idx in range(disk_size):
    if memory[idx] == '.':
        last_idx = find_non_empty_idx(memory,last_idx)
        memory[idx] = memory[last_idx]
        memory[last_idx] = '.'

checksum = 0
for idx, val in enumerate(memory):
    if idx < disk_size:
        checksum += (idx * int(val))
    else:
        break

print(checksum)
# print(memory)s