from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import scipy.fftpack as sfft
import random
import imageio
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


def join_phase_ampl(phase,ampl):
    tmp=np.zeros((ampl.shape[0],ampl.shape[1]),dtype=complex)
    for a in range(0,ampl.shape[0]):
        for b in range(0,ampl.shape[1]):
            tmp[a,b] = ampl[a,b]*np.exp(phase[a,b]*1.j)

    return tmp

def Beam_shape(sizex,sizey,sigma,mu):
    x, y = np.meshgrid(np.linspace(-1,1,sizex), np.linspace(-1,1,sizey))
    d = np.sqrt(x*x+y*y)
    g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )
    return g

def surface_plot (matrix, **kwargs):
    # acquire the cartesian coordinate matrices from the matrix
    # x is cols, y is rows
    (x, y) = np.meshgrid(np.arange(matrix.shape[0]), np.arange(matrix.shape[1]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(x, y, matrix, **kwargs)
    return (fig, ax, surf)

im = Image.open("Pinning_test_tweezers.bmp")
im_bin=np.array(im, dtype=np.uint8)
SIZE_X,SIZE_Y=im_bin.shape
init_ampl=np.sqrt(im_bin) ## Square of amplitude
init_ampl=init_ampl.astype(np.uint8) ## Cast back to uint8

PS_shape=Beam_shape(SIZE_X,SIZE_Y,255,0)


u=np.zeros((SIZE_X,SIZE_Y),dtype=complex)
ampl=np.zeros((SIZE_X,SIZE_Y),dtype=complex)

ampl=join_phase_ampl(2*np.pi*np.random.rand(SIZE_X,SIZE_Y)-np.pi,init_ampl)

images = []
error=[]


for x in range(20):
    u = sfft.fft2(ampl)
    u = sfft.fftshift(u)

    #The SLM renders the phase as multiple of 255 (255=2pi, 0 = 0pi). Some values of pi aren't permitted (discrete phase pattern)
    phase=np.round((np.angle(u)+np.pi)*255/(2*np.pi))

    ## For plotting algorithm evol.
    SLM_phase=phase
    ## End of plotting

    #Back to the range [-pi,pi] but keeping the discretization imposed by the SLM (integers in [0,255])
    phase=phase/255*(2*np.pi)-np.pi

    u=join_phase_ampl(phase,PS_shape.T)
    ampl=sfft.ifft2(u)
    #ampl = sfft.ifftshift(ampl)

    ## For plotting algorithm evol.
    tmp=np.square(np.abs(sfft.ifft2(u)))
    REAL_img=np.round(tmp/np.max(tmp)*255)
    images.append(np.uint8(np.hstack((SLM_phase, REAL_img))))
    ## End of plotting

    error.append(np.sum(np.square(REAL_img-im_bin)))

    ampl=join_phase_ampl(np.angle(ampl),init_ampl)


#plt.close('all')
#fig = plt.figure(2)

#plt.figure(1)
#plt.imshow(np.angle(u))
#plt.figure(2)
#plt.imshow(np.abs(sfft.ifft2(u)))

kwargs_write = {'fps':1.0, 'quantizer':'nq'}
imageio.mimsave('./SLM_evol.gif', images, fps=1)

plt.plot(error)
plt.show()

plt.imshow(REAL_img-init_ampl)
#plt.imshow(REAL_img)

plt.colorbar()
plt.show()
