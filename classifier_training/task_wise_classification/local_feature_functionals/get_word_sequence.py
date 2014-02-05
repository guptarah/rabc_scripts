#! /usr/bin/python

# script to get a sequence of words given a windown len and 50% overlap

import sys
import numpy
import math

def get_word_id(word_block):
	psy_vad = word_block[:,0]
	child_vad = word_block[:,1]
	pitch = word_block[:,2]
	intensity = word_block[:,3]

	# overlap_word
	if numpy.mean(psy_vad)>0 and numpy.mean(child_vad)>0 :
		
		joint_vad=numpy.logical_and(psy_vad,child_vad)
		if numpy.mean(joint_vad) > 0: # if in case there is true overlap
			#print psy_vad
			#print child_vad
			#print "overlap"
			return "overlap"
		elif numpy.mean(joint_vad) == 0: # in case both spoke in the same window
			#print psy_vad
			#print child_vad
			#print "overlap_partial"
			return "overlap_partial"

	elif numpy.mean(psy_vad)==0 and numpy.mean(child_vad)==0 :
		#print psy_vad
		#print child_vad
		#print "no_speech"
		return "no_speech"
	elif numpy.mean(psy_vad)>0 and numpy.mean(child_vad)==0 :
		if numpy.mean(psy_vad) == 1: # for the VAD word
			vad_word = "psy_ones"
		elif numpy.mean(psy_vad) < 1:
			vad_word = "psy_trans"

		relev_pitch = pitch[psy_vad == 1] # extracting part of pitch where psy spoke
		if numpy.mean(relev_pitch) == 1: 
			pitch_word="high"
		elif numpy.mean(relev_pitch) == 0:
			pitch_word="low"
		elif numpy.mean(relev_pitch) < 1 :
			pitch_word="trans"

		relev_intensity = intensity[psy_vad == 1] # extracting part of pitch where psy spoke
		if numpy.mean(relev_intensity) == 1: 
                        intensity_word="high"
                elif numpy.mean(relev_intensity) == 0:
                        intensity_word="low"
                elif numpy.mean(relev_intensity) < 1 :
                        intensity_word="trans"

		#print psy_vad
		#print relev_pitch
		#print relev_intensity
		#print vad_word + '_' + pitch_word + '_' + intensity_word

		return_word = vad_word + '_' + pitch_word + '_' + intensity_word
		return return_word

	elif numpy.mean(child_vad)>0 and numpy.mean(psy_vad)==0 :
		if numpy.mean(child_vad) == 1: # for the VAD word
                        vad_word = "child_ones"
                elif numpy.mean(child_vad) < 1:
                        vad_word = "child_trans"

		relev_pitch = pitch[child_vad == 1] # extracting part of pitch where child spoke
		if numpy.mean(relev_pitch) == 1: 
                        pitch_word="high"
                elif numpy.mean(relev_pitch) == 0:
                        pitch_word="low"
                elif numpy.mean(relev_pitch) < 1 :
                        pitch_word="trans"

		relev_intensity = intensity[child_vad == 1] # extracting part of pitch where psy spoke
		if numpy.mean(relev_intensity) == 1:
                        intensity_word="high"
                elif numpy.mean(relev_intensity) == 0:
                        intensity_word="low"
                elif numpy.mean(relev_intensity) < 1 :
                        intensity_word="trans"

		return_word = vad_word + '_' + pitch_word + '_' + intensity_word

		#print child_vad
		#print relev_pitch
		#print relev_intensity
		#print return_word
		
                return return_word
		
	else: 
		#print "error"
		return "error"
 

feature_file=sys.argv[1] # example ../../../../features/task_wise_features/RA016/RA016/task_features.task_id_rect.1.normalized
output_file=sys.argv[2]
win_len=int(sys.argv[3])
overlap=win_len/2

features=numpy.loadtxt(feature_file,dtype='float')
to_use_mat=features[:,1:5]

binarized_pitch=to_use_mat[:,2]>0
binarized_intensity=to_use_mat[:,3]>0
to_use_mat[:,2]=binarized_pitch
to_use_mat[:,3]=binarized_intensity

num_frames=to_use_mat.shape[0]
start_frame=0
end_frame=start_frame+overlap
list_words=[]

while end_frame < num_frames:
	word_block=to_use_mat[start_frame:end_frame,:]
	word_id_cur=get_word_id(word_block)
	list_words.append(word_id_cur)
	start_frame=end_frame-overlap
	end_frame=start_frame+win_len
	#print start_frame,end_frame

# #print the list to the output file
output_file_id = open(output_file,'w')
output_file_id.write("\n".join(list_words))
output_file_id.close()

