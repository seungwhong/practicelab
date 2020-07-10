import cv2
import numpy as np

img =cv2.imread("image/test_image.jpg")
kernel = np.ones((5,5), np.uint8) #define kernel to make every value as 1.


#Gray and Blur
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0) #they have to be odd numbers

#Canny = image edge detector
imgCanny = cv2.Canny(img, 150, 200)

# increase thickness of the edge
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #iterations affects to the values
imgEroded = cv2.erode(imgDialation, kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)