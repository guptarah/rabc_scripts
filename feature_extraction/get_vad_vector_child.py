#! /usr/bin/python

# script to get VAD vector from the annotation timing file
import sys
import math
import os
from os import system
import numpy

vad_file=sys.argv[1] # file containing the timing information
vad_file_output=sys.argv[2]

vad_len=numpy.loadtxt(vad_file+'.vad_len',dtype='float')

if os.path.getsize(vad_file+'.child') > 0:
	timings=numpy.loadtxt(vad_file+'.child',dtype='float')

	psy_timings=numpy.loadtxt(vad_file+'.psy',dtype='float')
	
	subtract_time=psy_timings[0,0]*numpy.ones(timings.shape)
	corrected_time=numpy.matrix(numpy.around(timings-subtract_time,decimals=2))
	
	vad_len = numpy.around(vad_len,decimals=2)*100
	print vad_len
	
	vad_vector = []
	print corrected_time,corrected_time.shape
	if corrected_time.shape[0] > 1:
		vad_vector = numpy.zeros([corrected_time[-1,1]*100,1])
		for utr_num in range(0,corrected_time.shape[0]):
	        	vad_vector[corrected_time[utr_num,0]*100:corrected_time[utr_num,1]*100] = 1
	elif corrected_time.shape[0] == 1:
		vad_vector = numpy.zeros([corrected_time[0,1]*100,1])
		for utr_num in range(0,corrected_time.shape[0]):
			vad_vector[corrected_time[utr_num,0]*100:corrected_time[utr_num,1]*100] = 1
	
	print vad_vector.shape
	
	if vad_len < vad_vector.shape[0]:
		vad_vector = vad_vector [0:vad_len-1] 
	else:
		print "incrementing vad vector size"
		vad_len_array = numpy.zeros([vad_len,1])
		vad_len_array[0:vad_vector.shape[0],:] = vad_vector
		vad_vector = vad_len_array
	

else:
	vad_len = numpy.around(vad_len,decimals=2)*100
        print vad_len
	vad_vector = numpy.zeros([vad_len,1])

numpy.savetxt(vad_file_output,vad_vector,fmt='%1e')
