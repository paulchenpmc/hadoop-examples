#!/usr/bin/env python
#reducer.py

import string
import sys

prev_ngram = None
count = 0

for line in sys.stdin:
    line = line.rstrip()
    line = line.replace('\t1', '')
    ngram = line.split(',')
    count += 1

    if prev_ngram == None:
        prev_ngram = ngram
        continue
    if prev_ngram == ngram:
        continue
    if prev_ngram != ngram:
        print('{}\t{}'.format(count, '\t'.join(prev_ngram)))
        count = 0
        prev_ngram = ngram
print('{}'.format('\t'.join(ngram)))