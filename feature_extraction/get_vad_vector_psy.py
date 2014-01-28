#! /usr/bin/python

# script to get VAD vector from the annotation timing file
import sys
import math
from os import system
import numpy

vad_file=sys.argv[1] # file containing the timing information
vad_file_output=sys.argv[2]


vad_len=numpy.loadtxt(vad_file+'.vad_len',dtype='float')
timings=numpy.loadtxt(vad_file+'.psy',dtype='float')

subtract_time=timings[0,0]*numpy.ones(timings.shape)
corrected_time=numpy.around(timings-subtract_time,decimals=2)

vad_vector = numpy.zeros([corrected_time[-1,1]*100,1])

for utr_num in range(0,corrected_time.shape[0]):
	vad_vector[corrected_time[utr_num,0]*100:corrected_time[utr_num,1]*100] = 1

# length of vad
vad_len = numpy.around(vad_len,decimals=2)*100
print vad_len
zeros_vad_len = numpy.zeros([vad_len,1])

if vad_len < vad_vector.shape[0]:
	vad_vector = vad_vector [0:vad_len] 
else:
	print vad_vector.shape,zeros_vad_len.shape
	zeros_vad_len[0:vad_vector.shape[0]] = vad_vector
	vad_vector = zeros_vad_len

numpy.savetxt(vad_file_output,vad_vector,fmt='%1e')
