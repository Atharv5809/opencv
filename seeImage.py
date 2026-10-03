import cv2

image= cv2.imread("Screenshot 2026-09-22 211011.png")
cv2.imshow("Window Title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("FirstCV.jpg",image)