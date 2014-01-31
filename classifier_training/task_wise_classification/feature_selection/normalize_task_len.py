#! /usr/bin/python

import sys
import numpy
import math

train_features_file = sys.argv[1]
test_features_file = sys.argv[2]

train_features = numpy.loadtxt(train_features_file,dtype='float',delimiter=',')
test_features = numpy.loadtxt(test_features_file,dtype='float',delimiter=',')

# for the train set
task_ids = train_features[:,0]
task_times = train_features[:,37]

mean_t1 = numpy.mean(task_times[task_ids==1,:])
mean_t2 = numpy.mean(task_times[task_ids==2,:])
mean_t3 = numpy.mean(task_times[task_ids==3,:])
mean_t4 = numpy.mean(task_times[task_ids==4,:])
mean_t5 = numpy.mean(task_times[task_ids==5,:])

to_divide = mean_t1*(task_ids==1)+mean_t2*(task_ids==2)+mean_t3*(task_ids==3)+mean_t4*(task_ids==4)+mean_t5*(task_ids==5)
normalized_task_times = numpy.divide(task_times,to_divide)

#save_mat = numpy.matrix([task_times,to_divide,task_ids,normalized_task_times])

train_features[:,37] = normalized_task_times

# for the test set
task_ids = test_features[:,0]
task_times = test_features[:,37]

to_divide = mean_t1*(task_ids==1)+mean_t2*(task_ids==2)+mean_t3*(task_ids==3)+mean_t4*(task_ids==4)+mean_t5*(task_ids==5)
normalized_task_times = numpy.divide(task_times,to_divide)

test_features[:,37] = normalized_task_times

numpy.savetxt(train_features_file+'.task_time_norm',train_features,delimiter=',')
numpy.savetxt(test_features_file+'.task_time_norm',test_features,delimiter=',')
