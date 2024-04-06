import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


# # double
# def cvt_allimg(org_path,save_path):
#     listfile = os.listdir(org_path)
#     for line in listfile:
#         if line[-4:]=='.jpg':
#             img = cv2.imread(org_path+line)
#             dst = cv2.bilateralFilter(img,0,40,5)
#             cv2.imwrite(save_path+line,dst)
#             print('done:'+line)
#
#
# cvt_allimg('test/','test_double/')


# gauss
def cvt_allimg(org_path,save_path):
    listfile = os.listdir(org_path)
    for line in listfile:
        if line[-4:]=='.jpg':
            img = cv2.imread(org_path+line)
            dst = cv2.GaussianBlur(img,(5,5),3)
            cv2.imwrite(save_path+line,dst)
            print('done:'+line)


cvt_allimg('train/','train_gauss/')
# x=cv2.Sobel(dst,cv2.CV_16S,1,0)
# y=cv2.Sobel(dst,cv2.CV_16S,0,1)
#
# absx=cv2.convertScaleAbs(x)
# absy=cv2.convertScaleAbs(y)
# dist=cv2.addWeighted(absx,0.5,absy,0.5,0)
#
# cv2.imshow('original_img',dst)
# cv2.imshow('y',absy)
# cv2.imshow('x',absx)
# cv2.imshow('dsit',dist)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


