#!/usr/bin/env python
#reducer.py

import sys
from collections import defaultdict
keydict = defaultdict(int)
prevk = None

for kvp in sys.stdin:
    kvp = kvp.strip()
    key1, key2, _ = kvp.split('\t')
    pair = '{},{}'.format(key1, key2)
    # Track all pairs until key1 changes
    if key1 != prevk and prevk is not None:
        N = sum(keydict.values())
        for key in keydict:
            probability = keydict[key] / float(N)
            pair_output = '{},{}'.format(key.split(',')[1], key.split(',')[0]) # Flip key order for output
            print('{}\t{}'.format(pair_output, probability))
        keydict.clear()
    keydict[pair] += 1
    prevk = key1

# Emit last key group
N = sum(keydict.values())
for key in keydict:
    probability = keydict[key] / float(N)
    pair_output = '{},{}'.format(key.split(',')[1], key.split(',')[0]) # Flip key order for output
    print('{}\t{}'.format(pair_output, probability))
keydict.clear()