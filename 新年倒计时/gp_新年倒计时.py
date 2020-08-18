#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 17:04
# @Author  : 请关注公众号「GitPython」
# @Site    : 
# @File    : gp_新年倒计时.py
# @Software: PyCharm

from PIL import Image, ImageDraw, ImageFont
import os

for i in range(8, 0, -1):
    # 创建图像,设置图像大小及颜色
    im_color = [(174,60,58,255),(210,96,57,255),(174,60,58,255),(210,96,57,255),
                (174,60,58,255),(210,96,57,255),(174,60,58,255),(210,96,57,255)]

    im = Image.new('RGBA', (1000, 2160), im_color[i-1])
    draw = ImageDraw.Draw(im)

    # 设置本次使用的字体
    fontsFolder = 'D:/05.python_code/00.py_projects/new_year_last'
    font1 = ImageFont.truetype(os.path.join(fontsFolder, 'wenzangshufang.ttf'), 580)
    font2 = ImageFont.truetype(os.path.join(fontsFolder, 'SourceHanSerifCN-SemiBold.otf'), 90)
    font3 = ImageFont.truetype(os.path.join(fontsFolder, 'SourceHanSerifCN-SemiBold.otf'), 180)

    # 绘制矩形
    left = pos_x_3
    top = 1750
    right = pos_x_3 + txtSize_3[0]
    bottom = 1700 + txtSize_3[1]
    draw.rectangle((left, top, right, bottom), fill=(217, 217, 217, 255))

    # 计算各文本的放置位置
    txtSize_1 = draw.textsize('距 离 新 年 还 有', font2)
    pos_x_1 = (1000 - txtSize_1[0]) / 2
    txtSize_2 = draw.textsize('天', font2)
    pos_x_2 = (1000 - txtSize_2[0]) / 2

    wenhou = ["除夕夜", "贴春联", "把面发", "置新衣", "煮肉肉", "买年货", "大扫除", "祭灶台"]
    txtSize_3 = draw.textsize(wenhou[i-1], font3)
    pos_x_3 = (1000 - txtSize_3[0]) / 2

    # 设置文本放置位置,居中
    draw.text((pos_x_1, 200), '距 离 新 年 还 有', fill=(217, 217, 217, 255), font=font2)
    draw.text((pos_x_2, 1400), '天', fill=(217, 217, 217, 255), font=font2)
    draw.text((pos_x_3, 1700), wenhou[i-1], fill=im_color[i-1], font=font3)

    # 设置变化的文本属性
    txtSize_4 = draw.textsize(str(i), font1)
    pos_x_4 = (1000 - txtSize_4[0]) / 2
    draw.text((pos_x_4, 600), str(i), fill=(255, 192, 0, 255), font=font1)

    # im.show()
    # 保存图像
    filename = 'day' + str(i) + '.png'
    im.save(filename)