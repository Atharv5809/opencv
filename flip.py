# flip= cv2.flip(image, flipcode)
# filpcode => 0 for vertical, 1 for horizontal and -1 for both flip.

import cv2

image= cv2.imread("m.jpg")
if image is not None:
    vert= cv2.flip(image, 0)
    horiz= cv2.flip(image,1)
    both= cv2.flip(image,-1)

    cv2.imshow("Original ",image)
    cv2.imshow("Vertically flipped ",vert)
    cv2.imshow("Horizontally flipped ",horiz)
    cv2.imshow("Horizontally and vertically flipped ",both)

    cv2.waitKey(0)
    cv2.destroyAllWindows

else:
    print("Image not found")