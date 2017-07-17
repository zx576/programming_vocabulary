## 单词分析

#### 文件结构

- settings.py 一些基本的设置
- analysis_book.py 分析文件，提取单词
- models_exp.py 使用 peewee 接口处理数据库设置
- test.py 一些测试/与项目本身无关
- translate.py 翻译接口
- work.py 启动项目
- spiders 收集书籍资料、文档、github、stackoverflow 的爬虫程序
- shanbay 批量导入单词到扇贝

#### 工作流程

1、 设置 settings.py 中的一些基本项目

2、 使用 spiders 文件夹下的爬虫收集资料

3、 运行 work.py 分析收集资料，提取单词

4、 运行 translate.py 调用翻译接口，完成翻译

5、 设置 shanbay 文件夹下的程序上传单词

6、 运行 db2csv.py 从数据库提取所有词汇到 csv

#### 技术细节

##### １.使用 peewee 库处理数据库文件

作为一名怕麻烦的程序员，写原生 sql　语句简直要命，一直希望能有 django-orm 那样的神器，用 python 的方式操作数据库，经过一番了解发现 peewee 和 SQLAlchemy 可以做到， 前者偏轻后者偏重。最后选择了 peewee 来开发。

peewee 文档：[peewee](https://peewee.readthedocs.io/en/latest/)

示例代码：

```python

from peewee import *

# 连接到数据库
new_db = SqliteDatabase('voca.db')

#　建表
class NewBook(Model):
    name = CharField()
    # 总词汇
    total = IntegerField(default=0)
    # 是否已经统计
    is_analyzed = BooleanField(default=False)
    # reserved columns
    # 保留字段，便于之后扩展
    re1 = CharField(default='')
    re2 = IntegerField(default=0)

    class Meta:
        database = new_db
        
```

以上截取了项目中部分代码，使用过 django 的同学应该很熟悉这种写法。


#### 2. 提取分析单词

这部分是整个项目的核心，但代码并不多，使用正则匹配出所有的单词，然后再使用 collections 下的 Counter 函数统计并输出词频较高的单词。

代码示例：

```python

import re
from collections import Counter
# 打开文件，读取数据
with open(filename, 'r', encoding='utf-8')as f:
    raw_words = f.read()

# 正则匹配所有单词
words = re.findall('[a-z]+', raw_words.lower())

# 统计单词
c = Counter(words)
# 提取出前词频前 100 的单词
c.most_common(100)

```

#### 3. 翻译接口

项目一共尝试了 3 种翻译接口， 百度/金山/扇贝 ， 最后确定使用金山家的接口，百度家的接口音标和单词意思是分开的请求，扇贝家的接口在返回信息方面不如其他两家完整，金山家的接口既有音标也有详细的解释。

接口的示例代码如下：

```python

import requests


def trans_ici(word):

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
    
    # 分别获取美/英 音标
    ph_en = '英 [' + data['ph_en'] + ']'
    ph_am = '美 [' + data['ph_am'] + ']'
    # 获取单词解释
    ex = ''
    for part in data['parts']:
        ex += part['part'] + ';'.join(part['means']) + ';'

    return ph_en+ph_am, ex
    
# 示例
res = trans_ici('hello')
print(res)
# >>> ("英 [hə'ləʊ]美 [həˈloʊ]", 'int.哈喽，喂;你好，您好;表示问候;打招呼;n.“喂”的招呼声或问候声;vi.喊“喂”;')
```

##### 4. spiders

spiders 文件夹下包含了 4 种不同形式的爬虫，分别是 pdf下载爬虫/github爬虫/stackoverflow爬虫/readthedocs爬虫。在资料收集阶段根据自己的需要，输入相应的需要被爬取的地址，然后运行文件即可。

以 github 爬虫为例：

首先输入需要被爬取地址

```python
# 资源整合项目地址
# 类似 awesome-python 
# 爬虫会爬取链接下的所有链接
# 接着请求获取的链接， 获取 readme 文档内容
self.projectsPool = ['https://github.com/vinta/awesome-python']

# 独立的项目
# 类似 django 
# 爬虫会直接获取该项目下的 readme 内容
self.projectsUrl = []

```


