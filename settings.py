# coding=utf-8
# author = zhouxin
# date = 2017.7.11
# description
# 该项目的一些设置

import os

_BASEDIR = os.path.dirname(__file__)

# 数据库名
DATABASE = os.path.join(_BASEDIR, 'vocabulary.db')


# 需要遍历的文件夹
DIRS = [
    # 示例， 该文件夹在项目文件夹下，名为 'files'
    os.path.join(_BASEDIR, 'files'),
]


# 文件也可以单独添加
FILES = [
    # 示例， 该文件在项目文件夹下， 名为 'python.txt'
    # os.path.join(_BASEDIR, 'afe.txt')

]

# 每本书抓取的词汇量
NUMBERS = [
    (100, 10),  # 小于 100 取 10 个
    (1000, 100),  # 100 - 1000 取 100 个
    (5000, 300),
    (10000, 500),
    (50000, 1000),
    (2**31, 1500) # 大于 50000 统一取 1500
]


# 收集一些需要被排除的词汇
exclude_list = [
        # 代词
        'i', 'you', 'he', 'she', 'it', 'we', 'they', # 主格
        'me', 'him', 'her', 'us', 'them', # 宾格
        'my', 'your', 'his', 'her', 'its', 'our', 'their', # 形容词性
        'mine', 'yours', 'his', 'hers', 'ours', 'yours', 'theirs',  # 名词性
        'myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves', # 反身代词
        'this', 'that', 'such', 'these', 'those', 'some',
         'who', 'whom', 'whose', 'which', 'what', 'whoever', 'whichever', 'whatever', 'when',
         'as', 'self',
         'one', 'some', 'any', 'each', 'every', 'none', 'no', 'many', 'much', 'few', 'little',
         'other', 'another', 'all', 'both', 'neither', 'either',
         # 冠词
         'a', 'an', 'the',

         # 简单介词
         'about', 'with',
         'into', 'out', 'of' , 'without',
         'at', 'in', 'on', 'by', 'to',

         # 简单连词
         'and', 'also', 'too','not', 'but',

         # 简单量词
         'one', 'two', 'three', 'four', 'five',
         # 简单动词
         'is', 'am', 'are', 'was', 'were', 'be',
         # 其他
         'or', 'if', 'else', 'for','have', 'must', 'has', 'new', 'time',

]

