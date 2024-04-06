import json
import cv2

with open('annotations/33.json',encoding='utf-8') as json_file:
    model= json.load(json_file)
all_anno= model["annotation"]["object"]
img_path=model["annotation"]["path"]
img = cv2.imread(img_path)
if type(all_anno)==dict:
    box = all_anno['bndbox']
    print(box)
    x1 = int(box['xmin'])
    y1 = int(box['ymin'])
    x2 = int(box['xmax'])
    y2 = int(box['ymax'])
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,255),2)
else:
    for anno in all_anno:
        box = anno["bndbox"]
        print(anno)
        x1 = int(box['xmin'])
        y1 = int(box['ymin'])
        x2 = int(box['xmax'])
        y2 = int(box['ymax'])
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,255),2)
cv2.imshow('img',img)
cv2.waitKey(0)
