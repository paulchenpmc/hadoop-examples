#!/usr/bin/env python
#mapper.py

import sys

MAXVAL = 9223372036854775807

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
    adjlist     = [int(i) for i in adjlist.split(',')]
    if sourceDist == 'Integer.MAX_VALUE':
        sourceDist = MAXVAL
    else:
        sourceDist = int(sourceDist)
    # Mapper logic
    if color == 'GRAY':
        color = 'BLACK'
        emit(source, adjlist, sourceDist, color, parent)

        for childsource in adjlist:
            childcolor = 'GRAY' # Process this layer next
            childparent = source # Set parent node
            childsourceDist = sourceDist + 1 # Distance increases by 1
            emit(childsource, None, childsourceDist, childcolor, childparent)
    else:
        # Emit node as is
        emit(source, adjlist, sourceDist, color, parent)
