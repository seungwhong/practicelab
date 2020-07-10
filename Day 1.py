#Personal image or pre processing practice and project.

import cv2 #stands for computer vision


#First image processing would be import the image from the computer. (이미지 처리)

#print ("Package Imported") #<- to check if the package is installed.
img = cv2.imread('image/test_image.jpg')
# "imread"this is for read the image and the path are at ("Desktop/...")

cv2.imshow("Practice Img-Process",img) #("name of the window, which image")
cv2.waitKey(0) # (value) values is million second


"""
#Video processing (영상처리)
cap=cv2.VideoCapture('image/test_video.MP4')
# to bring the video it requires while loop.

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #'q' is for close button.
        break
"""

"""
#Using External Camera

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100) #this is for brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #'q' is for close button.
        break
"""


