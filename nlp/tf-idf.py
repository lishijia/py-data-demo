# coding=utf-8
import os
import math

dir_path = "data"
doc_dict = dict()
index = 0

stopWords = set()
lines = open("stop-word", 'r')
for line in lines:
    if len(line.strip()) == 0:
        continue
    stopWords.add(line.strip())

# 循环读取每篇文章
for file_name in os.listdir(dir_path):
    file_path = dir_path + "/" + file_name
    # if index > 10:
    #     break
    index += 1
    word_dict = dict()
    # 每篇文章的总词数
    sum_cnt = 0
    # 循环每行读取文章
    for line in open(file_path, 'r'):
        if len(line.strip()) == 0:
            continue
        for word in line.strip().split(" "):
            if len(word.strip()) == 0:
                continue
            if word in stopWords:
                continue
            if word_dict.get(word, -1) == -1:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
            sum_cnt += 1
    # 计算每篇文章中每个词的词频
    for word in word_dict.keys():
        tmp = word_dict[word] / float(sum_cnt)
        word_dict[word] = tmp
        # print "%s %f %d" % (word, word_dict[word], sum_cnt)
    doc_dict[file_name] = word_dict

doc_num = float(index)

# 统计每篇文章中的词在几篇文章中出现
doc_freq = dict()
for doc in doc_dict:
    for word in doc_dict[doc].keys():
        if doc_freq.get(word, -1) == -1:
            doc_freq[word] = 1
        else:
            doc_freq[word] += 1

# 套idf公式
for word in doc_freq.keys():
    doc_freq[word] = math.log(doc_num/float(doc_freq[word]+1))
    print "%s %f" % (word, doc_freq[word])

