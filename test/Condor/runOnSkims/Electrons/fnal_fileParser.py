import re, math, os, sys

def usage() :
    print "[usage]  ./fileParser.py SAMPLE=BKG/Data/Signal ENTRY=number of samples  NFILE=number of files PATH=path to skimmed files"
    sys.exit(0)

nParameters=len(sys.argv)
SAMPLE=""
PATH=""
NFILE=0
ENTRY=0

s="\n".join(sys.argv)


if not ("SAMPLE" in s and "PATH" in s and "NFILE" in s and "ENTRY" in s):
    usage()


for i in range(1, nParameters):
    opt=sys.argv[i]
    if "SAMPLE=" in opt:
        SAMPLE=opt[7:]
    elif "PATH=" in opt:
        PATH=opt[5:]
    elif "NFILE=" in opt:
        NFILE=opt[6:]
    elif "ENTRY=" in opt:
	ENTRY=opt[6:]	
    else:
        print "User has supplied an invalid parameter " , opt
        sys.exit(0)

print SAMPLE

for n_file in range (1, int(NFILE)+1):
    if SAMPLE == 'muons':
        inputfile = open('dummy_os2lana_Muon.py')
    if SAMPLE == 'electrons':
        inputfile = open('dummy_os2lana_Electron.py')
    if 'dy' in SAMPLE:
        inputfile = open('dummy_os2lana_dy.py')
    if 'tprime' in SAMPLE: 
        inputfile = open('dummy_os2lana_T.py')
    if 'bprime' in SAMPLE:
        inputfile = open('dummy_os2lana_B.py')
    if 'WW' in SAMPLE  or 'WZ' in SAMPLE or 'ZZ' in SAMPLE or 'ttbar' in SAMPLE:
        inputfile = open('dummy_os2lana_other.py')

    outputfile = open(str(SAMPLE)+'/'+str(SAMPLE)+'_'+str(n_file)+'.py', 'w')
    for line in inputfile:
	line = line.replace('nsample' , str(ENTRY) )
	line = line.replace('njob' ,	str(n_file) )
        line = line.replace('path_to_sample', 'root://cmseos.fnal.gov/'+str(PATH)+'/Skim_'+str(SAMPLE)+'_'+str(n_file)+'.root')
        line = line.replace('CondOutputSkim', 'Skim_'+str(SAMPLE)+'_'+str(n_file)+'.root')
        line = line.replace('CondOutputEvt', 'Evt_'+str(SAMPLE)+'_'+str(n_file)+'.root')    
        outputfile.writelines(line)
    inputfile.close()
    outputfile.close()
