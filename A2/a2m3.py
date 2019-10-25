#!/usr/bin/env python
#mapper.py

import sys

for line in sys.stdin:
    # Parse input
    line = line.strip()
    if len(line) == 0:
        continue
    items = [int(i) for i in line.split()]
    # Mapper logic

    # Emit
    print('{}\t{}'.format(1, 1))
