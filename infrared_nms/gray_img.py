import cv2
import numpy as np
import matplotlib.pyplot as plt

# find the heastest place in every picture
for i in range(22):
    img = cv2.imread('infrared_fault/point_gray/cut/'+'{:0>2}'.format(i+1) + '.jpg')
    print(img.shape)
    im = img[:,:,0]

    position = np.where(im==np.max(im))
    print ("size of img:",img.shape)
    print ("num of boxes:",len(position[0]))
    for a in range(len(position[0])):
        x=position[1][a]
        y=position[0][a]
        print ("(x,y):", (x,y))
        if a!=0 and (x>=position[1][a-1]-10 or x<=position[1][a-1]+10) and im[y,x]<250:
            pass
        else:
            rbg_img=cv2.imread('infrared_fault/point/cut/'+'{:0>2}'.format(i+1) + '.jpg')
            cv2.rectangle(rbg_img,(x-15,y-15),(x+15,y+15),(0,255,255),1)
            cv2.imwrite('infrared_detect/point/'+'{:0>2}'.format(i+1) + '.jpg', rbg_img)

#
# # draw all boxes in one picture
# img = cv2.imread('./infrared_cut/try1.jpg')
# im = img[:,:,0]
# position = np.where(im==np.max(im))
# print 'size of img:',img.shape
# print 'number of boxes:',len(position[0])
# for i in range(len(position[0])):
#     x=position[1][i]
#     y=position[0][i]
#     print "(x,y):", (x,y)
#     cv2.rectangle(img,(x-5,y-5),(x+5,y+5),(0,255,255),1)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('./infrared_cut/tryheat1.jpg',img)



# # creat new img and draw box on it
# img= np.ones((240,320,3))*225
# cv2.imwrite('./baise.jpg',img)
# cv2.rectangle(img,(181,297),(201,317),(0,255,255),2)
# cv2.rectangle(img,(0,0),(10,10),(0,255,255),2)
# cv2.rectangle(img,(0,0),(20,20),(0,255,255),2)
# cv2.imshow("tu",img)
# cv2.waitKey(0)



# # convert img into gray
# for i in range(10):
#     img = cv2.imread('./infrared_cut/'+'{:0>3}'.format(i) + '.jpg')
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     cv2.imwrite('./infrared_cut_gray/'+'{:0>3}'.format(i) + '.jpg',img_gray)



# # test with one place
# x=position[0][0]
# y=position[1][0]
# cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,225),2)
# cv2.imshow("image",img)
# cv2.waitKey(0)