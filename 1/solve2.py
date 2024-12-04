from __future__ import absolute_import
from inputs import left, right

counts = {}
for i in right:
    counts[i] = counts.get(i) + 1 if counts.get(i) else 1

print(counts)

sim_score = 0
for idx, val in enumerate(left):
    sim_score += count * val if (count := counts.get(val)) else 0
    print(sim_score, counts.get(val), val)

print(sim_score)
