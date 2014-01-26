form Directory Names
   text wav_file
   text outdir
endform



    Read from file... 'wav_file$'
    object_name$ = selected$("Sound")

	time_length = Get total duration
	echo 'time_length'
 	
 	To Intensity... 75 0.01 no
	Down to Matrix
	Transpose
	Write to matrix text file... 'outdir$'/'object_name$'.intensity
	Remove
	select Matrix 'object_name$'
	Remove
	#select Matrix 'object_name$'
	#Remove
	select Intensity 'object_name$'
	Remove
	
	select Sound 'object_name$'
	To Pitch (ac)... 0.01 75 15 no 0.03 0.45 0.01 0.35 0.14 600
	select Pitch 'object_name$'
	Smooth... 10
	Interpolate
	To Matrix
	Transpose
	Write to matrix text file... 'outdir$'/'object_name$'.pitch
	Remove
	select Matrix 'object_name$'
	Remove
	select Pitch 'object_name$'
	Remove
	select Pitch 'object_name$'
	Remove
	select Pitch 'object_name$'
	Remove

	select Sound 'object_name$'
	To Pitch (ac)... 0.01 75 15 no  0.03  0.45 0.01 0.35 0.14 600
	select Pitch 'object_name$'
	Smooth... 10
	To Matrix
	Transpose
	Write to matrix text file... 'outdir$'/'object_name$'.pitch_raw
	Remove
	
	select Matrix 'object_name$'
	Remove
	select Pitch 'object_name$'
	Remove

	
	select Sound 'object_name$'
	plus Pitch 'object_name$'
	To PointProcess (cc)
	select Sound 'object_name$'
	plus Pitch 'object_name$'
	plus PointProcess 'object_name$'

	# get jitter and shimmer every .01 second for the complete interval
	# getting the duration of file
	
	num_iters  = (time_length-1.1)*100;


	for iter from 1 to num_iters
		time_start = 'iter'*0.01
		time_end = time_start+1
		voiceReport$ = Voice report... 'time_start' 'time_end' 75 600 1.3 1.6 0.03 0.45
		jitter = extractNumber(voiceReport$, "Jitter (local):")
		shimmer = extractNumber(voiceReport$,"Shimmer (local):")
	
		resultfile$ =" 'outdir$'/'object_name$'.jit_shim"
		fileappend "'resultfile$'"
		text$ = "'time_start' 'jitter' 'shimmer' 'newline$'"
		text$ >> 'outdir$'/'object_name$'.jit_shim
	endfor

	select Sound 'object_name$'
	plus Pitch 'object_name$'
	plus PointProcess 'object_name$'
	Remove

	
	

