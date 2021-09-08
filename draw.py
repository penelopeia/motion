import cv2
import numpy as np

def corner_gradient(image, color="grey"):
    if color == "red":
        c_ind = 2
    elif color == "green":
        c_ind = 1
    elif color == "blue":
        c_ind = 0
    else:
        c_ind = None
    h, w = image.shape[:2]
    row = []
    color = 0
    frame = np.copy(image)
    for n in range(h):
        for r in range(w):
            color += 1
            if c_ind is not None:
                bgr = [0,0,0]
                bgr[c_ind] = color
                frame[n, r] = (bgr[0], bgr[1], bgr[2])
            else:
                frame[n, r] = (color,color,color)
    return frame

def fill_gradient(image, color="grey"):
    c_ind = 0
    if color == "red":
        c_ind = 2
    elif color == "green":
        c_ind = 1
    elif color == "blue":
        c_ind = 0

    h, w = image.shape[:2]
    # build the row
    row = []
    # start black
    color = 0
    # work on an image copy
    frame = np.copy(image)

    print("height: {}, width: {}".format(h, w))

    debug_count = 0
    for n in range(h):
        debug_count += 1
        color = 0
        for r in range(w):
            color += 1
            # set the color for BGR
            bgr = [0,0,0]
            bgr[c_ind] = color
            frame[n, r] = (bgr[0], bgr[1], bgr[2])

    print("debug cnt: {}, color: {}".format(debug_count, color))

    return frame
