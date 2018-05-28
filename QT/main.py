from carDetector import carDetector
from camera import VideoCamera , IPCamera
import argparse
import imutils
import cv2
from read_number_plate import *
from pyANPD import *

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())

if not args.get("video", False):
    video_camera = VideoCamera(0)
    # otherwise, grab a reference to the video file
else:
    video_camera = VideoCamera(args["video"])


car_detector = carDetector()    


def loop():
	frame = video_camera.get_frame()
	cv2.imshow("input",frame)
	 
	car_detector.update_frame(frame)

	try:
		car_detector.detect_car()
		#cv2.imshow("output",car_detector.get_detected_car())
	except:
		print "car_detector failed"

	
	try: 
		output = process_image(frame, 0, type='rect')
		cv2.imshow("Detected Number plate",output)
		try:
			threshold_img = preprocess(output)
			contours= extract_contours(threshold_img)
			cleanAndRead(car_detector.get_detected_car(),contours)

		except:
			print "Number plate reader failed"
	except:
		print "Plate detector failed"
			
	

if __name__ == '__main__':
	while True:
		loop()
		key = cv2.waitKey(1) & 0xFF

		# if the 'q' key is pressed, stop the loop
		if key == ord("q"):
			break
