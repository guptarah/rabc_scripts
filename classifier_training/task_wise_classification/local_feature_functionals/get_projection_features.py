#! /usr/bin/python

import numpy
import sys

cur_dir=sys.argv[1]

train_elements = numpy.loadtxt(cur_dir+'train_elements',dtype='float',delimiter=',')
test_elements = numpy.loadtxt(cur_dir+'test_elements',dtype='float',delimiter=',')

train_features = []
test_features = []

for dict_id in range(3):

	dict_elem_file0=cur_dir+'/dict0_elem'
        dict_elems0 = numpy.loadtxt(dict_elem_file0,dtype='float',delimiter=',')
        normalization_factor = dict_elems0.shape[0]

        dict_elems_sum0 = (1.0/normalization_factor)*numpy.sum(dict_elems0,axis=0)

	
	dict_elem_file=cur_dir+'/dict'+str(dict_id)+'_elem'
	dict_elems = numpy.loadtxt(dict_elem_file,dtype='float',delimiter=',')
	normalization_factor = dict_elems.shape[0]
	
	dict_elems_sum = (1.0/normalization_factor)*numpy.sum(dict_elems,axis=0)
	save_dict_file=dict_elem_file+'_sum'
	numpy.savetxt(save_dict_file,dict_elems_sum,fmt='%f',delimiter=',')	

#	if dict_id>0:
#		dict_elems_sum = numpy.multiply(dict_elems_sum,(dict_elems_sum>dict_elems_sum0))

	#train_features_cur_mono = train_elements[:,0:39] * numpy.matrix(dict_elems_sum[0:39]).T
	#test_features_cur_mono = test_elements[:,0:39] * numpy.matrix(dict_elems_sum[0:39]).T
		
	to_divide = numpy.tile(numpy.matrix(dict_elems_sum[:]),(test_elements.shape[0],1))
	to_divide = to_divide - 0.001000*(to_divide == 0)
	
	train_features_cur_mono = train_elements[:,:] * numpy.matrix(dict_elems_sum[:]).T
        test_features_cur_mono = test_elements[:,:] * numpy.matrix(dict_elems_sum[:]).T

	divided_test_features = numpy.divide(test_elements,to_divide)
	numpy.savetxt(dict_elem_file+'test_proj',divided_test_features,fmt='%f',delimiter=',')

	
	if dict_id > 0:
		# for projecting onto the dictionary
		train_features = numpy.concatenate((train_features,train_features_cur_mono),axis=1)
		test_features = numpy.concatenate((test_features,test_features_cur_mono),axis=1)

		#train_features = numpy.concatenate((train_features,train_features_cur_bi),axis=1)
                #test_features = numpy.concatenate((test_features,test_features_cur_bi),axis=1)

	else:
		# for projecting onto the dictionary 
		train_features = train_features_cur_mono
		test_features = test_features_cur_mono

		#train_features = numpy.concatenate((train_features,train_features_cur_bi),axis=1)
                #test_features = numpy.concatenate((test_features,test_features_cur_bi),axis=1)
		
#		# getting the other features 
#		important_features_train = train_elements[:,[0,957,716,847,1261,63]]
#		important_feature_train_std = numpy.std(important_features_train,1)
#		important_feature_train_mean = numpy.mean(important_features_train,1)
#			
#		important_features_test = test_elements[:,[0,957,716,847,1261,63]]
#		important_feature_test_std = numpy.std(important_features_test,1)
#		important_feature_test_mean = numpy.mean(important_features_test,1)
#
#		imp_feat_train_stat = numpy.concatenate((numpy.matrix(important_feature_train_mean).T,numpy.matrix(important_feature_train_std).T),axis=1)
#		imp_feat_test_stat = numpy.concatenate((numpy.matrix(important_feature_test_mean).T,numpy.matrix(important_feature_test_std).T),axis=1)
#
#		train_features = numpy.concatenate((train_features,numpy.matrix(imp_feat_train_stat)),axis=1)
#		test_features = numpy.concatenate((test_features,numpy.matrix(imp_feat_test_stat)),axis=1)			

to_write_train_file = cur_dir+'/projection_feat.train'
to_write_test_file = cur_dir+'/projection_feat.test'

numpy.savetxt(to_write_train_file,train_features,fmt='%f',delimiter=',')
numpy.savetxt(to_write_test_file,test_features,fmt='%f',delimiter=',')

