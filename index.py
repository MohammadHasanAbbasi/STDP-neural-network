import numpy as np 
from layers import gaborFilterLayer

# gabor layer parameters given to this are (31, 31), 9, theta, 15,0.5,0

gb=gaborFilterLayer('./photo.jpg',(31,31),9,15,0.5,0)
gaborLayer=gb.make_filters(15)

print(np.amax(gaborLayer[5]) )


# pooling layer 


