import cv2
import numpy as np
import time

img = cv2.imread('sudoku3.jpg')
# blur = cv2.bilateralFilter(img,9,75,75)
gray = cv2.GaussianBlur(img,(7,7),0)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, gray = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
polygon = contours[1]
# second = contours[1]
# print(len(second))
# print(1980*18/5)
pts1 = []
X = [x for x in range(0, 450, 50)]
print(X)
epsilon = 0.1*cv2.arcLength(polygon,True)
approx = cv2.approxPolyDP(polygon,epsilon,True)
# print(approx)
for i in range(len(approx)):
	pts1.append([approx[i][0][0], approx[i][0][1]])
	cv2.circle(img, (approx[i][0][0], approx[i][0][1]), 3, (0,255,0), -1)

pts1 = np.float32(pts1)
pts2 = np.float32([[0,0],[450,0],[450,450],[0,450]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(450,450))

# for i in range(len(second)):
	# cv2.circle(img, (second[i][0][0], second[i][0][1]), 7, (255,0,0), -1)
# cv2.drawContours(img, contours[1], -1, (255,0,0), 3)
cv2.imshow('input', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
