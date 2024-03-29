[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)

### NOTE: This code hasn't been updated in a while. If you're searching a more up-to-date version (with GUI functionalities) of it check out [SLM Controller](https://github.com/mmazzanti/SLMcontroller)

# SLM Phase Pattern generator

Implementation of Gerchberg-Saxton algorithm for generating a SLM phase pattern from a target intensity image.
The code is meant for a Hamamatsu LCOS-SLM model X13138-5

The various files have the following purposes:
* GS.py : Gerchberg–Saxton algorithm. Generates a phase hologram in a range [0,255] corresponding to a [0,2pi] phase. In the SLM plane the assumption is that a the incident amplitude has the shape of a Gaussian beam.


| Phase pattern evolution for GS algorithm  | Errors and reconstructed image for the GS algorithm (40 iterations)|
|  :---:  |  :---:  |
|<img width="300" height="150" src="https://github.com/mmazzanti/SLM_phase_pattern/blob/master/Presentation_files/SLM_evol_show.gif"> | <img width="400" height="265" src="https://github.com/mmazzanti/SLM_phase_pattern/blob/master/Presentation_files/GS_results.png">|


* GSW.py : Weighted Gerchberg–Saxton algorithm. Improvement of the GS algorithm to obtain better hologram uniformity. Based on [1]

<p align="center">
 <strong>Errors and reconstructed image for the GSW algorithm (40 iterations)</strong></p>
 <p align="center">
<img width="400" height="265" src="https://github.com/mmazzanti/SLM_phase_pattern/blob/master/Presentation_files/GSW_results.png">
</p>

* Fresnel_gen.py : Generates a Fresnel lens pattern for the specified focus.

<p align="center">
  <img width="300" height="242" src="https://github.com/mmazzanti/SLM_phase_pattern/blob/master/Presentation_files/Lens_show.png">
</p>

* Blazed_grating_gen.py : Generates a blazed grating pattern for shifting the hologram from the zero order spot.

<p align="center">
  <img width="300" height="242" src="https://github.com/mmazzanti/SLM_phase_pattern/blob/master/Presentation_files/Grating_show.png">
</p>


[1] Roberto Di Leonardo, Francesca Ianni, and Giancarlo Ruocco, *"Computer generation of optimal holograms for optical trap arrays,"* Opt. Express 15, 1913-1922 (2007)
