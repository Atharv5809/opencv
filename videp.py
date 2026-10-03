# cv2.VideoCapture(source)
import cv2

capture= cv2.VideoCapture(0)
while True:
    ret,frame=capture.read()

    if not ret:
        print ("Could not read frame")
        break

    cv2.imshow("Webcam Feed ",frame)

    if (cv2.waitKey(1) & 0xFF) ==ord('q'): # & 0xFF is the bit wise and operator which corrects the value from linux or other sources 
       print ("Quitting...")
       break

capture.release()
cv2.destroyAllWindows()