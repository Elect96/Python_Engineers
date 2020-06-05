#! /usr/bin/python
# src: https://www.pythonforengineers.com/image-and-video-processing-in-python/
import cv2
import sys

image = cv2.imread(sys.argv[1])

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur it
blurred_image = cv2.GaussianBlur(gray_image, (7, 7), 0)

# Show both images
cv2.imshow("Original image", image)
cv2.imshow("Blurred image", blurred_image)

# Run the Canny edge detector
canny = cv2.Canny(blurred_image, 30, 100)
cv2.imshow("Canny", canny)

im, contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Number of objects found = ", len(contours))
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow("Objects Found", image)

cv2.waitKey(0)

