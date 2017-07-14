# coding=utf-8
# author=zhouxin
# date=2017.7.10
# description
# 调用翻译接口，逐步翻译数据库内词汇

import requests
import time

from models_exp import NewWord
from spiders.utils import Utils


class Translate:

    def __init__(self):
        # self.util = Utils()
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

    # iciba api / 金山词典 api
    # baidu api dont contain Phonogram , so change an api
    def _trans_ici(self, word):

        url = 'http://www.iciba.com/index.php?a=getWordMean&c=search&word=' + word
        try:
            req = requests.get(url)
            req.raise_for_status()
            info = req.json()
            data = info['baesInfo']['symbols'][0]
            assert info['baesInfo']['symbols'][0]
            # 去除没有音标的单词
            assert data['ph_am'] and data['ph_en']
            # 去除没有词性的单词
            assert data['parts'][0]['part']

        except:
            return

        ph_en = '英 [' + data['ph_en'] + ']'
        ph_am = '美 [' + data['ph_am'] + ']'
        ex = ''
        for part in data['parts']:
            ex += part['part'] + ';'.join(part['means']) + ';'

        return ph_en+ph_am

    # 扇贝单词 api
    def _trans_shanbay(self, word):
        url = 'https://api.shanbay.com/bdc/search/?word=' + word
        req = requests.get(url)
        print(req.json())

    def trans(self):

        query = NewWord.select().where(NewWord.explanation != '')
        if not query:
            return
        for word in query:

            res = self._trans_ici(word.name)
            print(res)
            if res:
                word.phonogram = res
                # word.
                # word.explanation = res

            else:
                word.is_valid = False
            word.save()
            time.sleep(1)

    def _test(self):
        query = NewWord.select()

        for word in query[:100]:
            print(word.name)
            print(word.explanation)
            print(word.frequency)


t = Translate()
# res = t._trans_shanbay('hello')
# print(res)
# t._test()
t.trans()