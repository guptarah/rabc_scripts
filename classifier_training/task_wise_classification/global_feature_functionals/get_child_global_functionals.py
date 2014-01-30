#! /usr/bin/python

# script to get the functional of child utterances
import sys 
import math
import os 
from os import system
import numpy  

all_features = sys.argv[1]
output_file = sys.argv[2]

all_features = numpy.loadtxt(all_features,dtype='float')

# get total number of utterances
child_vad = all_features[:,2]

if numpy.mean(child_vad)>0:
	diff_child_vad = numpy.diff(numpy.concatenate(([0],child_vad)))
	count = numpy.sum(diff_child_vad == 1)

	# get %age of vad on
	child_vad_perc = numpy.sum(child_vad == 1)/float(len(child_vad))

	# get pitch statisticals
	mean_child_pitch = numpy.mean(all_features[child_vad==1,3])
	var_child_pitch = numpy.var(all_features[child_vad==1,3])
	range_child_pitch = numpy.ptp(all_features[child_vad==1,3])
	median_child_pitch = numpy.median(all_features[child_vad==1,3])

	# get intensity statisticals
	mean_child_int = numpy.mean(all_features[child_vad==1,4])
	var_child_int = numpy.var(all_features[child_vad==1,4])
	range_child_int = numpy.ptp(all_features[child_vad==1,4])
	median_child_int = numpy.median(all_features[child_vad==1,4])

	# get jitter statisticals 
	child_jit = all_features[child_vad==1,5]
	child_jit = child_jit[child_jit>-100,:]
	if child_jit.shape[0] > 0:
		mean_child_jit = numpy.mean(child_jit)
		var_child_jit = numpy.var(child_jit)
		range_child_jit = numpy.ptp(child_jit)
		median_child_jit = numpy.median(child_jit)
	else:
		mean_child_jit = 0
		var_child_jit = 0
		range_child_jit = 0
		median_child_jit = 0

	# get shimmer statisiticals
	child_shim = all_features[child_vad==1,6]
	child_shim = child_shim[child_shim>-100,:]
	if child_shim.shape[0] > 0:
		mean_child_shim = numpy.mean(child_shim)
		var_child_shim = numpy.var(child_shim)
		range_child_shim = numpy.ptp(child_shim)
		median_child_shim = numpy.median(child_shim)
	else: 
		mean_child_shim = 0
		var_child_shim = 0
		range_child_shim = 0
		median_child_shim = 0 

	output_features = numpy.array([count,child_vad_perc,mean_child_pitch,var_child_pitch,range_child_pitch,median_child_pitch,mean_child_int,var_child_int,range_child_int,median_child_int,mean_child_jit,var_child_jit,range_child_jit,median_child_jit,mean_child_shim,var_child_shim,range_child_shim,median_child_shim])

else:
	output_features = numpy.zeros((1,18))

numpy.savetxt(output_file,numpy.matrix(output_features),fmt='%.18e')
