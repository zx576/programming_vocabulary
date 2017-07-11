# coding=utf-8
# author = zhouxin
# date = 2017.7.10

# description
# 将单词以及词频存入数据库

class VocDt:

    def __init__(self):
        self.conn = 'voc.db'
        self.build_or_connect()

    # 建立或链接数据库
    def build_or_connect(self, tablename):
        pass


    # 寻找数据库内是否存在某特定词汇
    def _search(self, word):
        pass

    # 插入新数据
    def insert(self, *args):
        pass

    # 更新数据
    def update(self, *args):
        pass

    # 显示数据,调试用
    def _showall(self):
        pass

    # 提取数据
    def extract(self):
        pass
