import cv2

camera_index = 2
cap = cv2.VideoCapture(camera_index,cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 848)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:

    ret, img = cap.read()
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('s'):
        cap.release()
        break

cv2.destroyAllWindows() 