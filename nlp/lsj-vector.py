# coding=utf-8
# 计算语句向量
import jieba
import math

# 计算一个向量值的平方和然后开更
def vector_to_pow_with_sqrt(vector):
    vectorPow = 0
    for x in vector:
        vectorPow += math.pow(x, 2)
    return math.sqrt(vectorPow)

# 转换为向量值
def word_to_vector(union_set, seg_list):
    data_vector = [0] * len(union_set)
    index=0
    for word in union_set:
        data_vector[index] = seg_list.count(word)
        index += 1
    return data_vector

# 加载stop word。可以直接通过百度搜索(停用词)
stopWords = set()
lines = open("stop-word", 'r')
for line in lines:
    if len(line.strip()) == 0:
        continue
    stopWords.add(line.strip())

s1 = "小孩很爱妈妈，妈妈也喜爱小孩"
s2 = "小孩不爱妈妈，但是妈妈还是喜爱小孩"

s1_seg_list = [x for x in jieba.cut(s1, True) if x != ""]
s2_seg_list = [x for x in jieba.cut(s2, True) if x != ""]

s1_seg_set = set(s1_seg_list)
s2_seg_set = set(s2_seg_list)
s1_with_s2_seg_set = s1_seg_set.union(s2_seg_list)

# 打印语句分词结果
for x in  s1_seg_list:
    print x,
print
for x in  s2_seg_list:
        print x,
print

# 打印句子1与句子2分并集结果
for x in  s1_with_s2_seg_set:
    print x,
print

# 分词句子转换成向量值
s1_vector = word_to_vector(s1_with_s2_seg_set, s1_seg_list)
s2_vector = word_to_vector(s1_with_s2_seg_set, s2_seg_list)
print s1_vector
print s2_vector

# 根据余弦相似度的计算公式 计算向量值的平方更结果
s1_vector_sqrt = vector_to_pow_with_sqrt(s1_vector)
s2_vector_sqrt = vector_to_pow_with_sqrt(s2_vector)

# 根据余弦相似度的计算公式 计算分母
consine_top = 0
for index in range(len(s1_vector)):
    consine_top += s1_vector[index] * s2_vector[index]

# 计算余弦值
consine = consine_top/(s1_vector_sqrt * s2_vector_sqrt)

print consine



