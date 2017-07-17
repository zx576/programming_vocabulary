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



