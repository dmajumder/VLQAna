#!/bin/bash                                                                                                                                                                                                                                                                                                                                                                                                                      

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src
eval `scram runtime -sh`

cd ${_CONDOR_SCRATCH_DIR}
echo ${_CONDOR_SCRATCH_DIR}
let "sample=${1}+1"
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Condor/vlqMass800/DoubleEG_prompt/DoubleEG_prompt_${sample}.py .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/*.txt .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/*.root .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/inputFiles_cfi.py .
cp /uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/*.csv .
cmsRun DoubleEG_prompt_${sample}.py
rm btag-eff-subjet.root
rm *.csv
rm PU*
rm Run*
rm dataset*
rm scale*
rm os2lana*
xrdcp *.root root://cmseos.fnal.gov//store/user/tmitchel/condor/vlqMass800/DoubleEG_prompt
rm DoubleEG_prompt_${sample}.py
rm *.root
ls
echo "DONE!"
