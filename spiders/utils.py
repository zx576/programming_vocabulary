# coding=utf-8
# author = zhouxin
# date = 2017.7.12

# description
# 一些通用方法

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


class _ProxyList:

    URL = 'http://lab.crossincode.com/proxy/get/?num=20'
    def __init__(self):
        self._proxies = []
        self.mark = 0
        self.offset = 20

        self._get_proxies()

    def _get_proxies(self, url=URL):
        req = requests.get(url)
        proxy_lst = req.json()['proxies']
        for proxy in proxy_lst:
            dct = {}
            dct['http'] = proxy['http']
            self._proxies.append(dct)

        return None

    def get_proxy(self):
        self._check()
        proxy = self._proxies[self.mark%len(self._proxies)]
        self.mark += 1
        return proxy

    def _check(self):
        if len(self._proxies) > 5:
            return

        else:
            url = URL + '&offset={}'.format(self.offset)
            self._get_proxies(url)
            self.offset += 20

        return

    def remove(self, item):
        if item in self._proxies:
            self._proxies.remove(item)
        else:
            print('无此IP')

    def __str__(self):
        return str(self._proxies)
