"""AoC solution. Day: 2"""
from __future__ import absolute_import
from inputs2 import rows

def problem_dampener(row: list[int]) -> bool:
    new_rows = []
    for idx, _ in enumerate(row):
        new_row = row.copy()
        new_row.pop(idx)
        new_rows.append(new_row)
    
    return new_rows
    

def is_safe(row: list[int]) -> bool:
    first_diff = row[0] - row[1]
    is_asc = True if first_diff < 0 else False
    print(row, 'ascending' if is_asc else 'descending')
    for idx in range(len(row)-1):
        diff = row[idx] - row[idx+1]
        print(row[idx], row[idx+1], diff)
        
        if abs(diff) < 1 or abs(diff) > 3:
            print("wrong steps")
            return False
        
        if (is_asc and diff > 0) or (not is_asc and diff < 0):
            print("not all increasing/decreasing")
            return False
        
    print("is safe")
    return True
            
num_safe = 0
num_corrected = 0
safe_rows = []
corrected_rows = []
for row in rows:
    if is_safe(row):
        safe_rows.append(row)
        num_safe += 1
    else:
        print("not safe, creating new")
        new_rows = problem_dampener(row)
        for new_row in new_rows:
            print("new row", new_row)
            if is_safe(new_row):
                corrected_rows.append((row, new_row))
                num_safe += 1
                num_corrected += 1
                break

import json
with open('./2/safe_rows.json','w') as f:
    json.dump(corrected_rows,f)

print("RESULT:",num_safe)
print("RESULT CORRECTED:",num_corrected)
