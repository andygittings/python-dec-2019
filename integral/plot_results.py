#
#
# Takes a set of files containing value data pairs and plot on a single graph
#
# Requires: matplotlib
#

import pylab

#
# File list contains a list of labels and results filenames.
# 
fileList = [ 	
		("Python", "python.txt")
#		("Numpy", "numpy.txt"),	
#		("Numba", "numba.txt"),	
#		("Cython", "cython.txt"),	
#		("MPI4py_4", "mpi4py_4.txt"),	
#		("MPI4py_8", "mpi4py_8.txt"),	
#		("MPI4py_16", "mpi4py_16.txt")	
	   ]
	     
#
# for each file read pairs and plot with appropriate label
#
for label, file in fileList:
    data = pylab.loadtxt(file)
    pylab.plot( data[:,0], data[:,1], label=label )

pylab.legend()

#
# Label graph...
#

pylab.title("Results")
pylab.xlabel("No. of trapeziums")
pylab.ylabel("Time (s)")

pylab.show()
