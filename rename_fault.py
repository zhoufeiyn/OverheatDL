# -*- coding:utf-8 -*-
# 将图像数据生成lmdb数据集
import os
import sys
import numpy as np
import random


# 生成分类标签文件

def rename_img(Img_dir):
    # 重新命名Img,这里假设图像名称表示为000011.jpg、003456.jpg、000000.jpg格式，最高6位，前补0
    # 列出图像，并将图像改为序号名称
    start=16
    listfile=os.listdir(Img_dir) # 提取图像名称列表
    name_dict = {}
    for line in listfile:  #把目录下的文件都赋值给line这个参数
        if line[-4:] == '.JPG':
            start+=1
            name_dict[str(start)]=line
            newname= '{:0>2}'.format(start)+'.jpg'
            print (newname)
            os.rename(os.path.join(Img_dir, line), os.path.join(Img_dir, newname))
    file =open('infrared_fault/point/name.txt','a+')
    file.write(str(name_dict))
    file.close()

rename_img('infrared_fault/point/')