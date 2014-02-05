#! /usr/bin/python

from os import system
import numpy
import sys

result_dir=sys.argv[1]

command = 'cat '+result_dir+'/*/prediction | grep " [0-9]" | sed \'s/\*//g;s/+//g;s/[\ ][\ ]*/\t/g;s/[0-9]://g\' | cut -f3-5 | sed \'s/,/\t/g\' > results'
print command
system(command)

# for the unselected features
results = numpy.loadtxt('results')

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

# for the selected features
print "for selected features"
results = numpy.loadtxt('results.sel')

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

