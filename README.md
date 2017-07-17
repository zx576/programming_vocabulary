## 单词分析

#### 文件说明

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

6、 从数据库提取所有词汇到 csv


#### python 高频词汇内容整理


##### 书籍系列

Head-First-Python-ora-2011.pdf
from-future-import-python.pdf
20-python-libraries-you-arent-using-but-should.pdf
functional-programming-python.pdf
hadoop-with-python.pdf
how-to-make-mistakes-in-python.pdf
OReilly-Core-PythonProgramming.pdf
a-whirlwind-tour-of-python.pdf
Learn-Python-The-Hard-Way-3rd-Edition-V413HAV.pdf
python-in-education.pdf
NaturalLanguageProcessingWithPython.pdf
Python_Succinctly.pdf
beautiful-soup-4.pdf
MongoDB-and-Python-Patterns-and-Processes-for-the-Popular-Document-Oriented-Database.pdf
Natural_Language_Processing_with_Python.pdf
Python4DataAnalysis.pdf
Python-Pocket-Reference-Python-in-Your-Pocke.pdf
SciPy_Programming_Succinctly.pdf
Learning-Python-5t-Edition.pdf
fluent-python-2015-.pdf


#### python 常用库文档：

scrapy.pdf
pandas.pdf
pillow.pdf
xlwt.pdf
flask.pdf
requests.pdf
django.pdf
numpy-ref-1.11.0.pdf
jinja2.pdf
peewee.pdf
lxmldoc-3.4.4.pdf
python官方文档


#### github

python-awesome 下近 400 个项目的 readme 文档
[python-awesome](https://github.com/vinta/awesome-python)


#### stackoverfolw 文档

##### python 以及相关 tag

python
django
algorithm
git
design-patterns
flask

共 396 个相关 topics


