# Autonomous-InterRow-Weed-Removing-Robot

## Project Partially Sponsored by Agnel Robotics Club (ARC)

#### Hello, I am Anish Dalvi from Mechanical Batch of 2021 from Fr. C. Rodrigues Institute of Technology, Vashi, Navi Mumbai, Maharashtra, India. This is my Final year Project. It is a Weeding Robot for Agricultural Farm field of any terrain powered by 6 planetary geared motors controlled by NVIDIA Jetson Nano 2GB. Robot design is based on Rocker-Bogie Mechanism which is used by NASA/JPL for it's Interplanetary rovers. For Autonomous Navigation it uses OpenCV's Hough Transform for Lane Detection and Deep learning model tiny-YOLOv4 for Crop detection.

## This Branch consists of Deep learning Codes that ran on Jetson Nano 2GB and follow this tutorial to make it run
* First Clone this Github Repo using 

git clone https://github.com/AlexeyAB/darknet

* Then you have to Enable CUDA so copy this and paste in your terminal. Make sure you change the Cuda version. (In this case the version was '10.0' but in future it will change)

export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

* Then you have to Enable GPU, CUDNN and OPENCV in the make file that is found in the darknet repo

GPU=1
CUDNN=1
OPENCV=1

* Then you can clone this branch(Deep_learning_Codes) to some other location and copy the content of darknet folder to the repo you were editing of AlexeyAB. Copy cfg and data folders too.
 
* Then go to darknet folder and run. It will take arround 5 minutes to complete

make

* Now you can run these codes

python3 yolo_crop_detection.py
python3 yolo_crop_detection_2_only.py
python3 yolo_crop_detection_both_camera.py
python3 yolo_crop_detection_both_camera_linear_regression_control.py
python3 yolo_crop_detection_both_camera_linear_regression_control_pid.py
python3 yolo_crop_detection_linear_regression.py
python3 yolo_crop_detection_linear_regression_control.py

## What does these Codes do?
* yolo_crop_detection is Single Camera Object Detection of Mock_Crops 
* yolo_crop_detection_2_only is also Single Camera Object Detection of Mock_Crops but for camera at device 2
* yolo_crop_detection_both_camera is for simultaneous detection with both cameras
* yolo_crop_detection_both_camera_linear_regression_control is simultaneous detection with creation of lines that passes through the centroid of bounding boxes. It also consists of bang-bang controller done with slave controller Arduino Mega. (Refer Arduino_Codes Branch for more information)
* yolo_crop_detection_both_camera_linear_regression_control_pid is same as above but instead of Bang-Bang controller, it is PID controller.

## Owners

* Anish Dalvi https://www.linkedin.com/in/anish-dalvi-769196186/
* Salvious Machado https://www.linkedin.com/in/salvious-machado-9716b2194/
* Shefin Airliy https://www.linkedin.com/in/victorshefin/
* Tushar Toraskar https://www.linkedin.com/in/tushartoraskar/

