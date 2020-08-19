#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 15:30
# @Author  : 请关注公众号「天作之程」
# @Site    : 
# @File    : runningman_bili.py
# @Software: PyCharm

import pprint
import json
from bilibili_api import video, Verify
from bilibili_api.video import VideoInfo
from bilibili_api.video import Danmaku
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

# 格式化显示评论信息
pp = pprint.PrettyPrinter()

# 1、创建视频信息对象
verify = Verify(sessdata="632da748%2C1602337725%2Cc4863*41", csrf="bili_jct")
video_info = VideoInfo(bvid="BV1gC4y1h722", verify=verify)

# 2、获取视频信息、评论、弹幕
basic_info = video_info.get_video_info()
comments = video_info.get_comments()
danmu = video_info.get_danmaku()


# 3、词云可视化
# 3\1 jieba分词

danmu_list = []
for i in danmu:
    # print(i.text)
    danmu_list.append(i.text)

dm_str = " ".join(danmu_list)

words_list = jieba.lcut(dm_str)  # 切分的是字符串,返回的是列表
words_str = " ".join(words_list)

# 3\2 设置文本随机颜色
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])
    return "hsl({}, {}%, {}%)".format(h, s, l)

# 3\3 词云背景图
background_Image = np.array(Image.open('2.jpg'))

# 3\4词云对象
wc = WordCloud(
    background_color='white',
    mask=background_Image,
    font_path=r'./SourceHanSerifCN-Medium.otf',

    color_func=random_color_func,
    random_state=50,
)

# 3\5 生成词云，保存图片
word_cloud = wc.generate(words_str) # 产生词云
word_cloud.to_file("rm.jpg") #保存图片

# 3\6 显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()





