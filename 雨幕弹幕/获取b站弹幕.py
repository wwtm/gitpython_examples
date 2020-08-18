import requests
from lxml import etree
import pandas as pd
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import random


# 许嵩新歌《雨幕》
url = 'https://comment.bilibili.com/123072475.xml'

response = requests.get(url)
xml = etree.fromstring(response.content)
dm = xml.xpath("/i/d/text()")
print(dm)  # list

# 把列表转换成 dataframe
dm_df = pd.DataFrame(dm, columns=['弹幕内容'])
print(dm_df)

# 存到本地
# 解决了中文乱码问题
# dm_df.to_csv('雨幕-弹幕.csv', encoding='utf_8_sig')

dm_str = " ".join(dm)
words_list = jieba.lcut(dm_str)  # 切分的是字符串,返回的是列表
words_str = " ".join(words_list)

# 设置文本随机颜色
def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h, s, l = random.choice([(188, 72, 53), (253, 63, 56), (12, 78, 69)])
    return "hsl({}, {}%, {}%)".format(h, s, l)

backgroud_Image = plt.imread('1.jpg')
wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='E:\03.设计相关\字体\宋体字推荐\思源宋体\SourceHanSerifCN-Medium.otf',

    max_words=2000,
    max_font_size=100,
    min_font_size=10,
    color_func=random_color_func,
    random_state=50,
)

word_cloud = wc.generate(words_str) # 产生词云
word_cloud.to_file("yumu.jpg") #保存图片

# 显示词云图片
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
