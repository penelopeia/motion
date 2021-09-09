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
    frame = np.copy(image)

    for n in range(h):
        for r in range(w):
            mult = (r/w)*255
            bgr = [0,0,0]
            bgr[c_ind] = mult
            # frame[n, r] = (mult, mult, mult)
            frame[n, r] = (bgr[0], bgr[1], bgr[2])

    return frame

def checkerboard_gradient(image):

    h, w = image.shape[:2]
    frame = np.copy(image)

    for n in range(h):
        s = 0
        for r in range(w):
            mult = (r/w)*255
            bgr = [0,0,0]
            
            # this determines the rainbow!
            norm_trans = n/(h/3)

            bott = False
            if n < h/3:
                # first section color, red
                c_ind = 2
                if n > h/6:
                    bott = True
                sec = 1
                s += 1
            elif n < h*(2/3):
                # second section color, green
                c_ind = 1
                if n > h*(1/2):
                    bott = True
                sec = 0
                s += 1
            else:
                # third section color, blue
                c_ind = 0
                if n > h*(5/6):
                    bott = True
                sec = 2
                s += 1
            bgr[c_ind] = mult
            if bott:
                bgr[sec] = (s/(h/6))*255
            else:
                bgr[sec] = (((h/6) - s)/(h/6))*255
            frame[n, r] = (bgr[0], bgr[1], bgr[2])

    return frame
