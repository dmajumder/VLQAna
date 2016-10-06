import FWCore.ParameterSet.Config as cms
from Analysis.VLQAna.ApplyLeptonSFs_cfi import *
from Analysis.VLQAna.ZCandSelector_cfi import *
from Analysis.VLQAna.ElectronMaker_cfi import *
from Analysis.VLQAna.MuonMaker_cfi import *
from Analysis.VLQAna.JetSelector_cfi import *

skim = cms.EDFilter("Skim",
    hltdecision                = cms.InputTag("evtcleaner","hltdecision"),
    evttype                    = cms.InputTag("evtcleaner","evttype"),
    evtwtGen                   = cms.InputTag("evtcleaner","evtwtGen"),
    evtwtPV                    = cms.InputTag("evtcleaner","evtwtPV"),
    DilepCandParams            = defaultZCandSelectionParameters.clone(
        massMin = cms.double(50),
    ),
    ZCandParams                = defaultZCandSelectionParameters.clone(
        massMin = cms.double(75),
        massMax = cms.double(105),
        ptMinLeadingLep = cms.double(45),
        ), 
    lepsfsParams            = defaultWP.clone(
        lepidtype = cms.string("TIGHT"),
        zdecayMode = cms.string("zelel"),
        ),
    zdecayMode                 = cms.string("zelel"),
    HTMin                      = cms.double (200.), 
    File_DYNLOCorr             = cms.string('scalefactors_v4.root'),
    Fun_DYNLOCorr              = cms.string('z_ewkcorr/z_ewkcorr_func'),
    applyHtCorr                = cms.bool(False),
    applyLeptonSFs             = cms.bool(False), 
    applyDYNLOCorr             = cms.bool(False),
    muselParams                = defaultMuonMakerParameters.clone(
        muIsoMax = cms.double(0.15),
        muidtype = cms.string("TIGHT"), 
    ), 
    elselParams                = defaultElectronMakerParameters.clone(
        elidtype = cms.string("TIGHT"),
    ), 
    jetAK4selParams            = defaultAK4JetSelectionParameters,
    )
