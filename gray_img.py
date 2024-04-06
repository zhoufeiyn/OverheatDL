import cv2
import os


listfile=os.listdir('infrared_fault/plate/')
for line in listfile:
    if line[-4:] == '.jpg':
        img = cv2.imread('infrared_fault/plate/'+line)
        img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imwrite('infrared_fault/plate_gray/'+line,img_gray)
