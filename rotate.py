# Matrix= cv2.getRotationMatrix2D(center,                  angle,          scale)
#                                    |                       |               |
#                         (x,y) -> (w//2,h//2)           (degrees)     (1 for same,<1 for minimized,>1 for max.)
# cv2.warpAffine(image,Matrix,(w,h))

import cv2

image= cv2.imread("Screenshot 2026-09-22 211011.png")

if image is not None:
    height,width=image.shape[:2]
    center=(width//2,height//2)
    M=cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated= cv2.warpAffine(image, M, center)

    cv2.imshow("Original ",image)
    cv2.imshow("Rotated ",rotated)
    cv2.imwrite("rotated.jpg",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows

else:
    print("Image not found")