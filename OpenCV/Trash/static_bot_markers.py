import cv2
import numpy as np

def nothing(x):
    pass

#cap = cv2.VideoCapture(1)       #Turn this on, if you need video as input

cap = cv2.VideoCapture(2, cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

while True:
    _, frame = cap.read()    #Turn this on, if you need video as input
    #frame = image        #Turn this on, if you need image as input
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([24, 32, 170])
    upper_blue = np.array([54, 73, 219])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours:
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours:
    cv2.drawContours(frame, contours, 0, (0, 255, 0), 2)

    # Calculate image moments of the detected contour
    M = cv2.moments(contours[0])
    
    # Print center (debugging):
    print("center X : '{}'".format(round(M['m10'] / M['m00'])))
    print("center Y : '{}'".format(round(M['m01'] / M['m00'])))



    # Draw a circle based centered at centroid coordinates
    cv2.circle(frame, (int(round(M['m10']) / M['m00']), int(round(M['m01'] / M['m00']))), 5, (0, 255, 0), -1)

    # Show image:

    cv2.imshow("outline contour & centroid", frame)

    #result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Final Image", frame)
    cv2.imshow("mask", mask)
    #cv2.imshow("result", result)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()