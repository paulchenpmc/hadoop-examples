import subprocess

numloops = 0
DFS_FILEPATH        = 'output2-{}'
MAPPER              = 'BFS-mapper.py'
REDUCER             = 'BFS-reducer.py'
INPUT_FILE          = 'user/a2ex2-input.txt'

DFS_RM_CMD          = 'hdfs dfs -rm -r hdfs://10.1.2.89:9000/{}/'
DFS_VIEW_OUTPUT_CMD = 'hadoop fs -cat /{}/*'
HADOOP_STREAM_CALL  =\
'$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/hadoop-streaming-2.7.6.jar\
 -jobconf mapred.reduce.tasks=2\
 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner\
 -input /{0}\
 -output /{1}/\
 -file {2}\
 -file {3}\
 -mapper {2}\
 -reducer {3}'

first_iteration = True
# Loop through MapReduce jobs until entire graph traversed
while True:
    # Format input from previous mapreduce job
    if first_iteration:
        inputfile = INPUT_FILE
        first_iteration = False
    else:
        inputfile = DFS_FILEPATH.format(numloops) + '/*'
    hadoop_call = HADOOP_STREAM_CALL.format(inputfile, DFS_FILEPATH.format(numloops+1), MAPPER, REDUCER)
    numloops += 1
    subprocess.call(DFS_RM_CMD.format(DFS_FILEPATH.format(numloops)).split()) # Delete output dir if it exists, start fresh
    # Run mapreduce job
    print(hadoop_call)
    proc = subprocess.Popen(hadoop_call, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    no_gray_nodes = True
    for line in proc.stderr:
        print(line.rstrip())
        if 'GRAY=' in line:
            no_gray_nodes = False
    # proc.wait()
    subprocess.call(DFS_RM_CMD.format(DFS_FILEPATH.format(numloops-1)).split()) # Remove old dir on dfs after finished reading
    if no_gray_nodes:
        print('No gray nodes left after this iteration, finishing...')
        break

# # View final output
# subprocess.call(DFS_VIEW_OUTPUT_CMD.format(DFS_FILEPATH.format(numloops)).split(), shell=True) # Not working yet...
print('Finished traversing all nodes in graph')