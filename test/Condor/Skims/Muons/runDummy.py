#!/bin/bash                                                                                                                                                                                                                           

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src
eval `scram runtime -sh`

cd ${_CONDOR_SCRATCH_DIR}
echo ${_CONDOR_SCRATCH_DIR}
let "sample=${1}+1"
cp PYTHON/SAMPLE/SAMPLE_${sample}.py .
cp TEST/*.txt .
cp TEST/*.root .
cp TEST/inputFiles_cfi.py .
cp TEST/*.csv .
cmsRun SAMPLE_${sample}.py
rm btag-eff-subjet.root
rm PU*
rm Run*
rm *.csv
rm *.txt
rm dataset*
rm os2lana*
rm scale*
xrdcp *.root root://cmseos.fnal.gov/OUTPUT/SAMPLE
rm SAMPLE_${sample}.py
rm *.root
ls
echo "DONE!"
