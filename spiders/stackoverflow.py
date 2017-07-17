# coding=utf-8
# author = zhouxin
# date = 2017.7.12
# description
# crwal stacloverflow's topic

import bs4

from spiders.utils import Utils


class _Settings():

    def __init__(self):

        # 手动设置
        # topic links
        self.topic = [
            # python topic
            # 'https://stackoverflow.com/documentation/python/topics'
            # 'https://stackoverflow.com/documentation/django/topics',
            # 'https://stackoverflow.com/documentation/algorithm/topics',
            # 'https://stackoverflow.com/documentation/git/topics',
            # 'https://stackoverflow.com/documentation/design-patterns/topics',
            'https://stackoverflow.com/documentation/flask/topics'
        ]
        # question links
        self.res = []
        # =======================
        #　 dont change anything below
        self.util = Utils()
        self.domain = 'https://stackoverflow.com'

    # 解析这个 topic 下的所有答案链接
    def _parse_topic(self):
        if not self.topic:
            return
        for url in self.topic:
            self._add_url(url)

    def _add_url(self, url):

        page = self.util.req(url)
        if not page:
            return
        soup = bs4.BeautifulSoup(page, 'lxml')
        soup_a = soup.find_all('a', class_='doc-topic-link')
        for a in soup_a:

            last = a.get('href', None)
            self.res.append(self.domain+last)

        soup_next = soup.find('a', attrs={'rel': 'next'})
        # get next page
        if soup_next:

            next_url =self.domain + soup_next['href']
            return self._add_url(next_url)


    def parse(self):

        self._parse_topic()
        return self.res


class Stspider:

    def __init__(self):
        self.links = _Settings().parse()
        self.util = Utils()

    # 获取所有文字内容
    def _get_words(self, url):
        page = self.util.req(url)
        if not page:
            return
        soup = bs4.BeautifulSoup(page, 'lxml')
        body = soup.find('body')
        if not body:
            return
        else:
            words = body.get_text(' ')

        return words

    # 保存文字内容
    def _save(self, url, words):
        if not words:
            return
        title = url.split('/')[-1]
        with open(r'stack/{}.txt'.format(title), 'w')as f:
            f.write(words)

    # 启动
    def start(self):

        if not self.links:
            return

        for url in self.links:
            words = self._get_words(url)
            self._save(url, words)
            print('successfully get {0} '.format(url))


if __name__ == '__main__':
    st = Stspider()
    st.start()


