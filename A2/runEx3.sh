#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/output3/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -jobconf mapred.reduce.tasks=2 \
    -jobconf stream.num.map.output.key.fields=1 \
    -input /user/retail.dat \
    -output /output3/ \
    -file a2m3.py \
    -file a2r3.py \
    -mapper a2m3.py \
    -reducer a2r3.py

hadoop fs -getmerge /output3/ result.txt && vim result.txt