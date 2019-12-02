import cv2
import numpy as np

def Add_salt_pepper_Noise(srcArr,pa,pb):
	N_SP_img = srcArr
	shape0 = srcArr.shape[0]-1
	shape1 = srcArr.shape[1]-1
	amount1 = int(pa*shape0*shape1)
	amount2 = int(pb*shape0*shape1)

	for i in range(amount1):
		x_random=np.random.random_integers(0,shape0)
		y_random=np.random.random_integers(0,shape1)
		N_SP_img[x_random,y_random]=0

	for i in range(amount2):
		x_random=np.random.random_integers(0,shape0)
		y_random=np.random.random_integers(0,shape1)
		N_SP_img[x_random,y_random]=255         
	return N_SP_img 

def Add_GNoise(srcArr,mean,sigma):
	N_G_img = srcArr.copy()
	cv2.randn(N_G_img,mean,sigma)
	cv2.add(srcArr,N_G_img,N_G_img)
	return N_G_img



def main():
	srcArr = cv2.imread("lena512color.tiff")
	img = cv2.resize(cv2.cvtColor(srcArr,cv2.COLOR_RGB2GRAY),(256,256))
	cv2.imwrite("ori.png",img)
	
# Gaussain noise
	mean = 0
	sigma = 10
	gaussian_noise = Add_GNoise(img,mean,sigma)
	cv2.imwrite("sigma10.jpg", gaussian_noise)

main()
