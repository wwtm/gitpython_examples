#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 12:17
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : juzi_luxun.py
# @Software: PyCharm

import requests
from lxml import etree
import pandas as pd
import time


headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
           }

# 保存数据
item_list = []

for i in range(0, 9):

    # 1、获取数据
    url = "http://www.shuoshuodaitupian.com/writer/128_" + str(i + 1)  # 1-10页
    result = requests.get(url, headers=headers).content.decode()

    # 2、解析数据
    html = etree.HTML(result)
    div_list = html.xpath('//div[@class="item statistic_item"]')
    div_list = div_list[1:-1]

    for div in div_list:
        # 遍历每一条信息

        item = {}

        # ./ 注意从当前节点，向下获取
        item['content'] = div.xpath('./a/text()')[0]
        item['source'] = div.xpath('./div[@class="author_zuopin"]/text()')[0]
        item['score'] = div.xpath('.//a[@class="infobox zan like "]/span/text()')[0]

        item_list.append(item)

    print("正在爬取第{}页".format(i + 1))
    time.sleep(0.1)

# 3、保存数据

# 把数据存成csv文件
df = pd.DataFrame(item_list)

# 保证不乱码
df.to_csv('鲁迅经典语录.csv', encoding='utf_8_sig')
