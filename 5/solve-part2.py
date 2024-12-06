# AoC solution. Day: 5; Part 2
import re
with open("./5/inputs.txt", "r") as f:
    definitions, prints = f.read().split("\n\n")

rules = {}
pattern = re.compile(r"^(\d+)\|(\d+)$")
for one in definitions.splitlines():
    rule_def = pattern.fullmatch(one)
    first, second = rule_def.groups()
    rules[first] = prev.union({second}) if (prev := rules.get(first)) else {second}

print(rules)

def solve_elem(elements:list[int],rule:set) -> bool:
    if len(elements) == 0:
        print("success")
        return True
    if rule is None:
        print("empty rule")
        return False
    elem = elements.pop(0)
    print("elem",elem)
    if elem not in rule:
        print(elem,"not in", rule)
        return False
    return solve_elem(elements,rule)
    
succesfull_prints = []
wrong_prints = []
middle_count = 0
wrong_middle_count = 0
for one in prints.splitlines():
    elements = one.split(',')
    print("CHECK",elements)
    out = True
    to_wrong = False
    for idx in range(len(elements)):
        wip_elems = elements.copy()
        is_success = False
        to_switch = idx
        while not is_success:
            elem = elements[to_switch]
            print("CHECK",elem)
            is_success = solve_elem(wip_elems.copy()[idx+1:],rules.get(elem))
            if not is_success:
                to_wrong = True
                to_switch += 1
                overflow = elements[to_switch]
                wip_elems[idx] = overflow
                wip_elems[to_switch] = elem
        elements = wip_elems

    if not to_wrong:
        print("SUCCESS",elements)
        middle_count += int(elements[len(elements)//2])
        succesfull_prints.append(elements)
    else:
        print("FAIL", elements)
        wrong_prints.append(elements)
        wrong_middle_count += int(elements[len(elements)//2])

print(f'{succesfull_prints=}')
print(f'{wrong_prints=}')
print(f"{middle_count=}")
print(f"{wrong_middle_count=}")
    