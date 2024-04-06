import numpy as np
import cv2
for num_img in range(6):
    print ("the", num_img, "image")
    edged_img = cv2.imread('./infrared_box/after_filteredbox/' + '{:0>3}'.format(num_img) + '.jpg')
    cut_gray = cv2.cvtColor(edged_img, cv2.COLOR_BGR2GRAY)  # convert the img into gray
    img = cv2.imread('./infrared_cut/' + '{:0>3}'.format(num_img) + '.jpg')
    past_temp = 0
    now_temp = 0
    # find the edge box of the image to use IOU
    column = edged_img.shape[1]
    row = edged_img.shape[0]
    find_edge = np.zeros(column)
    for c in range(column):
        for r in range(row):
            if cut_gray[r,c]!=0:
                find_edge[c]=c
                break
            else:
                find_edge[c]=2
    left=np.where(find_edge==np.min(find_edge))[0][0]
    right=np.where(find_edge==np.max(find_edge))[0][0]
    print ("find_edge",find_edge)
    print ("(left,right):",(left,right))
    # confirm that there are at most 4 points in one pic
    for num_point in range(4):
        position = np.where(cut_gray == np.max(cut_gray))
        now_temp = cut_gray[position[0][0], position[1][0]]
        print ("now_temp:",now_temp)
        if num_point==0 or past_temp-now_temp<20:
            print ("the", num_point,"nd point")
            past_temp = now_temp
            print ('no.',num_point, 'heatest in img', num_img, ':', past_temp)
            # draw the box
            x = position[1][0]
            y = position[0][0]
            print ("(x,y):",(x,y))
            # using iou max(left,x-8) and min(right,x+8)
            # l=max(left+7,x-8)
            # r=min(right,x+8)
            # if (r-l)/16>0:
            cv2.rectangle(img, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 225), 2)
            # using nms let the surroundings be gray
            cut_gray[y-20:y+20,:]=0
            # cv2.imwrite('./infrared_box/using_nms/' + '{:0>3}'.format(num_point) + '.jpg',cut_gray)
        else:
            break
    cv2.imwrite('./infrared_box/using_iou/' + '{:0>3}'.format(num_img) + '.jpg',img)
