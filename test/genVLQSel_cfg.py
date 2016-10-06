import FWCore.ParameterSet.Config as cms

process = cms.Process("VLQGen")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.FwkJob.limit=1
process.MessageLogger.cerr.ERROR = cms.untracked.PSet( limit = cms.untracked.int32(0) )

## Options and Output Report
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

###############################
####### Parameters ############
###############################
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.register('sigType', 'BPrime',
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.string,
                  "TT or BB? Choose: 'TPrime' or 'BPrime'"
                 )
options.parseArguments()

print options

# input
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
      'root://eoscms.cern.ch//store/group/phys_b2g/B2GAnaFW_76X_V1p2/BprimeBprime_M-800_TuneCUETP8M1_13TeV-madgraph-pythia8/B2GAnaFW_RunIIFall15MiniAODv2_25ns_v76x_v1p2/160411_160543/0000/B2GEDMNtuple_12.root',
      )
    )

# output 
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('EvtCounts_genVLQ')
    )

# gen info module
from Analysis.VLQAna.genVLQSel_cfi import genParams
process.genInfo = genParams.clone(sigtype= cms.string(options.sigType))

process.p = cms.Path(process.genInfo)

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('genVLQInfo.root'),
                               SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               dropMetaData = cms.untracked.string('DROPPED'),
                               outputCommands = cms.untracked.vstring('drop *',
                                                                      'keep *_GenInfo*_*_*',
                                                                      )
                               )

process.e = cms.EndPath(process.out)
