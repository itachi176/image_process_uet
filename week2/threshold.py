import cv2
img = cv2.imread('opencv.png',0)
img = cv2.resize(img, (640, 480))
for i in range(480):
    for j in range(640):
        if(img[i][j] > 200):
            img[i][j] = 255
        else:
            img[i][j] = 0
print(img)
cv2.imshow("img", img)
cv2.waitKey()