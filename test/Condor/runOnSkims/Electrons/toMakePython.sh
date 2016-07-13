#!/bin/bash
#SAMPLE=BKG/Data/Signal ENTRY=number of samples  NFILE=number of files PATH=path to skimmed files

python fnal_fileParser.py SAMPLE=tprime800 ENTRY=17 NFILE=17 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/tprime800/skims/
python fnal_fileParser.py SAMPLE=tprime1000 ENTRY=18 NFILE=18 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/tprime1000/skims/
python fnal_fileParser.py SAMPLE=tprime1200 ENTRY=19 NFILE=19 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/tprime1200/skims/

python fnal_fileParser.py SAMPLE=bprime800 ENTRY=18 NFILE=18 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/bprime800/skims/
python fnal_fileParser.py SAMPLE=bprime1000 ENTRY=18 NFILE=18 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/bprime1000/skims/
python fnal_fileParser.py SAMPLE=bprime1200 ENTRY=19 NFILE=19 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/bprime1200/skims/

python fnal_fileParser.py SAMPLE=ttbar ENTRY=4653 NFILE=4653 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/ttbar/skims/

python fnal_fileParser.py SAMPLE=dy_ht100-200 ENTRY=66 NFILE=66 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/dy_ht100-200/skims/
python fnal_fileParser.py SAMPLE=dy_ht200-400 ENTRY=23 NFILE=23 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/dy_ht200-400/skims/
python fnal_fileParser.py SAMPLE=dy_ht400-600 ENTRY=26 NFILE=26 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/dy_ht400-600/skims/
python fnal_fileParser.py SAMPLE=dy_ht600-Inf ENTRY=23 NFILE=23 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/dy_ht600-Inf/skims/

python fnal_fileParser.py SAMPLE=WW ENTRY=51 NFILE=51 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/WW/skims/
python fnal_fileParser.py SAMPLE=ZZto4 ENTRY=264 NFILE=264 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/ZZto4/skims/
python fnal_fileParser.py SAMPLE=ZZto2 ENTRY=226 NFILE=226 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/ZZto2/skims/
python fnal_fileParser.py SAMPLE=WZto2 ENTRY=700 NFILE=700 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/WZto2/skims/
python fnal_fileParser.py SAMPLE=WZto3 ENTRY=46 NFILE=46 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/WZto3/skims/

#python fnal_fileParser.py SAMPLE=muons ENTRY=6641 NFILE=6641 PATH=/store/user/lpcbprime/noreplica/tmitchel/muons/skims/
python fnal_fileParser.py SAMPLE=electrons ENTRY=6639 NFILE=6639 PATH=/store/user/lpcbprime/noreplica/tmitchel/Electrons/electrons/skims/ 



