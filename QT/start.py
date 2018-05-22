from webcam import Webcam
import cv2
import sys ,math
#import helper
import argparse as ap
from PyQt4 import QtCore, QtGui, uic
import numpy as np
from dashboard_gui import MyWindowClass











def nothing():
	print ""

def main(w , webcam):
    

    ####################################################################################
    ##USB WEB CAM
    if w.get_running_status():

        webcam.update_frame()
        retval, image = webcam.get_current_frame()
        if retval:

            w.update_frame_input(image)
            try:
                drawing = computer_vision.thresh_callback(thresh, image)
                w.update_frame_output(drawing)
            except:
                print "failed to make the drawing from thresh callback function"
        else:
            print "Falied to retrive image"
    #####################################################################################



    
    key = cv2.waitKey(10) % 256



    if key == 27:
        return 0
    else:
        return w, webcam, ip_cam, computer_vision, face_detector

    ##################################################################################################
    ##END OF MAIN


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', "--deviceID", help="Device ID")
    group.add_argument('-v', "--videoFile", help="Path to Video File")
    parser.add_argument('-l', "--dispLoc", dest="dispLoc", action="store_true")

    args = vars(parser.parse_args())



    points = 1

    ########################################################################
    webcam = Webcam(debug=False, name='webcam')
    try:
        list_of_video_devices = webcam.get_source_list(path='/dev/video*')
        webcam.set_source(0)
    except:
        print "Webcam not detected"
    #########################################################################




    ######################################################
    app = QtGui.QApplication(sys.argv)
    print ("UI initiating ............... ")
    try:
        w = MyWindowClass(None, debug=False, nodemcu_ip=nodemcu_ip, android_ip=android_ip)
        print "Window Class loaded"
        w.setWindowTitle('Robot AutoDocking')
        print "...................Finished UI init"
    except:
        print "Failed to initiate the UI"
    ######################################################

    




    while True:
        try:
            main(w, webcam)
            #t = threading.Thread(target=main , args= (w, webcam, ip_cam, computer_vision, face_detector))
            #t.deamon = True
            #t.start()
        except:
            print "Failed main"

        try:
            w.show()
        except:
            print "Failed UI"





