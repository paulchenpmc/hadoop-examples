#!/usr/bin/env python
#reducer.py

import sys

MAXVAL = 9223372036854775807
nodedict = {}
prevsource = None
prev_adjlist = None
prev_sourceDist = MAXVAL
prev_color = None
prev_parent = 'null'
last_emitted_black = False

def emit(source, adjlist, sourceDist, color, parent):
    if adjlist:
        adjlist = ','.join([str(s) for s in adjlist])
    print('{}\t{}|{}|{}|{}'.format(source, adjlist, sourceDist, color, parent))

for line in sys.stdin:
    # Parse input
    line = line.strip()
    if len(line) == 0:
        continue
    source,vals = line.split('\t')
    adjlist,sourceDist,color,parent = vals.split('|')
    source      = int(source)
    if adjlist == 'None':
        adjlist = None
    else:
        adjlist = [int(i) for i in adjlist.split(',')]
    if sourceDist == 'Integer.MAX_VALUE':
        sourceDist = MAXVAL
    else:
        sourceDist = int(sourceDist)

    # Reducer logic
    # Goal: Figure out the distance of each node from the source.

    # Emit last key group on new key
    if (prevsource is not None) and (prevsource != source):
        emit(prevsource, prev_adjlist, prev_sourceDist, prev_color, prev_parent)
        prev_adjlist = None
        prev_sourceDist = MAXVAL
        prev_color = None
        prev_parent = 'null'

    # Combine/aggregate node information
    if color == 'BLACK':
        prev_adjlist = adjlist
        prev_sourceDist = sourceDist
        prev_color = color
        prev_parent = parent
        prevsource = source
    if prev_color != 'BLACK':
        if color == 'GRAY' and sourceDist < MAXVAL:
            prev_color = color
            prev_parent = parent
            prev_sourceDist = sourceDist
        elif color == 'WHITE':
            prev_adjlist = adjlist
            if prev_color != 'GRAY':
                prev_color = color

    prevsource = source

    # Counter to determine when to stop MapReduce loop
    if color == 'GRAY':
        sys.stderr.write("reporter:counter:GRAY-NODE-COUNTER,GRAY,1\n") # Increments 'GRAY' in counters group 'CUSTOM' by 1

# Emit last record group
emit(prevsource, prev_adjlist, prev_sourceDist, prev_color, prev_parent)