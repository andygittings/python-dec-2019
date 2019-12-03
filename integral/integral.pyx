#
# Cython implementation
#

# always import cython
import cython
# import modules for multithreading
from cython.parallel import prange, parallel
cimport openmp
# import external C mathematical functions
from libc.math cimport sqrt

# eliminate Python checks
@cython.cdivision(True)


#
# ----- function to integrate
#
#cdef double func (double x) nogil:
#   """Function to integrate"""


#
# ----- integrator
#
#cpdef double trapint (double a, double b, int N, int nt=4):
#    """Compute a definite integral using the trapezium rule and pure Python"""


