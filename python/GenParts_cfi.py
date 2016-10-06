import FWCore.ParameterSet.Config as cms

defaultgenPartInfoParams = cms.PSet(

genPartInfoChargeLabel		= cms.InputTag("genPart", "genPartCharge"),
genPartInfoDau0IDLabel		= cms.InputTag("genPart", "genPartDau0ID"),
genPartInfoDau0StatusLabel	= cms.InputTag("genPart", "genPartDau0Status"),
genPartInfoDau1IDLabel		= cms.InputTag("genPart", "genPartDau1ID"),
genPartInfoDau1StatusLabel	= cms.InputTag("genPart", "genPartDau1Status"),
genPartInfoELabel		= cms.InputTag("genPart", "genPartE"),
genPartInfoEtaLabel		= cms.InputTag("genPart", "genPartEta"),
genPartInfoIDLabel		= cms.InputTag("genPart", "genPartID"),
genPartInfoMassLabel		= cms.InputTag("genPart", "genPartMass"),
genPartInfoMom0IDLabel		= cms.InputTag("genPart", "genPartMom0ID"),
genPartInfoMom0StatusLabel	= cms.InputTag("genPart", "genPartMom0Status"),
genPartInfoMom1IDLabel		= cms.InputTag("genPart", "genPartMom1ID"),
genPartInfoMom1StatusLabel	= cms.InputTag("genPart", "genPartMom1Status"),
genPartInfoPhiLabel		= cms.InputTag("genPart", "genPartPhi"),
genPartInfoPtLabel		= cms.InputTag("genPart", "genPartPt"),
genPartInfoStatusLabel		= cms.InputTag("genPart", "genPartStatus"),
genPartInfoYLabel		= cms.InputTag("genPart", "genPartY"),
    ids                 = cms.vint32(-8000001,-8000002,8000001,8000002,1,2,3,4,5,-1,-2,-3,-4,-5,23), 
    statuses            = cms.vint32(22), 
    checkstatus         = cms.bool(False),
    mom0ids             = cms.vint32(-8000001,-8000002,8000001,8000002), 
    mom1ids             = cms.vint32(-8000001,-8000002,8000001,8000002), 
    checkmomid          = cms.bool(False),
    dau0ids             = cms.vint32(-5,5,-6,6,23), 
    dau1ids             = cms.vint32(-5,5,-6,6,23), 
    checkdauid          = cms.bool(True),
)

#defaultgetGenParams = cms.PSet(

#    ids                 = cms.vint32(-8000001,-8000002,8000001,8000002), 
#    statuses            = cms.vint32(22), 
#    checkstatus         = cms.bool(False),
#    mom0ids             = cms.vint32(-8000001,-8000002,8000001,8000002), 
#    mom1ids             = cms.vint32(-8000001,-8000002,8000001,8000002), 
#    checkmomid          = cms.bool(False),
#    dau0ids             = cms.vint32(-5,5,-6,6,23), 
#    dau1ids             = cms.vint32(-5,5,-6,6,23), 
#   checkdauid          = cms.bool(True),
#)
