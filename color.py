import cv2

def filter_green(image):
    # image in must be HSV color
    frame = cv2.inRange(image, (120.0000, 100.0000, 19.6078), (120.0000, 100.0000, 100.0000))
    return frame

def filter_white(image):
    frame = cv2.inRange(image, (0, 0, 200), (145, 60, 255))
    return frame
