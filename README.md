setenv SCRAM_ARCH slc6_amd64_gcc493

cmsrel CMSSW_7_6_5

cd CMSSW_7_6_5/src/

cmsenv

git cms-init

git cms-merge-topic dmajumder:CMSSW_7_6_X_AnalysisDataFormats_BoostedObjects

git clone git@github.com:dmajumder/EventCounter.git Analysis/EventCounter 

git clone -b CMSSW_7_6_X git@github.com:skhalil/VLQAna.git Analysis/VLQAna  
 
#To just build this stuff
scram b -j4

# To run on OS2L analysis
cd Analysis/VLQAna/test

cmsRun os2lana_cfg.py

# To run crab jobs on B2GEDM Ntuples

Analysis/VLQAna/test/CRAB_B2G/ 

# make sure crab_dummy_os2lana.py is correct, and appropriate paths to allJobList.py, changle line 89 in run.py (comment 113 to get config file without submitting). Pay attenetion to relvant parameters, like config.General.requestName, config.Data.inputDataset, config.Data.outLFNDirBase, config.Site.storageSite etc.

# to run using crab
python run.py --options

# To run condor jobs on B2GEDM Ntuples

Analysis/VLQAna/test/Condor/<appropriate masspoint if relevant>
More to come....

Python run.py

Please see more details https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial for CRAB3 related issues.
