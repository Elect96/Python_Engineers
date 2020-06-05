#! /usr/bin/python
# src: https://www.pythonforengineers.com/image-and-video-processing-in-python/
import sys
import cv2

image = cv2.imread(sys.argv[1])
cv2.imshow("Image", image)
cv2.waitKey(0)