#!/usr/bin/env python
#mapper.py

import string
import sys
import random

percent_chance = 0.1

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = ''.join(ch for ch in line if ch.isalnum() or ch == ' ')
    if len(line) == 0:
        continue
    if random.random() < percent_chance:
        print('{}\t{}'.format(line, 1))
