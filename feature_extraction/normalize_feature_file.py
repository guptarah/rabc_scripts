#! /usr/bin/python

# script to normalize a feature file give the means and stds

import numpy
import sys
import math

feature_file = sys.argv[1]
mean_file = sys.argv[2]
output_file = sys.argv[3]

features = numpy.loadtxt(feature_file,dtype='float')
mean_std = numpy.loadtxt(mean_file,dtype='float')

child_vad = features[:,2]
#print "child_vad",child_vad
psy_vad = features[:,1] 
#print "psy vad true",psy_vad
psy_vad = psy_vad - numpy.logical_and(child_vad,psy_vad)
#print "psy_vad",psy_vad

# pitch normalization
cp_mean_vector = mean_std[2,0]*child_vad # child pitch mean vector
#print "cp_mean_vector",cp_mean_vector
cp_std_vector = numpy.logical_not(child_vad) + mean_std[3,0]*child_vad # child pitch std vector
#print "cp_std_vector",cp_std_vector
pp_mean_vector = mean_std[0,0]*psy_vad # psyc pitch mean vector
#print "pp_mean_vector",pp_mean_vector
pp_std_vector = numpy.logical_not(psy_vad) + mean_std[1,0]*psy_vad # psyc pitch std vector
#print "pp_std_vector",pp_std_vector
pitch_vector = features[:,3]
pitch_vector = pitch_vector - cp_mean_vector - pp_mean_vector
pitch_vector = numpy.divide(pitch_vector,cp_std_vector)
pitch_vector = numpy.divide(pitch_vector,pp_std_vector)
#print pitch_vector

# intensity normalization
ci_mean_vector = mean_std[2,1]*child_vad # child intensity mean vector
#print "ci_mean_vector",ci_mean_vector
ci_std_vector = numpy.logical_not(child_vad) + mean_std[3,1]*child_vad # child jit std vector
#print "ci_std_vector",ci_std_vector
pi_mean_vector = mean_std[0,1]*psy_vad # psyc jit mean vector
#print "pi_mean_vector",pi_mean_vector
pi_std_vector = numpy.logical_not(psy_vad) + mean_std[1,1]*psy_vad # psyc jit std vector
#print "pi_std_vector",pi_std_vector
int_vector = features[:,4]
int_vector = int_vector - ci_mean_vector - pi_mean_vector
int_vector = numpy.divide(int_vector,ci_std_vector)
int_vector = numpy.divide(int_vector,pi_std_vector)
#print int_vector

# jitter normalization
cj_mean_vector = mean_std[2,2]*child_vad # child jit mean vector
#print "cj_mean_vector",cj_mean_vector
cj_std_vector = numpy.logical_not(child_vad) + mean_std[3,2]*child_vad # child jit std vector
#print "cj_std_vector",cj_std_vector
pj_mean_vector = mean_std[0,2]*psy_vad # psy jit mean vector
#print "pj mean vector",pj_mean_vector
pj_std_vector = numpy.logical_not(psy_vad) + mean_std[1,2]*psy_vad
#print "pj std vector",pj_std_vector
jit_vector = features[:,5]
jit_vector = jit_vector - cj_mean_vector - pj_mean_vector
jit_vector = numpy.divide(jit_vector,cj_std_vector)
jit_vector = numpy.divide(jit_vector,pj_std_vector)

# shimmer normalization
cs_mean_vector = mean_std[2,3]*child_vad # child shim mean vector
#print "cs_mean_vector",cs_mean_vector
cs_std_vector = numpy.logical_not(child_vad) + mean_std[3,3]*child_vad # child shim std vector
#print "cs_std_vector",cs_std_vector
ps_mean_vector = mean_std[0,3]*psy_vad # psy shim mean vector
#print "ps mean vector",ps_mean_vector
ps_std_vector = numpy.logical_not(psy_vad) + mean_std[1,3]*psy_vad
#print "ps std vector",ps_std_vector
shim_vector = features[:,6]
shim_vector = shim_vector - cs_mean_vector - ps_mean_vector
shim_vector = numpy.divide(shim_vector,cs_std_vector)
shim_vector = numpy.divide(shim_vector,ps_std_vector)

normalized_features = numpy.zeros(features.shape)
normalized_features[:,0] = features[:,0]
normalized_features[:,1] = features[:,1]
normalized_features[:,2] = features[:,2]
normalized_features[:,3] = pitch_vector
normalized_features[:,4] = int_vector
normalized_features[:,5] = jit_vector
normalized_features[:,6] = shim_vector
numpy.savetxt(output_file,normalized_features,fmt='%.9e')
