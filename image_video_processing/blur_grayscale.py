#! /usr/bin/python
# src: https://www.pythonforengineers.com/image-and-video-processing-in-python/
import cv2
import sys

image = cv2.imread(sys.argv[1])
# convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur it
blurred_image = cv2.GaussianBlur(image, (7, 7), 0)

# Show all 3 images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)
