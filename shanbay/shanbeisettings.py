# coding=utf-8
# author = zhouxin
# date = 2017.7.15
# description
# batch upload words to shanbay.com
#

from collections import OrderedDict


# 需创建的单词章节名称
def create():
    count = 1
    # 总共创建多少个 章节
    total = 2
    dct = OrderedDict()
    # 章节名
    fix_key = 'Chapter-'
    # 描述
    fix_value = '第 {} 单元'
    while True:
        if count == total:
            break

        dct[fix_key+str(count)] = fix_value.format(str(count))

        count += 1

    # dct = tuple(dct)
    # print(dct)
    # for i in dct:
    #     print(i, dct[i])
    return dct

CHAPTER_NAME = create()


# 登录凭证
# 扇贝账户与密码 - 未实现
# 或者手动复制 cookie 信息

HEADER = {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            # 'Accept-Encoding':'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
            # 'Cache - Control': 'no-cache',
            # 'Connection': 'keep-alive',
            # 'Content-Length': '21',
            # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': """sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrOz83Nz9MDS0FFi_WcE5MzUn3zU1JznKAKdZB1ZwI1mpgZmppYmtYCAJS6HyY:1dVqdm:lsde3ncYWWJnay2wgBTkLXjxcTk"; csrftoken=HQDY8b1bHbSyiJVD1RgG2qBTqwQL6VYw; _ga=GA1.2.1254111374.1497746577; __utmt=1; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Inp4NTc2IiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjo0NjE1NDk1LCJleHAiOjE1MDExNDkxMDB9.eo3vJ-ylhqCaGs3DKK0pV_ny8H8rq_NSHY3ei1Lfe70; userid=4615495; __utma=183787513.1254111374.1497746577.1500258334.1500285087.13; __utmb=183787513.5.10.1500285087; __utmc=183787513; __utmz=183787513.1499999350.5.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic""",
            # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',
            # 'Host': 'www.shanbay.com',
            # 'Pragma': 'no-cache',
            # 'Origin': 'https://www.shanbay.com'
        }


# 创建的单词书ID
WORKBOOKID = 187633

# workbook_id 输出文件地址
WORKBOOK_PATH = 'workbook_id_test.txt'



