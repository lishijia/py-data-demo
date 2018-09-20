#!/usr/bin/env python
# coding=utf-8

import sys

for line in sys.stdin:
    ss = line.strip().split(' ')
    for word in ss:
        print "%s\t%d" % (word,1)