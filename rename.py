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
    total=786
    listfile=os.listdir(Img_dir) # 提取图像名称列表
    for line in listfile:  #把目录下的文件都赋值给line这个参数
        if line[-4:] == '.jpg':
            total+=1
            newname= '{:0>4}'.format(total)+'.jpg'
            print (newname)
            os.rename(os.path.join(Img_dir, line), os.path.join(Img_dir, newname))
rename_img('all_img3/')