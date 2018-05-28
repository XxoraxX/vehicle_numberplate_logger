import dlib
import cv2
import cvutils 
import sys
import os
import time
from skimage import io
import argparse
import imutils
#load car detector
detector = dlib.fhog_object_detector("../DATA/SVM/car_detector.svm")
win = dlib.image_window()
#give path of video on which you want it to run and process frame by frame
#if you want to use my video then download that from here 
#https://drive.google.com/file/d/19iE0RuCi9uVm_xLjOuG7fYkRfLktYDis/view?usp=sharing
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	cap = cv2.VideoCapture(0)

# otherwise, grab a reference to the video file
else:
	cap = cv2.VideoCapture(args["video"])
#cap = cv2.VideoCapture('')
while(True):
#     # Capture frame-by-frame
     ret, frame = cap.read()
     #process in BGR2RGB for more detections
     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
     
     try:		
     	dets = detector(frame)
     except:
        print "Car detector failed"

     for d in dets:
         cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
        
#     # Display the resulting frame
     cv2.imshow("frame",frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
     	

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
