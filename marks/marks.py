# bounding_box.py


# add t_libs to path
import sys
import cv2
sys.path.append("../../t_libs")

from queriesfiles.uc_db_interface import *

level = 12
def mark():
    boxes = query_bounding_boxes(12)
    l = len(boxes)
    possibilities = 2**l
    for i in range(possibilities):
        img = cv2.imread("None.png")
        filtered = filter_boxes(boxes,i)
        for box in filtered:
            point1 = (int(box[0][0]),int(box[0][1]))
            point2 = (int(box[1][0]),int(box[1][1]))
            cv2.rectangle(img, point1, point2, (0, 0, 255))
        name = "{0:b}".format(i) + ".png"
        cv2.imwrite( name, img );

def filter_boxes(boxes,i):
    filtered = []
    bstring = "{0:b}".format(i)
    for i,c in enumerate(bstring):
        if c == '0':
            filtered.append(boxes[i])
    return filtered

mark()