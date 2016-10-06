from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")

config.General.requestName = DUMMY_NAME
config.General.workArea = DUMMY_WORKDIR
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'os2lana_cfg.py'
config.JobType.pyCfgParams = [DATa, MODE, PUOFF, LEPSF, FILTERSIGNAL, SIGNALTYPE, OPTIMIZERECO]
config.JobType.inputFiles = ['Fall15_25nsV2_DATA_L2L3Residual_AK4PFchs.txt',  'Fall15_25nsV2_DATA_L2Relative_AK8PFchs.txt',  'Fall15_25nsV2_DATA_Uncertainty_AK4PFchs.txt',  'Fall15_25nsV2_MC_L2Relative_AK8PFchs.txt',  'Fall15_25nsV2_MC_Uncertainty_AK4PFchs.txt', 'Fall15_25nsV2_DATA_L2L3Residual_AK8PFchs.txt',  'Fall15_25nsV2_DATA_L3Absolute_AK4PFchs.txt',  'Fall15_25nsV2_DATA_Uncertainty_AK8PFchs.txt',  'Fall15_25nsV2_MC_L3Absolute_AK4PFchs.txt',  'Fall15_25nsV2_MC_Uncertainty_AK8PFchs.txt', 'Fall15_25nsV2_DATA_L2Relative_AK4PFchs.txt',    'Fall15_25nsV2_DATA_L3Absolute_AK8PFchs.txt',  'Fall15_25nsV2_MC_L2Relative_AK4PFchs.txt',     'Fall15_25nsV2_MC_L3Absolute_AK8PFchs.txt', 'PUDistMC_2015_25ns_Startup_PoissonOOTPU.root',  'RunII2015_25ns_PUXsec65550nb.root',  'RunII2015_25ns_PUXsec69000nb.root',  'RunII2015_25ns_PUXsec72450nb.root',  'btag-eff-subjet.root']
#config.JobType.inputFiles = ['Summer15_25nsV6_MC_L2L3Residual_AK8PFchs.txt', 'Summer15_25nsV6_MC_L3Absolute_AK8PFchs.txt', 'hnpv_data_Run2015D_mc_RunIISpring15DR74-Asympt25ns_pvwt.root', 'PUDistData_Run2015ABCD.root', 'PUDistMC_2015_25ns_Startup_PoissonOOTPU.root']

config.section_("Data")
config.Data.inputDataset = DUMMY_DATASET
config.Data.inputDBS = 'phys03'
config.Data.splitting = DUMMY_BASE
config.Data.unitsPerJob = DUMMY_NUMBER
config.Data.ignoreLocality = False
config.Data.publication = False
config.Data.outLFNDirBase = DUMMY_OUTPUT_PATH

config.section_("Site")
config.Site.storageSite = DUMMY_SITE
config.section_('User')

