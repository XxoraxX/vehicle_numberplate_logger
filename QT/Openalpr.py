from openalpr import Alpr
import sys
import cv2
import argparse
import imutils
from camera import VideoCamera
from hog_detector import detect_car
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


def read_number_plate(im):
	alpr = Alpr("us", "../DATA/runtime_data/config/us.conf", "../DATA/runtime_data")
	if not alpr.is_loaded():
    		print("Error loading OpenALPR")
    		sys.exit(1)

	alpr.set_top_n(20)
	alpr.set_default_region("ca")

	#results = alpr.recognize_file("/home/chris/Desktop/vehicle_numberplate_logger/DATA/testData/self-driving.jpg")
	results = alpr.recognize_ndarray(im)
	i = 0
	#print results
	plate = results['results'][0]
	candidate = plate['candidates'][0]
	#plate_coordinates = plate['candidates']['coordinates']
	#print plate_coordinates	
	plate_coordinates = results['results'][0]['coordinates']	
	#print candidate
	#for plate in results['results']:
    		#i += 1
    		#print("Plate #%d" % i)
    		#print("   %12s %12s" % ("Plate", "Confidence"))
    		#for candidate in plate['candidates']:
        	#	prefix = "-"
        	#	if candidate['matches_template']:
            	#		prefix = "*"

        	#	print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
		#print plate
	#candidate = plate['candidates'] in max(plate['candidates']['confidence'])
	#print("   %12s%12f" % ( candidate['plate'], candidate['confidence']))

		# Call when completely done to release memory
	alpr.unload()
	im = im[plate_coordinates[0]['y']:plate_coordinates[2]['y']+20, plate_coordinates[0]['x']:plate_coordinates[1]['x']+20]
	return candidate['plate'] , candidate['confidence'] , im


if __name__ == '__main__':
	
	while True:
		frame = video_camera.get_frame()
		key = cv2.waitKey(1) & 0xFF

		# if the 'q' key is pressed, stop the loop
		if key == ord("q"):
			break
		try:
			cv2.imshow("input",frame)
		except:
			print "failed"
		try:
			out = detect_car(frame)
			try: 	
				_,_,out = (read_number_plate(out))
				cv2.imshow("cropped plate",out)
				#read_number_plate(frame)
			except:
				print "numberplate not found"
			
		except:
			print "Hog failed"

		
