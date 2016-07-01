import FWCore.ParameterSet.Config as cms

from Analysis.VLQAna.VLQParams_cfi import *

genParams = cms.EDProducer("GenVLQSel",
   verbose                    = cms.bool(True),
   #sigtype                    = cms.string("TPrime"),
   TtZParams                  = cms.PSet(genPartParams,TtZParams), 
   TtHParams                  = cms.PSet(genPartParams,TtHParams), 
   TbWParams                  = cms.PSet(genPartParams,TbWParams), 
   BbZParams                  = cms.PSet(genPartParams,BbZParams), 
   BbHParams                  = cms.PSet(genPartParams,BbHParams), 
   BtWParams                  = cms.PSet(genPartParams,BtWParams), 
   )
