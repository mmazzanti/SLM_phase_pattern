import numpy as np
from matplotlib import pyplot as plt
import png as png
from pylab import *

SLM_X_SIZE=0.016          # SLM size in m (x direction)
SIZE_X,SIZE_Y=1272,1024    # SLM size in pixel
Grating=np.zeros((SIZE_Y, SIZE_X))

thetaB=5/360*2*np.pi       # Angle of diffraction of the 1st order (angle between incident beam and reflection)
wl=0.000008                # Wavelength of light

d=wl/(np.sin(thetaB)*2)    # Spacing of the diffraction grating
N=SLM_X_SIZE/d             # Number of steps (sawtooth) fitting in the slm area
incr=round(SIZE_X/N) 

for a in range(0,SIZE_Y):
    for b in range(0,SIZE_X):
        Grating[a,b]=b%incr*255/(incr-1)

Grating2=Grating.astype(uint8)
png.from_array(Grating2, 'L').save("Grating.png")

plt.imshow(Grating2)
plt.colorbar()
plt.show()      

plt.ion()
SIZE_X,SIZE_Y=1272,1024
Lens=np.zeros((SIZE_Y, SIZE_X))
x=round(SIZE_X/2)
y=round(SIZE_Y/2)

f=0.12                # focus in mm
wl=0.0000008          # WaveLength
xlens=0.006           # lens x-size in mm
ylens=0.006           # lens y-size in mm
scalex=xlens/SIZE_X   # scaling matrix to real size (here the lens size should be the SLM head size ??)
scaley=xlens/SIZE_X

for a in range(0,x):
    for b in range(0,y):
        phi=(2*np.pi/wl*(((b-0)*scalex)**2+((a-0)*scaley)**2)/(2*f))%(2*np.pi)
        Lens[y+b,x+a]=phi
        Lens[y+b,x-a]=phi
        Lens[y-b,x+a]=phi
        Lens[y-b,x-a]=phi

Lens=Lens/(2*np.pi)*256
Lens2=Lens.astype(uint8)
png.from_array(Lens2, 'L').save("Lens.png")

plt.imshow(Lens2)
plt.colorbar()
plt.draw()
plt.ioff()
plt.show()  

Tot=(Lens+Grating)%256
Tot2=Tot.astype(uint8)
png.from_array(Tot2, 'L').save("Lens+Grating.png")
plt.imshow(Tot2)
plt.colorbar()
plt.draw()