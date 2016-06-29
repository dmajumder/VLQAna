/*
 * FindGenPart.cc
 *
 *  Created on: Nov 12, 2015
 *      Author: tyler
 */

#include <iostream>

#include "Analysis/VLQAna/interface/FindGenPart.h"
//#include "FindGenPart.h"


FindGenPart::FindGenPart(const edm::ParameterSet& iConfig) :
genPartInfoDau0ID_		(iConfig.getParameter<edm::InputTag>("genPartInfoDau0IDLabel"))		,
genPartInfoDau0Status_		(iConfig.getParameter<edm::InputTag>("genPartInfoDau0StatusLabel"))	,
genPartInfoDau1ID_		(iConfig.getParameter<edm::InputTag>("genPartInfoDau1IDLabel"))		,
genPartInfoDau1Status_		(iConfig.getParameter<edm::InputTag>("genPartInfoDau1StatusLabel"))	,
genPartInfoE_			(iConfig.getParameter<edm::InputTag>("genPartInfoELabel"))		,
genPartInfoEta_			(iConfig.getParameter<edm::InputTag>("genPartInfoEtaLabel"))		,
genPartInfoID_			(iConfig.getParameter<edm::InputTag>("genPartInfoIDLabel"))		,
genPartInfoMass_		(iConfig.getParameter<edm::InputTag>("genPartInfoMassLabel"))		,
genPartInfoMom0ID_		(iConfig.getParameter<edm::InputTag>("genPartInfoMom0IDLabel"))		,
genPartInfoMom0Status_		(iConfig.getParameter<edm::InputTag>("genPartInfoMom0StatusLabel"))	,
genPartInfoMom1ID_		(iConfig.getParameter<edm::InputTag>("genPartInfoMom1IDLabel"))		,
genPartInfoMom1Status_		(iConfig.getParameter<edm::InputTag>("genPartInfoMom1StatusLabel"))	,
genPartInfoPhi_			(iConfig.getParameter<edm::InputTag>("genPartInfoPhiLabel"))		,
genPartInfoPt_			(iConfig.getParameter<edm::InputTag>("genPartInfoPtLabel"))		,
genPartInfoStatus_		(iConfig.getParameter<edm::InputTag>("genPartInfoStatusLabel"))		,

ids_                 		(iConfig.getParameter<std::vector<int>>("ids"))				,
statuses_            		(iConfig.getParameter<std::vector<int>>("statuses"))			,
checkstatus_         		(iConfig.getParameter<bool>("checkstatus"))				,
mom0ids_             		(iConfig.getParameter<std::vector<int>>("mom0ids"))			,
mom1ids_             		(iConfig.getParameter<std::vector<int>>("mom1ids"))			,
checkmomid_          		(iConfig.getParameter<bool>("checkmomid"))				,
dau0ids_             		(iConfig.getParameter<std::vector<int>>("dau0ids"))			,
dau1ids_             		(iConfig.getParameter<std::vector<int>>("dau1ids"))			,
checkdauid_          		(iConfig.getParameter<bool>("checkdauid"))
{}


FindGenPart::~FindGenPart(){};

const GenParticleCollection FindGenPart::operator() (edm::Event& evt){

	using namespace std;

	typedef edm::Handle <std::vector<float>> Hfloat ;

	Hfloat genPartInfoDau0ID; 		evt.getByLabel( genPartInfoDau0ID_		, genPartInfoDau0ID		);
	Hfloat genPartInfoDau0Status; 		evt.getByLabel( genPartInfoDau0Status_		, genPartInfoDau0Status		);
	Hfloat genPartInfoDau1ID; 		evt.getByLabel( genPartInfoDau1ID_		, genPartInfoDau1ID		);
	Hfloat genPartInfoDau1Status; 		evt.getByLabel( genPartInfoDau1Status_		, genPartInfoDau1Status		);
	Hfloat genPartInfoE; 			evt.getByLabel( genPartInfoE_			, genPartInfoE			);
	Hfloat genPartInfoEta; 			evt.getByLabel( genPartInfoEta_			, genPartInfoEta		);
	Hfloat genPartInfoID; 			evt.getByLabel( genPartInfoID_			, genPartInfoID			);
	Hfloat genPartInfoMass; 		evt.getByLabel( genPartInfoMass_		, genPartInfoMass		);
	Hfloat genPartInfoMom0ID; 		evt.getByLabel( genPartInfoMom0ID_		, genPartInfoMom0ID		);
	Hfloat genPartInfoMom0Status; 		evt.getByLabel( genPartInfoMom0Status_		, genPartInfoMom0Status		);
	Hfloat genPartInfoMom1ID; 		evt.getByLabel( genPartInfoMom1ID_		, genPartInfoMom1ID		);
	Hfloat genPartInfoMom1Status; 		evt.getByLabel( genPartInfoMom1Status_		, genPartInfoMom1Status		);
	Hfloat genPartInfoPhi; 			evt.getByLabel( genPartInfoPhi_			, genPartInfoPhi		);
	Hfloat genPartInfoPt; 			evt.getByLabel( genPartInfoPt_			, genPartInfoPt			);
	Hfloat genPartInfoStatus; 		evt.getByLabel( genPartInfoStatus_		, genPartInfoStatus		);


	for (unsigned ind = 0; ind < (genPartInfoID.product())->size(); ind++){

		if ( std::find(ids_.begin(), ids_.end(), (genPartInfoID.product())->at(ind)) == ids_.end() ) continue ;
//
//		if ( checkstatus_ && std::find(statuses_.begin(), statuses_.end(), (genPartInfoStatus.product())->at(ind)) == statuses_.end() ) continue ;
//		if ( checkmomid_ && std::find(mom0ids_.begin(), mom0ids_.end(), (genPartInfoMom0ID.product())->at(ind)) == mom0ids_.end() ) 	   continue ;
//		if ( checkmomid_ && std::find(mom1ids_.begin(), mom1ids_.end(), (genPartInfoMom1ID.product())->at(ind)) == mom1ids_.end() )     continue ;
//		if ( checkdauid_ && std::find(dau0ids_.begin(), dau0ids_.end(), (genPartInfoDau0ID.product())->at(ind)) == dau0ids_.end() )     continue ;
//		if ( checkdauid_ && std::find(dau1ids_.begin(), dau1ids_.end(), (genPartInfoDau1ID.product())->at(ind)) == dau1ids_.end() )     continue ;

	    TLorentzVector genPartsP4 ;
	    vlq::GenParticle genParticle ;
	    genPartsP4.SetPtEtaPhiM( (genPartInfoPt.product())->at(ind), (genPartInfoEta.product())->at(ind),
	    						 (genPartInfoPhi.product())->at(ind), (genPartInfoMass.product())->at(ind) )  ;
	    genParticle.setP4( genPartsP4 ) 																			;
	    genParticle.setPdgID      ( (genPartInfoID.product())->at(ind) )			;
	    genParticle.setStatus     ( (genPartInfoStatus.product())->at(ind) )		;
	    genParticle.setMom0PdgID  ( (genPartInfoMom0ID.product())->at(ind) ) 		;
	    genParticle.setMom1PdgID  ( (genPartInfoMom1ID.product())->at(ind) ) 		;
	    genParticle.setDau0PdgID  ( (genPartInfoDau0ID.product())->at(ind) ) 		;
	    genParticle.setDau1PdgID  ( (genPartInfoDau1ID.product())->at(ind) ) 		;
	    genParticle.setMom0Status ( (genPartInfoMom0Status.product())->at(ind) ) 		;
	    genParticle.setMom1Status ( (genPartInfoMom1Status.product())->at(ind) ) 		;
	    genParticle.setDau0Status ( (genPartInfoDau0Status.product())->at(ind) ) 		;
	    genParticle.setDau1Status ( (genPartInfoDau1Status.product())->at(ind) ) 		;
	    genPartsInfo_.push_back(genParticle) 						;
	}
return(genPartsInfo_);
}


TLorentzVector FindGenPart::partFinder(vlq::GenParticle part, int PdgID, int MoPdgID){							// I think I can loop over PickGenPart::genPartsInfos_ and pass
	TLorentzVector found;																						// individual elements as vlq::GenParticel parameter
		if (part.getPdgID() == PdgID && part.getMom0PdgID() == MoPdgID)
			found = part.getP4();
		return (found);
}

TLorentzVector FindGenPart::qFinder(vlq::GenParticle part, int PdgIDlow, int PdgIDhigh, int MoPdgID){
	TLorentzVector found;
		if (part.getPdgID() >= PdgIDlow && part.getPdgID() <= PdgIDhigh && part.getMom0PdgID() == MoPdgID)
			found = part.getP4();
		return (found);
}

double FindGenPart::add(TLorentzVector q1, TLorentzVector q2, TLorentzVector b){
	double	sum = (q1 + q2 + b).M();
	return (sum);
}
