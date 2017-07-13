# coding=utf-8
# author = zhouxin
# date = 2017.7.12
# description
# test some functions about the project

# analysis_book.py

from analysis_book import AnlysisBook
from models import Book, Word

def show_all_book():
    books = Book.select()
    for i in books:
        print(i.name)
        print(i.total)

# show_all_book()

def show_all_words():
    words = Word.select()
    print(len(words))
    for word in words[:100]:
        print(word.name)
        print(word.explanation)
        print(word.frequency)


show_all_words()
