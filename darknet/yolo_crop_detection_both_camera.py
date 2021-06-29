from ctypes import *                                               # Import libraries
import math
import random
import os
import cv2
import numpy as np
import time
import darknet


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
                #print(Point_center)
                cv2.circle(img, Point_center, 5, color, 3)
                cv2.putText(img, label + " [" + confidence + "]", (pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return img


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

    '''
    if netMain1 is None:                                             # Checks the metaMain, NetMain and altNames. Loads it in script
        netMain1 = darknet.load_net_custom(configPath1.encode( 
            "ascii"), weightPath1.encode("ascii"), 0, 1)             # batch size = 1
    
    if metaMain1 is None:
        metaMain1 = darknet.load_meta(metaPath1.encode("ascii"))
    
    if altNames1 is None:
        try:
            with open(metaPath1) as metaFH1:
                metaContents1 = metaFH1.read()
                import re
                match = re.search("names *= *(.*)$", metaContents1,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames1 = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass

    '''

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
        image = cvDrawBoxes(detections, frame_resized)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cv2.imshow('Demo', image)
        
        print("camera1 done")
        
        ret, frame_read1 = cap1.read()
        frame_rgb1 = cv2.cvtColor(frame_read1, cv2.COLOR_BGR2RGB)      # Convert frame into RGB from BGR and resize accordingly
        frame_resized1 = cv2.resize(frame_rgb1, (frame_width, frame_height), interpolation=cv2.INTER_LINEAR)
        darknet.copy_image_from_bytes(darknet_image1,frame_resized1.tobytes())
        detections1 = darknet.detect_image(network, class_names, darknet_image1, thresh=0.40)             # Call the function cvDrawBoxes() for colored bounding box per class
        image1 = cvDrawBoxes(detections1, frame_resized1)
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        cv2.imshow('Demo2', image1)                                    # Display Image window
        print("camera2 done")
        print(time.time())
        print(prev_time)

        cv2.waitKey(3)
        #out.write(image)                                             # Write that frame into output video
    
    cap.release()                                                    # For releasing cap and out. 
    #out.release()
    print(":::Video Write Completed")

if __name__ == "__main__":  
    YOLO()                                                           # Calls the main function YOLO()