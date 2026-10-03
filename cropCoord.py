import cv2

image=cv2.imread("Screenshot 2026-09-21 085255.png")
cropped= image[100:1200,50:1150] #[y1:y2,x1:x2]

cv2.imshow("Original ",image)
cv2.imshow("Cropped ",cropped)
cv2.waitKey(0)
cv2.detsroyAllWindows