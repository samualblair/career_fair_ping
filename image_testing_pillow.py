# Created by: Michael Johnson - 05-09-2025
# Leveraging f5py module
# Testing with 'pillow' image library

import time
# Also could use pillow
# via pip: pip install pillow
# or via homebrew: brew install pillow
# from pillow import image as computerimage
from PIL import Image as image
import sys # to access the system

# Open images
img_success_green = image.open('./src/images/forest_small.jpg')
img_failure_brown = image.open('./src/images/smith_rock_small.jpg')



# status = True
status = False

while True:

    print("Looping again...")

    if status is True:
        #Shows the image for up
        img_success_green.show()

    if status is False:
        #Shows the image for down
        img_failure_brown.show()

    time.sleep(5)

