#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/output1/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -jobconf mapred.reduce.tasks=2 \
    -jobconf stream.num.map.output.key.fields=2 \
    -input /user/matrix.txt \
    -output /output1/ \
    -file matrixTranspose-mapper.py \
    -file matrixTranspose-reducer.py \
    -mapper matrixTranspose-mapper.py \
    -reducer matrixTranspose-reducer.py

hadoop fs -getmerge /output1/ result.txt && vim result.txt