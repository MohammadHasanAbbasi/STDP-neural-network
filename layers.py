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

class poolingLayer:
    
    def __init__(self,pooling_size):
            self.pooling_size=pooling_size
       
    
    def make_filter(self, gabor_filtered_Layer):
        
        pooling_filtered_images=[]
        index=0
        for gabor_matrix in gabor_filtered_Layer:
            pooled_matrix=[]
            for i in range(0,len(gabor_matrix),self.pooling_size):
                row=[]
                for j in range(0,len(gabor_matrix),self.pooling_size):
                        max=-100
                        for k in range(0,self.pooling_size):
                                for l in range(0,self.pooling_size):
                                        if max <gabor_matrix[i+k][j+l]:
                                                max=gabor_matrix[i+k][j+l]
                                        #  print(gabor_filtered_Layer[index][i+k][j+l],end=" ")
                        
                        row.append(max)
                pooled_matrix.append(row)
                        #  pooling_filtered_images.append((i/pooling_size,j/pooling_size,max))        
            pooling_filtered_images.append(pooled_matrix)
            cv2.imwrite("./output/pooling/{}.png".format(index), np.array(pooled_matrix) )
            index +=1
            
        return pooling_filtered_images
        
                
