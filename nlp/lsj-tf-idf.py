# coding=utf-8
import os
import math

dir_path = "data"
doc_dict = dict()
index = 0

# 获取停用词
stopWords = set()
lines = open("stop-word", 'r')
for line in lines:
    if len(line.strip()) == 0:
        continue
stopWords.add(line.strip())

# 循环读取目录下所有文件，组装数据。计算每篇文章中词的词频
# doc_dict['doc_name',doc_dict['word','tf']]
for file_name in os.listdir(dir_path):
    file_path = dir_path + "/" + file_name
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

# 统计每篇文章中的词在几篇文章中出现，用于计算idf
# doc_dict['word','in_doc_num']
doc_freq = dict()
for doc in doc_dict:
    for word in doc_dict[doc].keys():
        if doc_freq.get(word, -1) == -1:
            doc_freq[word] = 1
        else:
            doc_freq[word] += 1

# 套idf公式计算每个词的idf
for word in doc_freq.keys():
    doc_freq[word] = math.log(doc_num/float(doc_freq[word]+1))
    # print "%s %f" % (word, doc_freq[word])

# 找出一篇文章中的关键字,倒序
for doc in doc_dict:
    doc_word_list = []
    for word in doc_dict[doc].keys():
        # tf * idf
        doc_word_list.append((word, doc_dict[doc][word] * doc_freq[word]))
    doc_word_list.sort(key=lambda x:x[1], reverse = True)
    if doc == '1597auto.seg.cln.txt':
        for x in  doc_word_list:
            print "%s,%f" % (x[0], x[1])