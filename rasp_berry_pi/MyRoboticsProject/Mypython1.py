import cv2
import numpy as np
img = cv2.imread("messi5.jpg",0) # image read 
cv2.imshow("img",img)    # image show 
k = cv2.waitKey(0) & 0xFF
if k==ord("s"):
    cv2.destroyAllWindows()
