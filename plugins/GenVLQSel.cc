// -*- C++ -*-
//
// Package:    Analysis/VLQAna
// Class:      GenVLQSel
// 
/**\class GenVLQSel GenVLQSel.cc Analysis/VLQAna/plugins/GenVLQSel.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Sadia Khalil
//         Created:  Mon, 31 Aug 2015 17:57:17 GMT
//
//
///////////////////////////////////////////////////////////////////////
#include "Analysis/VLQAna/interface/GenVLQSel.h"
using namespace reco;
using namespace std;
using namespace edm;

void
GenVLQSel::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{ 
   if(!iEvent.isRealData()){
      
      vlq::GenParticleCollection vlqTtZ = pickTtZ(iEvent) ;
      vlq::GenParticleCollection vlqTtH = pickTtH(iEvent) ;
      vlq::GenParticleCollection vlqTbW = pickTbW(iEvent) ;
      vlq::GenParticleCollection vlqBbZ = pickBbZ(iEvent) ;
      vlq::GenParticleCollection vlqBbH = pickBbH(iEvent) ;
      vlq::GenParticleCollection vlqBtW = pickBtW(iEvent) ;

      std::auto_ptr< unsigned >  tZbW      (new unsigned (0));
      std::auto_ptr< unsigned >  tHbW      (new unsigned (0));
      std::auto_ptr< unsigned >  tZtH      (new unsigned (0));
      std::auto_ptr< unsigned >  bWbW      (new unsigned (0));
      std::auto_ptr< unsigned >  tHtH      (new unsigned (0));
      std::auto_ptr< unsigned >  tZtZ      (new unsigned (0));
      std::auto_ptr< unsigned >  bZtW      (new unsigned (0));
      std::auto_ptr< unsigned >  bHtW      (new unsigned (0));
      std::auto_ptr< unsigned >  bZbH      (new unsigned (0));
      std::auto_ptr< unsigned >  tWtW      (new unsigned (0));
      std::auto_ptr< unsigned >  bHbH      (new unsigned (0));
      std::auto_ptr< unsigned >  bZbZ      (new unsigned (0));         
      
      if (type_ == TPrime){
         if ( vlqTtZ.size() == 1 && vlqTbW.size() == 1 ) {*tZbW = 1; h1_["tZbW_Evts"]->Fill(1);}
         else if ( vlqTtH.size() == 1 && vlqTbW.size() == 1 ) {*tHbW = 1; h1_["tHbW_Evts"]->Fill(1);}
         else if ( vlqTtZ.size() == 1 && vlqTtH.size() == 1 ) {*tZtH = 1; h1_["tZtH_Evts"]->Fill(1);}
         else if ( vlqTbW.size() == 2 ){*bWbW = 1; h1_["bWbW_Evts"]->Fill(1);}
         else if ( vlqTtH.size() == 2 ){*tHtH = 1; h1_["tHtH_Evts"]->Fill(1);}
         else if ( vlqTtZ.size() == 2 ){*tZtZ = 1; h1_["tZtZ_Evts"]->Fill(1);}
      }
      else if (type_ == BPrime){
         if ( vlqBbZ.size() == 1 && vlqBtW.size() == 1 ) {*bZtW = 1; h1_["bZtW_Evts"]->Fill(1);}
         else if ( vlqBbH.size() == 1 && vlqBtW.size() == 1 ) {*bHtW = 1; h1_["bHtW_Evts"]->Fill(1);}
         else if ( vlqBbZ.size() == 1 && vlqBbH.size() == 1 ) {*bZbH = 1; h1_["bZbH_Evts"]->Fill(1);}
         else if ( vlqBtW.size() == 2 ){*tWtW = 1; h1_["tWtW_Evts"]->Fill(1);}
         else if ( vlqBbH.size() == 2 ){*bHbH = 1; h1_["bHbH_Evts"]->Fill(1);}
         else if ( vlqBbZ.size() == 2 ){*bZbZ = 1; h1_["bZbZ_Evts"]->Fill(1);}
      }
   
      if (verbose_){
         if (type_ == TPrime){
            cout << "tHbW = " << *tHbW <<", tZbW = " << *tZbW <<", tZtH = " << *tZtH << ", bWbW = " << *bWbW <<", tHtH = "<< *tHtH <<", tZtZ = " << *tZtZ << endl;
         }
         else if (type_ == BPrime){
            cout << "bHtW = " << *bHtW <<", bZtW = " << *bZtW <<", bZbH = " << *bZbH << ", tWtW = " << *tWtW <<", bHbH = "<< *bHbH <<", bZbZ = " << *bZbZ << endl;
         }
         else{
            edm::LogError(">>>>ERROR>>>>GenVLQSel >>>>  WrongSignalType: ") << type_<< " Check the signal type !!!";
         }
      }
      if (type_ == TPrime){
         iEvent.put ( tZbW, "tZbW" );
         iEvent.put ( tHbW, "tHbW" );
         iEvent.put ( tZtH, "tZtH" );
         iEvent.put ( bWbW, "bWbW" );
         iEvent.put ( tHtH, "tHtH" );
         iEvent.put ( tZtZ, "tZtZ" );
      }
      else if (type_ == BPrime){      
         iEvent.put ( bZtW, "bZtW" );
         iEvent.put ( bHtW, "bHtW" );
         iEvent.put ( bZbH, "bZbH" );
         iEvent.put ( tWtW, "tWtW" );
         iEvent.put ( bHbH, "bHbH" );
         iEvent.put ( bZbZ, "bZbZ" );
      }  
   }
}


//define this as a plug-in
DEFINE_FWK_MODULE(GenVLQSel);
