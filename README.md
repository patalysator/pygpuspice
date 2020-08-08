# pygpuspice

Example SPICE implementation to start off: 
https://ahkab.github.io/ahkab/

For equation solving on GPUs, two frameworks are available:
- OpenGL, which works with any graphics processor (AMD and Nvidia)
- CUDA, which works with Nvidia exclusively

When working with Python, this is realized as:
- PyViennaCL, which provides linear algebra functions on the basis of OpenGL, so it has a high level implementation of what we need, but
it is not so well maintained.  
- PyCUDA for CUDA

Way forward:
1. Try to build a solver for large-scale circuits only using current/voltage sources and resistors, running on a GPU through PyViennaCL
2. Extend the solver to work with non-linear components as well (diodes for example). Whereas (1) only needs to solve one matrix equation, 
this requires solving a matrix equation iteratively. Important: the number of messages passed between GPU and memory must be minimized to 
get the most out of its performance. Communication between memory and GPU is comparatively slow.