#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/2/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -jobconf mapred.reduce.tasks=2 \
    -input /user/a2ex2-input.txt \
    -output /output2/ \
    -file a2m2.py \
    -file a2r2.py \
    -mapper a2m2.py \
    -reducer a2r2.py

hadoop fs -getmerge /output2/ result.txt && vim result.txt