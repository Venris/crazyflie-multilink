import numpy as np
import cv2
import time

# img = cv2.imread('testimgage_2.tif',0)
img2 = cv2.imread('testimage_2.tif',0)
# imgcolor = cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
imgcolor2 = cv2.cvtColor(img2,cv2.COLOR_BAYER_BG2BGR)



# cv2.imshow('a0',img)
# cv2.imshow('a2',imgcolor)
cv2.imshow('a4',img2)
cv2.imshow('a8',imgcolor2)
# print img
# print type(img)
print img2
print img2.dtype
# print imgcolor
# print type(imgcolor)
print imgcolor2
print type(imgcolor2)

while(cv2.waitKey(0)):
    cv2.destroyAllWindows()