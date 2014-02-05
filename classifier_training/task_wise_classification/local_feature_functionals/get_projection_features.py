#! /usr/bin/python

import numpy
import sys

cur_dir=sys.argv[1]

train_elements = numpy.loadtxt(cur_dir+'train_elements',dtype='float',delimiter=',')
test_elements = numpy.loadtxt(cur_dir+'test_elements',dtype='float',delimiter=',')


for dict_id in range(3):
	dict_elem_file=cur_dir+'/dict'+str(dict_id)+'_elem'
	dict_elems = numpy.loadtxt(dict_elem_file,dtype='float',delimiter=',')
	normalization_factor = dict_elems.shape[0]
	
	dict_elems_sum = (1.0/normalization_factor)*numpy.sum(dict_elems,axis=0)
	print numpy.matrix(dict_elems_sum).T.shape, numpy.matrix(train_elements).shape,(train_elements * numpy.matrix(dict_elems_sum).T).shape

	train_features_cur = train_elements * numpy.matrix(dict_elems_sum).T
	test_features_cur = test_elements * numpy.matrix(dict_elems_sum).T
		
	if dict_id > 0:
		train_features = numpy.concatenate((train_features,train_features_cur),axis=1)
		test_features = numpy.concatenate((test_features,test_features_cur),axis=1)
	else: 
		train_features = train_features_cur
		test_features = test_features_cur
		print "hi"

to_write_train_file = cur_dir+'/projection_feat.train'
to_write_test_file = cur_dir+'/projection_feat.test'

numpy.savetxt(to_write_train_file,train_features,fmt='%f',delimiter=',')
numpy.savetxt(to_write_test_file,test_features,fmt='%f',delimiter=',')
