# coding=utf-8
# 计算文章语句向量
import jieba

def word_to_vector(union_set, seg_list):
    data_vector=[0]*len(union_set)
    index=0
    for word in union_set:
        data_vector[index] = seg_list.count(word)
        index += 1
    return data_vector

stopWords = set()
lines = open("stop-word", 'r')
for line in lines:
    if len(line.strip()) == 0:
        continue
    stopWords.add(line.strip())

# for word in stopWords:
#     print word

s1 = "这只皮靴号码大了。那只号码合适"
s2 = "这只皮靴号码不小，那只更合适"

s1_seg = "/".join(x for x in jieba.cut(s1, True) if x!="")
s2_seg = "/".join(x for x in jieba.cut(s2, True) if x!="")

# word ='这'
#
# if word in stopWords:
#     print word

# s1_list = jieba.cut(s1, cut_all=True)
# for word in s1_list:
#     wordTmp = word.encode("utf-8")
#     if wordTmp != "" and wordTmp not in stopWords:
#         print wordTmp

# s1_seg_list = [x for x in jieba.cut(s1, True) if x != "" and x.encode("utf-8") not in stopWords]
# s2_seg_list = [x for x in jieba.cut(s2, True) if x != "" and x.encode("utf-8") not in stopWords]

s1_seg_list = [x for x in jieba.cut(s1, True) if x != ""]
s2_seg_list = [x for x in jieba.cut(s2, True) if x != ""]

s1_seg_set = set(s1_seg_list)
s2_seg_set = set(s2_seg_list)
s1_with_s2_seg_set = s1_seg_set.union(s1_seg_set)

s1_vector = word_to_vector(s1_with_s2_seg_set, s1_seg_list)
s2_vector = word_to_vector(s1_with_s2_seg_set, s2_seg_list)
print s1_vector
print s2_vector


