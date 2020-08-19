#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 20:43
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : tz_进度条4.py
# @Software: PyCharm

import time
from progressbar import *

progress = ProgressBar()
for i in progress(range(1000)):
    time.sleep(0.01)