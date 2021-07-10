# USAGE
# python ball_tracking.py --video ball_tracking_example.mp4
# python ball_tracking.py

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time
from plistlib import Data


# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points

greenLower = (24, 32, 170)
greenUpper = (54, 73, 219)
pts = deque(maxlen=64)

#vs = cv2.VideoCapture('http://192.168.29.55:8080/video') #ipwebcam app
#vs = cv2.VideoCapture(0)

vs = cv2.VideoCapture(2, cv2.CAP_V4L)
vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	ret, frame = vs.read()
	

	# if we are viewing a video and we did not grab a frame, then we have reached the end of the video
	if frame is None:
		break

	# resize the frame, blur it, and convert it to the HSV color space

	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
 
	#print (cnts[0][1])
	print("One frame over")
	#print (len(cnts))
	# only proceed if at least one contour was found
	if len(cnts) == 2:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		'''
		if cnts[0] > 400:
			print ("Found 400")

		if cnts[0] < 200:
			print ("Fount 200")
		
		'''
		c = max(cnts, key=cv2.contourArea)
		c1 = min(cnts, key=cv2.contourArea)

		M = cv2.moments(c)
		M1 = cv2.moments(c1)

		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))

		#print ("center",center)
		left = []
		right = []

		if center[0] < 200:
			#print ("Left side")
			left.append((center))

		if center1[0] < 200:
			#print ("Left side")
			left.append((center1))

		if center[0] > 200:
			right.append((center))
			#print("right side")
			
		if center1[0] > 200:
			right.append((center1))
			#print("right side")

		#print(left)

		if left: #if left exisits
			#print(left[0])
			cv2.circle(frame, (left[0]), 5, (0, 0, 255), -1)

		#print("left 2",left[1])
		# only proceed if the radius meets a minimum size
		
		if right:
			cv2.circle(frame, (right[0]), 5, (255, 0, 0), -1)
			#print(right[0][0])

		#print("centre 2",center1[0])
		#print("centre",center[0])
		
		if left and right:
			print("Distance between centres", ((right[0][0]) - (left[0][0])))


	else:
		print("Less or more countors found")

	# update the points queue
	#pts.appendleft(center)

	# loop over the set of tracked points

	# show the frame to our screen
	cv2.imshow("Mask", mask)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break


# close all windows
cv2.destroyAllWindows()