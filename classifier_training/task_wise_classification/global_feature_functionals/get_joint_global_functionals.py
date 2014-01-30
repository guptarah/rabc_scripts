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

psyc_vad = all_features[:,1]
child_vad = all_features[:,2]

len_session = len(psyc_vad)

# get the number of overlaps
overlap_vad = numpy.logical_and(psyc_vad,child_vad)
diff_overlap_vad = numpy.diff(numpy.concatenate(([0],overlap_vad)))
count = numpy.sum(diff_overlap_vad == 1)

numpy.savetxt(output_file,numpy.matrix([len_session,count]),fmt='%.18e')
