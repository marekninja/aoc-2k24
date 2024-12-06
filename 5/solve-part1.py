# AoC solution. Day: 5; Part 1
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
middle_count = 0
for one in prints.splitlines():
    elements = one.split(',')
    print("CHECK",elements)
    out = True
    for idx in range(len(elements)):
        elem = elements[idx]
        print("CHECK",elem)
        is_success = solve_elem(elements.copy()[idx+1:],rules.get(elem))
        print(f"{is_success=}")
        if not is_success:
            out = False
            break

    if out:
        print("SUCCESS",elements)
        middle_count += int(elements[len(elements)//2])
        succesfull_prints.append(elements)

print(succesfull_prints)
print(f"{middle_count=}")
    