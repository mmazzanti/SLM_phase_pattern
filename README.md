# SLM Phase Pattern generator

Implementation of Gerchberg-Saxton algorithm for generating a SLM phase pattern from a target intensity image.
The code is meant for a Hamamatsu LCOS-SLM model X13138-5

The various files have the following purposes:
* SLM_pattern.py : G-S algorithm. Generates a phase hologram in a range [0,255] corresponding to a [0,2pi] phase. In the SLM plane the assumption is that a the incident amplitude has the shape of a Gaussian beam.
![alt text](https://github.com/mmazzanti/SLM_phase_pattern/blob/master/Presentation_files/SLM_evol_show.gif)

* Fresnel_gen.py : Generates a Fresnel lens pattern for the specified focus.

* Blazed_grating_gen.py : Generates a blazed grating pattern for shifting the hologram from the zero order spot.
