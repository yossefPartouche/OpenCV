import cv2
import numpy as np

#create shapes and add lines and text in imags
img = np.zeros((512,512),np.uint8)
#check the dimension
print(img.shape)
#to color the image
#img[:] =255,0,0

cv2.line(img, (0,0), (img.shape[1], img.shape[0]),
         (100,0,0),3)
cv2.rectangle(img, (0,0), (250,350), (255,255,0),1)
cv2.circle(img,(400,50),30, (255,255,0),5)
cv2.imshow("Image",img)
cv2.putText(img," OPENCV ", (200, 300), cv2.FONT_HERSHEY_TRIPLEX,1, (100,0,0),1)
cv2.waitKey(0)
