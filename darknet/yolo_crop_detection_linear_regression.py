from ctypes import *                                               # Import libraries
import math
import random
import os
import cv2
import numpy as np
import time
import darknet
from sklearn.linear_model import LinearRegression

def convertBack(x, y, w, h):
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax


def cvDrawBoxes(detections, img):
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
        x, y, w, h = (bbox[0], bbox[1], bbox[2], bbox[3])
        name_tag = label
        for name_key, color_val in color_dict.items():
            if name_key == name_tag:

                color = color_val 
                xmin, ymin, xmax, ymax = convertBack(float(x), float(y), float(w), float(h))
                pt1 = (xmin, ymin)
                pt2 = (xmax, ymax)
                cv2.rectangle(img, pt1, pt2, color, 1)
                #print(pt1)
                #print(pt2)
                
                Point_center = (int((xmin + xmax)/2), int((ymin + ymax)/2))
                #print("Centroid",Point_center)
                
                #Linear Regression begin
                #X = Point_center.iloc[:, 0].values.reshape(-1,1)

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

                #print(Y)
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

    #print(X)
    #print(Point_center)
    #print("X",X)
    #print("Y",Y)
    
    return img, X1, Y1, X2, Y2, X3, Y3, X4, Y4


netMain = None
metaMain = None
altNames = None


def YOLO():
   
    global metaMain, netMain, altNames
    configPath = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/cfg/custom-yolov4-tiny-detector.cfg"                                 # Path to cfg
    weightPath = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/custom-yolov4-tiny-detector_best.weights"                                 # Path to weights
    metaPath = "/home/anish/Desktop/FinalYear Project (Files too big)/Strawberry_Yolo_v4/darknet/cfg/obj_tiny.data"                                    # Path to meta data
    if not os.path.exists(configPath):                              # Checks whether file exists otherwise return ValueError
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    
    
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

    #cap = cv2.VideoCapture(0)                                      # Uncomment to use Webcam
    #cap = cv2.VideoCapture("test2.mp4")                             # Local Stored video detection - Set input video
    cap = cv2.VideoCapture(0 ,cv2.CAP_V4L)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    frame_width = 640                           # Returns the width and height of capture video
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
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=0.45)    # Detection occurs at this line and return detections, for customize we can change the threshold.                                                                                   
        
        image, X1, Y1, X2, Y2, X3, Y3, X4, Y4 = cvDrawBoxes(detections, frame_resized)              # Call the function cvDrawBoxes() for colored bounding box per class

        print(X1.size )
        print(X2.size )
        print(X3.size )
        print(X4.size )
        #print(Y)
        if ((X1.size is 0) or (X2.size is 0) or (X3.size is 0) or (X4.size is 0) or (X1.size is 1) or (X2.size is 1) or (X3.size is 1) or (X4.size is 1)) is True:
            print("No Crops found")
    
        else:
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
            print("Slope 1",slope1)

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
            print("Slope 2",slope2)

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
            print("Slope 3",slope3)

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
            print("Slope 4",slope4)

            #cv2.polylines(image, np.int32([Array1]), isClosed = False, color = (0,255,0), thickness = 3)

        #print(X1.size)


              
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        print("FPS ",1/(time.time()-prev_time))

        cv2.imshow('Demo', image)                                    # Display Image window
        cv2.waitKey(3)
        #out.write(image)                                             # Write that frame into output video
    cap.release()                                                    # For releasing cap and out. 
    #out.release()
    print(":::Video Write Completed")

if __name__ == "__main__":  
    YOLO()                                                           # Calls the main function YOLO()