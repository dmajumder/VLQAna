import sys
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('outFileName', 'os2lana_skim.root',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
    )
options.register('doPUReweightingOfficial', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Do pileup reweighting using official recipe"
    )
options.register('applyLeptonSFs', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply lepton SFs to the MC"
    )
options.register('isData', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Is data?"
    )
options.register('applyHtCorr', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply corrections to efficiency due to HT"
    )
options.register('runSignal', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Store the channel normalization for signal"
    )
options.register('sigType', 'BPrime',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "TT or BB? Choose: 'TPrime' or 'BPrime'"
    )
options.register('zdecaymode', 'zelel',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Z->mumu or Z->elel? Choose: 'zmumu' or 'zelel'"
    )
options.register('applyDYNLOCorr', False, ### Set to true only for DY process ### Only EWK NLO k-factor is applied
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Apply DY EWK k-factor to DY MC"
    )

options.setDefault('maxEvents', 1000)
options.parseArguments()
print options

hltpaths = []
if options.zdecaymode == "zmumu":
  hltpaths = [
    "HLT_DoubleIsoMu17_eta2p1_v",
    "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
    ]
elif options.zdecaymode == "zelel":
  hltpaths = [
    "HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v",
    "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v"
    ]
else:
  sys.exit("!!!Error: Wrong Z decay mode option chosen. Choose either 'zmumu' or 'zelel'!!!")

process = cms.Process("Skim")

# message logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# input
#from inputFiles_cfi import *
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
      #options.outFileName
      'root://eoscms.cern.ch//store/group/phys_b2g/B2GAnaFW_76X_V1p2/BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2/160411_160543/0000/B2GEDMNtuple_12.root',
      )
    )

# output 
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('EvtCounts_'+options.outFileName)
    )

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outFileName),
    SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p')),
    dropMetaData = cms.untracked.string('DROPPED'),
    outputCommands = cms.untracked.vstring("keep *",)
    )

#Event counter
from Analysis.EventCounter.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone(isData=options.isData)
process.cleanedEvents = eventCounter.clone(isData=options.isData)
process.finalEvents = eventCounter.clone(isData=options.isData)

# VLQGenFilter
from Analysis.VLQAna.genVLQSel_cfi import genParams
process.genInfo = genParams.clone(sigtype= cms.string(options.sigType))

#Event cleaner 
process.load("Analysis.VLQAna.EventCleaner_cff")
process.evtcleaner.isData = options.isData
process.evtcleaner.hltPaths = cms.vstring (hltpaths)
process.evtcleaner.DoPUReweightingOfficial = cms.bool(options.doPUReweightingOfficial)

#Skim
from Analysis.VLQAna.Skim_cff import *
process.skim = skim.clone(
    zdecayMode = cms.string(options.zdecaymode),
    applyLeptonSFs = cms.bool(options.applyLeptonSFs),
    applyDYNLOCorr = cms.bool(options.applyDYNLOCorr),
    applyHtCorr = cms.bool(options.applyHtCorr),
    )
process.skim.lepsfsParams.zdecayMode = cms.string(options.zdecaymode)

if options.runSignal and not options.isData:
  process.p = cms.Path(
    process.allEvents
    *process.genInfo 
    *process.evtcleaner
    *process.skim
    *process.finalEvents
    )
else:
  process.p = cms.Path(
    process.allEvents
    *process.evtcleaner
    *process.skim
    *process.finalEvents
  )
  
process.outpath = cms.EndPath(process.out)
