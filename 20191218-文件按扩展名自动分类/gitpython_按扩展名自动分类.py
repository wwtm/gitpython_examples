import os
import shutil

"""
1.打开指定文件夹（目录）
2.遍历文件
3.如果有文件后缀名的文件夹，直接移动到那个文件夹
4.如果没有，先创建一个文件夹，在移动文件
"""

path = "./"  # py文件所在的目录下
file = os.listdir(path)


for f in file:
    # print(f)

    folder_name = path + f.split(".")[-1]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        shutil.move(f, folder_name)
    else:
        shutil.move(f, folder_name)

