# Created by: Michael Johnson - 05-09-2025
# Leveraging f5py module
# Testing with 'cv2' image library

import time
# May consider opencv for python only, could be installed with pip
# pip install opencv-python
# For now just expecting opencv to be installed
#import cv2
#import cv as computervision
# Also expects numpy

# Note that cv2.waitKey(0) waits indefinitely for a key press, 
# and cv2.destroyAllWindows() closes all OpenCV windows


import sys # to access the system
import cv2
img_success_green = cv2.imread('./src/images/forest_small.jpg', cv2.IMREAD_ANYCOLOR)
img_failure_brown = cv2.imread('./src/images/smith_rock_small.jpg', cv2.IMREAD_ANYCOLOR)

# status = True
status = False

while True:

    print("Looping again...")

    if status is True:
        cv2.imshow("Success as Green Trees", img_success_green)
        cv2.waitKey(0)
        # sys.exit() # to exit from all the processes
        False
    
    if status is False:
        cv2.imshow("Failure as brown Trees", img_failure_brown)
        cv2.waitKey(0)
        #sys.exit() # to exit from all the processes

    time.sleep(5)

 
# Can destroy all windows
# cv2.destroyAllWindows()
