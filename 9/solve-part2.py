# AoC solution. Day: 9; Part 2

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

    return memory, disk_size, val//2

def search_for_block_reverse(memory, accepted_value) -> tuple[int,int]:
    first_idx = None
    last_idx = None
    block_complete = None
    block_val = None
    for idx in range(len(memory)-1, -1,-1):
            if memory[idx] == accepted_value:
                if block_val != memory[idx]:
                    block_val = memory[idx]
                    last_idx = idx

                if idx - 1 >= 0:
                    first_idx = idx
                    block_complete = True if memory[idx -1] != block_val else False
        
            if block_complete:
                return first_idx, last_idx
            
    return None, None
            
def search_for_leftmost_empty(memory, end_idx, target_len) -> tuple[int,int]:
    first_idx = None
    last_idx = None
    block_complete = None
    block_val = None
    if target_len is None:
        return None, None
    for idx in range(end_idx+1):
            if memory[idx] == '.':
                if block_val != memory[idx]:
                    block_val = memory[idx]
                    first_idx = idx

                if idx + 1 < end_idx:
                    last_idx = idx
                    block_complete = True if memory[idx +1] != block_val else False
            else:
                block_val = None
                block_complete = False
        
            if block_complete and (last_idx - first_idx + 1) >= target_len:
                return first_idx, last_idx
    return None, None


memory, disk_size, biggest_val = create_mem(line)
for accepted_idx in range(biggest_val, -1, -1):
    start_idx, end_idx = search_for_block_reverse(memory, str(accepted_idx))
    target_len = end_idx - start_idx +1 if start_idx and end_idx else None
    empty_start_idx, empty_end_idx = search_for_leftmost_empty(memory,end_idx,target_len)

    if start_idx and end_idx and empty_end_idx and empty_start_idx:
        for ref_empty, ref_idx in zip(range(empty_start_idx, empty_end_idx+1), range(start_idx,end_idx+1)) :
            memory[ref_empty] = memory[ref_idx]
            memory[ref_idx] = '.'

print("".join(memory))
checksum = 0
for idx, val in enumerate(memory):
    if val != '.':
        checksum += (idx * int(val))

print(checksum)