# 《Python实用脚本》 V1.0

[TOC]

## 写在前面

no example say a what.  

Talk is cheap.  Show me the code.

你好，我是天作。

这份《Python实用脚本》V1.0，收录了《天作之程》公众号关于 Python 脚本的系列文章，经过重新编排、制作而成。

## 内容概览

目前收录的脚本如下：

- [用 Python 实现文件自动归类](https://mp.weixin.qq.com/s/7wqKjirvfCz1-xIwTOiBEQ)
- [用 Python 自动监测Github项目并打开网页](https://mp.weixin.qq.com/s/8LftVDvFGwNM0Rqm7dNr6A)
- [用 Python 帮你生成双色球](https://mp.weixin.qq.com/s/iGERT_SmrL1yK0RRyOqE0g)
- [用 Python 每日更换“必应图片”为“桌面壁纸”](https://mp.weixin.qq.com/s/18CzsemRc0Q2NM1LDNVRaQ)
- [用 Python 批量加水印](https://mp.weixin.qq.com/s/88WmbZFnXAEdAlIPB49jDA)
- [用 Python 暴力破解 zip压缩文件](https://mp.weixin.qq.com/s/vwEwdUu4Wnoj54euteHjGw)
- [用 Python 批量下载百度图片](https://mp.weixin.qq.com/s/wi70_LC2QGYq6_DswIYxZg)
- [用 Python 编写一个天气查询应用（可视化界面）](https://mp.weixin.qq.com/s/vNuN0-kANrlBCIQDlJ7M1A)

## 源码地址

> 重要的事情说三遍、
>
> 点击对应链接，在文中下载代码，或在对应文末找到源码下载地址。
> 点击对应链接，在文中下载代码，或在对应文末找到源码下载地址。
> 点击对应链接，在文中下载代码，或在对应文末找到源码下载地址。

## 支持一下

1. 以上的实用脚本均来自公众号《天作之程》，可扫描下面的二维码 (左) 关注，解锁更多你不知道的好玩的 Python！
2. 为了照顾各位的阅读体验，正文中没有任何多余的广告或者链接。本文档如果能帮助到你，也可以通过下面的二维码 (右) 打赏我！

![赞赏和联系](D:\03.公众号\头像、二维码等\赞赏和联系.jpg)

# 用 Python 实现文件自动归类



这几天和几个小伙伴，在一起做一个ppt。

做ppt之前有原版的ppt，和一个word大纲，在制作过程中，又不断添加图片、视频等素材，最终，整个目录变得杂乱不堪（见下图-处理之前）

那我想，可不可以做一个脚本实现文件按照扩展名自动分类呢?

这样，就可以相对轻松的找到文件了。

## 效果展示

使用方法很简单，只要把python脚本文件，放到待处理的文件夹目录下，运行python文件即可。

![image-20200725224459585](C:\Users\痴。\AppData\Roaming\Typora\typora-user-images\image-20200725224459585.png)


## 预备知识

这个脚本实现比较简单，我把涉及的知识点列了出来。

### **1）相对路径、绝对路径**

绝对路径就是最完整的路径。

>  'D:/code/gitpython.py'

相对路径的相对指的就是相对于当前文件夹路径，就是你编写的这个py文件所放的文件夹路径。

> 'gitpython.py' 或者 './gitpython.py'

### **2）os模块和shutil模块**

> os.listdir(path)    path--需要列出的目录路径

```python
import os

# 打开文件
path = "./"
dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
   print file

# 运行结果：
1.docx
1.jpg
1.pptx
```

> 移动文件（目录）    shutil.move("oldpos","newpos")

## 源码展示

```python
import os
import shutil

path = "./"  # py文件所在的文件夹下
file = os.listdir(path)  # 列出当前文件夹的所有文件

# 循环遍历每个文件
for f in file:
    # print(f)

    # 以扩展名为名称的子文件夹
    folder_name = path + f.split(".")[-1]

    # 如果不存在该目录，先创建，再移动文件
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

        # 举例：这里的f为 1.png 等同于 ./1.png (因为是相对路径)
        shutil.move(f, folder_name)

    # 直接移动文件
    else:
        shutil.move(f, folder_name)
```

# 用 Python 自动监测Github项目并打开网页

## 写在前边

Github项目的更新，提醒方式是邮箱，而大家平时都是不怎么用邮箱的！

那么，如果项目更新，我们怎么能及时的发现，并打开项目主页呢？

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMVt1U9at8uOS7uJGHxibbwgAGyNoTXe7uoTiba4iccOEsGFqYlRkvFoKe230bBSkRRYtJFdQIWdvAQdw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

项目地址：

> https://github.com/kenwoodjw/python_interview_question

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMVt1U9at8uOS7uJGHxibbwgAvtxrbVsMFK6gVibYibKXHdp1g9XE7sOyC1goyYMmJWiaJib7RwKq2RG8hw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 实现过程

### 1）获取数据

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMVt1U9at8uOS7uJGHxibbwgAnSzbtBnV9W3iaXh2h0FtNevVias5jjYeav4Bt2OR4tKMcGHlCVAmgicmw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Github官方提供了详细的数据接口，并且数据是以Json字符串的方式保存的。

项目的数据地址：

> https://api.github.com/repos/kenwoodjw/python_interview_question

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMVt1U9at8uOS7uJGHxibbwgAWvzGoVjMU6UoDrm1H1CJvzmKAiaEqhicbMvsgBgpVvOAbUiahfiasqHElQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

每一个项目的数据地址，类似于本地磁盘目录。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMVt1U9at8uOS7uJGHxibbwgAWTaY2PRg43ib8kEIiasMDGpGDpPu63Do89Utqs1RqX6MVKjtNgyqft3A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

我们通过数据接口的url地址，就可以获取到更新时间。

```python
import request

# 1.Github项目及API接口数据
api = 'https://api.github.com/repos/kenwoodjw/python_interview_question'
web_page = "https://github.com/kenwoodjw/python_interview_question

# 2.发送请求，获取数据
all_info = requests.get(api).json()

# 3.解析想要的数据，并打印
cur_update = all_info['updated_at']
print(cur_update)
```

### 2）定时监测数据变化

### 3）打开网页

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMVt1U9at8uOS7uJGHxibbwgAzoSGpksnaM7qaZOq1ibUM29XjVl7VARk081cJbBht7f86JibFTyRNEXg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

设置一个循环，每隔10分钟获取一次update_at的数据，如果前后时间不一致，说明数据更新，并自动打开项目主页。

```python
while True:

    all_info = requests.get(api).json()
    cur_update = all_info['updated_at']
    print(cur_update)

    # 假设第一次运行之前，不知道上次的更新时间
    # 如果last_update 为 none，会执行下面的语句，把当前的时间给到上次时间
    if not last_update:
        last_update = cur_update

    # 第一次两个时间相等，不会执行
    # 假设10分钟后，cur_update更新，那么就会自动打开网页
    # 接下来，把 当前时间 赋值 给上次时间
    # 开始新一轮的监测
    if last_update < cur_update:
        webbrowser.open(web_page)
        last_update = cur_update

    # 间隔 10分钟，再次while循环，观察新的更新时间是否发生变化
    time.sleep(600)
```

# 用 Python 帮你生成双色球号码


![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMWH1eWfbbhibYGagAwiarYIRyLqjyXwfjeSqcIeaCGJzPHYfySzNLGVugCJjA27iazfRDpZGxSd4iciaDw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 双色球

顾名思义，就是两种颜色的球，红色和蓝色。

红球从1-33中取出6个，篮球从1-16取出1个。注意，红球为不放回采样，也就是不能有重复的。

## 用python生成双色球

> 其实很简单，只用到一个随机数模块。
> 先说红球共6个，每次从1-33个数中随机选择一个，且不重复的情况下，添加到一个列表中；蓝球从1-16个球中随机选择一个即可。

## 源码解析

```python
import random

red_ball = []
while True:
    # 生成一位随机数
    a = random.randint(1, 34)

    # 避免重复
    if a not in red_ball:
        # 把不重复的数字，添加到列表
        red_ball.append(a)

        # 返回6个不重复的红球
        if len(red_ball) == 6:
            print("红球:", red_ball)
            break

# 生成蓝球
blue_ball = random.randint(1, 17)
print("蓝球:", blue_ball)

# 运行结果：
红球: [17, 28, 24, 19, 29, 23]
蓝球: 9
```

## 我是小结

运行上面程序，就会随机生成一组“双色球”啦。

不过你说，这样选出来的数据有啥用，真的也只能在平淡的生活多了那么一丝期待。

还是踏踏实实学编程吧！

# 用 Python每日更换“必应图片”为“桌面壁纸”

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMX2JzsbYH6ACkzUU92icWQMVPUz7YDibxNDBI7b1vtia5qpjm4r2ow0VnFaQESznBZ5tUBr2bNZUiaapQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

不少同学都知道，必应每天都会更新壁纸，都十分漂亮，有时候还十分惊艳，同时还会根据每个地区的特色应用不同的壁纸。

那么，如何让自己的电脑每天同步必应每日图片作为桌面背景呢？

下面用python脚本抓取必应每日图片，并实现桌面壁纸的每天自动切换。

## 思路整理

1. 通过网页，获取图片地址
2. 保存图片到绝对路径
3. 设置该绝对路径所指向的图片为壁纸
4. 批处理壁纸自动切换

需要用到的模块：

```python
import urllib.request
import requests
import os.path
import ctypes
```

## 获取图片地址

这个函数主要通过requests模块，根据必应的网页地址，获取到当日图片的最终img地址。

```python
# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url="https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)
    img_url = r.url  # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url
```

## 保存图片到本地

这个函数的作用就是把图片保存到你自己设置的一个目录下，并返回当前目录的绝对地址。

```python
def save_img(img_url, dirname):
    # 保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print('文件夹', dirname, '不存在，重新建立')
            # os.mkdir(dirname)
            os.makedirs(dirname)
        # 获得图片文件名，包括后缀
        basename = "bing.jpg"
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)
    print("Save", filepath, "successfully!")

    return filepath
```

## 设置该绝对路径所指向的图片为壁纸

通过之前获得的图片所在的绝对路径，把该图片设置为桌面壁纸。

```python
def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
```

## 运行代码的main函数

```python
def main():
    dirname = "D:\\bingImg"  # 图片要被保存在的位置
    img_url = get_img_url()
    filepath = save_img(img_url, dirname)  # 图片文件的路径
    set_img_as_wallpaper(filepath)
```

运行效果（此时，可以回看一下文章首图中的左上角那张图片）

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMX2JzsbYH6ACkzUU92icWQMVUcoTbZLBjydtlL0THgFhSibJnf2loXXg6nJsbM8wpuh2yYAib6UicUIFg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **批处理自动更换壁纸**

此时，可以在python脚本的同一目录下创建名为py_bingying.bat的批处理文件，批处理内容如下：

```python
@echo off
del g:\bingImg\*.jpg
python SetBingImgAsWallpaper.py
```

第二行在运行python脚本前先删除前一天下载的必应图片，这样就实现了旧壁纸的每日清理，最大限度节省了存储空间。

第三行为运行上面的python脚本。如何实现壁纸的自动切换呢，这里采用开机运行上面的批处理程序的方法。

复制上面创建的批处理文件，到下方目录下，右键-粘贴为快捷方式。

这样就实现了开机启动批处理程序，自动清除和更新壁纸。

>C:\User\yourname\AppData\Roaming\Microsoft\Windows\开始菜单\程序\启动

每次开机都执行一遍更换壁纸的操作还不够完美的话，可以用Windows任务计划程序来添加任务，设置每天指定时间点运行批处理程序。

# 用 Python 批量加水印

为了保护版权，需要给作品中的图片加上水印。

厉害的水印是下图这个样子的。

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMXqrgrv8TQxJczsoiba4TPG939cJnGW89orKAibfkEf0KXh1AlNCmeOywWQBj1sNPEMPrRQ4uHcBajw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

今天就来带大家，用Python把图片批量加上水印。

有的小伙伴可能会说，网上也有很多工具有类似的功能，何必重复造轮子，嗯，我猜到了。

先看看用Python做这个工具的特点吧：

- 可以设置字体（大小）
- 可以设置角度
- 可以设置透明度
- 可以设置颜色
- 可以批量处理
- 可以设置水印的间隔

## Github项目

这个工具，其实是一个大神开源在Github上的项目，我只是个搬运工。

贴个地址：

>https://github.com/2Dou/watermarker

代码可以从Github上下载，也可在“文末”找到下载方式。

重要的事说三遍：

>记得把文件夹放在英文目录下
>记得把文件夹放在英文目录下
>记得把文件夹放在英文目录下

下载之后的目录结构是这样的：

- font
- input
- output
- marker.py
- README.md

“字体”文件夹，存放的是“青鸟华光简琥珀.ttf ”

“input”文件夹，存放的是你要处理的图片，那么“output”自然就是输出的结果了

“marker.py”是实现功能的脚本文件，

“README.md”是一个介绍文档

值得注意的有两点：

1、把“青鸟华光简琥珀.ttf ”改为“bird.ttf”,名字不重要，只要是换成英文。另外，你也可以把你本地的字体（你喜欢的）替换过来。

2、在“marker.py”脚本中，把对应的字体名称替换掉。

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMXqrgrv8TQxJczsoiba4TPG9xgCU1qFdTucgdU7CU1eDBkaichsC5vjicLACqniaAic4754tqHy739zZvA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 看看效果

到这里，可以运行试试了。

在“marker.py”的同级目录下，打开Terminal/cmd，输入如下命令：

>python marker.py -f ./input/test.png -m 天作之程

- -f参数，输入图片的位置（可以是具体的一张照片，也可以是整个文件夹）
- -m参数，你要添加的内容

另外，上边提到的功能参数：

- -o 参数，指定输出水印文件的位置，默认为output文件夹。
- -c 参数，指定水印的颜色，默认值为黄色，#8B8B1B
- -s 参数，指定水印之间的空隙，默认值为75
- -a 参数，指定水印的旋转角度，默认值30度。
- --size参数，指定水印文本字体大小，默认值为50。
- --opacity参数，指定透明度，默认为0.15，数值越小越透明。

这里放一个我觉得比较舒服的参数：

>python marker.py -f ./input -m 天作之程 -c#232862 --opacity 0.05

如果你觉得颜色不够完美，可以从下面的链接找到颜色对应的16进制，copy过来就行。

>https://www.sioe.cn/yingyong/yanse-rgb-16/

贴个效果图：

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMXqrgrv8TQxJczsoiba4TPG99FEcbWlSCsF8DJJIpgaMelLTZXK7Yic6zcQe5GibsPYVMhzI6Emw4OTQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

介绍就到这里了，有运行有问题的小伙伴，欢迎留言或者私聊。

## 源码下载

可在后台回复“水印”下载源码。

原创不易，“在看” 和 “留言” 就是对我最大的支持和鼓励啊！

## 参考文献

> https://zhuanlan.zhihu.com/p/138732523

#  用 Python 破解 zip压缩文件

![image-20200725221643841](C:\Users\痴。\AppData\Roaming\Typora\typora-user-images\image-20200725221643841.png)

曾经，在网上下载过一份“学习资料”，zip格式的一份不小的压缩文件。

费劲巴拉的从“某盘”下载下来，却发现解压需要“密码”，顿时心里有句不当讲的话...

为了破解压缩文件的密码，我在搜索引擎输入“python zip”两个关键词。

经过过一番总结，发现破解的思路都是一样的（穷举），也就是暴力破解。

过程如下：

1. 建立密码字典（常用密码）
2. 尝试用每一个密码，来解压文件
3. 解压成功，跳出循环

## 密码字典

比如，现在一个纯数字的六位密码“050825”

可以从依次遍历“000000”到“999999”，把所有的结果保存到txt文件。

这样的缺点就是比较死板，只能是6位数字，另外就是比较占内存。

于是，有个大神写了个“字典生成器”，你需要做的是传入两个参数“字典的组成元素”和“密码的长度列表”

比如，纯数字的“050825”，你就传入如下的参数：

- [0,1,2,3,4,5,6,7,8,9]，数字就这9个
- [6]，密码的长度

如此，便可按你的要求得到密码的Python 生成器。我们知道，生成器是不占用内存的。

如果数字不过瘾，比如有的密码是字符串。可以考虑在第一个参数中，加入“a-z”和“A-Z”

## zipfile加压文件

zipfile模块是python自带的，用于对zip文件的读、写、追加、解压操作等。

“解压”主要是用到ZipFile对象的extractall()方法

extractall(path=None, members=None, pwd=None)方法主要有三个参数。

我们来看一下每个参数的含义：

- path 指定解压后文件的存储位置
- members（可选）指定Zip文件中要解压的文件，这个文件名称必须是通过namelist()方法返回列表的子集
- pwd 指定Zip文件的解压密码（编码“utf-8”）

贴个代码：

```python
import zipfile 
try:
    with zipfile.ZipFile('test.zip') as zFile:     
        # 创建ZipFile对象
        # 解压文件
        zFile.extractall(path='./',pwd=b'1234')
        print('解压成功!')
except:
    print('解压失败')
```


## 进度条可视化

上次的进度条，这次派上用场了，关于进度条，本程序使用 tqdm扩展库。

贴个代码：

代码中的tqdm有两个参数：

- 1、密码迭代器
- 2、密码总个数

```python
for pwd in tqdm(chain.from_iterable(all_passwd(dictionaries, maxlen) for maxlen in lengths), total=total):
    if extract(zfile, pwd):    # 记得extract函数返回的是bool类型的哦
        break
```

这是破解的结果：

```python
5%|▌         | 50691/1000000 [00:04<01:23, 11389.24it/s]
Password is: 050825
```

bingo，4s结束战斗。

## 我是小结

如果是密码相对简单的，值得一试。如果过于复杂的话，假设你有时间，可以等一等，毕竟有进度条了（手动狗头），等着也不会那么枯燥。

下回见...

# 我是怎么批量下载百度图片的，当然是用 Python了！

![image-20200725224840161](C:\Users\痴。\AppData\Roaming\Typora\typora-user-images\image-20200725224840161.png)

为了做一个图像分类的小项目，需要制作自己的数据集。要想制作数据集，就得从网上下载大量的图片，再统一处理。

这时，一张张的保存下载，就显得很繁琐。那么，有没有一种方法可以把搜索到的图片直接下载到本地电脑中呢？

有啊！用python吧！

我以“泰迪”、“柯基”、“拉布拉多”等为关键词，分别下载了500张图片。下一篇，我打算写一个小狗分类器，不知道各位意见如何！

## 结果演示

![img](https://mmbiz.qpic.cn/mmbiz_gif/ltD0oohZnMWfiaBPKbXztoZXbZicJ8iaBkJCU0YzAaehJJ3yWcoBKuHzYknJWpshZVO5mjj95Ig2Qe35liaMtXpRzw/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## 编写思路

### **1.获取图片的url链接**

首先，打开百度图片首页，注意下图url中的index

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMWfiaBPKbXztoZXbZicJ8iaBkJrCjAgRk0ibZ5fa6jnrlDFxMJH51Aib9sKLRAHq2E7Mjd1Y42OtutvJ1Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

接着，把页面切换成传统翻页版（flip），因为这样有利于我们爬取图片！

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMWfiaBPKbXztoZXbZicJ8iaBkJrCjAgRk0ibZ5fa6jnrlDFxMJH51Aib9sKLRAHq2E7Mjd1Y42OtutvJ1Q/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

对比了几个url发现，pn参数是请求到的数量。通过修改pn参数，观察返回的数据，发现每页最多只能是60个图片。

注：gsm参数是pn参数的16进制表达，去掉无妨

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMWfiaBPKbXztoZXbZicJ8iaBkJWYp9smKCyovFQSSoSSGbVqZiczfKR7rbS5zgs1BwUV5iaXcSmb4ym6mg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

然后，右键检查网页源代码，直接（ctrl+F）搜索 objURL

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMWfiaBPKbXztoZXbZicJ8iaBkJBgHKevn92jzHNtmr5X4y0CO9IkibOxWnE6gibW0KvEichLuRbWVRdLvNw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这样，我们发现了需要图片的url了。

### **2.把图片链接保存到本地**

现在，我们要做的就是将这些信息爬取出来。

注：网页中有objURL，hoverURL…但是我们用的是objURL，因为这个是原图

那么，如何获取objURL？用正则表达式！

那我们该如何用正则表达式实现呢？其实只需要一行代码…

```
results = re.findall('"objURL":"(.*?)",', html) 
```

## 核心代码

### 1.获取图片url

```python
# 获取图片url连接
def get_parse_page(pn,name):

    for i in range(int(pn)):
        # 1.获取网页
        print('正在获取第{}页'.format(i+1))

        # 百度图片首页的url
        # name是你要搜索的关键词
        # pn是你想下载的页数

        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d' %(name,i*20)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4843.400 QQBrowser/9.7.13021.400'}

        # 发送请求，获取相应
        response = requests.get(url, headers=headers)
        html = response.content.decode()
        # print(html)

        # 2.正则表达式解析网页
        # "objURL":"http://n.sinaimg.cn/sports/transform/20170406/dHEk-fycxmks5842687.jpg"
        results = re.findall('"objURL":"(.*?)",', html) # 返回一个列表

        # 根据获取到的图片链接，把图片保存到本地
        save_to_txt(results, name, i)
```

### 2.保存图片到本地

```python
# 保存图片到本地
def save_to_txt(results, name, i):

    j = 0
    # 在当目录下创建文件夹
    if not os.path.exists('./' + name):
        os.makedirs('./' + name)

    # 下载图片
    for result in results:
        print('正在保存第{}个'.format(j))
        try:
            pic = requests.get(result, timeout=10)
            time.sleep(1)
        except:
            print('当前图片无法下载')
            j += 1
            continue

        # 可忽略，这段代码有bug
        # file_name = result.split('/')
        # file_name = file_name[len(file_name) - 1]
        # print(file_name)
        #
        # end = re.search('(.png|.jpg|.jpeg|.gif)$', file_name)
        # if end == None:
        #     file_name = file_name + '.jpg'

        # 把图片保存到文件夹
        file_full_name = './' + name + '/' + str(i) + '-' + str(j) + '.jpg'
        with open(file_full_name, 'wb') as f：
            f.write(pic.content)

        j += 1
```

核心代码：

```python
    f.write(pic.content)
    pic = requests.get(result, timeout=10)
```

### 3.主函数

```python
# 主函数
if __name__ == '__main__':

    name = input('请输入你要下载的关键词：')
    pn = input('你想下载前几页（1页有60张）:')
    get_parse_page(pn, name)
```

## 使用说明

```python
# 配置以下模块
import requests 
import re
import os
import time

# 1.运行 py源文件
# 2.输入你想搜索的关键词，比如“柯基”、“泰迪”等
# 3.输入你想下载的页数，比如5，那就是下载 5 x 60=300 张图片
```

## 我是总结

我把文章中的一些重要的内容，总结在了下面的一张图里，方便大家保存、查阅。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMWfiaBPKbXztoZXbZicJ8iaBkJmq9mzPZTAaLSmymm8ROlplgVLAFoo3SjibXAuuGjFR69icNLxPwT7ZMQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

# 用 Python 编写一个自己的天气查询应用（可视化界面）

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ltD0oohZnMUTehibZCicZOBpa0VYJPdIeF2P27lSgBTQQiaHWgiaq4iaTKCwBoyrVZkvjfnevDOBic6roeOdAunlQXiaQ/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 效果预览

![img](https://mmbiz.qpic.cn/mmbiz_gif/ltD0oohZnMVFcZvZTvINIkVgsKZYGEV4ib3lcSnEaGbRglqfvY3EicVicaOaThMWK6nrT6EGZfUx8x54mGoVcwxHg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

## 获取天气信息

使用python获取天气有两种方式:

1. 是通过爬虫的方式获取天气预报网站的HTML页面，然后使用xpath或者bs4解析HTML界面的内容。
2. 另一种方式是根据天气预报网站提供的API，直接获取结构化数据，省去了解析HTML页面的步骤。

本例使用的是第二种方式，请求地址为：

> http://wthrcdn.etouch.cn/weather_mini?citykey=城市代码

部分城市代码对应：

> 北京 101010100
>
> 天津 101030100
>
> 上海 101020100

浏览器返回的天津气温情况如下，该信息其实就是一个JSON字符串，格式化之后的样子如下所示：

```PYTHON
{
    "data": {
        "yesterday": {
            "date": "1日星期五",
            "high": "高温 17℃",
            "fx": "东北风",
            "low": "低温 8℃",
            "fl": "<![CDATA[<3级]]>",
            "type": "多云"
        },
        "city": "北京",
        "forecast": [
            {
                "date": "2日星期六",
                "high": "高温 14℃",
                "fengli": "<![CDATA[<3级]]>",
                "low": "低温 8℃",
                "fengxiang": "北风",
                "type": "小雨"
            },

        ],
        "ganmao": "昼夜温差较大，较易发生感冒，请适当增减衣服。体质较弱的朋友请注意防护。",
        "wendu": "12"
    },
    "status": 1000,
    "desc": "OK"
}
```

获取天气的主要代码如下：

```python
# cityCode 替换为具体某一个城市的对应编号# 1、发送请求，获取数据
url = f'http://wthrcdn.etouch.cn/weather_mini?citykey={cityCode}'
res = requests.get(url)
res.encoding = 'utf-8'res_json = res.json()

# 2、数据格式化
data = res_json['data']
city = f"城市：{data['city']}\n"  
# 字符串格式化的一种方式 f"{}" 通过字典传递值

today = data['forecast'][0]
date = f"日期：{today['date']}\n"  # \n 换行
now = f"实时温度：{data['wendu']}度\n"
temperature = f"温度：{today['high']} {today['low']}\n"
fengxiang = f"风向：{today['fengxiang']}\n"
type = f"天气：{today['type']}\n"
tips = f"贴士：{data['ganmao']}\n"

result = city + date + now + temperature + fengxiang + type + tips

print(result)

```

## 界面的实现

### 1、使用Qt Designer绘制窗口，保存为ui文件

![img](https://mmbiz.qpic.cn/mmbiz_png/ltD0oohZnMVFcZvZTvINIkVgsKZYGEV4N6je5Oa7EZQw7MnlAj8UBS5oHCKxtwlEUFxOhBbOEtQkK8eLP4VuSg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

### 2、把ui文件转为py文件

- 在生成的ui文件目录下，打开cmd

- 输入以下命令（注意替换名称）

```
pyuic5 -o destination.py source.ui
```

### 3、信号与槽函数的连接

```python
# 1、清空按钮与对应函数连接
clearBtn.clicked.connect(widget.clearResult)

# 2、查询按钮与对应函数连接
queryBtn.clicked.connect(widget.queryWeather)
```

### 4、调用主窗口类

```python
import sys     
from PyQt5.QtWidgets import QApplication , QMainWindow
from WeatherWin import Ui_widget
import requests
import json

class MainWindow(QMainWindow ):
    def __init__(self, parent=None):    
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_widget()
        self.ui.setupUi(self)

        # 通过文本框传入想要搜索的城市名称:天津
        cityName = self.ui.weatherComboBox.currentText()

        # 获取天气部分省略
        # 在文本框显示查询结果
        self.ui.resultText.setText(result)

    def clearResult(self):
        print('* clearResult  ')
        self.ui.resultText.clear()  

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    win = MainWindow()  
    win.show()  
    sys.exit(app.exec_()) 
```