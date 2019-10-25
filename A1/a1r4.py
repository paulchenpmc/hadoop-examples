#!/usr/bin/env python
#reducer.py

import string
import sys

prev_key = None

for word in sys.stdin:
    word = word.rstrip()
    bin,word,garbage = word.split('\t')
    print('{}'.format(word))