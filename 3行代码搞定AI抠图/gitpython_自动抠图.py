#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 10:17
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : gitpython_自动抠图.py
# @Software: PyCharm

from removebg import RemoveBg
rmbg = RemoveBg("dpv---", "error.log")  # 第一个引号内是你获取的API
rmbg.remove_background_from_img_file("D:/gitpython.jpg")  # 图片地址