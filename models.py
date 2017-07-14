# coding=utf-8
# author = zhouxin
# date = 2017.7.10

# description
# 将单词以及词频存入数据库

from peewee import *
# from settings import DATABASE

db = SqliteDatabase('vocabulary.db')


class Book(Model):

    name = CharField()
    # 总词汇
    total = IntegerField(default=0)
    # 是否已经统计
    is_analyzed = BooleanField(default=False)

    class Meta:
        database = db

class Word(Model):
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

    class Meta:
        database = db


