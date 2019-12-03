#!/usr/bin/env python


#
# ===== pure Python implementation
#

import math

#
# ----- function to integrate
#
def funcPython (x):
    """Function to integrate"""
    return 2.0*math.sqrt(1.0-x*x)

#
# ----- integrator
#
def trapintPython (a, b, N):
    """Compute a definite integral using the trapezium rule and pure Python"""

    # interval length (N intervals = N+1 nodes)
    h = (b - a) / float (N)

    # initial and final point only count with weight half
    v = (funcPython (a) + funcPython (b)) / 2.0

    # add the interior points
    for n in xrange(1,N):
        x = a + n*h
        v = v + funcPython (x)

    # scale by the interval width
    return v*h

#
#-----------------------------------------------------------------------
#

#
# ===== Numpy implementation
#

# use numpy.sin, which can work on numpy arrays
#import numpy

#
# ----- function to integrate
#
#def funcNumpy (x):
#    """Function to integrate"""

#
# ----- integrator
#
#def trapintNumPy (a, b, N):
#    """Compute a definite integral using the trapezium rule and NumPy arrays"""

#
#-----------------------------------------------------------------------
#

#
# ===== Numba implementation
#

#
# ----- integrator
#
#from numba import jit
#from numba import vectorize

#def funcNumba (x):
#    """Function to integrate"""

#def trapintNumba (a, b, N):
#    """Compute a definite integral using the trapezium rule and pure Python"""

#
# ===== importable module: main does nothing
#

if __name__ == "__main__":
    import warnings
    warnings.simplefilter ("ignore")
