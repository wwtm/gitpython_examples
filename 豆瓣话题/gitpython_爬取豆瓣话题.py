#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 10:50
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : gitpython_爬取豆瓣话题.py
# @Software: PyCharm

import requests

for i in range(0,200,20):

    # 通过浏览器检查，得到数据的URL来源链接
    url = 'https://m.douban.com/rexxar/api/v2/gallery/topic/125573/items?' \
          'sort=new&start={}&count=20&status_full_text=1&guest_only=0&ck=null'.format(i)

    # 破解防爬虫，带上请求头
    # 这两个不能省略
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0".3809.100 Safari/537.36',
               'Referer': 'https://www.douban.com/gallery/topic/125573/?from=gallery_trend&sort=hot'}

    # 发送请求，获取响应
    reponse = requests.get(url, headers=headers)
    html = reponse.json()

    # 解析数据，获得短评
    # 保存到本地
    for j in range(19):
        abs = html['items'][j]['abstract']
        with open("want_after.txt", "a", encoding='utf-8') as f:
            f.write(abs)
            print(abs)

