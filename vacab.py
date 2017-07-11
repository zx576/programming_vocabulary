# coding=utf-8
# author = zhouxin
# date = 2017.7.10


from collections import Counter
import re

# 引入排除词汇
from exclude import exclude_list


# 打开文件
def open_file(filename):

    with open(filename, 'r', encoding='utf-8')as f:
        raw_words = f.read()

    return raw_words


# 筛选词汇，默认词频前 500
def filter_words(raw_words, count=500):

    words = re.findall('[a-z]+', raw_words.lower())

    new_words = []
    for word in words:
        if word not in exclude_list and len(word)>1:
            new_words.append(word)

    c = Counter(new_words)

    return c.most_common(count)


# 插入数据库
def insert_2_dt(words):
    

def main():

    filename = 'Data+Structures+and+Algorithms+Using+Python.txt'
    raw = open_file(filename)
    res = filter_words(raw)
