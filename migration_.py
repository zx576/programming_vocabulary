# coding=utf-8
# author = zhouxin
# date = 2014.7.14

# 迁移数据库，预留多个字段

from settings import DATABASE
from models import Word, Book
from models_exp import NewBook, NewWord, new_db
import os

class _Connect:

    def __init__(self):
        self.build()

    def build(self):

        created = os.path.exists(DATABASE)

        if not created:
            new_db.connect()
            new_db.create_tables([NewWord, NewBook])


class Migrate:

    def __init__(self):

        # self.check = _Connect().build()
        pass
    def _migrate_word(self):

        query = Word.select().where(Word.is_valid == True).order_by(-Word.frequency)
        print(len(query))
        for word in query:
            NewWord.create(
                name=word.name,
                frequency=word.frequency,
                explanation=word.explanation,
                is_valid=word.is_valid
            )

    def _migrate_book(self):
        query = Book.select()
        print(len(query))
        for book in query:
            NewBook.create(
                name=book.name,
                total=book.total,
                is_analyzed=book.is_analyzed
            )

    def migrate(self):

        self._migrate_word()
        self._migrate_book()


m = Migrate()
m.migrate()

