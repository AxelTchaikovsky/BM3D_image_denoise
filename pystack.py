import cv2
import numpy as np

img1 = cv2.imread('sigma10.jpg')
img2 = cv2.imread('Basic3.jpg')
img3 = cv2.imread('Final3.jpg')

img4 = np.hstack((img1,img2,img3))

cv2.imwrite('cat.jpg',img4)