# cv2.putText(image, text, origin, font, font scale, color, thickness)
# To access font styles, use a special function cv2.FONT_"".

import cv2

image= cv2.imread("m.jpg")

if image is not None:
    cv2.putText(image, "Yokoso Watashino soul society", (350,100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.2, (100,0,150), 2)
    cv2.imshow("Text ",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image not found") 