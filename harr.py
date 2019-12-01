#!ipython
# -*- coding:utf-8 -*-

import numpy as np
import cv2

def haar(block):
    vertical_lowpass = (block[:, ::2]/2 + block[:, 1::2]/2)
    print(block[:,::2])
    print(block[:,::2]+block[:,1::2])
    vertical_highpass = (block[:, ::2]/2 - block[:, 1::2]/2)
    print(vertical_highpass)
    vertical_dwt = np.hstack((vertical_lowpass, vertical_highpass))

    horizontal_lowpass = (vertical_dwt[::2,:]/2 + vertical_dwt[1::2,:]/2)
    horizontal_highpass = (vertical_dwt[::2,:]/2 - vertical_dwt[1::2,:]/2)
    dwt = np.vstack((horizontal_lowpass, horizontal_highpass))
    dwt = threshold(dwt)
    return dwt



'''
dwt(block)
Applies 3 stage 2D Haar wavelet transform on each block, returning an 8x8
array of the following form:
---------------------------------
|LL3|HL3|HL2    |HL1            |
----+---|       |               |
|LH3|HH3|       |               |
--------+-------|               |
|LH2    |HH2    |               |
|       |       |               |
|       |       |               |
----------------+----------------
|LH1            |HH1            |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
---------------------------------
'''

def dwt(block):
    # First dwt transform
    dwt = haar(block)
    # Second dwt transform
    dwt = haar(dwt[:int(block.shape[0]/2), :int(block.shape[1]/2)])
    # Third dwt transform
    dwt[:int(block.shape[0]/4), :int(block.shape[1]/4)] = haar(dwt[:int(block.shape[0]/4), :int(block.shape[1]/4)])
    return dwt

def threshold(block):
    dwt = block
    for i in range(0,dwt.shape[0]):
        for j in range(0, dwt.shape[1]):
            if dwt[i,j]<0.02:
                dwt[i,j] = 0
    return dwt
######
cv2.setUseOptimized(True)   # OpenCV 中的很多函数都被优化过（使用 SSE2，AVX 等）。也包含一些没有被优化的代码。使用函数cv2.setUseOptimized() 来开启优化。
img_name = "/Users/arcadia/Documents/DIP/bm3d/lena512color.tiff"  # 图像的路径
img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)    # 读入图像，cv2.IMREAD_GRAYSCALE:以灰度模式读入图像

cv2.imwrite('original.jpg', img)
#print(img)
after_harr = dwt(img)
cv2.imwrite('test_harr.jpg', after_harr)
#print(after_harr)