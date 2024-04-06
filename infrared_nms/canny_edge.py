import cv2
import numpy as np


## test, easy to adjust
# if __name__ == '__main__':
#     def nothing(*arg):
#         pass
#     cv2.namedWindow('edge')
#     cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
#     cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)
#
#     cap = cv2.VideoCapture(0)
#     while True:
#         img = cv2.imread('./infrared_cut/001.jpg')
#         img = cv2.GaussianBlur(img, (3, 3), 0)
#
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
#         thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
#         edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
#         vis = img.copy()
#         vis = np.uint8(vis / 2.)
#         vis[edge != 0] = (0, 255, 0)
#         # cv2.imwrite('./box.jpg',vis)
#         cv2.imshow('edge', vis)
#         ch = cv2.waitKey(5) & 0xFF
#         if ch == 27:
#             break
#     cv2.destroyAllWindows()



#
# thrs1 = 1000
# thrs2 = 1550
# for i in range(1):
#     img=cv2.imread('./infrared_cut/'+'{:0>3}'.format(i) + '.jpg')
#     img= cv2.GaussianBlur(img,(3,3),0)
#     gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     cv2.imwrite('./infrared_box/gray.jpg',gray)
#     edge = cv2.Canny(gray,thrs1,thrs2,apertureSize=5)
#     vis = img.copy()
#     vis = np.uint8(vis/2.)
#     vis[edge!=0]=(0,225,0)
#     cv2.imwrite('./infrared_box/'+'{:0>3}'.format(i) + '.jpg',vis)
#
#
#
# # draw edge for all pictures and save it
# thrs1 = 1000
# thrs2 = 1550
# for i in range(22):
#     img=cv2.imread('infrared_fault/insulator/cut/'+'{:0>2}'.format(i+1) + '.jpg')
#     img= cv2.GaussianBlur(img,(3,3),0)
#     gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     edge = cv2.Canny(gray,thrs1,thrs2,apertureSize=5)
#     print ("edge shape:",edge.shape)
#     np.savetxt('infrared_detect/canny_insulator/'+'{:0>2}'.format(i+1) + '.txt',edge)
#     vis = img.copy()
#     vis = np.uint8(vis/2.)
#     vis[edge!=0]=(0,225,0)
#     cv2.imwrite('infrared_detect/canny_insulator/'+'{:0>2}'.format(i+1) + '.jpg',vis)



# # test the edge for one picture
# edge = np.loadtxt("./infrared_box/000.txt")
# column = edge.shape[1]
# row = edge.shape[0]
#
# num_edge = np.zeros((column))
# for i in range(column):
#     a=0
#     for j in range(row):
#         if edge[j,i] ==255.:
#             a+=1
#         num_edge[i]=a
# print num_edge
# print "num_edge shape:", num_edge.shape
# for i in range (column):
#     if i<=13 or i>=46:
#         edge[:,i]=0
# print edge
# np.savetxt('./infrared_cut/removesomebox0.txt',edge)
# img=cv2.imread('./infrared_cut/000.jpg')
# img= cv2.GaussianBlur(img,(3,3),0)
# # vis = img.copy()
# # vis = np.uint8(vis/2.)
# img[edge!=0]=(0,225,0)
# cv2.imwrite("./infrared_cut/removesomebox0.jpg", img)



#
# # test the edge for all picture
# for a in range(22):      ## work through each image
#     print ("the",a,"nd image.....")
#     edge = np.loadtxt('infrared_detect/canny_insulator/'+'{:0>2}'.format(a+1) + '.txt')
#     print ("edge shape:", edge.shape)
#     column = edge.shape[1]
#     row = edge.shape[0]
#     num_edge = np.zeros((column))
#     ## get the num of edges in each column of one image
#     for i in range(column):
#         b=0
#         for j in range(row):
#             if edge[j, i] ==255.:
#                 b+=1
#                 num_edge[i]=b
#     print ("num_edge in each column:", num_edge)
#     print ("num_edge shape:", num_edge.shape)
#     need_pos = np.where(num_edge == np.max(num_edge))
#     print ('max_pos:',[need_pos[0][0]])
#     ## get the maximum edge
#     half_max = num_edge[need_pos[0][0]]/2-1
#     print ('half of max:', half_max)
#
#     ## find more edges in continous column
#     for i in range(column):
#         if num_edge[i] < half_max:
#             num_edge[i]=0
#         else:
#             num_edge[i]=1
#     yes_ones={}
#     count=0
#     print ("become ones num_edge:",num_edge)
#     for i in range(column):
#         if num_edge[i] ==1:
#             count+=1
#         else:
#             if i>1 and num_edge[i-1]==1:
#                 yes_ones[i-1]=count
#             count=0
#     print ("yes_ones:",yes_ones)
#     max_one=max(yes_ones,key=yes_ones.get)
#     num_of_one=yes_ones[max_one]
#     print ("max_one, num_of_one:",max_one,num_of_one)
#     min_pos=max_one-num_of_one+1
#     max_pos=max_one
#     print ("min_pos:", min_pos)
#     print ("max_pos:", max_pos)
#     for k in range(column):
#         if k<=min_pos-1 or k>=max_pos+2:
#             edge[:,k]=0
#     np.savetxt('infrared_detect/canny_insulator/filter_edge/'+'{:0>2}'.format(a+1) + '.txt',edge)
#     img=cv2.imread('infrared_fault/insulator/cut/'+'{:0>2}'.format(a+1) + '.jpg')
#     img= cv2.GaussianBlur(img,(3,3),0)
#     img[edge!=0]=(0,225,0)
#     cv2.imwrite('infrared_detect/canny_insulator/filter_edge/'+'{:0>2}'.format(a+1) + '.jpg', img)


#
#
## find the heatest place in all pictures
# print ("find the heatest place in all pictures")
# for a in range(22):
#     print("...the",a,'image')
#     new_edge = np.loadtxt('infrared_detect/canny_insulator/filter_edge/'+'{:0>2}'.format(a+1) + '.txt') #filtered box have the edge
#     img = cv2.imread('infrared_fault/insulator/cut/'+'{:0>2}'.format(a+1) + '.jpg')
#     row = new_edge.shape[0]
#     column = new_edge.shape[1]
#     for i in range(row):
#         weizhi = np.where(new_edge[i,:]==255.0)[0]
#         print("find the edge pixel in each row:",weizhi)
#         if  len(weizhi)==0:
#             pass
#         else:
#             min = np.where(weizhi==np.min(weizhi))[0][0]
#             max = np.where(weizhi==np.max(weizhi))[0][0]
#             print("min and max of the edge:",min,max)
#             for j in range(weizhi[min]-1,weizhi[max]+1):
#                 new_edge[i,j]=255
#     img[new_edge==0]=(0,0,0) # image after the filtered box have been saved others discard
#     cv2.imwrite('infrared_detect/canny_insulator/hot_insulator/'+'{:0>2}'.format(a+1) + '.jpg',img)
#
#
#
# draw all boxes in all picture
print ("find the heatest place in all pictures")
for a in range(22):
    print ("the",a,"image")
    edged_img = cv2.imread('infrared_detect/canny_insulator/filter_insulator/'+'{:0>2}'.format(a+1) + '.jpg')
    img_gray = cv2.cvtColor(edged_img, cv2.COLOR_BGR2GRAY) # convert the img into gray
    img =cv2.imread('infrared_fault/insulator/cut/'+'{:0>2}'.format(a+1) + '.jpg')
    # im = edged_img[:,:,0]
    im = img_gray
    position = np.where(im==np.max(im))
    print ('size of img:',img.shape)
    print ('number of boxes:',len(position[0]))
    for i in range(len(position[0])):
        x=position[1][i] #all heatest box in one picture
        y=position[0][i]
        print ("(x,y):", (x,y))
        cv2.rectangle(img,(x-15,y-15),(x+15,y+15),(0,255,255),1)
    cv2.imwrite('infrared_detect/canny_insulator/hot_insulator/'+'{:0>2}'.format(a+1) + '.jpg',img)
