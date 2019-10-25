#!/usr/bin/env python
#mapper.py

# $HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar -jobconf mapred.reduce.tasks=4 -jobconf stream.num.map.output.key.fields=2 -jobconf num.key.fields.for.partition=1 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -input /user/shakespeare1.txt -output /output4/ -file a1m4.py -file a1r4.py -mapper a1m4.py -reducer a1r4.py

# A - E : 1
# F - L : 2
# M - S : 3
# T - Z : 4
# 0 - 9 : 5

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    line = line.replace('\t', ' ')
    line = ''.join(ch for ch in line if ch.isalnum() or ch == ' ')
    if len(line) == 0:
        continue
    words = line.split()
    for word in words:
        first_letter = word[0]
        if first_letter >= 'a' and first_letter <= 'e':
            bin = 1
        elif first_letter >= 'f' and first_letter <= 'l':
            bin = 2
        elif first_letter >= 'm' and first_letter <= 's':
            bin = 3
        elif first_letter >= 't' and first_letter <= 'z':
            bin = 4
        else:
            bin = 5
        print('{}\t{}\t{}'.format(bin, word, None))
