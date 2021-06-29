from ctypes import *                                               # Import libraries
import math
import random
import os
import cv2
import numpy as np
import time
import darknet
from sklearn.linear_model import LinearRegression
import smbus
import Jetson.GPIO as GPIO

bus = smbus.SMBus(1)
address = 0x08

def writeData(value):
    bus.write_byte(address, value)
    return -1

def convertBack(x, y, w, h):
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax


def cvDrawBoxes1(detections, img):
    # Colored labels dictionary
    color_dict = {
        'test_crop' : [0, 255, 0]
    }

    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    X3 = []
    Y3 = []
    X4 = []
    Y4 = []

    for label, confidence, bbox in detections:
        x, y, w, h = (bbox[0],
                bbox[1],
                bbox[2],
                bbox[3])
        name_tag = label
        for name_key, color_val in color_dict.items():
            if name_key == name_tag:
                color = color_val 
                xmin, ymin, xmax, ymax = convertBack(
                float(x), float(y), float(w), float(h))
                pt1 = (xmin, ymin)
                pt2 = (xmax, ymax)
                cv2.rectangle(img, pt1, pt2, color, 1)
                #print(pt1)
                #print(pt2)
                Point_center = (int((xmin + xmax)/2), int((ymin + ymax)/2))
                
                if Point_center[0] > 0 and Point_center[0] <= 200:
                    X1.append(Point_center[0])
                    Y1.append(Point_center[1])

                if Point_center[0] >= 200 and Point_center[0] <= 321:    
                    X2.append(Point_center[0])
                    Y2.append(Point_center[1]) 

                if Point_center[0] > 321 and Point_center[0] <= 450:               
                    X3.append(Point_center[0])
                    Y3.append(Point_center[1])  

                if Point_center[0] > 450 and Point_center[0] <= 640:              
                    X4.append(Point_center[0])
                    Y4.append(Point_center[1])                
                
                #print(Point_center)
                cv2.circle(img, Point_center, 5, color, 3)
                cv2.putText(img, label + " [" + confidence + "]", (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    X1 = np.reshape(X1, (-1, 1))
    Y1 = np.reshape(Y1, (-1, 1))
    X2 = np.reshape(X2, (-1, 1))
    Y2 = np.reshape(Y2, (-1, 1))
    X3 = np.reshape(X3, (-1, 1))
    Y3 = np.reshape(Y3, (-1, 1))
    X4 = np.reshape(X4, (-1, 1))
    Y4 = np.reshape(Y4, (-1, 1))
    
    
    return img, X1, Y1, X2, Y2, X3, Y3, X4, Y4

def cvDrawBoxes2(detections, img):
    # Colored labels dictionary
    color_dict = {
        'test_crop' : [0, 255, 0]
    }

    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    X3 = []
    Y3 = []
    X4 = []
    Y4 = []

    for label, confidence, bbox in detections:
        x, y, w, h = (bbox[0],
                bbox[1],
                bbox[2],
                bbox[3])
        name_tag = label
        for name_key, color_val in color_dict.items():
            if name_key == name_tag:
                color = color_val 
                xmin, ymin, xmax, ymax = convertBack(
                float(x), float(y), float(w), float(h))
                pt1 = (xmin, ymin)
                pt2 = (xmax, ymax)
                cv2.rectangle(img, pt1, pt2, color, 1)
                #print(pt1)
                #print(pt2)
                Point_center = (int((xmin + xmax)/2), int((ymin + ymax)/2))
                
                if Point_center[0] > 0 and Point_center[0] <= 215:
                    X1.append(Point_center[0])
                    Y1.append(Point_center[1])

                if Point_center[0] >= 215 and Point_center[0] <= 310:    
                    X2.append(Point_center[0])
                    Y2.append(Point_center[1]) 

                if Point_center[0] > 310 and Point_center[0] <= 396:               
                    X3.append(Point_center[0])
                    Y3.append(Point_center[1])  

                if Point_center[0] > 396 and Point_center[0] <= 640:              
                    X4.append(Point_center[0])
                    Y4.append(Point_center[1])                
                
                #print(Point_center)
                cv2.circle(img, Point_center, 5, color, 3)
                cv2.putText(img, label + " [" + confidence + "]", (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    X1 = np.reshape(X1, (-1, 1))
    Y1 = np.reshape(Y1, (-1, 1))
    X2 = np.reshape(X2, (-1, 1))
    Y2 = np.reshape(Y2, (-1, 1))
    X3 = np.reshape(X3, (-1, 1))
    Y3 = np.reshape(Y3, (-1, 1))
    X4 = np.reshape(X4, (-1, 1))
    Y4 = np.reshape(Y4, (-1, 1))
    
    
    return img, X1, Y1, X2, Y2, X3, Y3, X4, Y4


netMain = None
metaMain = None
altNames = None


def YOLO():
   
    global metaMain, netMain, altNames, metaMain1, netMain1, altNames1
    configPath = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/cfg/custom-yolov4-tiny-detector.cfg"                                 # Path to cfg
    weightPath = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/custom-yolov4-tiny-detector_best.weights"                                 # Path to weights
    metaPath = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/cfg/obj_tiny.data"                                    # Path to meta data
    
    configPath1 = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/cfg/custom-yolov4-tiny-detector.cfg"                                 # Path to cfg
    weightPath1 = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/custom-yolov4-tiny-detector_last.weights"                                 # Path to weights
    metaPath1 = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/cfg/obj_tiny.data"                                    # Path to meta data
    
    
    if not os.path.exists(configPath):                              # Checks whether file exists otherwise return ValueError
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    
    if not os.path.exists(configPath1):                              # Checks whether file exists otherwise return ValueError
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath1)+"`")
    if not os.path.exists(weightPath1):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath1)+"`")
    if not os.path.exists(metaPath1):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath1)+"`")
        
    
    if netMain is None:                                             # Checks the metaMain, NetMain and altNames. Loads it in script
        netMain = darknet.load_net_custom(configPath.encode( 
            "ascii"), weightPath.encode("ascii"), 0, 1)             # batch size = 1
    
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass


    network, class_names, class_colors = darknet.load_network(configPath,  metaPath, weightPath, batch_size=1)
    network1, class_names1, class_colors1 = darknet.load_network(configPath1,  metaPath1, weightPath1, batch_size=1)


    cap = cv2.VideoCapture(0 ,cv2.CAP_V4L)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    cap1 = cv2.VideoCapture(2 ,cv2.CAP_V4L)
    cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    #cap = cv2.VideoCapture(0)
    #cap1 = cv2.VideoCapture(2)                                    # Uncomment to use Webcam
    #cap = cv2.VideoCapture("test2.mp4")                             # Local Stored video detection - Set input video
    frame_width = 640                          # Returns the width and height of capture video
    frame_height = 360
    print(frame_height)
    print(frame_width)
    # Set out for video writer
    #out = cv2.VideoWriter(                                          # Set the Output path for video writer
    #    "./Demo/output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 10.0,
    #    (frame_width, frame_height))

    #print("Starting the YOLO loop...")

    # Create an image we reuse for each detect
    darknet_image = darknet.make_image(frame_width, frame_height, 3) # Create image according darknet for compatibility of network
    darknet_image1 = darknet.make_image(frame_width, frame_height, 3)
    previous_postion = 'Forward'
    while True:                                                      # Load the input frame and write output frame.
        prev_time = time.time()
        ret, frame_read = cap.read()                                 # Capture frame and return true if frame present
        # For Assertion Failed Error in OpenCV
        if not ret:                                                  # Check if frame present otherwise he break the while loop
            break
        
        #print("after frame read")
        frame_rgb = cv2.cvtColor(frame_read, cv2.COLOR_BGR2RGB)      # Convert frame into RGB from BGR and resize accordingly
        frame_resized = cv2.resize(frame_rgb, (frame_width, frame_height), interpolation=cv2.INTER_LINEAR)
        darknet.copy_image_from_bytes(darknet_image,frame_resized.tobytes())                # Copy that frame bytes to darknet_image
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=0.40)    # Detection occurs at this line and return detections, for customize we can change the threshold.                                                                                   
        image, X1, Y1, X2, Y2, X3, Y3, X4, Y4 = cvDrawBoxes1(detections, frame_resized)              # Call the function cvDrawBoxes() for colored bounding box per class
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        #print(X1.size)
        #print("camera1 done")
        
        ret, frame_read1 = cap1.read()
        frame_rgb1 = cv2.cvtColor(frame_read1, cv2.COLOR_BGR2RGB)      # Convert frame into RGB from BGR and resize accordingly
        frame_resized1 = cv2.resize(frame_rgb1, (frame_width, frame_height), interpolation=cv2.INTER_LINEAR)
        darknet.copy_image_from_bytes(darknet_image1,frame_resized1.tobytes())
        detections1 = darknet.detect_image(network, class_names, darknet_image1, thresh=0.40)             # Call the function cvDrawBoxes() for colored bounding box per class
        image1, A1, B1, A2, B2, A3, B3, A4, B4 = cvDrawBoxes2(detections1, frame_resized1)
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
  
        #print("camera2 done")
        '''
        print(X1.size is 0)
        print(X4.size is 0)
        print(X1.size is 1)
        print(X4.size is 1)
        print(A1.size is 0)
        print(A4.size is 0)
        print(A1.size is 1)
        print(A4.size is 1)
        print((((X1.size is 0) or (X4.size is 0) or (X1.size is 1) or (X4.size is 1)) is 1) and (((A1.size is 0) or (A4.size is 0) or (A1.size is 1) or (A4.size is 1)) is 0))
        print((X1.size is 0) or (X4.size is 0) or (X1.size is 1) or (X4.size is 1))
        print(((A1.size is 0) or (A4.size is 0) or (A1.size is 1) or (A4.size is 1)) is False)
        '''

        if (((X1.size is 0) or (X4.size is 0) or (X1.size is 1) or (X4.size is 1)) and ((A1.size is 0) or (A4.size is 0) or (A1.size is 1) or (A4.size is 1))) is True:
            print("No Crops found in Both Camera")
            image = cv2.putText(image, 'No Crops found', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
            image1 = cv2.putText(image1, 'No Crops found', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
            writeData(0xB6)   

        elif ((((X1.size is 0) or (X4.size is 0) or (X1.size is 1) or (X4.size is 1)) is True) and (((A1.size is 0) or (A4.size is 0) or (A1.size is 1) or (A4.size is 1)) is False)) is True:
            print("No Crops found in Front Camera")
            previous_postion = "Reverse"
            #image = cv2.putText(image, 'No Crops found', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)

            lr1_C2 = LinearRegression()
            lr1_C2.fit(A1, B1)
            B_pred1 = lr1_C2.predict(A1)
            Array_1_C2 = np.dstack((A1, B_pred1))
            Array1_C2 = np.reshape(Array_1_C2, (-1, 2))
            #print("Array1", np.int32([Array1]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image1, np.int32([Array1_C2]), 0, (0,255,0), 3)
            parameters1_C2 = np.polyfit((Array1_C2[0,0], Array1_C2[1,0]), (Array1_C2[0,1], Array1_C2[1,1]), 1)
            slope1_C2 = parameters1_C2[0]
            #print("Slope 1",slope1)
            angle1_C2 = math.degrees(math.atan(slope1_C2))
            #print("Angle 1",angle1)

            '''
            lr2_C2 = LinearRegression()
            lr2_C2.fit(A2, B2)
            B_pred2 = lr2_C2.predict(X2)
            Array_2_C2 = np.dstack((X2, Y_pred2))
            Array2_C2 = np.reshape(Array_2_C2, (-1, 2))
            #print("Array2", np.int32([Array2]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image1, np.int32([Array2_C2]), 0, (0,255,0), 3)
            parameters2_C2 = np.polyfit((Array2_C2[0,0], Array2_C2[1,0]), (Array2_C2[0,1], Array2_C2[1,1]), 1)
            slope2_C2 = parameters2_C2[0]
            #print("Slope 2",slope2)
            angle2_C2 = math.degrees(math.atan(slope2_C2))
            print("Angle 2 ",angle2_C2)

            lr3_C2 = LinearRegression()
            lr3_C2.fit(A3, B3)
            B_pred3 = lr3.predict(A3)
            Array_3_C2 = np.dstack((A3, B_pred3))
            Array3_C2 = np.reshape(Array_3_C2, (-1, 2))
            #print("Array3", np.int32([Array3]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image1, np.int32([Array3]), 0, (0,255,0), 3)
            parameters3 = np.polyfit((Array3_C2[0,0], Array3_C2[1,0]), (Array3_C2[0,1], Array3_C2[1,1]), 1)
            slope3_C2 = parameters3_C2[0]
            #print("Slope 3",slope3)
            angle3_C2 = math.degrees(math.atan(slope3_C2))
            #print("Angle 3 ",angle3_C2)
            '''

            lr4_C2 = LinearRegression()
            lr4_C2.fit(A4, B4)
            B_pred4 = lr4_C2.predict(A4)
            Array_4_C2 = np.dstack((A4, B_pred4))
            Array4_C2 = np.reshape(Array_4_C2, (-1, 2))
            #print("Array4", np.int32([Array4]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image1, np.int32([Array4_C2]), 0, (0,255,0), 3)
            parameters4_C2 = np.polyfit((Array4_C2[0,0], Array4_C2[1,0]), (Array4_C2[0,1], Array4_C2[1,1]), 1)
            slope4_C2 = parameters4_C2[0]
            #print("Slope 4",slope4_C2)
            angle4_C2 = math.degrees(math.atan(slope4_C2))
            #print("Angle 4 ",angle4_C2)

            #cv2.polylines(image, np.int32([Array1]), isClosed = False, color = (0,255,0), thickness = 3)


            #Motion Algo:
            print("Back Cam", angle1_C2 + angle4_C2)

            if (angle1_C2 + angle4_C2) < 3 and (angle1_C2 + angle4_C2) > -3:
                #print("Reverse")
                image1 = cv2.putText(image1, 'Reverse', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x97) #Steering Angle
                writeData(0x19) #Speed

            elif ((angle1_C2 + angle4_C2) > 3 and (angle1_C2 + angle4_C2) < 30):
                #print("clockwise")
                image1 = cv2.putText(image1, 'Reverse Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0xB1) #Steering Angle right
                writeData(0x19) #Speed

            elif ((angle1_C2 + angle4_C2) < -3 and (angle1_C2 + angle4_C2) > -30) :
                #print("anticlockwise")
                image1 = cv2.putText(image1, 'Reverse Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x83) #Steering Angle left
                writeData(0x19) #Speed 

            elif (angle1_C2 < 0 and angle4_C2 < 0):
                #print("clockwise (Slope change)")
                image = cv2.putText(image, 'Reverse Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0xB1) #Steering Angle right
                writeData(0x19) #Speed

            elif (angle1_C2 > 0 and angle4_C2 > 0) :
                #print("anticlockwise (Slope change)")
                image1 = cv2.putText(image1, 'Reverse Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x83) #Steering Angle left
                writeData(0x19) #Speed             

            else:
                print("Stop")
                writeData(0xB6)

            #writeData(0xB6)

        elif ((((X1.size is 0) or (X4.size is 0) or (X1.size is 1) or (X4.size is 1)) is False) and (((A1.size is 0) or (A4.size is 0) or (A1.size is 1) or (A4.size is 1)) is True)) is True:
            print("No Crops found in Back Camera")
            previous_postion = "Forward"
            #image1 = cv2.putText(image, 'No Crops found', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)

            lr1 = LinearRegression()
            lr1.fit(X1, Y1)
            Y_pred1 = lr1.predict(X1)
            Array_1 = np.dstack((X1, Y_pred1))
            Array1 = np.reshape(Array_1, (-1, 2))
            #print("Array1", np.int32([Array1]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image, np.int32([Array1]), 0, (0,255,0), 3)
            parameters1 = np.polyfit((Array1[0,0], Array1[1,0]), (Array1[0,1], Array1[1,1]), 1)
            slope1 = parameters1[0]
            #print("Slope 1",slope1)
            angle1 = math.degrees(math.atan(slope1))
            #print("Angle 1",angle1)

            '''
            lr2 = LinearRegression()
            lr2.fit(X2, Y2)
            Y_pred2 = lr2.predict(X2)
            Array_2 = np.dstack((X2, Y_pred2))
            Array2 = np.reshape(Array_2, (-1, 2))
            #print("Array2", np.int32([Array2]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image, np.int32([Array2]), 0, (0,255,0), 3)
            parameters2 = np.polyfit((Array2[0,0], Array2[1,0]), (Array2[0,1], Array2[1,1]), 1)
            slope2 = parameters2[0]
            #print("Slope 2",slope2)
            angle2 = math.degrees(math.atan(slope2))
            print("Angle 2 ",angle2)

            lr3 = LinearRegression()
            lr3.fit(X3, Y3)
            Y_pred3 = lr3.predict(X3)
            Array_3 = np.dstack((X3, Y_pred3))
            Array3 = np.reshape(Array_3, (-1, 2))
            #print("Array3", np.int32([Array3]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image, np.int32([Array3]), 0, (0,255,0), 3)
            parameters3 = np.polyfit((Array3[0,0], Array3[1,0]), (Array3[0,1], Array3[1,1]), 1)
            slope3 = parameters3[0]
            #print("Slope 3",slope3)
            angle3 = math.degrees(math.atan(slope3))
            print("Angle 3 ",angle3)
            '''

            lr4 = LinearRegression()
            lr4.fit(X4, Y4)
            Y_pred4 = lr4.predict(X4)
            Array_4 = np.dstack((X4, Y_pred4))
            Array4 = np.reshape(Array_4, (-1, 2))
            #print("Array4", np.int32([Array4]))
            #image = np.zeros([512, 512, 3],np.uint8)
            cv2.drawContours(image, np.int32([Array4]), 0, (0,255,0), 3)
            parameters4 = np.polyfit((Array4[0,0], Array4[1,0]), (Array4[0,1], Array4[1,1]), 1)
            slope4 = parameters4[0]
            #print("Slope 4",slope4)
            angle4 = math.degrees(math.atan(slope4))
            #print("Angle 4 ",angle4)

            #cv2.polylines(image, np.int32([Array1]), isClosed = False, color = (0,255,0), thickness = 3)


            #Motion Alog:
            print(angle1 + angle4)

            if (angle1 + angle4) < 7 and (angle1 + angle4) > 0:
                #print("forward")
                image = cv2.putText(image, 'Forward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x5B) #Steering Angle
                writeData(0x19) #Speed

            elif ((angle1 + angle4) > 7 and (angle1 + angle4) < 30):
                #print("clockwise")
                image = cv2.putText(image, 'Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x41) #Steering Angle right
                writeData(0x19) #Speed

            elif ((angle1 + angle4) < 0 and (angle1 + angle4) > -30) :
                #print("anticlockwise")
                image = cv2.putText(image, 'Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x6F) #Steering Angle left
                writeData(0x19) #Speed 

            elif (angle1 < 0 and angle4 < 0):
                #print("clockwise (Slope change)")
                image = cv2.putText(image, 'Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x41) #Steering Angle right
                writeData(0x19) #Speed

            elif (angle1 > 0 and angle4 > 0) :
                #print("anticlockwise (Slope change)")
                image = cv2.putText(image, 'Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                writeData(0x6F) #Steering Angle left
                writeData(0x19) #Speed             

            else:
                print("Stop")
                writeData(0xB6)
            #writeData(0xB6) 


        elif (((X1.size is 0) or (X4.size is 0) or (X1.size is 1) or (X4.size is 1)) or ((A1.size is 0) or (A4.size is 0) or (A1.size is 1) or (A4.size is 1))) is False:
            
            print("Both rows detected")
            if previous_postion is "Forward":

                lr1 = LinearRegression()
                lr1.fit(X1, Y1)
                Y_pred1 = lr1.predict(X1)
                Array_1 = np.dstack((X1, Y_pred1))
                Array1 = np.reshape(Array_1, (-1, 2))
                #print("Array1", np.int32([Array1]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image, np.int32([Array1]), 0, (0,255,0), 3)
                parameters1 = np.polyfit((Array1[0,0], Array1[1,0]), (Array1[0,1], Array1[1,1]), 1)
                slope1 = parameters1[0]
                #print("Slope 1",slope1)
                angle1 = math.degrees(math.atan(slope1))
                #print("Angle 1",angle1)

                '''
                lr2 = LinearRegression()
                lr2.fit(X2, Y2)
                Y_pred2 = lr2.predict(X2)
                Array_2 = np.dstack((X2, Y_pred2))
                Array2 = np.reshape(Array_2, (-1, 2))
                #print("Array2", np.int32([Array2]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image, np.int32([Array2]), 0, (0,255,0), 3)
                parameters2 = np.polyfit((Array2[0,0], Array2[1,0]), (Array2[0,1], Array2[1,1]), 1)
                slope2 = parameters2[0]
                #print("Slope 2",slope2)
                angle2 = math.degrees(math.atan(slope2))
                print("Angle 2 ",angle2)

                lr3 = LinearRegression()
                lr3.fit(X3, Y3)
                Y_pred3 = lr3.predict(X3)
                Array_3 = np.dstack((X3, Y_pred3))
                Array3 = np.reshape(Array_3, (-1, 2))
                #print("Array3", np.int32([Array3]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image, np.int32([Array3]), 0, (0,255,0), 3)
                parameters3 = np.polyfit((Array3[0,0], Array3[1,0]), (Array3[0,1], Array3[1,1]), 1)
                slope3 = parameters3[0]
                #print("Slope 3",slope3)
                angle3 = math.degrees(math.atan(slope3))
                print("Angle 3 ",angle3)
                '''

                lr4 = LinearRegression()
                lr4.fit(X4, Y4)
                Y_pred4 = lr4.predict(X4)
                Array_4 = np.dstack((X4, Y_pred4))
                Array4 = np.reshape(Array_4, (-1, 2))
                #print("Array4", np.int32([Array4]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image, np.int32([Array4]), 0, (0,255,0), 3)
                parameters4 = np.polyfit((Array4[0,0], Array4[1,0]), (Array4[0,1], Array4[1,1]), 1)
                slope4 = parameters4[0]
                #print("Slope 4",slope4)
                angle4 = math.degrees(math.atan(slope4))
                #print("Angle 4 ",angle4)

                #cv2.polylines(image, np.int32([Array1]), isClosed = False, color = (0,255,0), thickness = 3)

                print("Front Cam",angle1 + angle4)

                if (angle1 + angle4) < 7 and (angle1 + angle4) > 0:
                    #print("forward")
                    image = cv2.putText(image, 'Forward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x5B) #Steering Angle
                    writeData(0x19) #Speed

                elif ((angle1 + angle4) > 7 and (angle1 + angle4) < 30):
                    #print("clockwise")
                    image = cv2.putText(image, 'Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x41) #Steering Angle right
                    writeData(0x19) #Speed

                elif ((angle1 + angle4) < 0 and (angle1 + angle4) > -30) :
                    #print("anticlockwise")
                    image = cv2.putText(image, 'Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x6F) #Steering Angle left
                    writeData(0x19) #Speed 

                elif (angle1 < 0 and angle4 < 0):
                    #print("clockwise (Slope change)")
                    image = cv2.putText(image, 'Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x41) #Steering Angle right
                    writeData(0x19) #Speed

                elif (angle1 > 0 and angle4 > 0) :
                    #print("anticlockwise (Slope change)")
                    image = cv2.putText(image, 'Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x6F) #Steering Angle left
                    writeData(0x19) #Speed             

                else:
                    print("Stop")
                    writeData(0xB6)

            if previous_postion is "Reverse":
                lr1_C2 = LinearRegression()
                lr1_C2.fit(A1, B1)
                B_pred1 = lr1_C2.predict(A1)
                Array_1_C2 = np.dstack((A1, B_pred1))
                Array1_C2 = np.reshape(Array_1_C2, (-1, 2))
                #print("Array1", np.int32([Array1]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image1, np.int32([Array1_C2]), 0, (0,255,0), 3)
                parameters1_C2 = np.polyfit((Array1_C2[0,0], Array1_C2[1,0]), (Array1_C2[0,1], Array1_C2[1,1]), 1)
                slope1_C2 = parameters1_C2[0]
                #print("Slope 1",slope1)
                angle1_C2 = math.degrees(math.atan(slope1_C2))
                #print("Angle 1",angle1)

                '''             
                lr2_C2 = LinearRegression()
                lr2_C2.fit(A2, B2)
                B_pred2 = lr2_C2.predict(X2)
                Array_2_C2 = np.dstack((X2, Y_pred2))
                Array2_C2 = np.reshape(Array_2_C2, (-1, 2))
                #print("Array2", np.int32([Array2]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image1, np.int32([Array2_C2]), 0, (0,255,0), 3)
                parameters2_C2 = np.polyfit((Array2_C2[0,0], Array2_C2[1,0]), (Array2_C2[0,1], Array2_C2[1,1]), 1)
                slope2_C2 = parameters2_C2[0]
                #print("Slope 2",slope2)
                angle2_C2 = math.degrees(math.atan(slope2_C2))
                print("Angle 2 ",angle2_C2)

                
                lr3_C2 = LinearRegression()
                lr3_C2.fit(A3, B3)
                B_pred3 = lr3.predict(A3)
                Array_3_C2 = np.dstack((A3, B_pred3))
                Array3_C2 = np.reshape(Array_3_C2, (-1, 2))
                #print("Array3", np.int32([Array3]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image1, np.int32([Array3]), 0, (0,255,0), 3)
                parameters3 = np.polyfit((Array3_C2[0,0], Array3_C2[1,0]), (Array3_C2[0,1], Array3_C2[1,1]), 1)
                slope3_C2 = parameters3_C2[0]
                #print("Slope 3",slope3)
                angle3_C2 = math.degrees(math.atan(slope3_C2))
                #print("Angle 3 ",angle3_C2)
                '''


                lr4_C2 = LinearRegression()
                lr4_C2.fit(A4, B4)
                B_pred4 = lr4_C2.predict(A4)
                Array_4_C2 = np.dstack((A4, B_pred4))
                Array4_C2 = np.reshape(Array_4_C2, (-1, 2))
                #print("Array4", np.int32([Array4]))
                #image = np.zeros([512, 512, 3],np.uint8)
                cv2.drawContours(image1, np.int32([Array4_C2]), 0, (0,255,0), 3)
                parameters4_C2 = np.polyfit((Array4_C2[0,0], Array4_C2[1,0]), (Array4_C2[0,1], Array4_C2[1,1]), 1)
                slope4_C2 = parameters4_C2[0]
                #print("Slope 4",slope4_C2)
                angle4_C2 = math.degrees(math.atan(slope4_C2))
                #print("Angle 4 ",angle4_C2)
                


                #cv2.polylines(image, np.int32([Array1]), isClosed = False, color = (0,255,0), thickness = 3)


                #Motion Algo:
                
                print("Back Cam", angle1_C2 + angle4_C2)

                if (angle1_C2 + angle4_C2) < 3 and (angle1_C2 + angle4_C2) > -3:
                    #print("Reverse")
                    image1 = cv2.putText(image1, 'Reverse', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x97) #Steering Angle
                    writeData(0x19) #Speed

                elif ((angle1_C2 + angle4_C2) > 3 and (angle1_C2 + angle4_C2) < 30):
                    #print("clockwise")
                    image1 = cv2.putText(image1, 'Reverse Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0xB1) #Steering Angle right
                    writeData(0x19) #Speed

                elif ((angle1_C2 + angle4_C2) < -3 and (angle1_C2 + angle4_C2) > -30) :
                    #print("anticlockwise")
                    image1 = cv2.putText(image1, 'Reverse Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x83) #Steering Angle left
                    writeData(0x19) #Speed 

                elif (angle1_C2 < 0 and angle4_C2 < 0):
                    #print("clockwise (Slope change)")
                    image1 = cv2.putText(image1, 'Reverse Left', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0xB1) #Steering Angle right
                    writeData(0x19) #Speed

                elif (angle1_C2 > 0 and angle4_C2 > 0) :
                    #print("anticlockwise (Slope change)")
                    image1 = cv2.putText(image1, 'Reverse Right', (50, 50), cv2.FONT_HERSHEY_SIMPLEX , 1 , (255, 0, 0), 2, cv2.LINE_AA)
                    writeData(0x83) #Steering Angle left
                    writeData(0x19) #Speed             

                else:
                    print("Stop")
                    writeData(0xB6)
        

        cv2.imshow('Back Camera', image1)                                    # Display Image window
        cv2.imshow('Front Camera', image)
        print("FPS ",1/(time.time()-prev_time))
        cv2.waitKey(3)
        #out.write(image)                                             # Write that frame into output video
    
    cap.release()                                                    # For releasing cap and out. 
    #out.release()
    print(":::Video Write Completed")

if __name__ == "__main__":  
    YOLO()                                                           # Calls the main function YOLO()