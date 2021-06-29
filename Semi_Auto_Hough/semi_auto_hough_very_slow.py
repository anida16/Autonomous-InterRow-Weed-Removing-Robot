from __future__ import print_function
import cv2
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

#import xbox
import smbus
import time
import math
import Jetson.GPIO as GPIO
import os
bus = smbus.SMBus(1)
address = 0x08

semi_auto_button = 32
def nothing(x):
    pass

def fmtFloat(n):
    return '{:6.3f}'.format(n)
    #writeData(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")
        #writeData(arg)
        #print()

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
        #print(ifTrue)
        writeData(ifTrue)
    else:
        show(ifFalse)

def writeData(value):
    #time.sleep(3)
    #byteValue = StringToBytes(value)  
    #bus.write_i2c_block_data(address,0x08,byteValue) #first byte is 0=command byte.. just is.
    bus.write_byte(address, value)
    return -1

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

def angleFromCoords(x,y):
    angle = 0.0
    if x==0.0 and y==0.0:
        angle = -1
    elif x>=0.0 and y>=0.0:
        # first quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else 90.0
    elif x<0.0 and y>=0.0:
        # second quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x<0.0 and y<0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x))
        angle += 180.0
    elif x>=0.0 and y<0.0:
        # third quadrant
        angle = math.degrees(math.atan(y/x)) if x!=0.0 else -90.0
        angle += 360.0
    return angle
 
camera_index = 0
cap = cv2.VideoCapture(camera_index, cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 848)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#img = cv2.imread("Green_Crop_1.jpg")
'''
def calculate_coordinates(img, parameters):
    slope, intercept = parameters
    # Sets initial y-coordinate as height from top down (bottom of the frame)
    y1 = img.shape[0]
    # Sets final y-coordinate as 150 above the bottom of the frame
    y2 = int(y1 - 600)
    # Sets initial x-coordinate as (y1 - b) / m since y1 = mx1 + b
    x1 = int((y1 - intercept) / slope)
    # Sets final x-coordinate as (y2 - b) / m since y2 = mx2 + b
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def visualize_lines(img, lines):
    # Creates an image filled with zero intensities with the same dimensions as the frame
    lines_visualize = np.zeros_like(img)
    # Checks if any lines are detected
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            # Draws lines between two coordinates with green color and 5 thickness
            parameters1 = np.polyfit((x1, x2), (y1, y2), 1)
            slope = parameters1[0]
            y_intercept = parameters1[1]

            if slope > 8 or slope < -8:
                #print("printing lines")
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return lines_visualize
'''
'''
def calculate_lines(img, lines):
    # Empty arrays to store the coordinates of the left and right lines
    #left = []
    #right = []

    Kmean = KMeans(n_clusters = 4)
    Kmean.fit(lines)
    print ("................. Cluster Centers ..........")
    print (Kmean.cluster_centers_)
    centre = []
    centre2 = []
    kemean_array = []
    # Loops through every detected line
    # for line in lines:
    #     # Reshapes line from 2D array to 1D array
    #     x1, y1, x2, y2 = line.reshape(4)
    #     # Fits a linear polynomial to the x and y coordinates and returns a vector of coefficients which describe the slope and y-intercept
    #     parameters = np.polyfit((x1, x2), (y1, y2), 1)
    #     slope = parameters[0]
    #     y_intercept = parameters[1]
    #     print(x1)
    #     print(line)
    #     #print(x2)
    #     #print(slope)
    #     #print(line.reshape(2,-1)=)s
    #     #two_d = rgrtvgtv
    #     print(Kmean.fit(line.reshape(2,-1)))
    #     centers1 = Kmean.cluster_centers_
    #     print("centres", centers1)


        # if x1 >= 210 and x1 < 300: #220 is for real time image, make sure to change is back to this value once you're done WFH
        #     #leftx1.append((x1))
        #     centre.append((slope, y_intercept))

        # if x1 < 210 and x1 > 140: #220 is for real time image, make sure to change is back to this value once you're done WFH
        #     #rightx1.append((x1))
        #     centre2.append((slope, y_intercept))

        #if x1 >= 303:
        #    right.append((slope, y_intercept))

        #if x1 <= 133:
        #    left.append((slope, y_intercept))        
        
        # if x2 > 240: #220 is for real time image, make sure to change is back to this value once you're done WFH
        #     #leftx2.append((x2))
        #     left.append((slope, y_intercept))

        # if x2 < 240: #220 is for real time image, make sure to change is back to this value once you're done WFH
        #     #rightx2.append((x2))
        #     right.append((slope, y_intercept))
        

        #print(left)
        
        # If slope is negative, the line is to the left of the lane, and otherwise, the line is to the right of the lane
        #if slope < -54 and slope > -70:
        #    left.append((slope, y_intercept))
        #if slope > 8 or slope < -8:
        #    centre.append((slope, y_intercept))
        #if slope > -2 and slope < -1:
        #    centre2.append((slope, y_intercept))
        #if slope > -54 and slope < 70:
        #    right.append((slope, y_intercept))


    
    left_x1_avg = np.average(left)
    right_x1_avg = np.average(right)

    left_x2_avg = np.average(left)
    right_x2_avg = np.average(right)

    left_y1_avg = np.average(left)
    right_y1_avg = np.average(right)

    left_y2_avg = np.average(left)
    right_y2_avg = np.average(right)

    print("average x1 left is",left_x1_avg)
    print("average x1 right is",right_x1_avg)
    
    # Averages out all the values for left and right into a single slope and y-intercept value for each line
    #left_avg = np.average(left, axis = 0)
    #right_avg = np.average(right, axis = 0)
    centre_avg = np.average(centre, axis = 0)
    centre_avg2 = np.average(centre2, axis = 0)
    # Calculates the x1, y1, x2, y2 coordinates for the left and right lines
    #left_line = calculate_coordinates(img, left_avg)
    #right_line = calculate_coordinates(img, right_avg)
    centre_line = calculate_coordinates(img, centre_avg)
    centre_line2 = calculate_coordinates(img, centre_avg2)
    #print("left line is" ,left_line)
    #print(centre_line)
    #print("right line is",right_line)
    #print(centre_line2)
    #return np.array([left_line, right_line, centre_line, centre_line2])
    return np.array([centre_line, centre_line2])
'''
#Adjust thresold & rho to increase/decrease no. of lines


#Adjust thresold & rho to increase/decrease no. of lines


GPIO.setmode(GPIO.BOARD)
#roi = img[0: 280, 150: 320]

while True:

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(semi_auto_button, GPIO.IN)  # button pin set as input
    
    if GPIO.input(32) is 1:
        print("exiting")
        exit()

    ret, img = cap.read()
    ret, original = cap.read()
    #original = cv2.imread("Green_Crop_1.jpg")

    cv2.circle(original, (148, 4), 5, (0, 0, 255), -1)
    cv2.circle(original, (725, 5), 5, (0, 0, 255), -1)
    cv2.circle(original, (16, 477), 5, (0, 0, 255), -1)
    cv2.circle(original, (805, 478), 5, (0, 0, 255), -1)

    pts1 = np.float32([[148, 4], [725, 5], [16, 477], [805, 478]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 600], [400, 600]])
    #pts2 = pts1
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    img = cv2.warpPerspective(img, matrix, (400, 600))

    #cv2.namedWindow("Trackbars")

    #cv2.createTrackbar("point1", "Trackbars", 5, 10, nothing)
    #cv2.createTrackbar("point2", "Trackbars", 670, 1200, nothing)
    #cv2.createTrackbar("point3", "Trackbars", 200, 2000, nothing)

    #cv2.imshow("lines", lines)

    #
    #ROI for Tushar jowari here
    mask = np.zeros(img.shape, dtype=np.uint8)

    roi_corners = np.array([[(320,600), (2000,300), (320,0)]], dtype=np.int32)
    roi_corners1 = np.array([[(60,600), (0,0), (120,0)]], dtype=np.int32)
    roi_corners2 = np.array([[(120,600), (0,596), (120,0)]], dtype=np.int32)
    roi_corners3 = np.array([[(0,0), (120,300), (0,600)]], dtype=np.int32) 

    channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
    ignore_mask_color = (255,)*channel_count

    cv2.fillPoly(mask, roi_corners, ignore_mask_color)
    cv2.fillPoly(mask, roi_corners1, ignore_mask_color)
    cv2.fillPoly(mask, roi_corners2, ignore_mask_color)
    cv2.fillPoly(mask, roi_corners3, ignore_mask_color)

    #cv2.fillPoly(mask, roi_corners, ignore_mask_color)
    # from Masterfool: use cv2.fillConvexPoly if you know it's convex

    # apply the mask
    masked_image = cv2.bitwise_and(img, mask)
    img2 = cv2.subtract(img, masked_image)

    #ROI for Tushar jowari here
    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    #lower_blue = np.array([50, 75, 111]) #real photo
    #upper_blue = np.array([61, 255, 255]) #real photo
    lower_blue = np.array([45, 62, 52]) #35 #38, 83, 122 for evening #42, 52, 140 skips inside plant - for morning
    upper_blue = np.array([72, 255, 255])
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

    hough = cv2.HoughLinesP(skel, 4, np.pi/180, 1000, maxLineGap=1500)
    #for gazebo_ss.png (skel, 4, np.pi/180, 48, maxLineGap=500)
    #lines = cv2.HoughLinesP(skel, 5, np.pi/180, 1100, maxLineGap=50)
    #for tushar groundnut image skel, 5, np.pi/180, 600, maxLineGap=50
    #for crop row 001 image(skel, 2, np.pi/180, 91, maxLineGap=50)
    #for crop row 001 image skel, 2, np.pi/180, 134, maxLineGap=50
    #[[698   2 734 409]]
    # print ("Shape: ")
    # print (hough.shape)
    # print (hough[0])
    while(hough is None):

        print("No lines found")


    #print ("hough",hough)

    reshape_hough = np.reshape(hough, (hough.shape[0]*2,2))

    if reshape_hough is None:
        print("No lines found")

    #print (reshape_hough[0])

    Kmean = KMeans(n_clusters = 4)
    Kmean.fit(reshape_hough)

    #print ("................. Cluster Centers ..........")
    #print("One point")
    #print (Kmean.cluster_centers_)
    top_left = []
    top_right = []
    bottom_left = []
    bottom_right = []
    #print("One point")
    #print(type(Kmean.cluster_centers_))
    #print (Kmean.cluster_centers_[0, 1])
    point1 = int(Kmean.cluster_centers_[1, 0])
    point2 = int(Kmean.cluster_centers_[1, 1])
    point3 = int(Kmean.cluster_centers_[0, 0])
    point4 = int(Kmean.cluster_centers_[0, 1])
    point5 = int(Kmean.cluster_centers_[2, 0])
    point6 = int(Kmean.cluster_centers_[2, 1])
    point7 = int(Kmean.cluster_centers_[3, 0])
    point8 = int(Kmean.cluster_centers_[3, 1])

    #print(point2)
    #print(point1)
    img = cv2.circle(img, (point1, point2), 5, color=(0, 0, 255), thickness=-1)
    img = cv2.circle(img, (point3, point4), 5, color=(0, 0, 255), thickness=-1)
    img = cv2.circle(img, (point5, point6), 5, color=(0, 0, 255), thickness=-1)
    img = cv2.circle(img, (point7, point8), 5, color=(0, 0, 255), thickness=-1)



    if point1 < 200 and point2 < 300:
        top_left.append(Kmean.cluster_centers_[1])

    if point3 < 200 and point4 < 300:
        top_left.append(Kmean.cluster_centers_[0])

    if point5 < 200 and point6 < 300:
        top_left.append(Kmean.cluster_centers_[2])

    if point7 < 200 and point8 < 300:
        top_left.append(Kmean.cluster_centers_[3])



    if point1 > 200 and point2 < 300:
        top_right.append(Kmean.cluster_centers_[1])

    if point3 > 200 and point4 < 300:
        top_right.append(Kmean.cluster_centers_[0])

    if point5 > 200 and point6 < 300:
        top_right.append(Kmean.cluster_centers_[2])

    if point7 > 200 and point8 < 300:
        top_right.append(Kmean.cluster_centers_[3])



    if point1 < 200 and point2 > 300:
        bottom_left.append(Kmean.cluster_centers_[1])

    if point3 < 200 and point4 > 300:
        bottom_left.append(Kmean.cluster_centers_[0])

    if point5 < 200 and point6 > 300:
        bottom_left.append(Kmean.cluster_centers_[2])

    if point7 < 200 and point8 > 300:
        bottom_left.append(Kmean.cluster_centers_[3])



    if point1 > 200 and point2 > 300:
        bottom_right.append(Kmean.cluster_centers_[1])

    if point3 > 200 and point4 > 300:
        bottom_right.append(Kmean.cluster_centers_[0])

    if point5 > 200 and point6 > 300:
        bottom_right.append(Kmean.cluster_centers_[2])

    if point7 > 200 and point8 > 300:
        bottom_right.append(Kmean.cluster_centers_[3])

    #print("bottom array",bottom_left)


    if bottom_left and bottom_right and top_left and top_right and 1 is not 0:
        print("Found both crop lines")
        x1 = int(bottom_left[0][0])
        y1 = int(bottom_left[0][1])

        x2 = int(top_left[0][0])
        y2 = int(top_left[0][1])

        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

        x3 = int(bottom_right[0][0])
        y3 = int(bottom_right[0][1])

        if top_right is not 0:
            x4 = int(top_right[0][0])
            y4 = int(top_right[0][1])

        cv2.line(img, (x3, y3), (x4, y4), (0, 255, 0), 5)  
        

    else:
   
        print("clockwise")
        #print(x1)

    parameters_left = np.polyfit((x1, x2), (y1, y2), 1)
    slope_left = parameters_left[0]
    y_intercept_left = parameters_left[1]

    parameters_right = np.polyfit((x3, x4), (y3, y4), 1)
    slope_right = parameters_right[0]
    y_intercept_right = parameters_right[1]   

    print("slope_left",slope_left) 
    print("slope_right",slope_right)


    #bottom_left
    #top_left

    #bottom_right
    #top_right

    #print("bottom array",bottom_left)
    #print(bottom_right)

    

    # Averages multiple detected lines from hough into one line for left border of lane and one line for right border of lane
    #lines = calculate_lines(img, reshape_hough)
    # Visualizes the lines
    #lines_visualize = visualize_lines(img, lines)
    # Overlays lines on frame by taking their weighted sums and adding an arbitrary scalar value of 1 as the gamma argument
    #output = cv2.addWeighted(img, 0.9, lines_visualize, 1, 1)
    # Opens a new window and displays the output frame

    '''
    if lines is None:
        print("Line Not Detected")
 
    if lines is not None:
        for line in lines: #this is fucked up, 0 lines created, need to study hough in depth first
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 10)
            cv2.putText(img,'lines_detected',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
            print("Line Detected")
    '''
    

    #print("line")

    cv2.imshow("Original", original)
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
