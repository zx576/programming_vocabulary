# coding=utf-8
# author = zhouxin
# date = 2017.7.17
# description
# extract all valid words to a csv file
# 提取所有有效单词到 csv 文件


from models_exp import NewWord
import csv
import chardet

def extract():

    query = NewWord.select().where((NewWord.is_valid == True) & (NewWord.re1 == 'added')).order_by(-NewWord.frequency)
    # print(len(query))
    for word in query:
        # print(chardet.detect(word.name))
        res = []
        for i in [word.name, word.phonogram, word.explanation]:
            res.append(i)

        yield res

def save(res):

    with open('python-words.csv', 'a+', errors='ignore', newline='')as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(res)


def main():

    row = extract()
    count = 1
    while True:
        try:
            row_data = next(row)
        except:
            break
        save(row_data)
        count += 1

if __name__ == '__main__':
    main()
    # res = extract()
    # print(next(res))
    # print(next(res))
    # print(next(res))
