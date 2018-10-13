#!/usr/bin/env python
# coding=utf-8
# python udf function for hive
import sys
for line in sys.stdin:
    tmp_line = line.upper()
    # 增加一个,号使之不换行，要不然在hive 命令控制台的时候，会看到多余的一个空行
    print tmp_line ,