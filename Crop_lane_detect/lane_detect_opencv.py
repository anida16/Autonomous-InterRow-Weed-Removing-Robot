import cv2
import numpy as np

def nothing(x):
    pass

camera_index = 0
cap = cv2.VideoCapture(camera_index,cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 848)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#img = cv2.imread("Green_Crop_1.jpg")


#Adjust thresold & rho to increase/decrease no. of lines



#roi = img[0: 280, 150: 320]

while True:

    ret, img = cap.read()
    #ret, original = cap.read()
    #original = cv2.imread("Green_Crop_1.jpg")
    '''
    cv2.circle(original, (137, 5), 5, (0, 0, 255), -1)
    cv2.circle(original, (576, 5), 5, (0, 0, 255), -1)
    cv2.circle(original, (5, 370), 5, (0, 0, 255), -1)
    cv2.circle(original, (708, 370), 5, (0, 0, 255), -1)
    '''
    pts1 = np.float32([[137, 5], [576, 5], [5, 313], [708, 313]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    img = cv2.warpPerspective(img, matrix, (500, 600))

    #cv2.namedWindow("Trackbars")

    #cv2.createTrackbar("point1", "Trackbars", 5, 10, nothing)
    #cv2.createTrackbar("point2", "Trackbars", 670, 1200, nothing)
    #cv2.createTrackbar("point3", "Trackbars", 200, 2000, nothing)

    #cv2.imshow("lines", lines)

    #
    #ROI for Tushar jowari here
    mask = np.zeros(img.shape, dtype=np.uint8)

    #roi_corners = np.array([[(263,0), (527,0), (527,631)]], dtype=np.int32)
    channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count
        
    #cv2.fillPoly(mask, roi_corners, ignore_mask_color)
    # from Masterfool: use cv2.fillConvexPoly if you know it's convex

    # apply the mask
    masked_image = cv2.bitwise_and(img, mask)
    img2 = cv2.subtract(img, masked_image)

    #ROI for Tushar jowari here
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    #lower_blue = np.array([50, 75, 111]) #real photo
    #upper_blue = np.array([61, 255, 255]) #real photo
    lower_blue = np.array([38, 83, 122])
    upper_blue = np.array([61, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(img2, img2, mask=mask)

    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    edges = gray
    #edges = cv2.Canny(gray, 75, 150)

    # Step 1: Create an empty skeleton
    size = np.size(edges)
    skel = np.zeros(edges.shape, np.uint8)

    # Get a Cross Shaped Kernel
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

    # Repeat steps 2-4
    while True:
        #Step 2: Open the image
        open = cv2.morphologyEx(edges, cv2.MORPH_OPEN, element)
        #Step 3: Substract open from the original image
        temp = cv2.subtract(edges, open)
        #Step 4: Erode the original image and refine the skeleton
        eroded = cv2.erode(edges, element)
        skel = cv2.bitwise_or(skel,temp)
        edges = eroded.copy()
        #cv2.imshow("Edges", edges)
        # Step 5: If there are no white pixels left ie.. the image has been completely eroded, quit the loop
        if cv2.countNonZero(edges)==0:
            break


    #p1 = cv2.getTrackbarPos("point1", "Trackbars")
    #p2 = cv2.getTrackbarPos("point2", "Trackbars")
    #p3 = cv2.getTrackbarPos("point3", "Trackbars")

#    lines = cv2.HoughLinesP(skel, 5, np.pi/180, 670, maxLineGap=200)
    #for gazebo_ss.png (skel, 4, np.pi/180, 48, maxLineGap=500)
    #lines = cv2.HoughLinesP(skel, 5, np.pi/180, 1100, maxLineGap=50)
    #for tushar groundnut image skel, 5, np.pi/180, 600, maxLineGap=50
    #for crop row 001 image(skel, 2, np.pi/180, 91, maxLineGap=50)
    #for crop row 001 image skel, 2, np.pi/180, 134, maxLineGap=50

#    for line in lines: #this is fucked up, too many lines created, need to study hough in depth first
#        x1, y1, x2, y2 = line[0]
#        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 10)

    #cv2.imshow("hsv", hsv)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result", result)
#    cv2.imshow("Image", img)
#    cv2.imshow("Skelenton", skel)
    #cv2.imshow("ROI", roi)  

#    key = cv2.waitKey(1)

#    if key == 27:
#        break

#p1 = cv2.getTrackbarPos("point1", "Trackbars")
#p2 = cv2.getTrackbarPos("point2", "Trackbars")
#p3 = cv2.getTrackbarPos("point3", "Trackbars")

    lines = cv2.HoughLinesP(skel, 5, np.pi/180, 1000, maxLineGap=300)
    #for gazebo_ss.png (skel, 4, np.pi/180, 48, maxLineGap=500)
    #lines = cv2.HoughLinesP(skel, 5, np.pi/180, 1100, maxLineGap=50)
    #for tushar groundnut image skel, 5, np.pi/180, 600, maxLineGap=50
    #for crop row 001 image(skel, 2, np.pi/180, 91, maxLineGap=50)
    #for crop row 001 image skel, 2, np.pi/180, 134, maxLineGap=50
    #[[698   2 734 409]]


    if lines is None:
        print("Line Not Detected")
 
    if lines is not None:
        for line in lines: #this is fucked up, 0 lines created, need to study hough in depth first
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 10)
            cv2.putText(img,'lines_detected',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            print("Line Detected")

    #print("line")

    #cv2.imshow("Original", original)
    #cv2.imshow("hsv", hsv)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result", result)
    cv2.imshow("Image", img)
    #cv2.imshow("Skelenton", skel)
    #cv2.imshow("ROI", roi)  
    #cv2.waitKey(10)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
