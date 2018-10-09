HADOOP_CMD="/home/lishijia/Soft/hadoop-2.7.2/bin/hadoop"

STREAM_JAR_PATH="/home/lishijia/Soft/hadoop-2.7.2/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar"

INPUT_FILE_PATH_ORDER="/lishijia/input/mapreducejoin/order"
INPUT_FILE_PATH_ITEM="/lishijia/input/mapreducejoin/order_item"

OUTPUT_PATH_ORDER="/lishijia/output/maporder"
OUTPUT_PATH_ITEM="/lishijia/output/maporderitem"

OUTPUT_PATH_JOIN="/lishijia/output/mapreducejoin/"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH_ORDER $OUTPUT_PATH_ITEM $OUTPUT_PATH_JOIN

$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_ORDER \
    -output $OUTPUT_PATH_ORDER \
    -mapper "python map_order.py" \
    -file ./map_order.py \

$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_ITEM \
    -output $OUTPUT_PATH_ITEM \
    -mapper "python map_item.py" \
    -file ./map_item.py \


$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $OUTPUT_PATH_ORDER,$OUTPUT_PATH_ITEM \
    -output $OUTPUT_PATH_JOIN \
    -mapper "cat" \
    -reducer "python reduce_join.py" \
    -file ./reduce_join.py