import FWCore.ParameterSet.Config as cms

defaultMETParameters = cms.PSet(
    metFullPhiLabel			= cms.InputTag("metFull","metFullPhi"),
    metFullPtLabel 			= cms.InputTag("metFull","metFullPt"),
    metFullPxLabel			= cms.InputTag("metFull","metFullPx"),
    metFullPyLabel			= cms.InputTag("metFull","metFullPy"),
    metFulluncorPhiLabel		= cms.InputTag("metFull","metFulluncorPhi"),
    metFulluncorPtLabel			= cms.InputTag("metFull","metFulluncorPt"),
    metFulluncorSumEtLabel		= cms.InputTag("metFull","metFulluncorSumEt"),
    )
