HADOOP_CMD="/home/lishijia/Soft/hadoop-2.7.2/bin/hadoop"
STREAM_JAR_PATH="/home/lishijia/Soft/hadoop-2.7.2/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar"

INPUT_FILE_PATH="/lishijia/input/the_man_of_property.txt"
OUTPUT_PATH="/lishijia/output/mapreduce/"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.

$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH \
    -output $OUTPUT_PATH \
    -mapper "python map.py" \
    -reducer "python reduce.py" \
    -file ./map.py \
    -file ./reduce.py