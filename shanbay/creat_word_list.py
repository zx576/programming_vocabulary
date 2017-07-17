# coding=utf-8
# author = zhouxin
# date = 2017.7.15
# description
# 创建单词书章节

import requests
import time

from shanbay.shanbeisettings import CHAPTER_NAME, HEADER, WORKBOOKID,WORKBOOK_PATH

class Create_list:

    def __init__(self):
        self.chapter = CHAPTER_NAME
        # self.cookie = COOKIE
        self.bookid = WORKBOOKID
        self.header = HEADER
        self.url = 'https://www.shanbay.com/api/v1/wordbook/wordlist/'

    def _create_lst(self, name, description):

        keywords = {
            'name': name,
            'description': description,
            'wordbook_id': self.bookid
        }
        print(keywords)
        # self.header['cookie'] = self.cookie
        # print(self.header)
        try:
            req = requests.post(self.url, keywords, headers=self.header)
            req.raise_for_status()
            print(req.status_code)
            print(req.json()['data']['id'])
            assert req.json()['data']
        except Exception as e:
            print(e)
            return

        return req.json()['data']['id']


    def create(self):

        for key in self.chapter:
            # if '1' in key or '2' in key:
            #     continue
            print('创建单词章节{0}, 描述为{1}'.format(key, self.chapter[key]))
            id = self._create_lst(key, self.chapter[key])

            time.sleep(1)


c = Create_list()
c.create()