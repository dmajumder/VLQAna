#!/usr/bin/env tcsh

echo "user provided this target " $1 
set myPWD = $PWD
cd $1
find . -type f -size -1024 -printf "%f\n" > $myPWD/root_files_to_sibmit.txt
find . -type f -size -1024 -delete
cd myPWD





