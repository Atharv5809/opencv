#cv2.line (image, point1, point2, color, thickness)

import cv2

image=cv2.imread("m.jpg") 
color=(120, 0, 150) #BGR
point1= (0,100)
point2= (1900,1000)
if image is not None:
    cv2.line(image, point1, point2, color, 3)
    cv2.imshow("Line ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print ("Image not found")