# coding=utf-8
# author = zhouxin
# date = 2017.7.12

# description
# 一些通用方法, 目前只有请求网页的方法

import requests


class Utils:

    def __init__(self):
        # self.pr = _ProxyList()
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; U;'
                                     ' Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

    def _req_url(self, url, headers, proxies):

        try:
            req = requests.get(url, headers=headers, proxies=proxies, timeout=2)
            req.raise_for_status()
            return req.text

        except:
            return None

    def req(self, url, error=0):

        if error == 5:
            print('请求网页 {0} 失败'.format(url))
            return None

        # proxies = self.pr.get_proxy()
        proxies = None
        return self._req_url(url, headers=self.header, proxies=proxies) or self.req(url, error=error + 1)

