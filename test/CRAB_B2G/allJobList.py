#! /bin/python

def list_Zelel(isData):
    if isData:  
        jobList = [
            ['/DoubleEG/devdatta-Run2015D-05Oct2015-v1_B2GAnaFW_v74x_v8p4-ff3168b63d5cee365f49bf7ea3ba6ef3/USER', 'DoubleEG-Run2015D-05Oct2015-v1', '40', ''],
            ]
        return jobList
    else:
        jobList = [  
            ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/vorobiev-B2GAnaFW_Run2Spring15MiniAODv2_25ns_v74x_v84-50153fb607659b6f9fb41d9f35391d0e/USER', 'DY_amcatnlo', '10',''],
            #['/TT_TuneCUETP8M1_13TeV-powheg-pythia8/jkarancs-B2GAnaFW_v74x_V8p4_RunIISpring15MiniAODv2-74X_mcRun2_asymptotic_v2_ext3-v1-7b09a84a5c42d0a63b01d8e8e63c7a89/USER', 'TT_powheg', '20', ''],
            ]
        return jobList

def list_Zmumu(isData):
    if isData:    
        jobList = [
            ['/DoubleMuon/devdatta-B2GAnaFW_76X_V1p2-69b00753dd36562e8813bc06510c861e/USER', 'DoubleMuon-Run2015D-PromptReco-v4', '20', ''],
            ]
        return jobList
    else:
        jobList = [ 
            #['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/vorobiev-B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2-bf3ef703e3bdb5dcc5320cf3ff6ce74d/USER', 'DY_madgraphInclusive', '5', ''],
	    ['/TT_TuneCUETP8M1_13TeV-powheg-pythia8/vorobiev-B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2-bf3ef703e3bdb5dcc5320cf3ff6ce74d/USER', 'TT_powheg', '20', ''],
	    ]
        return jobList
