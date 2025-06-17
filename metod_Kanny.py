import cv2
import numpy as np
from resize import resize_img


edges = cv2.Canny(resize_img, 100, 200)

cv2.imshow("Classic", resize_img)
cv2.imshow('Kanny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()