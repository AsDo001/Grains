import cv2
import numpy as np


classic_img = cv2.imread("CORN_WHITE.jpg", cv2.IMREAD_GRAYSCALE)


if classic_img is None:
    print("")
    exit()


resize_img = cv2.resize(classic_img, (500, 500))

cv2.imshow('Resized Image', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()