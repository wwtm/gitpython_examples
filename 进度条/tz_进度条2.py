#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 20:38
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : tz_进度条2.py
# @Software: PyCharm

import sys, time

print("正在下载......")
for i in range(11):
    if i != 10:
        sys.stdout.write("==")
    else:
        sys.stdout.write("== " + str(i * 10) + "%/100%")
    sys.stdout.flush()
    time.sleep(0.2)
print("\n" + "下载完成")