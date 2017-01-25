from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")

config.General.requestName = DUMMY_NAME
config.General.workArea = DUMMY_WORKDIR
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'os2lana_cfg.py'
config.JobType.pyCfgParams = [DATA, MODE, FILTERSIGNAL,'applyBTagSFs=False', 'applyTriggerSFs=False', DYNLO,'skim=True']
config.JobType.inputFiles = ['RunII2016ReReco_25ns_PUXsec65550nb.root','RunII2016Rereco_25ns_PUXsec69000nb.root','RunII2016Rereco_25ns_PUXsec72450nb.root','PUDistMC_Summer2016_25ns_Moriond17MC_PoissonOOTPU.root','scalefactors_v4.root','inputFiles_cfi.py','Spring16_25nsV6_MC_L2Relative_AK8PFchs.txt','Spring16_25nsV6_MC_L3Absolute_AK8PFchs.txt','CSVv2_ichep.csv','Spring16_25nsV6_MC_Uncertainty_AK4PFchs.txt','Spring16_25nsV6_MC_Uncertainty_AK8PFchs.txt']

config.section_("Data")
config.Data.inputDataset = DUMMY_DATASET
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = DUMMY_NUMBER
config.Data.ignoreLocality = False
config.Data.publication = False
config.Data.outLFNDirBase = DUMMY_OUTPUT_PATH

config.section_("Site")
config.Site.storageSite = DUMMY_SITE
config.section_('User')

