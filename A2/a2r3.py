#!/usr/bin/env python
#reducer.py

import sys
prevk = None

for kvp in sys.stdin:
    kvp = kvp.strip()
    pair, _ = kvp.split('\t')
    key1 = pair.split(',')[0]
    # Track all pairs until key1 changes
    # print('{}\t{}'.format(1, 1))