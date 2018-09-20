HADOOP_CMD="/home/soft/hadoop-2.6.1/bin/hadoop"
STREAM_JAR_PATH="/home/soft/hadoop-2.6.1/share/hadoop/tools/lib/hadoop-streaming-2.6.1.jar"

#INPUT_FILE_PATH_1 = "/"
INPUT_FILE_PATH_1="/jiarong/input/mapreduce/the_man_of_property.txt"
OUTPUT_PATH="/jiarong/output/mapreduce/"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.

$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py" \
    -reducer "python reduce.py" \
    -file ./map.py \
    -file ./reduce.py
