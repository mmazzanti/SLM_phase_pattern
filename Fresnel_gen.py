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
Lens=np.zeros((SIZE_Y, SIZE_X))
x=round(SIZE_X/2)
y=round(SIZE_Y/2)

f=0.1                # focus in mm
wl=0.0000008          # WaveLength
xlens=0.068*f           # lens x-size in mm
ylens=0.068*f           # lens y-size in mm
scalex=xlens/SIZE_X   # scaling matrix to real size (here the lens size should be the SLM head size ??)
scaley=xlens/SIZE_X

# for a in range(0,x):
#     for b in range(0,y):
#         phi=(2*np.pi/wl*(((b-0)*scalex)**2+((a-0)*scaley)**2)/(2*f))%(2*np.pi)
#         Lens[y+b,x+a]=phi
#         Lens[y+b,x-a]=phi
#         Lens[y-b,x+a]=phi
#         Lens[y-b,x-a]=phi

f=200e-3              # focus in mm
wl=760e-9          # WaveLength
pixel_pitch = 12.5e-6 # pixel pitch in m
scalex=xlens/SIZE_X   # scaling matrix to real size (here the lens size should be the SLM head size ??)
scaley=xlens/SIZE_Y
lens_size = SIZE_X if SIZE_X > SIZE_Y else SIZE_Y
x=round(lens_size - SIZE_X)/2
y=round(lens_size - SIZE_Y)/2



Lens=np.zeros((lens_size, lens_size))

# Generate meshgrid for the lens
x_list = np.linspace(-SIZE_X/2,SIZE_X/2,SIZE_X+1)
y_list = np.linspace(-SIZE_Y/2,SIZE_Y/2,SIZE_Y+1)
X, Y = np.meshgrid(x_list,y_list)

# Scaling factor of the lens
gamma = np.pi/(wl*f)
# Maximum phase-ring radius that we can generate on the SLM (limited by the SLM pixel pitch)
rN = wl*f/(2*pixel_pitch)
# Lens offset 
x_offset, y_offset= 0.0, 0.0
# Lens size mask
r = np.sqrt((X - x_offset)**2 + (Y - y_offset)**2)
mask = r < rN/pixel_pitch
# Generate lens
phi = ((1+np.cos(gamma*((X*pixel_pitch)**2+(Y*pixel_pitch)**2)))/2)
# Scale by 2*pi --> 255
Lens=mask*phi*255
Lens2=Lens.astype(uint8)
png.from_array(Lens2, 'L').save("Lens.png")

plt.imshow(Lens2)
plt.colorbar()
plt.draw()
#plt.ioff()
#plt.show()
