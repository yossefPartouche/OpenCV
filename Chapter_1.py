import cv2

img = cv2.imread("/Users/yossipartouche/Desktop/Doc Photo/ISRAELI ID.jpeg")
im_Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray_Image", im_Gray)
cv2.waitKey(0)