# coding = utf-8
# author = zhouxin
# date = 2017.7.14
# description
# expand exsited database, add some nessary column, and reserve some columns

from settings import DATABASE
from peewee import *

new_db = SqliteDatabase('voca.db')


class NewBook(Model):

    name = CharField()
    # 总词汇
    total = IntegerField(default=0)
    # 是否已经统计
    is_analyzed = BooleanField(default=False)
    # reserved columns
    re1 = CharField(default='')
    re2 = CharField(default='')
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = new_db

class NewWord(Model):
    # foreignkey , which books the word collect from
    # book = ForeignKeyField(Book)
    # 单词名
    name = CharField()
    # 解释
    explanation = TextField(default='')
    # 词频
    frequency = IntegerField(default=0)
    # 是否有效
    is_valid = BooleanField(default=True)
    # 音标
    phonogram = CharField(default='')
    # reserved columns
    re1 = CharField(default='')
    re2 = CharField(default='')
    re3 = IntegerField(default=0)
    re4 = IntegerField(default=0)

    class Meta:
        database = new_db