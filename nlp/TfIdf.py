# coding=utf-8
import jieba

s1 = "这只皮靴号码大了。那只号码合适"
s2 = "这只皮靴号码不小，那只更合适"

s1_seg = "/".join(x for x in jieba.cut(s1, True) if x!="")
s2_seg = "/".join(x for x in jieba.cut(s1, True) if x!="")

print s1_seg
print s2_seg