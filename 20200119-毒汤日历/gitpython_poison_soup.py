#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/18 20:28
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : gitpython_poison_soup.py
# @Software: PyCharm

import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.117 Safari/537.36' }

# url = 'https://www.nihaowua.com/home.html'
url = 'https://8zt.cc/'

def get_data():
    count = 0
    # 无数次循环遍历
    while True:
        try:
            # 写入txt文本
            with open("poison_soup_zt.txt", "a", encoding='utf-8') as f:
                res = requests.get(url=url, headers=headers, timeout=10)
                selector = etree.HTML(res.text)
                # content = selector.xpath('//section/div/*/text()')[0]
                content = selector.xpath('//div[@class="main-wrapper"]//span[@id="sentence"]/text()')[0]
                text = str(count) + str(content)
                f.write(text + '\n')
                count += 1
                print('正在爬取中，这是第{}次爬取，内容为：{}'.format(count, content))

        # 捕获所有异常通常是由于程序员在某些复杂操作中并不能记住所有可能的异常。
        # 如果你不是很细心的人，这也是编写不易调试代码的一个简单方法。
        except Exception as e:
            # 打印异常类型的内容e
            print('exception:', e)
            continue


if __name__ == '__main__':
    get_data()