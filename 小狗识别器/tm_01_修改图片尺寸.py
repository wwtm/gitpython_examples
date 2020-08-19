#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 11:52
# @Author  : T.M.
# @File    : tm_01_修改图片尺寸.py
# @Software: PyCharm

import os
from PIL import Image

# 修改尺寸
def resize_cat(width=100,height=100):

    for dog_name in os.listdir('./dog_kinds'):


        for jpgfile in os.listdir('./dog_kinds/' + dog_name):
            # print(jpgfile)
            img_path = './dog_kinds/' + dog_name + '/' + jpgfile
            img = Image.open(img_path)

            try:
                new_img = img.resize((width, height), Image.BILINEAR)
                new_img.save(os.path.join('./dog_kinds_after/' + dog_name, jpgfile))
            except Exception as e:
                print(e)

resize_cat()


