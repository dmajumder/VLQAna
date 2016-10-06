import re, math, os, sys
import shutil

inputfile = open('root_files_to_sibmit.txt')
print "root files found: "
samples_num = 0
for line in inputfile:
    print line
    if  "root" in line.split(".")[1]:
        samples_num = samples_num + 1
        print samples_num
        root_file_name = line.split(".")[0]
        name_mod = "_".join(root_file_name.split("_")[:-1] )
	shutil.copy2(str(name_mod)+'/'+str(root_file_name[:len(root_file_name)])+'.py', 'resubmitted_samples/resubmitted_'+str(samples_num)+'.py')
