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

for a in range(0,x):
    for b in range(0,y):
        phi=(2*np.pi/wl*(((b-0)*scalex)**2+((a-0)*scaley)**2)/(2*f))%(2*np.pi)
        Lens[y+b,x+a]=phi
        Lens[y+b,x-a]=phi
        Lens[y-b,x+a]=phi
        Lens[y-b,x-a]=phi

Lens=Lens/(2*np.pi)*255
Lens2=Lens.astype(uint8)
png.from_array(Lens2, 'L').save("Lens.png")

plt.imshow(Lens2)
plt.colorbar()
plt.draw()
plt.ioff()
plt.show()