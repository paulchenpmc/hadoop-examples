#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None
fileset = set()

for kvp in sys.stdin:
    kvp = kvp.rstrip()
    word,filename = kvp.split('\t')
    if (prev_key is not None) and (word != prev_key):
        print('{}\t{}'.format(prev_key, list(fileset)))
        fileset.clear()
    fileset.add(filename)
    prev_key = word
print('{}\t{}'.format(word, list(fileset)))