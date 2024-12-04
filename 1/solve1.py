from __future__ import absolute_import
from inputs import left, right

left.sort()
right.sort()

dist = 0

for idx, val in enumerate(left):
    dist += abs(left[idx] - right[idx])
    print(f'{abs(left[idx] - right[idx])=}={abs(left[idx] - right[idx])}')

print(dist)
