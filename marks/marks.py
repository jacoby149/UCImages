# bounding_box.py


# add t_libs to path
import sys
import cv2
import tlibs.queriesfiles as q

level = 12


def mark():
    boxes = q.query_bounding_boxes(12)
    l = len(boxes)
    possibilities = 2**l
    for i in range(possibilities):
        img = cv2.imread("None.png", cv2.IMREAD_UNCHANGED)
        bstring = "{0:b}".format(i)
        while len(bstring) < l:
            bstring = "0" + bstring
        filtered = filter_boxes(boxes, bstring)
        for box in filtered:
            point1 = (int(box[0][0]), int(box[0][1]))
            point2 = (int(box[1][0]), int(box[1][1]))
            cv2.rectangle(img, point1, point2, (0, 0, 255, 255))
        name = bstring + ".png"
        cv2.imwrite(name, img)


def filter_boxes(boxes, bstring):
    filtered = []
    for i, c in enumerate(bstring):
        if c == '0':
            filtered.append(boxes[i])
    return filtered


mark()
