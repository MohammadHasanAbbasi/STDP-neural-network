import numpy as np 
from layers import GaborFilterLayer,PoolingLayer
import cv2
from objects import neuron
import random
gabor_degree=15

kernel_height=128
kernel_weight=128

# gabor layer parameters given to this are (31, 31), 9, theta, 15,0.5,0

gb=GaborFilterLayer('./photo.jpg',(31,31),9,15,0.5,0)
gabor_filtered_Layer=gb.make_filters(gabor_degree)

# print((gabor_filtered_Layer[5]) )


# pooling layer with size 5
pooling_sorted_spikes=[]
poolingLayer=PoolingLayer(5)
pooling_sorted_spikes=poolingLayer.make_filter(gabor_filtered_Layer)

# complex layer with extracting 8 features in size of 10*10 neurons in each matrices
features_size=8
neurons_matrice_size=10
feature_list_neuron_matrices=[]
for i in range(features_size):
    neurons_matrice=[neuron() for i in range(neurons_matrice_size**2)]
    
    neurons_matrice=np.array(neurons_matrice).reshape((neurons_matrice_size,neurons_matrice_size))

    feature_list_neuron_matrices.append(neurons_matrice)
   

# prepare complex layer kernel in size of 12*128*128 and value of random for first time
complex_layer_kernels=[]

for i in range(features_size):
        kernel_cube=[]
        
        for height in range(len(gabor_filtered_Layer)):
            for row in range(kernel_height):
                for col in range(kernel_weight):
                    kernel_cube.append([height,row,col,random.random()*-0.4+0.2])

        complex_layer_kernels.append(kernel_cube)

# implement spike over neurons based on the time (order of pooling_sorted_spike)
for pooling_index,row,col,value in pooling_sorted_spikes:
    print(pooling_index,row,col,value)
    if pooling_index==3:
        break


 