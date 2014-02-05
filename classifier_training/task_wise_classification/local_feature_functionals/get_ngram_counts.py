#! /usr/bin/python

# scripts to get n gram counts given the sequence of numbers as in local_feature_strings10/*/*/$task_id.numerized

import numpy
import sys
import math

sequence_file = sys.argv[1]

sequence = numpy.loadtxt(sequence_file,dtype='float')
num_words = 39 # the number of words # hardcoded # may need to change

len_seq = len(sequence)

mono_count = numpy.zeros((num_words,1))
bi_count = numpy.zeros((num_words,num_words))

for word_id in range(len_seq):
	mono_count[sequence[word_id]-1] += 1.0

	if word_id < len_seq-1 :
		bi_count[sequence[word_id]-1,sequence[word_id+1]-1] += 1.0
	

print numpy.sum(mono_count),(1.0/numpy.sum(mono_count))
print numpy.sum(bi_count)

mono_normalized = (1.0/numpy.sum(mono_count))*mono_count
bi_normalized = (1.0/numpy.sum(bi_count))*bi_count

numpy.savetxt(sequence_file+'.mono',mono_count,fmt='%d')
numpy.savetxt(sequence_file+'.bi',bi_count,fmt='%d')

numpy.savetxt(sequence_file+'.mono.norm',mono_normalized,fmt='%f')
numpy.savetxt(sequence_file+'.bi.norm',bi_normalized,fmt='%f')

bi_normalized_flat = numpy.matrix(numpy.reshape(bi_normalized,num_words*num_words))
print bi_normalized_flat.shape
numpy.savetxt(sequence_file+'.mono.norm.flat',mono_normalized.T,fmt='%f')
numpy.savetxt(sequence_file+'.bi.norm.flat',bi_normalized_flat,fmt='%f') 
