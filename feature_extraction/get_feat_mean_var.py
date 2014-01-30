#! /usr/bin/python

# script to extract mean and variance from matrix

import numpy
import math
from os import system
import sys

mat_file = sys.argv[1]
output_file = sys.argv[2]

mat_file = numpy.loadtxt(mat_file,dtype='float')

psy_mat = mat_file[mat_file[:,1]==1,:]
child_mat = mat_file[mat_file[:,2]==1,:]

print "\n"
print output_file 

means_stds = numpy.zeros((4,4))

#psy
#pitch
psy_mean_pitch = numpy.mean(psy_mat[:,3])
psy_std_pitch = numpy.std(psy_mat[:,3])
print psy_mean_pitch,psy_std_pitch

# intensity
psy_mean_int = numpy.mean(psy_mat[:,4]) 
psy_std_int = numpy.std(psy_mat[:,4])
print psy_mean_int,psy_std_int

# jit shim
psy_jit_ds = psy_mat[psy_mat[:,5]>0,5]
psy_shim_ds = psy_mat[psy_mat[:,6]>0,6]
psy_mean_jit = numpy.mean(psy_jit_ds)
psy_std_jit = numpy.std(psy_jit_ds)
psy_mean_shim = numpy.mean(psy_shim_ds)
psy_std_shim = numpy.std(psy_shim_ds)
print psy_mean_jit, psy_std_jit, psy_mean_shim, psy_std_shim

#child
if child_mat.shape[0] >0:
	# pitch
	child_mean_pitch = numpy.mean(child_mat[:,3])
	child_std_pitch = numpy.std(child_mat[:,3])

	# intensity
	child_mean_intensity = numpy.mean(child_mat[:,4])
	child_std_intensity = numpy.std(child_mat[:,4])

	# jit shim
	child_jit_ds = child_mat[child_mat[:,5]>0,5]
	child_shim_ds = child_mat[child_mat[:,6]>0,6]
	child_mean_jit = numpy.mean(child_jit_ds)
	child_std_jit = numpy.std(child_jit_ds)
	child_mean_shim = numpy.mean(child_shim_ds)
	child_std_shim = numpy.mean(child_shim_ds)


	print "------------"	
	print child_mean_pitch,child_std_pitch
	print child_mean_intensity, child_std_intensity
	print child_mean_jit, child_std_jit, child_mean_shim, child_std_shim
	print "-------------\n-------------"

	means_stds[2,0] = child_mean_pitch
	means_stds[2,1] = child_mean_intensity
	means_stds[2,2] = child_mean_jit
	means_stds[2,3] = child_mean_shim

	means_stds[3,0] = child_std_pitch
	means_stds[3,1] = child_std_intensity
	means_stds[3,2] = child_std_jit
	means_stds[3,3] = child_std_shim


means_stds[0,0] = psy_mean_pitch
means_stds[0,1] = psy_mean_int
means_stds[0,2] = psy_mean_jit
means_stds[0,3] = psy_mean_shim

means_stds[1,0] = psy_std_pitch
means_stds[1,1] = psy_std_int
means_stds[1,2] = psy_std_jit
means_stds[1,3] = psy_std_shim

numpy.savetxt(output_file,means_stds,fmt='%10e')
