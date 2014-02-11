#! /usr/bin/python

# script to get distance from the lsq line fit on 0 instances in the train file

import numpy 
import sys
import math

def line_fit(data): # get the vector giving direction vector and a point on the line for mmsq fit
	datamean = data.mean(axis=0)
	uu, dd, vv = numpy.linalg.svd(data - datamean)
	norm_vv = (1.0/numpy.linalg.norm(vv[0],ord=2))*vv[0]
	return vv[0],datamean


train_proj_file = sys.argv[1]
train_proj_lab_file = sys.argv[2]
test_proj_file = sys.argv[3]

train_proj = numpy.loadtxt(train_proj_file,dtype='float',delimiter=',')
train_lables = numpy.loadtxt(train_proj_lab_file,dtype='int',delimiter=',')
test_proj = numpy.loadtxt(test_proj_file,dtype='float',delimiter=',')

#train_proj0 = train_proj[train_lables==0,:]
train_proj0 = train_proj
dir_vect,data_mean = line_fit(train_proj0)

train_distances = numpy.zeros(train_proj.shape[0])
for id in range (train_proj.shape[0]):
	train_distances[id]=numpy.linalg.norm(numpy.cross((train_proj[id,:] - data_mean),dir_vect),ord=2)
	#train_distances[id] = train_distances[id]/numpy.linalg.norm(train_proj[id,:],ord=1)

test_distances = numpy.zeros(test_proj.shape[0])
for id in range(test_proj.shape[0]):
	test_distances[id]=numpy.linalg.norm(numpy.cross((test_proj[id,:] - data_mean),dir_vect),ord=2)
	#test_distances[id] = test_distances[id]/numpy.linalg.norm(test_proj[id,:],ord=2)


train_save_file = train_proj_file+'.dist'
test_save_file = test_proj_file+'.dist'
numpy.savetxt(train_save_file,train_distances,fmt='%f')
numpy.savetxt(test_save_file,test_distances,fmt='%f')
