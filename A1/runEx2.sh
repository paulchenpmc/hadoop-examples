#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/output2/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -input /user/shakespeare1.txt \
    -output /output2/ \
    -file a1m2.py \
    -file a1r2.py \
    -mapper a1m2.py \
    -reducer a1r2.py

hadoop fs -getmerge /output2/ result.txt && vim result.txt