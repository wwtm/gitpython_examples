#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 11:28
# @Author  : T.M.
# @File    : tm_github_auto.py
# @Software: PyCharm

# api https://api.github.com/repos/kenwoodjw/python_interview_question
# web_page https://github.com/kenwoodjw/python_interview_question

import requests
import webbrowser
import time

# 1.Github项目及API接口数据
api = 'https://api.github.com/repos/kenwoodjw/python_interview_question'
web_page = "https://github.com/kenwoodjw/python_interview_question"

last_update = None
# '2019-09-28T01:20:42Z'

while True:

    all_info = requests.get(api).json()
    cur_update = all_info['updated_at']
    print(cur_update)

    # 假设第一次运行之前，不知道上次的更新时间
    # 如果last_update 为 none，会执行下面的语句，把当前的时间给到上次时间
    if not last_update:
        last_update = cur_update

    # 第一次两个时间相等，不会执行
    # 假设10分钟后，cur_update更新，那么就会自动打开网页
    # 接下来，把 当前时间 赋值 给上次时间
    # 开始新一轮的监测
    if last_update < cur_update:
        webbrowser.open(web_page)
        last_update = cur_update

    # 间隔 10分钟，再次while循环，观察新的更新时间是否发生变化
    time.sleep(600)

