#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    # Clean input
    line = line.strip()
    line = line.lower()
    line = line.replace('\t', ' ')
    # line = ''.join(ch for ch in line if ch.isalnum() or ch == ' ')
    if len(line) == 0:
        continue
    # Mapper logic
    row,col,val = line.split(',')
    # Emit
    print('{}\t{}\t{}'.format(col, row, val))
