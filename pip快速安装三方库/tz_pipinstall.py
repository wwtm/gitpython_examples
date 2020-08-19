import os

mirrors = {"清华":"https://pypi.tuna.tsinghua.edu.cn/simple ",
           "阿里云":"http://mirrors.aliyun.com/pypi/simple ",
           "中科大":"https://pypi.mirrors.ustc.edu.cn/simple ",
           "豆瓣":"http://pypi.douban.com/simple "
           }

print("清华 | 阿里云 | 中科大 | 豆瓣")
web = input("请输入您想选择的镜像源名称（推荐使用清华）：")
lib = input("请输入您想安装的扩展库名称：")

# 选择其中一个镜像源，下载安装库
os.system("pip3 install -i "+ mirrors[web] + lib)
