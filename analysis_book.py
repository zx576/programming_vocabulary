# coding=utf-8
# author = zhouxin
# date = 2017.7.10
# description
# 导入某文件夹下的所有 txt 文件，逐一分析，提取出词汇，存入数据库


from collections import Counter
import re

# 引入排除词汇
from settings import exclude_list, NUMBERS
# 数据库操作
# from models import Word, Book
from models_exp import NewBook, NewWord


class AnlysisBook():

    # open file and return all english words
    def _open_file(self, filename):

        with open(filename, 'r', encoding='utf-8')as f:
            raw_words = f.read()

        words = re.findall('[a-z]+', raw_words.lower())

        return words

    # insert the information of the book into database
    def new_book(self, path, words):

        bookname = path.split('/')[-1]
        query_book = NewBook.select().where((NewBook.name == bookname) & (NewBook.is_analyzed == True))
        if query_book:
            return

        newbook = NewBook.create(
            name=bookname,
            total=len(words)

        )
        return newbook

    # filter valid words
    # select the 500(default, you can change it in settings.py) frequency words
    def _filter_words(self, raw_words, count=NUMBERS):

        new_words = []
        for word in raw_words:
            if word not in exclude_list and len(word) > 1:
                new_words.append(word)

        # 根据书籍字数确定从该书取多少单词
        ct = 10
        for i, j in NUMBERS:
            if len(new_words) < i:

                ct = j
                break

        print(ct)

        c = Counter(new_words)
        return c.most_common(ct)

    # insert words into database
    # firstly, it will check out if the book exist in the database
    # if not, the words will be inserted into database
    # or , it will return cos the words has been handled
    # last, the book will be marked as analyzed
    def _insert_book(self, book, words):

        # 检查数据库内是否有该书籍
        if not book:
            return

        # 向数据库内插入数据
        for word, fre in words:
            query = NewWord.select().where(NewWord.name == word)
            if query:
                word_ins = query[0]
                word_ins.frequency += fre
                word_ins.save()
            else:
                word_ins = NewWord.create(
                            name=word,
                            frequency=fre,
                        )
        print('处理了 {} 个单词'.format(len(words)))
        # 标记该书已经被处理
        book.is_analyzed = True
        book.save()

    def analysis(self, lst_files):

        # filename = 'Data+Structures+and+Algorithms+Using+Python.txt'
        for i in lst_files:
            raw_words = self._open_file(i)
            bookins = self.new_book(i, raw_words)
            filter_words = self._filter_words(raw_words)
            self._insert_book(bookins, filter_words)
