

#
# ===== simple Python implementation
#
import random
def numQuadrantHitsPython (numPoints):
    nhits = 0
    for n in range(numPoints):
        # generate random point inside the unit square (0,0), (0,1), (1,1), (1,0)
        x = random.random ()
        y = random.random ()
        # if inside unit circle, count a hit
        if (x*x + y*y) <= 1.0:
            nhits += 1
    return nhits


#
# ===== Numpy implementation
#
#import numpy
#def numQuadrantHitsNumPy (numPoints):


#
# ===== Numba implementation
#
#from numba import jit
#def numQuadrantHitsNumba (numPoints):

#
# ===== Numpy implementation MODIFIED for multiprocessing
#
#import numpy
#def numQuadrantHitsNumpyMOD ((numPoints, seed)):

#
# ===== Multi-Processing implementation
#
#import multiprocessing
#def numQuadrantHitsMP (numPoints, numProcs=4):


#
# ===== importable module: main does nothing
#

if __name__ == "__main__":
    import warnings
    warnings.simplefilter ("ignore")
