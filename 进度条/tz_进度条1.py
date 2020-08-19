#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 20:34
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : tz_进度条.py
# @Software: PyCharm


import time

for i in range(0, 101, 2):
  time.sleep(0.1)
  num = i // 2
  if i == 100:
    process = "\r[%3s%%]: |%-50s|\n" % (i, '|' * num)
  else:
    process = "\r[%3s%%]: |%-50s|" % (i, '|' * num)
  print(process, end='', flush=True)