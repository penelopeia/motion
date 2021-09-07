import cv2

from color import filter_green, filter_white
from draw import corner_gradient

cap = cv2.VideoCapture(0)

while True: #cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        print("Frame not recieved. Exiting ...")
        break

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    filter_frame = filter_white(frame_HSV)

    # mask it on original
    result = cv2.bitwise_and(frame, frame, mask=filter_frame)

    grad = corner_gradient(frame)

    cv2.imshow('frame', grad)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()