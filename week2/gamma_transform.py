import cv2 
import numpy as np 

def gamma_adjust(img, gamma = 1.0):
    img = np.array(255.0*(img/255.0)**gamma,np.uint8)

    return img 

img = cv2.imread('lenna.jpg', 0)
img = cv2.resize(img, (640, 480))
gamma_img = gamma_adjust(img, 0.4)
cv2.imshow("origin", img)
cv2.imshow("gamma", gamma_img)
cv2.waitKey()