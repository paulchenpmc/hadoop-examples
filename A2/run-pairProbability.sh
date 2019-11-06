#!/bin/bash

echo "If this script fails, try running dos2unix on it and try again"

hdfs dfs -rm -r hdfs://10.1.2.89:9000/output3/

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar \
    -jobconf mapred.reduce.tasks=2 \
    -jobconf stream.num.map.output.key.fields=2 \
    -jobconf num.key.fields.for.partition=1 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
    -input /user/retail.dat \
    -output /output3/ \
    -file pairProbability-mapper.py \
    -file pairProbability-reducer.py \
    -mapper pairProbability-mapper.py \
    -reducer pairProbability-reducer.py

hadoop fs -getmerge /output3/ result.txt && vim result.txt