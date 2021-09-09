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

def rainbow_gradient(image):

    h, w = image.shape[:2]
    frame = np.copy(image)

    for n in range(h):
        for r in range(w):
            mult = (r/w)*255
            bgr = [0,0,0]
            
            # this determines the rainbow!
            norm_trans = n/(h/3)
            if n < h/3:
                # first section color, red
                c_ind = 2
            elif n < h*(2/3):
                # second section color, green
                c_ind = 1
            else:
                # third section color, blue
                c_ind = 0
            bgr[c_ind] = mult
            frame[n, r] = (bgr[0], bgr[1], bgr[2])

    return frame
