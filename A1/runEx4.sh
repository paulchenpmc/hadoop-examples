#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/output4/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -jobconf mapred.reduce.tasks=4 \
    -jobconf stream.num.map.output.key.fields=2 \
    -jobconf num.key.fields.for.partition=1 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input /user/shakespeare1.txt \
    -output /output4/ \
    -file a1m4.py \
    -file a1r4.py \
    -mapper a1m4.py \
    -reducer a1r4.py

hadoop fs -getmerge /output4/ result.txt && vim result.txt