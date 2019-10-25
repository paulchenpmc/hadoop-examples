#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/output3/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -input /user/*.txt \
    -output /output3/ \
    -file a1m3.py \
    -file a1r3.py \
    -mapper a1m3.py \
    -reducer a1r3.py

hadoop fs -getmerge /output3/ result.txt && vim result.txt