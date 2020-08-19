# coding: utf-8
# Author: An Chao

from PIL import Image
import numpy as np
import argparse
import os

def read_img(img_path):
    '''
    读取图片，并将其转化为包含alpha通道的“RGBA”格式图片。
    img_path：图片路径
    '''
    image=Image.open(img_path)
    image = image.convert('RGBA')
    size = image.size
    image = np.array(image)
    return size, image

def get_elesign(size,image):
    '''
    签名是黑色区域，像素值接近0。
    size：输入图片尺寸
    image：numpy array格式的图像
    '''
    points = []
    for j in range(size[0]):
        for i in range(size[1]):
            if image[i][j][0]>100 and image[i][j][1]>100 and image[i][j][2]>100:
                image[i][j][3] = 0
            else:
                image[i][j][0],image[i][j][1],image[i][j][2] = 0,0,0
                points.append((i,j)) 
    return points, image

def clip_image(points, image, save_path, offset=5):
    '''
    找到签名区域，返回电子签名。
    point：签名像素点位置列表
    image：处理过的签名图片
    offset：位置修正
    save_path：电子签名保存位置
    '''
    points = np.array(points).reshape((-1, 2))
    min_value = np.min(points,axis=0)
    x1,y1 = min_value[0]-offset,min_value[1]-offset
    max_value = np.max(points,axis=0)
    x2,y2 = max_value[0]+offset,max_value[1]+offset
    sign_area = image[x1:x2,y1:y2]
    sign_area = Image.fromarray(sign_area)
    sign_area.save(save_path)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="制作电子签名!")
    parser.add_argument("--image_path",type=str, help = "签名图片位置, dir or file")
    parser.add_argument("--offset",type=int, default=5, help = "签名向外扩张范围，默认为5个像素")
    arg = parser.parse_args()
    
    user_give = arg.image_path
    offset = arg.offset
    if os.path.isdir(user_give):
        imgs_name = os.listdir(user_give)
        for i,name in enumerate(imgs_name):
            if os.path.splitext(name)[-1] in [".jpeg",".JPG",".PNG",".jpg",".png"]:
                basename = os.path.splitext(name)[0]
                img_path = os.path.join(user_give,name)
                save_path = "ele_sign_"+basename+"_%d.png"%i
                size,image = read_img(img_path)
                points, image = get_elesign(size,image)
                clip_image(points, image,  save_path, offset)
    elif os.path.isfile:
        img_path = user_give
        save_path = "ele_sign.png"
        size,image = read_img(img_path)
        points, image = get_elesign(size,image)
        clip_image(points, image, save_path, offset)
