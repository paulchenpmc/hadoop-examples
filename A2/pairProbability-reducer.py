#!/usr/bin/env python
#reducer.py

# Calculates Normalized Word Co-occurence Matrix

import sys
prevk1      = None
prevk2      = '-' # '-' comes before all alphanumeric chars in the ascii table
DENOMINATOR = 0
PAIR_COUNT  = 0

for kvp in sys.stdin:
    kvp = kvp.strip()
    key1, key2, _ = kvp.split('\t')
    pair = '{},{}'.format(key1, key2)
    # Track all pairs until key1 changes
    if key2 != prevk2 and prevk2 is not '-':
        probability = PAIR_COUNT / float(DENOMINATOR)
        pair_output = '{},{}'.format(prevk1, prevk2)
        print('{}\t{}'.format(pair_output, probability))
        PAIR_COUNT = 0
    if key2 == '-' and prevk2 != '-':
        DENOMINATOR = 0
    if key2 == '-':
        DENOMINATOR += 1
    else:
        PAIR_COUNT += 1
    prevk1 = key1
    prevk2 = key2


# Emit last key group
probability = PAIR_COUNT / float(DENOMINATOR)
pair_output = '{},{}'.format(key1, key2)
print('{}\t{}'.format(pair_output, probability))
