#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 13:22
# @Author  : T.M.
# @File    : tm_01_修改图片名称.py
# @Software: PyCharm

import os

# 修改名字
def renames_cat(filepath, kind=1):
    for dog_list in os.listdir(filepath):
        images_path = filepath + '/' + dog_list
        images = os.listdir(images_path)
        for name in images:
            image_path = images_path + '/'
            os.rename(image_path + name, image_path + str(kind) +'_' + name.split('.')[0]+'.jpg')

        kind += 1

renames_cat('./dog_kinds_after')