from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import scipy.fftpack as sfft
import random
import imageio
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import png as png

plt.ion()
SIZE_X,SIZE_Y=1272,1024
SLM_SIZE_X, SLM_SIZE_Y = 1280,1024 

Lens=np.zeros((SIZE_Y, SIZE_X))
SLMIMAGE=np.zeros((SLM_SIZE_Y, SLM_SIZE_X))

f=400e-3              # focus in mm
wl=760e-9          # WaveLength
pixel_pitch = 12.5e-6 # pixel pitch in m

# Generate meshgrid for the lens
x_list = np.linspace(-SIZE_X/2,SIZE_X/2,SIZE_X)
y_list = np.linspace(-SIZE_Y/2,SIZE_Y/2,SIZE_Y)
X, Y = np.meshgrid(x_list,y_list)

# Scaling factor of the lens
gamma = np.pi/(wl*f)
gamma = 1/(wl*f)
# Maximum phase-ring radius that we can generate on the SLM (limited by the SLM pixel pitch)
rN = wl*f/(2*pixel_pitch)
print("rN = ", 2*rN*1e3, " mm")
# Lens offset 
x_offset, y_offset= 0, 0
# Lens size mask
r = np.sqrt((X - x_offset)**2 + (Y - y_offset)**2)
mask = r < rN/pixel_pitch
# Generate lens
phi = gamma*(((X - x_offset)*pixel_pitch)**2+((Y - y_offset)*pixel_pitch)**2)/2
  
#phi = ((1+np.cos(gamma*((X*pixel_pitch)**2+(Y*pixel_pitch)**2)))/2)
# Scale by 2*pi --> 255
Lens=mask*phi*255
SLMIMAGE[0:1024,0:1272] = Lens
SLMIMAGE = SLMIMAGE.astype(uint8)
png.from_array(SLMIMAGE, 'L').save("Lens.png")

plt.imshow(SLMIMAGE)
plt.colorbar()
plt.draw()
#plt.ioff()
#plt.show()
