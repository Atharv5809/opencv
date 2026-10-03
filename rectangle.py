#cv2.rectangle(image, pt1, pt2, color, thickness)
import cv2

image=cv2.imread("m.jpg")
if image is not None:
    cv2.line(image, (100,100), (1100,550), (100,0,150), 2)
    cv2.rectangle(image, (100,100), (1100,550), (100,0,150), -1)
    cv2.imshow("Rectangle ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found")