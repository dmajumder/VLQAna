#include <memory>
#include <TH1D.h>
#include <TFile.h>
#include <TF1.h>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "Analysis/VLQAna/interface/MuonMaker.h"
#include "Analysis/VLQAna/interface/DileptonCandsProducer.h"
#include "Analysis/VLQAna/interface/CandidateFilter.h"
#include "Analysis/VLQAna/interface/ElectronMaker.h"
#include "Analysis/VLQAna/interface/JetMaker.h"
#include "Analysis/VLQAna/interface/ApplyLeptonSFs.h"
#include "Analysis/VLQAna/interface/CandidateCleaner.h"
#include "Analysis/VLQAna/interface/HT.h"

class Skim : public edm::EDFilter {
  public:
    explicit Skim(const edm::ParameterSet&);
    ~Skim(); 
  private:
    virtual void beginJob() override;
    virtual bool filter(edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;
    double GetDYNLOCorr(const double dileppt)    ;
    double htCorr(double ht,double p0,double p1) ;
    edm::EDGetTokenT<string>   t_evttype         ;
    edm::EDGetTokenT<double>   t_evtwtGen        ;
    edm::EDGetTokenT<double>   t_evtwtPV         ;
    edm::EDGetTokenT<bool>     t_hltdecision     ;
    edm::ParameterSet DilepCandParams_           ;
    edm::ParameterSet ZCandParams_               ; 
    const std::string zdecayMode_                ;
    const double HTMin_                          ;
    const bool applyLeptonSFs_                   ;
    const bool applyHtCorr_                      ;
    const bool applyDYNLOCorr_                   ;
    const std::string fname_DYNLOCorr_           ;
    const std::string funname_DYNLOCorr_         ;
    ElectronMaker electronmaker                  ; 
    MuonMaker muonmaker                          ; 
    JetMaker jetAK4maker                         ; 
    JetMaker jetAK8maker                         ; 
    ApplyLeptonSFs  lepsfs                       ;
    edm::Service<TFileService> fs                ; 
    std::map<std::string, TH1D*> h1_             ;
}; 

Skim::Skim(const edm::ParameterSet& iConfig) : 
  t_evttype               (consumes<string>  (iConfig.getParameter<edm::InputTag>("evttype"))),
  t_evtwtGen              (consumes<double>  (iConfig.getParameter<edm::InputTag>("evtwtGen"))),
  t_evtwtPV               (consumes<double>  (iConfig.getParameter<edm::InputTag>("evtwtPV"))),
  t_hltdecision           (consumes<bool>    (iConfig.getParameter<edm::InputTag>("hltdecision"))),
  DilepCandParams_        (iConfig.getParameter<edm::ParameterSet> ("DilepCandParams")),
  ZCandParams_            (iConfig.getParameter<edm::ParameterSet> ("ZCandParams")),
  zdecayMode_             (iConfig.getParameter<std::string>       ("zdecayMode")),
  HTMin_                  (iConfig.getParameter<double>            ("HTMin")),
  applyLeptonSFs_         (iConfig.getParameter<bool>              ("applyLeptonSFs")),
  applyHtCorr_            (iConfig.getParameter<bool>              ("applyHtCorr")),
  applyDYNLOCorr_         (iConfig.getParameter<bool>              ("applyDYNLOCorr")),
  fname_DYNLOCorr_        (iConfig.getParameter<std::string>       ("File_DYNLOCorr")),
  funname_DYNLOCorr_      (iConfig.getParameter<std::string>       ("Fun_DYNLOCorr")),
  electronmaker           (iConfig.getParameter<edm::ParameterSet> ("elselParams"),consumesCollector()), 
  muonmaker               (iConfig.getParameter<edm::ParameterSet> ("muselParams"),consumesCollector()),
  jetAK4maker             (iConfig.getParameter<edm::ParameterSet> ("jetAK4selParams"),consumesCollector()), 
  lepsfs                  (iConfig.getParameter<edm::ParameterSet> ("lepsfsParams"))
{}

Skim::~Skim() {}

bool Skim::filter(edm::Event& evt, const edm::EventSetup& iSetup) {
  using namespace edm ; 

  Handle<bool>     h_hltdecision ; evt.getByToken(t_hltdecision, h_hltdecision) ;
  const bool hltdecision(*h_hltdecision.product()) ;
  if ( !hltdecision ) return false;

  Handle<string>   h_evttype     ; evt.getByToken(t_evttype    , h_evttype    ) ;

  double evtwt(1.0) ; 
  if (*h_evttype.product() != "EvtType_Data") {
     Handle<double>   h_evtwtGen    ; evt.getByToken(t_evtwtGen   , h_evtwtGen   ) ;
     Handle<double>   h_evtwtPV     ; evt.getByToken(t_evtwtPV    , h_evtwtPV    ) ;
     evtwt = (*h_evtwtGen.product()) * (*h_evtwtPV.product()) ;
  }

  // dilepton properties: M > 50, lead pt > 45, second pt > 25
  DileptonCandsProducer dileptonsprod(DilepCandParams_) ;
  vlq::CandidateCollection dimuons, dielectrons, dileptons, zll;

  vlq::ElectronCollection goodElectrons; 
  electronmaker(evt, goodElectrons) ; 
  dileptonsprod.operator()<vlq::ElectronCollection>(dielectrons, goodElectrons) ;

  vlq::MuonCollection goodMuons; 
  muonmaker(evt, goodMuons) ; 
  dileptonsprod.operator()<vlq::MuonCollection>(dimuons, goodMuons);  

  if (zdecayMode_ == "zmumu") {dileptons = dimuons; }
  else if (zdecayMode_ == "zelel") {dileptons = dielectrons;}

  // dilepton candidate
  if (dileptons.size()  < 1) return false;
 
  // Get Dy EWK correction SF
  if ( applyDYNLOCorr_ && *h_evttype.product() != "EvtType_Data") {
    double EWKNLOkfact(GetDYNLOCorr(dileptons.at(0).getPt())) ;
    evtwt *= EWKNLOkfact ;
  }

  //  get lepton ID and Iso SF
  if (applyLeptonSFs_ && *h_evttype.product() != "EvtType_Data") {
     if (zdecayMode_  == "zmumu"){
        evtwt *= lepsfs(goodMuons.at(0).getPt(),goodMuons.at(0).getEta()) * lepsfs(goodMuons.at(1).getPt(), goodMuons.at(1).getEta() ) ;
     }
     else if (zdecayMode_  == "zelel"){
        evtwt *= lepsfs(goodElectrons.at(0).getPt(),goodElectrons.at(0).getEta()) * lepsfs(goodElectrons.at(1).getPt(), goodElectrons.at(1).getEta() ) ;
     }
  }  

  // Get jets and clean them w.r.t leptons:
  vlq::JetCollection goodAK4Jets;
  jetAK4maker(evt, goodAK4Jets) ;

  CandidateCleaner cleanjets(0.4);
  if (zdecayMode_ == "zmumu") {cleanjets(goodAK4Jets, goodMuons);}
  else if (zdecayMode_ == "zelel") {cleanjets(goodAK4Jets, goodElectrons);}
  
  HT htak4(goodAK4Jets) ;
  double ht = htak4.getHT();
   
  // event weight due to HT correction
  if (applyHtCorr_ && *h_evttype.product() != "EvtType_Data"){
     double corr(1.);
     if (zdecayMode_ == "zmumu"){
        corr = htCorr(ht, 1.16045, -0.000492635);
     }
     else if (zdecayMode_ == "zelel"){
        corr = htCorr(ht, 1.456, -0.000695945);
     }
     if (corr > 0.) evtwt *= corr;
  }
 
  //Fill the events with Trig and dilepton cut applied
  h1_["cutflow"] -> Fill(1, evtwt) ;

  //at least 3 AK4 jets in event
  if (goodAK4Jets.size() > 2 ) {h1_["cutflow"] -> Fill(2, evtwt) ;}
  else return false;

  // at least HT > 200 in event
  if ( htak4.getHT() > HTMin_ ) h1_["cutflow"] -> Fill(3, evtwt) ;
  else return false ;

  //Z mass candidate filter: 75 < M < 105, lead pt > 45, 2nd pt > 25, Z pt > 0
  CandidateFilter zllfilter(ZCandParams_) ; 
  zllfilter(dileptons, zll);
  if(zll.size() > 0) {h1_["cutflow"] -> Fill(4, evtwt) ;}
  else return false ;

  return true ; 
}

void Skim::beginJob() { 
  h1_["cutflow"] = fs->make<TH1D>("cutflow", "cut flow with event weights", 4, 0.5, 4.5) ;   
  h1_["cutflow"] -> GetXaxis() -> SetBinLabel(1, "Trig.+l^{+}l^{-}") ; 
  h1_["cutflow"] -> GetXaxis() -> SetBinLabel(2, "N(AK4) #geq 3") ; 
  h1_["cutflow"] -> GetXaxis() -> SetBinLabel(3, "H_{T} #geq 200") ; 
  h1_["cutflow"] -> GetXaxis() -> SetBinLabel(4, "75 #lt M(l^{+}l^{-}) #lt 105");
  //  h1_["cutflow_nowt"] = fs->make<TH1D>("cutflow_nowt", "cut flow", 2, 0.5, 2.5) ; 
  //h1_["cutflow_nowt"] -> GetXaxis() -> SetBinLabel(1, "All") ; 
  //h1_["cutflow_nowt"] -> GetXaxis() -> SetBinLabel(2, "Passed") ; 
  return ; 
} 

double Skim::GetDYNLOCorr(const double dileppt) {
  std::unique_ptr<TFile >file_DYNLOCorr = std::unique_ptr<TFile>(new TFile(fname_DYNLOCorr_.c_str())) ;
  std::unique_ptr<TF1>fun_DYNLOCorr = std::unique_ptr<TF1>(dynamic_cast<TF1*>(file_DYNLOCorr->Get(funname_DYNLOCorr_.c_str()))) ;
  double EWKNLOkfact = fun_DYNLOCorr->Eval(dileppt);
  return EWKNLOkfact;
}

double Skim::htCorr(double ht, double p0, double p1){
  return(p1*ht + p0);
}

void Skim::endJob() { return ; }

DEFINE_FWK_MODULE(Skim);
