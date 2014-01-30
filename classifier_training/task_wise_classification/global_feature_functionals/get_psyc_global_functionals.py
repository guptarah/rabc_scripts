#! /usr/bin/python

# script to get the functional of psyc utterances
import sys 
import math
import os 
from os import system
import numpy  

all_features = sys.argv[1]
output_file = sys.argv[2]

all_features = numpy.loadtxt(all_features,dtype='float')

# get total number of utterances
psyc_vad = all_features[:,1]
diff_psyc_vad = numpy.diff(numpy.concatenate(([0],psyc_vad)))
count = numpy.sum(diff_psyc_vad == 1)

# get %age of vad on
psyc_vad_perc = numpy.sum(psyc_vad == 1)/float(len(psyc_vad))

# get pitch statisticals
mean_psyc_pitch = numpy.mean(all_features[psyc_vad==1,3])
var_psyc_pitch = numpy.var(all_features[psyc_vad==1,3])
range_psyc_pitch = numpy.ptp(all_features[psyc_vad==1,3])
median_psyc_pitch = numpy.median(all_features[psyc_vad==1,3])

# get intensity statisticals
mean_psyc_int = numpy.mean(all_features[psyc_vad==1,4])
var_psyc_int = numpy.var(all_features[psyc_vad==1,4])
range_psyc_int = numpy.ptp(all_features[psyc_vad==1,4])
median_psyc_int = numpy.median(all_features[psyc_vad==1,4])

# get jitter statisticals 
psyc_jit = all_features[psyc_vad==1,5]
psyc_jit = psyc_jit[psyc_jit>-100,:]
mean_psyc_jit = numpy.mean(psyc_jit)
var_psyc_jit = numpy.var(psyc_jit)
range_psyc_jit = numpy.ptp(psyc_jit)
median_psyc_jit = numpy.median(psyc_jit)

# get shimmer statisiticals
psyc_shim = all_features[psyc_vad==1,6]
psyc_shim = psyc_shim[psyc_shim>-100,:]
mean_psyc_shim = numpy.mean(psyc_shim)
var_psyc_shim = numpy.var(psyc_shim)
range_psyc_shim = numpy.ptp(psyc_shim)
median_psyc_shim = numpy.median(psyc_shim)

output_features = numpy.array([count,psyc_vad_perc,mean_psyc_pitch,var_psyc_pitch,range_psyc_pitch,median_psyc_pitch,mean_psyc_int,var_psyc_int,range_psyc_int,median_psyc_int,mean_psyc_jit,var_psyc_jit,range_psyc_jit,median_psyc_jit,mean_psyc_shim,var_psyc_shim,range_psyc_shim,median_psyc_shim])

numpy.savetxt(output_file,numpy.matrix(output_features),fmt='%.18e')
