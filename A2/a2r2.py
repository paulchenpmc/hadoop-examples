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
    # figure out the distance of each node from the source and the shortest path from each node to the source.
    if color == 'BLACK':
        emit(source, adjlist, sourceDist, color, parent)
        prev_adjlist = None
        prev_sourceDist = MAXVAL
        prev_color = None
        prev_parent = 'null'
        prevsource = source
        last_emitted_black = True
        continue
    if prevsource == source and last_emitted_black:
        # Case where black was emitted, ignore all other records
        continue
    if prevsource != source and not last_emitted_black:
        emit(prevsource, prev_adjlist, prev_sourceDist, prev_color, prev_parent)
        prev_adjlist = None
        prev_sourceDist = MAXVAL
        prev_color = None
        prev_parent = 'null'
    if adjlist:
        prev_adjlist = adjlist
    if not prev_color:
        prev_color = color
    if prev_color == 'WHITE':
        prev_color = color # Causes precedence of GRAY over WHITE
    if sourceDist < prev_sourceDist:
        prev_sourceDist = sourceDist
        if parent is not 'null':
            prev_parent = parent
    last_emitted_black = False
    prevsource = source
# Remember to emit last group here
if not last_emitted_black:
    emit(prevsource, prev_adjlist, prev_sourceDist, prev_color, prev_parent)