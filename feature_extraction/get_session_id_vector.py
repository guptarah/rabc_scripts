#! /usr/bin/python 

# script to get VAD vector from the annotation timing file 
import sys 
import math 
import os 
from os import system
import numpy 

session_times=sys.argv[1]
start_end_times=sys.argv[2]
output_file = sys.argv[3]


timings = numpy.loadtxt(session_times,dtype='float')
start_end_times = numpy.around(numpy.loadtxt(start_end_times,dtype='float'),decimals=2)

timings[0,0] = start_end_times[0]

session_ids = timings[:,2]
print session_ids

corrected_time = timings[:,0:2]
print corrected_time
subtract_time = corrected_time[0,0]*numpy.ones(corrected_time.shape)
corrected_time = numpy.around(corrected_time - subtract_time,decimals=2)
print corrected_time

vad_len = (start_end_times[1] - start_end_times[0])*100
vad_vector = numpy.zeros([vad_len,1])
for line_num in range(0,corrected_time.shape[0]):
	print session_ids[line_num],corrected_time[line_num,1]*100,corrected_time[line_num,0]*100
	vad_vector[corrected_time[line_num,0]*100:corrected_time[line_num,1]*100] = session_ids[line_num]

numpy.savetxt(output_file,vad_vector,fmt='%1e')

