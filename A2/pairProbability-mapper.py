#!/usr/bin/env python
#mapper.py

# Calculates Normalized Word Co-occurence Matrix

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
        key = '{}\t{}'.format(pair[0], pair[1]) # Make 2 part key
        print('{}\t-\t1'.format(pair[0])) # Emit just the first key to count denominator, '-' is to guarantee first place in sorting order
        print('{}\t1'.format(key)) # Emit both grocery items as 2 part key
