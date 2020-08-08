# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 11:48:55 2020

"""

# based on: http://viennacl.sourceforge.net/pyviennacl/doc/examples/direct-solvers.html
# for the purpose of spice, this would be more appropriate: 
# http://viennacl.sourceforge.net/pyviennacl/doc/examples/iterative-solvers.html
import pyviennacl as p
import numpy as np
import random

N = 100
A = np.zeros((N, N), dtype = np.float32)

for i in range(N):
    for j in range(N):
        if j >= i:
            A[i, j] = np.float32(random.randint(0,1000) / 100.0)

A = p.Matrix(A)
b = p.Vector(np.random.rand(N).astype(np.float32))
x = p.solve(A, b, p.upper_tag())

# Copy the solution from the device to host and display it
print("Solution of Ax = b for x:\n%s" % x)

