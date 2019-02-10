import numpy as np
import cv2
from matplotlib import pyplot as plt

class gaborFilterLayer:
    
    def __init__(self,image_path, size, sigma, lamda, gamma, psi):
        self.image_path=image_path
        self.size = size
        self.sigma = sigma
        self.lamda = lamda
        self.gamma = gamma
        self.psi = psi
        
    def make_filters(self,change_degree):
        gabor_filtered_images=[]
        
        change_radian=np.pi*change_degree/180

        img = cv2.imread(self.image_path,cv2.IMREAD_GRAYSCALE)
        for theta in np.arange(0, np.pi, change_radian):
            kernel=cv2.getGaborKernel(self.size, self.sigma, theta, self.lamda,self.gamma,0)
            filtered_img=cv2.filter2D(img,cv2.CV_8UC3,kernel)
            cv2.imwrite("./output/gabor/gabor{}.png".format(theta/np.pi*180), filtered_img)
            gabor_filtered_images.append(filtered_img)

        return gabor_filtered_images


