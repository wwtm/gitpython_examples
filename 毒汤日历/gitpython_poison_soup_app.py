#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 21:30
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : gitpython_poison_soup_app.py
# @Software: PyCharm

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.117 Safari/537.36' }

url = 'http://www.dutangapp.cn/u/toxic?date=2020-01-18'

def get_data():
    try:
        # 以"附加写"的方式写入txt文本
        with open("poison_soup_app.txt", "a", encoding='utf-8') as f:
            res = requests.get(url=url, headers=headers, timeout=10).json()

            res_contents = res['data']
            for i in res_contents:
                text = i['data']
                f.write(text + '\n')
                print(text)

    # 捕获所有异常通常是由于程序员在某些复杂操作中并不能记住所有可能的异常。
    # 如果你不是很细心的人，这也是编写不易调试代码的一个简单方法。
    except Exception as e:
        # 打印异常类型的内容e
        print('exception:', e)


if __name__ == '__main__':
    get_data()