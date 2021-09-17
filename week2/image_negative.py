import cv2 
img = cv2.imread('lenna.jpg', 0)
img = cv2.resize(img, (640, 480))
print(img.shape)
# for i in range(48
negative_img = 255 - img
cv2.imshow("img", img)
cv2.imshow("negative_img", negative_img)
cv2.waitKey()