from numpy import load
import numpy as np
from scipy import ndimage
from scipy.ndimage.interpolation import zoom
vox_size = 32
# load array
data = load('voxelsFloat/11_115891_198292_118752_200556.npy')
# print the array
# print(data.shape)
# n = 100
# desiredshape = np.array([n,n,n])
# zoomArray = desiredshape.astype(float) / data.shape
# zoomed = zoom(data, zoomArray).astype(int)
# print(zoomed.shape)
# print(zoomed)
# #normalise data
# for i in range(3):
#     print("max before",np.max(data[:,i]))
#     data[:,i] = data[:,i]-np.min(data[:,i])
#     print("max after",np.max(data[:,i]))

# print("max all",np.max(data))
# print("ratio",np.max(data)/vox_size)
# data = data/(np.max(data)/(vox_size-1))

# for i in range(3):
#     print("max after",np.max(data[:,i]))

# data = data.astype(int)

# #make immages 
# img = np.zeros([vox_size,vox_size,vox_size])

# for voxel in data:
#     #print(voxel)
#     img[voxel[0],voxel[1],voxel[2]]= 1

#print(np.unique(img,return_counts=True))         
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# # N1 = 10
# N2 = 10
# N3 = 10
# ma = np.random.choice([0,1], size=(N1,N2,N3), p=[0.99, 0.01])


fig = plt.figure()
#ax = fig.gca(projection='3d')

#ax.voxels(data[40:60,40:60,40:60], edgecolor="k")
for l in range(0,100,1):
     plt.imshow(data[:,:,l])
     plt.show()

print(np.unique(data,return_counts=True))