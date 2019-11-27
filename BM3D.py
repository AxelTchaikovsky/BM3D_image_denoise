import cv2
import PSNR
import numpy

cv2.setUsePptimized(True)

#parameters initialization
sigma = 25
Threshold_Hard3D = 2.7*sigma
First_Match_threshold = 2500
Step1_Max_matched_cnt = 16
Step1_Blk_Size = 8
Step1_Blk_Step = 3
Step1_Search_Step = 3
Step1_Search_Window = 39

