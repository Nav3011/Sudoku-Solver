import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
polygon = contours[0]
print(polygon[1][0])
for i in range(4):
	cv2.circle(img, (polygon[i][0][0], polygon[i][0][1]), 15, (0,255,0), -1)
cv2.imshow('input', img)
cv2.waitKey(0)

cv2.destroyAllWindows()