#!/bin/bash
#SAMPLE=BKG/Data/Signal ENTRY=number of samples  NFILE=number of files PATH=path to skimmed files
python fnal_fileParser.py SAMPLE=tprime ENTRY=17 NFILE=17 PATH=/store/group/phys_b2g/B2GAnaFW_76X_V1p2/TprimeTprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2/160410_203417/000
python fnal_fileParser.py SAMPLE=bprime ENTRY=18 NFILE=18 PATH=/store/group/phys_b2g/B2GAnaFW_76X_V1p2/BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2/160411_160543/000
python fnal_fileParser.py SAMPLE=ttbar ENTRY=4653 NFILE=4653 PATH=/store/group/phys_b2g/B2GAnaFW_76X_V1p2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2/160408_145006/000
# #python fnal_fileParser_MC.py SAMPLE=dy_incl ENTRY=5849 NFILE=5849 PATH=/store/group/phys_b2g/B2GAnaFW_76X_V1p2/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2/160410_211811/000
  python fnal_fileParser.py SAMPLE=dy_ht100-200 ENTRY=66 NFILE=66 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_102503/000
  python fnal_fileParser.py SAMPLE=dy_ht200-400 ENTRY=23 NFILE=23 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_102629/000
  python fnal_fileParser.py SAMPLE=dy_ht400-600 ENTRY=26 NFILE=26 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_102749/000
  python fnal_fileParser.py SAMPLE=dy_ht600-Inf ENTRY=23 NFILE=23 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_102909/000
python fnal_fileParser.py SAMPLE=WW ENTRY=51 NFILE=51 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/WWTo2L2Nu_13TeV-powheg/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_105301/000
python fnal_fileParser.py SAMPLE=ZZto4 ENTRY=264 NFILE=264 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/ZZTo4L_13TeV-amcatnloFXFX-pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_110200/000 
python fnal_fileParser.py SAMPLE=ZZto2 ENTRY=226 NFILE=226 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/ZZTo2L2Nu_13TeV_powheg_pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_110317/000
 python fnal_fileParser.py SAMPLE=WZto2 ENTRY=700 NFILE=700 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_105808/000
 python fnal_fileParser.py SAMPLE=WZto3 ENTRY=46 NFILE=46 PATH=/store/user/jkarancs/SusyAnalysis/B2GEdmNtuple/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/B2GAnaFW_76X_V1p1_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/160401_105652/000 
 python fnal_fileParser.py SAMPLE=muons ENTRY=6641 NFILE=6641 PATH=/store/group/phys_b2g/B2GAnaFW_76X_V1p2/DoubleMuon/B2GAnaFW_76X_V1p2/160406_175248/000
#python fnal_fileParser.py SAMPLE=electrons ENTRY=6639 NFILE=6639 PATH=/store/group/phys_b2g/B2GAnaFW_76X_V1p2/DoubleEG/B2GAnaFW_76X_V1p2/160406_175235/000



