#For any image, we can get height and width using '.shape'.
#We also get the channels(only for brg or rgb and not grayscale).

import cv2

image= cv2.imread("Screenshot 2026-09-22 211011.png")
if image is not None:
    height,width,channel=image.shape
    print (f"Image loaded:\nHeigth: {height}\nWidth: {width}\nChannels: {channel}")

else:
    print ("Could not find the image\n")
    