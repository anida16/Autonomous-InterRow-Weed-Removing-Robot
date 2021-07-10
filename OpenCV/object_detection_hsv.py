import cv2
import numpy as np

def nothing(x):
    pass

#cap = cv2.VideoCapture(1)       #Turn this on, if you need video as input

cap = cv2.VideoCapture(2, cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#image = cv2.imread("crop_row_263.JPG")       #Turn this on, if you need image as input



cv2.namedWindow("Trackbars")

cv2.createTrackbar("L ? H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L ? S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L ? V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U ? H", "Trackbars", 179, 255, nothing)
cv2.createTrackbar("U ? S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U ? V", "Trackbars", 255, 255, nothing)

while True:
    _, frame = cap.read()    #Turn this on, if you need video as input
    #frame = image        #Turn this on, if you need image as input
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L ? H", "Trackbars")
    l_s = cv2.getTrackbarPos("L ? S", "Trackbars")
    l_v = cv2.getTrackbarPos("L ? V", "Trackbars")
    u_h = cv2.getTrackbarPos("U ? H", "Trackbars")
    u_s = cv2.getTrackbarPos("U ? S", "Trackbars")
    u_v = cv2.getTrackbarPos("U ? V", "Trackbars")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()