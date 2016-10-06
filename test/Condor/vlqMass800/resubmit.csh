#!/usr/bin/env tcsh

echo "user provided this target " $1 
if ( "$1" != "") then
    set myPWD = $PWD
    cd $1
    find . -type f -size -5 -printf "%f\n" >> $myPWD/root_files_to_sibmit.txt
    find . -type f -size -5 -delete
    pwd
    cd myPWD
endif
