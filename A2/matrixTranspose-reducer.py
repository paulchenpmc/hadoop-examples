#!/usr/bin/env python
#reducer.py

import string
import sys

for kvp in sys.stdin:
    kvp = kvp.strip()
    row,col,val = kvp.split('\t')
    print('{}\t{}\t{}'.format(row, col, val))