import cv2
import numpy as np
from PIL import Image

scale = 2

def haar_wavelet_tranform(data):
    if (len(data) == 1):
        return data.copy()
    assert len(data) % 2 == 0   , "length needs to be even"
    mid_val = (data[0::2] + data[1::2]) / scale
    side_val = (data[0::2] - data[1::2]) / scale
    return np.hstack((haar_wavelet_tranform(mid_val), side_val))

def ihaar(data):
    if len(data) == 1:
        return data.copy()
    assert len(data) % 2 == 0, "length needs to be even"
    mid = ihaar(data[0:int(len(data)/2)]) * scale
    side = data[int(len(data)/2):] * scale
    out = np.zeros(len(data), dtype=float)
    out[0::2] = (mid + side) / 2.
    out[1::2] = (mid - side) / 2.
    return out

def haar_2d(srcImg):
    h,w = srcImg.shape
    rows = np.zeros(srcImg.shape, dtype=float)
    for y in range(h):
        rows[y] = haar_wavelet_tranform(srcImg[y])
    cols = np.zeros(srcImg.shape, dtype=float)
    for x in range(w):
        cols[:,x] = haar_wavelet_tranform(rows[:,x])
    return cols

def ihaar_2d(coeffs):
    h,w = coeffs.shape
    cols = np.zeros(coeffs.shape, dtype=float)
    for x in range(w):
        cols[:,x] = ihaar(coeffs[:,x])
    rows = np.zeros(coeffs.shape, dtype=float)
    for y in range(h):
        rows[y] = ihaar(cols[y])
    return rows

  ######
# cv2.setUseOptimized(True)   # OpenCV 中的很多函数都被优化过（使用 SSE2，AVX 等）。也包含一些没有被优化的代码。使用函数cv2.setUseOptimized() 来开启优化。
# img_name = "/Users/arcadia/Documents/DIP/bm3d/lena512color.tiff"  # 图像的路径
# img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)    # 读入图像，cv2.IMREAD_GRAYSCALE:以灰度模式读入图像

# cv2.imwrite('original.jpg', img)
# after_harr = haar_2d(img)
# cv2.imwrite('test_harr.jpg', after_harr)
# cv2.imwrite('ihaar.jpg', ihaar_2d(after_harr))


#srcImg = to_float(load('img_name.png')) #loading image

# img = np.array([[1,2,3,4,5,6,7,8],
#         [2,3,4,5,6,7,8,9],
#         [3,4,5,6,7,8,9,10],
#         [4,5,6,7,8,9,10,11],
#         [5,6,7,8,9,10,11,12],
#         [6,7,8,9,10,11,12,13],
#         [7,8,9,10,11,12,13,14],
#         [8,9,10,11,12,13,14,15]])
# print(img)

# after = haar_2d(img)
# print(after)

# after_th = ihaar_2d(after)
# print(after_th)
