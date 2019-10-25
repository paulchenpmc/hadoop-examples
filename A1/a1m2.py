#!/usr/bin/env python
#mapper.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = ''.join(ch for ch in line if ch.isalnum() or ch == ' ')
    if len(line) == 0:
        continue
    words = line.split()
    for i in range(len(words) - 1): # -1 to ensure no out of bounds access on words list
        print('{},{}\t1'.format(words[i], words[i + 1]))
