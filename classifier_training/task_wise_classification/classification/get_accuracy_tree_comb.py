#! /usr/bin/python

# get results after combining child and psyc results

from os import system
import numpy
import sys

results_psy=sys.argv[1]
results_child=sys.argv[2]

# for the unselected features
results_psy = numpy.loadtxt(results_psy)
results_child = numpy.loadtxt(results_child)

#usage_vect = numpy.loadtxt('child_only_results/usage_indicator') > 0
usage_vect = numpy.loadtxt('child_only_results/usage_indicator') > -1
usage_vect = numpy.matrix(usage_vect).T
to_divide_vector = (usage_vect == 0) + 2*(usage_vect > 0)
usage_vect = numpy.tile(usage_vect,5)
to_divide_vector = numpy.tile(to_divide_vector,5)
results = results_psy + numpy.multiply(results_child,usage_vect)
results = numpy.divide(results,to_divide_vector)

results[:,0] = numpy.matrix(results_psy[:,0]).T

# remake resuls based on probabilities
class0 = results[:,2]>0.8

class1or2 = results[:,2]<0.8
class1 = results[:,3] > 2*results[:,4]
class2 = 2*results[:,4] > results[:,3]
class1 = numpy.logical_and(class1or2,class1)
class2 = numpy.logical_and(class1or2,class2)
results[:,1] = 1*class1+2*class2


# calculate accuracy
true_values = (results[:,0]==results[:,1])
accuracy = numpy.sum(true_values)/float(results.shape[0]) 

num_classes = 3
confusion_mat=numpy.zeros((num_classes,num_classes))
# calculate confusion matrix  
for instance_id in range(results.shape[0]):  
	confusion_mat[results[instance_id,0],results[instance_id,1]] += 1

print confusion_mat

# get accuracies
instances_sum = numpy.sum(confusion_mat, axis=1) 
instances_sum = numpy.tile(instances_sum,(num_classes,1))
instances_sum = instances_sum.T 
norm_confusion_mat = numpy.divide(confusion_mat,instances_sum) 
print norm_confusion_mat 

# get unw accuracy
cum_acc_class=0 
for class_id in range(num_classes):
        cum_acc_class += norm_confusion_mat[class_id,class_id] 
unw_acc = cum_acc_class/num_classes
print unw_acc


# results based on which ones the max
class0 = numpy.logical_and(results[:,2]>results[:,3],results[:,2]>results[:,4])
class1 = numpy.logical_and(results[:,3]>results[:,2],results[:,3]>results[:,1])
class2 = numpy.logical_and(results[:,4]>results[:,2],results[:,4]>results[:,3])

results[:,1] = 1*class1+2*class2


# calculate accuracy
true_values = (results[:,0]==results[:,1])
accuracy = numpy.sum(true_values)/float(results.shape[0])

num_classes = 3
confusion_mat=numpy.zeros((num_classes,num_classes))
# calculate confusion matrix  
for instance_id in range(results.shape[0]):
        confusion_mat[results[instance_id,0],results[instance_id,1]] += 1

print confusion_mat

# get accuracies
instances_sum = numpy.sum(confusion_mat, axis=1)
instances_sum = numpy.tile(instances_sum,(num_classes,1))
instances_sum = instances_sum.T
norm_confusion_mat = numpy.divide(confusion_mat,instances_sum)
print norm_confusion_mat

# get unw accuracy
cum_acc_class=0
for class_id in range(num_classes):
        cum_acc_class += norm_confusion_mat[class_id,class_id]
unw_acc = cum_acc_class/num_classes
print unw_acc

