#!/usr/bin/env python
# coding=utf-8
import sys
cur_word = None
cur_sum = 0
for line in sys.stdin:
    ss = line.strip().split('\t')
    if len(ss) != 2:
        continue
    word, value = ss
    if cur_word == None:
        cur_word = word
    if cur_word == word:
        cur_sum += (int(value))
    else:
        print "%s\t%d" % (cur_word, cur_sum)
        cur_word = word
        cur_sum = (int(value))
print "%s\t%d" % (cur_word, cur_sum)