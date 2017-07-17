# coding=utf-8
# author = zhouxin
# date = 2017.7.12
# description
# test some functions about the project

# analysis_book.py

from analysis_book import AnlysisBook
from models_exp import  NewBook, NewWord


def show_all_book():
    books = NewWord.select()
    print(len(books))
    # for i in books:
    #     print(i.name)
    #     print(i.total)

# show_all_book()

def show_all_words():
    # words = NewWord.select().where((NewWord.is_valid == True) & (NewWord.re1 == 'added')).order_by(-NewWord.frequency)
    # words = NewWord.select().where(NewWord.name == 'could')

    words = NewWord.select().where((NewWord.is_valid == True) & (NewWord.re1 == 'added')).order_by(-NewWord.frequency)
    print(len(words))
    # w = words[1000]
    # print(w.frequency)
    # print(w.name)
    for word in words[:10]:
        print(word.id)
        print(word.name)
        print(word.explanation)
        print(word.frequency)
        print(word.phonogram)
        print(word.re1)


show_all_words()

# translate.py

import requests

# url = 'http://fanyi.baidu.com/#en/zh/hello'
# url2 = 'http://fanyi.baidu.com/pcnewcollection?req=check&fanyi_src=hello&direction=en2zh&_=1499994079190'
#
# header = {
# 'Cookie': 'BAIDUID=044B5DCCB2EC706CE959B6E32B9098AC:FG=1; BDUSS=VJLV3d3aU5xakdzMGpseVJCWWV3UlBxRXpPN1lEVnpLT1BtV0xBc1FJV2lCVUpaSVFBQUFBJCQAAAAAAAAAAAEAAADq1XwMWElO09DB6dniAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKJ4GlmieBpZM; BIDUPSID=044B5DCCB2EC706CE959B6E32B9098AC; PSTM=1499253499; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE=1; cflag=15%3A3; PSINO=2; H_PS_PSSID=1444_21092_17001_19898_20930; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; hasSeenTips=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1499828490,1499828503,1499828898,1499994076; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1499994079',
# 'Referer': 'http://fanyi.baidu.com/'
#     }
#
#
# req = requests.get(url2, headers=header)
#
# print(req.text)

# url = 'https://www.shanbay.com/api/v1/wordlist/vocabulary/'
#
# dct = {'word': 'item', 'id': 539857}
#
# header = {
# 'Cookie': '__utmt=1; _gat=1; csrftoken=Z9SIpLVE7gBcQ1Q3I3BOwQLP8ipSWgZ5; sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrOz83Nz9MDS0FFi_WcE5MzUn3zU1JznKAKdZB1ZwI1mpgZmppYmtYCAJS6HyY:1dVq4g:-pBn-rq9L3y0tJOtMSI9gYczduQ"; _ga=GA1.2.1254111374.1497746577; language_code=zh-CN; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Inp4NTc2IiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjo0NjE1NDk1LCJleHAiOjE1MDA4NjIyOTR9._a3ZY5ocdW47HsYFuP2fQpn0VkEoifAtshxdz62ObOk; userid=4615495; __utma=183787513.1254111374.1497746577.1497753963.1499998044.4; __utmb=183787513.10.10.1499998044; __utmc=183787513; __utmz=183787513.1497746577.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
# }
# req = requests.post(url, dct, headers=header)
#
# print(req.json())


