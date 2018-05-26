from collections import deque
import numpy as np
import argparse
import imutils
import cv2
from matplotlib import pyplot as plt
import numpy as np
import cv2
from copy import deepcopy
from PIL import Image
import pytesseract as tess

class carDetector(object):
	"""docstring for carDetector"""
	def __init__(self):
		#Code for car detector
		self.car_cascade = cv2.CascadeClassifier('../DATA/cascades/cars.xml')
		self.frame = None
		self.detected_car = None
	def update_frame(self,frame):
		self.frame = frame
	def get_frame(self):
		return self.frame

	def detect_car(self):
		frame = self.frame
		try:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		except:
			print "\n\nConversion on RGB to Greyscale failed\n\n"
			gray = None	
		cars = []
		ncars = 0
		try:
			cars = self.car_cascade.detectMultiScale(gray, 1.4, 6)
		except:
			print("\n\nCar detector failed\n\n")
		# Draw border

		for (x, y, w, h) in cars:
			cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
			ncars = ncars + 1
			self.detected_car = frame[y:y+h, x:x+w]
			
			
	def get_detected_car(self):
		
		return self.detected_car


	
