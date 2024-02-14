import cv2

#Resizing and Cropping
img = cv2.imread("/Users/yossipartouche/Desktop/Doc Photo/ISRAELI ID.jpeg")
print(img.shape)
#                                   height, width
#   x-direction---->
#  |
#  |
#  v
#  y-direction
imgResize = cv2.resize(img, (500, 400))

imgCropped = img[0:100, 100:200]

#cv2.imshow("resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
#cv2.imshow("Image", img)
cv2.waitKey(0)