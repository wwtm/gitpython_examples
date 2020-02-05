#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 7:46
# @Author  : T.M.
# @File    : gitpython_词云.py
# @Software: PyCharm

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import jieba

# 停用词
words = pd.read_csv('stopwords_zh.txt', error_bad_lines=False, engine ='python', names=['stopword'])
# print(words)
stopwords = set('')
stopwords.update(words['stopword'])

# 获得wordcloud 需要的 文本格式
with open("want_after.txt", "r", encoding='utf-8') as f:
     text = ' '.join(jieba.cut(f.read(),cut_all=False))
     # print(text)

backgroud_Image = plt.imread('豆瓣.jpg')  # 背景图

# 词云的一些参数设置
wc = WordCloud(
      background_color='white',
      mask=backgroud_Image,
      font_path='SourceHanSerifCN-Medium.otf',
      max_words=200,
      max_font_size=200,
      min_font_size=8,
      random_state=50,
      stopwords=stopwords
    )


# 生成词云
word_cloud = wc.generate_from_text(text)

# 看看词频高的有哪些
process_word = WordCloud.process_text(wc, text)
sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
sort_after = sort[:50]
print(sort_after)

# 把数据存成csv文件
df = pd.DataFrame(sort_after)
# 保证不乱码
df.to_csv('sort_after.csv', encoding='utf_8_sig')

plt.imshow(word_cloud)
plt.axis('off')

wc.to_file('结果.jpg')

