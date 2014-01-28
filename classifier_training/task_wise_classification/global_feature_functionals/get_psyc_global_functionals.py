#! /usr/bin/python

# script to get the functional of psyc utterances
import sys 
import math
import os 
from os import system
import numpy  

all_features = sys.argv[1]
all_features = numpy.loadtxt(all_features,dtype='float')

# get total number of utterances
psyc_vad = all_features[:,1]
diff_psyc_vad = numpy.diff(numpy.concatenate(([0],psyc_vad)))
count = numpy.sum(diff_psyc_vad == 1)

# get %age of vad on
psyc_vad_perc = numpy.sum(psyc_vad == 1)/float(len(psyc_vad))


print count,psyc_vad_perc
