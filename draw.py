import cv2
import numpy as np

def corner_gradient(image):
    h, w = image.shape[:2]
    row = []
    color = 0
    frame = np.copy(image)
    for n in range(h):
        for r in range(w):
            color += 1
            frame[n, r] = (color,color,color)
    return frame
