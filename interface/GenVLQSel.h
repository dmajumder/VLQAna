#ifndef GenVLQSel_h
#define GenVLQSel_h

// system include files
#include <memory>
#include <vector>
#include <string>
#include <TH1D.h>
#include <TFile.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/Utils/interface/TFileDirectory.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Particle.h"
#include "Analysis/VLQAna/interface/PickGenPart.h"
//
// class declaration
//

class GenVLQSel : public edm::EDProducer {
public:
   enum SIGNALTYPES_t {TPrime, BPrime} ;
   explicit GenVLQSel(const edm::ParameterSet&);
   ~GenVLQSel();
private:
   virtual void beginJob();
   virtual void produce(edm::Event&, const edm::EventSetup&);
   virtual void endJob();
   // ----------member data ---------------------------
   void setPointers(std::vector<const reco::Candidate *> decayList);
   bool verbose_;
   SIGNALTYPES_t     type_ ;
   edm::ParameterSet TtZParams_;
   edm::ParameterSet TtHParams_;
   edm::ParameterSet TbWParams_;
   edm::ParameterSet BbZParams_;
   edm::ParameterSet BbHParams_;
   edm::ParameterSet BtWParams_;
   PickGenPart pickTtZ;
   PickGenPart pickTtH;
   PickGenPart pickTbW;
   PickGenPart pickBbZ;
   PickGenPart pickBbH;
   PickGenPart pickBtW;
   std::map<std::string, TH1D*> h1_;
   edm::Service<TFileService> fs;
};
#endif
//
// constants, enums and typedefs
//
typedef reco::Candidate::PolarLorentzVector LorentzV;
typedef std::vector< LorentzV > p4_vector;
typedef std::vector< int > pdgID_vector;
typedef edm::Handle <std::vector<float>> hfloat ;
//
// static data member definitions
//
void GenVLQSel::setPointers(std::vector<const reco::Candidate *> decayList){
   for(std::vector<const reco::Candidate *>::iterator iter = decayList.begin(); decayList.end() != iter; ++iter){
      *iter = 0;
   }
}

//
// constructors and destructor
//
GenVLQSel::GenVLQSel(const edm::ParameterSet& iConfig):
   verbose_               (iConfig.getParameter<bool>              ("verbose"  )),
   TtZParams_             (iConfig.getParameter<edm::ParameterSet> ("TtZParams")),
   TtHParams_             (iConfig.getParameter<edm::ParameterSet> ("TtHParams")),
   TbWParams_             (iConfig.getParameter<edm::ParameterSet> ("TbWParams")),
   BbZParams_             (iConfig.getParameter<edm::ParameterSet> ("BbZParams")),
   BbHParams_             (iConfig.getParameter<edm::ParameterSet> ("BbHParams")),
   BtWParams_             (iConfig.getParameter<edm::ParameterSet> ("BtWParams")),
   pickTtZ                (TtZParams_,consumesCollector()),
   pickTtH                (TtHParams_,consumesCollector()),
   pickTbW                (TbWParams_,consumesCollector()),
   pickBbZ                (BbZParams_,consumesCollector()),
   pickBbH                (BbHParams_,consumesCollector()),
   pickBtW                (BtWParams_,consumesCollector())
{
   std::string sigType = iConfig.getParameter<std::string>("sigtype") ;
   if ( sigType == "TPrime" ) type_ = TPrime ;
   else if ( sigType== "BPrime" ) type_ = BPrime ;   
   else edm::LogError(">>>>ERROR>>>>GenVLQSel >>>>  WrongSignalType: ") << type_<< " Check the signal type !!!" ;
   //register your products
   produces<unsigned> ("tZbW");
   produces<unsigned> ("tHbW"); 
   produces<unsigned> ("tZtH");  
   produces<unsigned> ("bWbW");
   produces<unsigned> ("tHtH");
   produces<unsigned> ("tZtZ");
   produces<unsigned> ("bZtW");
   produces<unsigned> ("bHtW"); 
   produces<unsigned> ("bZbH");  
   produces<unsigned> ("tWtW");
   produces<unsigned> ("bHbH");
   produces<unsigned> ("bZbZ");
}
                           

GenVLQSel::~GenVLQSel()
{
}

// ------------ method called once each job just before starting event loop  ------------
void 
GenVLQSel::beginJob()
{
   if(type_ == TPrime){
      h1_["tZbW_Evts"] = fs->make<TH1D>("tZbW_Evts", "TT #rightarrow tZbW Evts", 2, 0.5, 2.5);
      h1_["tHbW_Evts"] = fs->make<TH1D>("tHbW_Evts", "TT #rightarrow tHbW Evts", 2, 0.5, 2.5);
      h1_["tZtH_Evts"] = fs->make<TH1D>("tZtH_Evts", "TT #rightarrow tZtH Evts", 2, 0.5, 2.5);
      h1_["bWbW_Evts"] = fs->make<TH1D>("bWbW_Evts", "TT #rightarrow bWbW Evts", 2, 0.5, 2.5);
      h1_["tHtH_Evts"] = fs->make<TH1D>("tHtH_Evts", "TT #rightarrow tHtH Evts", 2, 0.5, 2.5);
      h1_["tZtZ_Evts"] = fs->make<TH1D>("tZtZ_Evts", "TT #rightarrow tZtZ Evts", 2, 0.5, 2.5);
   }
   else if (type_ == BPrime){
      h1_["bZtW_Evts"] = fs->make<TH1D>("bZtW_Evts", "BB #rightarrow bZtW Evts", 2, 0.5, 2.5);
      h1_["bHtW_Evts"] = fs->make<TH1D>("bHtW_Evts", "BB #rightarrow bHtW Evts", 2, 0.5, 2.5);
      h1_["bZbH_Evts"] = fs->make<TH1D>("bZbH_Evts", "BB #rightarrow bZbH Evts", 2, 0.5, 2.5);
      h1_["tWtW_Evts"] = fs->make<TH1D>("tWtW_Evts", "BB #rightarrow tWtW Evts", 2, 0.5, 2.5);
      h1_["bHbH_Evts"] = fs->make<TH1D>("bHbH_Evts", "BB #rightarrow bHbH Evts", 2, 0.5, 2.5);
      h1_["bZbZ_Evts"] = fs->make<TH1D>("bZbZ_Evts", "BB #rightarrow bZbZ Evts", 2, 0.5, 2.5);
   }
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GenVLQSel::endJob() {
   std::cout << "----------------------------------------------------------------------------------------" << std::endl;
   std::cout << "So long, and thanks for all the fish..." << std::endl;
   std::cout << "----------------------------------------------------------------------------------------" << std::endl;
}



