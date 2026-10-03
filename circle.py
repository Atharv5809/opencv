#cv2.circle(image, center, radius, color, thickness)
import cv2

image=cv2.imread("m.jpg")
if image is not None:
    cv2.circle(image, (600,400), 250, (100,0,150), -1)
    cv2.imshow("Drawing ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image not found")    