#!/usr/bin/env python
# coding=utf-8

import sys

for line in sys.stdin:
    order = line.strip().split(',')
    if len(order) == 3:
        print "%s,1,%s,%s" % (order[0], order[1], order[2])
    elif len(order) == 4:
        print "%s,2,%s,%s,%s" % (order[0], order[1], order[2], order[3])