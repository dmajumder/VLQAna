/*
 * FindGenPart.h
 *
 *  Created on: Nov 12, 2015
 *      Author: tyler
 */

#ifndef FINDGENPART_H_
#define FINDGENPART_H_

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "AnalysisDataFormats/BoostedObjects/interface/GenParticle.h"
#include "AnalysisDataFormats/BoostedObjects/interface/GenParticleWithDaughters.h"


typedef std::vector<vlq::GenParticle> GenParticleCollection ;

class FindGenPart{
public:
	explicit FindGenPart(const edm::ParameterSet&);
	~FindGenPart();
	const GenParticleCollection operator() (edm::Event&);
	TLorentzVector partFinder(vlq::GenParticle, int, int);
	TLorentzVector qFinder(vlq::GenParticle, int, int, int);
	double add(TLorentzVector, TLorentzVector, TLorentzVector);

	friend class OS2LAna;

private:
	edm::InputTag genPartInfoDau0ID_;
	edm::InputTag genPartInfoDau0Status_;
	edm::InputTag genPartInfoDau1ID_;
	edm::InputTag genPartInfoDau1Status_;
	edm::InputTag genPartInfoE_;
	edm::InputTag genPartInfoEta_;
	edm::InputTag genPartInfoID_;
	edm::InputTag genPartInfoMass_;
	edm::InputTag genPartInfoMom0ID_;
	edm::InputTag genPartInfoMom0Status_;
	edm::InputTag genPartInfoMom1ID_;
	edm::InputTag genPartInfoMom1Status_;
	edm::InputTag genPartInfoPhi_;
	edm::InputTag genPartInfoPt_;
	edm::InputTag genPartInfoStatus_;

    std::vector<int> ids_ ;
    std::vector<int> statuses_ ;
    bool checkstatus_ ;
    std::vector<int> mom0ids_ ;
    std::vector<int> mom1ids_ ;
    bool checkmomid_ ;
    std::vector<int> dau0ids_ ;
    std::vector<int> dau1ids_ ;
    bool checkdauid_ ;


    GenParticleCollection genPartsInfo_ ;
};



#endif /* FINDGENPART_H_ */
