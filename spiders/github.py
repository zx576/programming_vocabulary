# coding=utf-8
# author = zhouxin
# date = 2017.7.12
# description
# crawl README's words about most projects of awesome-python on the github.com
# 爬取 github 上的资源集合， 或者某个独立的项目

import bs4
import re

from spiders.utils import Utils


PATH_DIR = 'github/'
# add some github projects
# return all projects' urls base on githubur
# 添加一些 github 项目/仓库地址，　返回所有仓库地址
class _Settings:

    def __init__(self):

        # github projects which contain many python directories
        # 资源集合
        self.projectsPool = [
            # 'https://github.com/vinta/awesome-python'
        ]
        # dependent directories
        # 独立的仓库
        self.projectsUrl = [
            'https://github.com/zx576/scancode_backend'
        ]
        # invoke general class
        # 爬虫工具箱
        self.util = Utils()

    # parse projects(like awesome-python)
    # return all directories' url which domain url are github.com
    # 解析类似 awesome-python 的项目，返回所有项目的 github 地址，过滤掉指向站外的 url
    def _parse_pool(self):

        if not self.projectsPool:
            return []

        links = []
        for project in self.projectsPool:
            page = self.util.req(project)
            if not page:
                continue
            links += self._parse_html_get_links(page)

        return links

    # use bs4 parse html
    # return all links
    def _parse_html_get_links(self, page):

        soup = bs4.BeautifulSoup(page, 'lxml')
        soup_a = soup.find_all('a', href=re.compile('https://github.com/'))
        links = []
        for a in soup_a:
            links.append(a['href'])

        return links


    def parse(self):

        # deduplicate urls
        return list(set(self.projectsUrl+self._parse_pool()))


# 爬虫程序
class GitSpider:

    def __init__(self):
        self.links = _Settings().parse()
        self.util = Utils()

    def _get_words(self, url):
        text = self.util.req(url)
        if not text:
            return

        soup = bs4.BeautifulSoup(text, 'lxml')
        soup_article = soup.find('article')

        return soup_article.get_text(' ') if soup_article else None


    def _save(self, url, words):

        self.util.checkpath(PATH_DIR)
        if not words:
            return
        title = url.split('/')[-1]
        with open(PATH_DIR+'{}.txt'.format(title), 'w')as f:
            f.write(words)

    def start(self):

        if not self.links:
            return

        for url in self.links:
            words = self._get_words(url)
            self._save(url, words)
            print('successfully get {0} '.format(url))


if __name__ == '__main__':
    gs = GitSpider()
    gs.start()