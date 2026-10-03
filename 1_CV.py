#red   - [255,0,0]
#green - [0,255,0]
#blue  - [0,0,255]
#jpg, tiff, png, bmp -> image types based on resolutions
import cv2

print ("OpenCV version: ",cv2.__version__)
image= cv2.imread("Screenshot 2026-09-21 085255.png")
if image is None:
  print ("Error")
else:
  print ("Image found")