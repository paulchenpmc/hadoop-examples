#!/usr/bin/env python
#reducer.py

import string
import sys

for line in sys.stdin:
    line = line.rstrip()
    line,count = line.split('\t')
    print('{}'.format(line))