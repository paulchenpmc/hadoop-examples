#!/usr/bin/env python
#mapper.py

import string
import sys
import os

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = line.replace('\t', ' ')
    line = ''.join(ch for ch in line if ch.isalnum() or ch == ' ')
    if len(line) == 0:
        continue
    filename = os.getenv('map_input_file')
    words = line.split()
    for word in words:
        print('{}\t{}'.format(word, filename))
