import cv2
import numpy as np

img = cv2.imread("/Users/yossipartouche/Desktop/Doc Photo/ISRAELI ID.jpeg")
#(x,x) --> matrix of size
#uint8 --> Unsigned Ints of 8 bits --> 255 colors
#the tuple refers to the thickness of each line.
kernel = np.ones((2,2), np.uint8)


im_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
im_Blur = cv2.GaussianBlur(im_Gray,(5,5),0)
im_Canny = cv2.Canny(img, 150, 200)
img_Dialation = cv2.dilate(im_Canny,kernel,iterations=1)
im_Eroded = cv2.erode(img_Dialation, kernel, iterations=1)

cv2.imshow("Gray_Image", im_Gray)
cv2.imshow("blurred Image", im_Blur)
cv2.imshow("Canny Image", im_Canny)
cv2.imshow("Dialation Image", img_Dialation)
cv2.imshow("Erosion image", im_Eroded)

cv2.waitKey(0)