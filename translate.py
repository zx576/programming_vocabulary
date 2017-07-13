# coding=utf-8
# author=zhouxin
# date=2017.7.10
# description
# 调用翻译接口，逐步翻译数据库内词汇

import requests
import time

from models import Word


class Translate:

    def __init__(self):
        # self.req = Rep()
        pass

    # translation api, tranlate a english word to chinese
    # return translation result
    def _trans(self, word):
        # res = self.trans.translate('hello', dest='zh-CN')
        url = 'http://fanyi.baidu.com/sug'
        dct = {'kw': word}
        req = requests.post(url, dct)
        req.raise_for_status()
        res = req.json().get('data')
        if not res:
            return None
        return res[0].get('v', None)

    def trans(self):

        query = Word.select().where(Word.explanation == '')
        if not query:
            return
        for word in query:

            res = self._trans(word.name)
            print(res)
            if res:
                word.explanation = res

            else:
                word.is_valid = False
            word.save()
            time.sleep(1)

    def _test(self):
        query = Word.select()

        for word in query[:100]:
            print(word.name)
            print(word.explanation)
            print(word.frequency)


t = Translate()
# res = t._trans('student')
# print(res)
# t._test()
t.trans()

