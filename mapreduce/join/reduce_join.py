#!/usr/bin/env python
# coding=utf-8

import sys
v_order = None
for line in sys.stdin:
    order = line.strip().split(',')
    if v_order == None:
        v_order = order
    elif order[1] == "1":
        v_order = order
    elif order[1] == "2":
        print "%s\t%s\t%s\t%s\t%s\t%s" % (v_order[0], v_order[2], v_order[3], order[2], order[3], order[4])