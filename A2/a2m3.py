#!/usr/bin/env python
#mapper.py

import sys
import itertools

for line in sys.stdin:
    # Parse input
    line = line.strip()
    if len(line) == 0:
        continue
    items = [int(i) for i in line.split()]
    # Mapper logic
    all_pairs = list(itertools.permutations(items, 2))
    # Emit
    for pair in all_pairs:
        key = '{},{}'.format(pair[0], pair[1])
        print('{}\t{}'.format(key, 1)
