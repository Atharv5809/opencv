import cv2

image= cv2.imread("Screenshot 2026-09-22 211011.png")
if image is None:
    print ("Image not found")

else:
    resized=cv2.resize(image,(300,300)) #In the tuple- we first store the width and then the height
    cv2.imshow("Original image: ",image)
    cv2.imshow("Resized image: ",resized)
    cv2.imwrite("resizedImage.jpg",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  