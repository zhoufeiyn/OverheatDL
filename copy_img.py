import os
import cv2


def copy_img(read_dir,save_dir):
    filelist =os.listdir(read_dir)
    for item in filelist:
        if item.endswith('1166.jpg'):
            save_path = os.path.join(save_dir,item)
            read_path = os.path.join(read_dir,item)
            img = cv2.imread(read_path)
            cv2.imwrite(save_path,img)


copy_img('four_classes/train/','four_classes/not_sure/train/')