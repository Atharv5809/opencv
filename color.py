import cv2

image= cv2.imread("Screenshot 2026-09-22 211011.png")
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if image is not None:
  cv2.imshow("Window Title", gray)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

else:
  print ("Image not found")