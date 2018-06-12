import dlib
import sys
import cv2
import argparse
import imutils
from camera import VideoCamera


#load car detector
detector = dlib.fhog_object_detector("../DATA/SVM/car_detector.svm")
win = dlib.image_window()



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
ap.add_argument("-m", "--model",
    help="path to trained model")
args = vars(ap.parse_args())




if not args.get("video", False):
    video_camera = VideoCamera(0)
    # otherwise, grab a reference to the video file
else:
    video_camera = VideoCamera(args["video"])

def detect_car(frame):
	try:
		dets = detector(frame)
		for d in dets:
			cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
			print (int(d.left()), int(d.top()) ), (int(d.right()), int(d.bottom()) )
		frame = frame[int(d.top()):int(d.bottom()+20),int(d.left()): int(d.right()+20)]
		cv2.imshow("HOG output",frame)
		return frame
			
	except:
		print "HOG detector failed"
		return NONE

if __name__ == '__main__':
	
	while True:
		frame = video_camera.get_frame()
		try:
			cv2.imshow("input",frame)
		except:
			print "failed"
		detect_car(frame)
		key = cv2.waitKey(1) & 0xFF

		# if the 'q' key is pressed, stop the loop
		if key == ord("q"):
			break
