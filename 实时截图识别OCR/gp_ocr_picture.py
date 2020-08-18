#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 12:23
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : gp_ocr_picture.py
# @Software: PyCharm

from PIL import Image
from PIL import ImageGrab
import keyboard
import pytesseract
import time
from aip import AipOcr

# 1.截图
keyboard.wait(hotkey="f1")  # 输入键盘的触发事件
keyboard.wait(hotkey="ctrl+c")
time.sleep(0.1)

# 2.保存图片
image = ImageGrab.grabclipboard()  # 把图片从剪切板保存到当前路径
image.save("screen.png")

# 3.识别图片上的内容

# 法一
text = pytesseract.image_to_string(Image.open("screen.png"), lang='chi_sim')
print(text)

# 法二
# SDK文档

# APP_ID = '你的 App ID'
# API_KEY = '你的 Api Key'
# SECRET_KEY = '你的 Secret Key'

# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
#
# # 读取图片
# with open("screen.png", 'rb') as f:
#     image = f.read()
#
#     # 调用百度API通用文字识别（高精度版），提取图片中的内容
#     text = client.basicAccurate(image)
#     result = text["words_result"]
#     for i in result:
#         print(i["words"])
#     # print(text)
