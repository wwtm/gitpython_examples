#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 20:42
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : tz_进度条3.py
# @Software: PyCharm

from time import sleep
from tqdm import tqdm

for i in tqdm(range(20)):
    sleep(0.5)