# coding=utf-8
# author = zhouxin
# description
# 下载 pdf 文件， 将 pdf 下载地址添加到 downlst ,运行程序即可

import requests
from spiders.utils import Utils

PATH_DIR = 'download/'
util = Utils()

def download(url):

    util.checkpath(PATH_DIR)

    req = requests.get(url)
    c = req.content
    name = url.split('/')[-1]
    with open(PATH_DIR+name, 'wb')as f:
        f.write(c)


downlst = [
    # 'http://files2.syncfusion.com/Downloads/Ebooks/SciPy_Programming_Succinctly.pdf',
    # 'https://docs.google.com/file/d/0B8IUCMSuNpl7MnpaQ3hhN2R0Z1k/edit'
    # 'http://stock.ethop.org/pdf/python/Learning%20Python,%205th%20Edition.pdf',
    # 'http://slav0nic.org.ua/static/books/python/OReilly%20-%20Core%20Python%20Programming.pdf',
    #  ///////////
    # 'http://www.oreilly.com/programming/free/files/functional-programming-python.pdf',
    # 'https://doc.lagout.org/programmation/python/Python%20Pocket%20Reference_%20Python%20in%20Your%20Pocket%20%285th%20ed.%29%20%5BLutz%202014-02-09%5D.pdf',
    # 'http://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf',
    # 'http://www.oreilly.com/programming/free/files/20-python-libraries-you-arent-using-but-should.pdf',
    # 'http://www.oreilly.com/programming/free/files/hadoop-with-python.pdf',
    # 'http://www.oreilly.com/programming/free/files/how-to-make-mistakes-in-python.pdf',
    # 'http://www.oreilly.com/programming/free/files/functional-programming-python.pdf',
    # 'http://www.oreilly.com/programming/free/files/python-in-education.pdf',
    # 'http://www.oreilly.com/programming/free/files/from-future-import-python.pdf'
    # 'http://trickntip.com/wp-content/uploads/2017/01/Head-First-Python-ora-2011.pdf'
    # ''''''''''''''''
    # 'http://victoria.lviv.ua/html/fl5/NaturalLanguageProcessingWithPython.pdf',
    # 'http://www3.canisius.edu/~yany/python/Python4DataAnalysis.pdf',
    # 'ftp://ftp.micronet-rostov.ru/linux-support/books/programming/Python/[O%60Reilly]%20-%20Programming%20Python,%204th%20ed.%20-%20[Lutz]/[O%60Reilly]%20-%20Programming%20Python,%204th%20ed.%20-%20[Lutz].pdf
    # ..for 
    # 'https://media.readthedocs.org/pdf/requests/latest/requests.pdf',
    # 'http://gsl.mit.edu/media/programs/nigeria-summer-2012/materials/python/django.pdf',
    # 'https://media.readthedocs.org/pdf/beautiful-soup-4/latest/beautiful-soup-4.pdf',
    # 'https://media.readthedocs.org/pdf/flask/0.7/flask.pdf',

    # 'https://media.readthedocs.org/pdf/jinja2/latest/jinja2.pdf',
    # 'http://lxml.de/3.4/lxmldoc-3.4.4.pdf',
    # 'https://docs.scipy.org/doc/numpy-1.11.0/numpy-ref-1.11.0.pdf',
    # 'https://pandas.pydata.org/pandas-docs/stable/pandas.pdf',
    # 'https://media.readthedocs.org/pdf/peewee/latest/peewee.pdf',
    # 'https://media.readthedocs.org/pdf/pillow/latest/pillow.pdf',
    # 'https://media.readthedocs.org/pdf/scrapy/1.0/scrapy.pdf',
'https://media.readthedocs.org/pdf/xlwt/latest/xlwt.pdf'
#     'http://1.droppdf.com/files/X06AR/fluent-python-2015-.pdf',
#     'http://files.meetup.com/18552511/Learn%20Python%20The%20Hard%20Way%203rd%20Edition%20V413HAV.pdf',


]

if __name__ == '__main__':

    for l in downlst:
        download(l)