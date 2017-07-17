# coding=utf-8
# author = zhouxin
# date = 2017.7.14

# description
# 将单词添加到扇贝，手动版
import requests
import time
import bs4

from models_exp import NewWord
from shanbay.shanbeisettings import HEADER,WORKBOOK_PATH



class ShanBay:

    def __init__(self):
        self.header = HEADER
        self.url = 'https://www.shanbay.com/api/v1/wordlist/vocabulary/'
        # 一共添加 500 单词
        self.count = 0
        # 每个列表添加 200, 满了则换列表 id
        self.list_count = 0
        self.listid = []
        self.book_url = 'https://www.shanbay.com/wordbook/187711/'
        # print(HEADER)

    def _parse_id(self):

        req = requests.get(self.book_url, headers=self.header)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text)
        soup_a = soup.find_all('a', attrs={'desc': True})
        for a in soup_a:
            id = a['unit-id']
            print(id)
            self._save_id(id)

    def _save_id(self, id):
        with open(WORKBOOK_PATH, 'a+')as f:
            f.write(str(id))
            f.write('\n')

    def _open_bookid(self):
        with open(WORKBOOK_PATH, 'r')as f:
            for i in f.readlines():
                self.listid.append(int(i))

        print(self.listid)


    def _add_one(self, word, listid):

        dct = {
            'id': listid,
            'word': word
        }
        # print(dct)
        # 请求错误
        try:
            req = requests.post(self.url, dct, headers=self.header)
            req.raise_for_status()
            res = req.json()
            print('单词 {}'.format(word), res)
            print(req.status_code)
        except:
            return '1'

        return res['msg']

    def add(self):

        query = NewWord.select().where((NewWord.is_valid == True) & (NewWord.re1 == '')).order_by(-NewWord.frequency)


        iter_word = iter(query)
        self._open_bookid()
        iter_lst = iter(self.listid)
        id = next(iter_lst)
        while True:

            # 单词添加完毕，程序结束
            try:
                next_word = next(iter_word)
            except:
                break

            res = self._add_one(next_word.name, id)
            # 设置请求错误处理
            if res == '1':
                print('请求错误，稍后再试')
                break

            # 设置单词无效处理
            elif 'NOT' in res:
                next_word.re1 = 'invalid'
                next_word.save()
                continue

            # 换单词表
            elif '过上限' in res:
                id = next(iter_lst)
                self.list_count = 0
                self._add_one(next_word.name, id)

            # 标记该单词已经添加
            next_word.re1 = 'added'
            next_word.save()

            # time.sleep(0.5)

            self.count += 1
            self.list_count += 1


    def test_add(self):
        self._add_one('define', 539857)

if __name__ == '__main__':

    s = ShanBay()
    s.add()
    # s._parse_id()
    # s._open_bookid()