#ifndef ANALYSIS_VLQANA_APPLYLEPTONSFS_HH
#define ANALYSIS_VLQANA_APPLYLEPTONSFS_HH

class ApplyLeptonSFs {
  public:
    enum LEPTONIDTYPES_t {LOOSE, TIGHT} ; 
    ApplyLeptonSFs (edm::ParameterSet const& pars) : 
      sf_(1),
      zdecayMode_(pars.getParameter<std::string>("zdecayMode")) 
  {
     std::string lepidtypestr = pars.getParameter<std::string>("lepidtype") ; 
     if ( lepidtypestr == "LOOSE" ) type_ = LOOSE ;  
     else if ( lepidtypestr == "TIGHT" ) type_ = TIGHT ; 
     else edm::LogError("ApplyLeptonSF") << " >>>> WrongElectronIdType: " << type_<< " Check lepton id type !!!" ; 
  }
    ~ApplyLeptonSFs () {} 
    double operator () (double pt, double eta){
       if (type_ == TIGHT && zdecayMode_ == "zelel"){
          if(pt > 200.) pt = 200.; 
          if(pt > 10 && pt <= 20){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.05805;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  1.00872;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  1.14344;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  1.07572;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  1.00477;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  1.00477;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  1.07572;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  1.14344;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  1.00872;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.05805;
          }
          else if(pt > 20 && pt <= 30){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.0;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  0.951172;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.996894;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.988484;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.98915;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.98915;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.988484;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.996894;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  0.951172;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.0;
          }
          else if(pt > 30 && pt <= 40){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  0.996909;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  0.970497;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.972574;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.990755;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.982009;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.982009;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.990755;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.972574;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  0.970497;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  0.996909;
          }
          else if(pt > 40 && pt <= 50){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.00983;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  0.993084;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.993421;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.990424;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.981208;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.981208;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.990424;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.993421;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  0.993084;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.00983;
          }
          else if(pt > 50 && pt <= 200){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.0239;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  1.00521;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  1.0062;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.980867;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.983648;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.983648;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.980867;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  1.0062;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  1.00521;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.0239;
          }
         
       }//end TIGHT and zelel
       if (type_ == LOOSE  && zdecayMode_ == "zelel"){
          if(pt > 200.) pt = 200.; 
          if(pt > 10 && pt <= 20){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.03894;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  1.02685;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  1.07143;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  1.07717;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  1.00916;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  1.00916;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  1.07717;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  1.07143;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  1.02685;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.03894;
          }
          else if(pt > 20 && pt <= 30){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.00526;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  0.978581;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.976654;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.990897;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.989835;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.989835;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.990897;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.976654;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  0.978581;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.00526;
          }
          else if(pt > 30 && pt <= 40){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.0036;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  0.989349;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.9838;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.990805;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.989738;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.989738;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.990805;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.9838;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  0.989349;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.0036;
          }
          else if(pt > 40 && pt <= 50){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.01387;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  1.00562;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.981459;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.990228;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.990239;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.990239;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.990228;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.981459;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  1.00562;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.01387;
          }
          else if(pt > 50 && pt <= 200){
             if(eta <= -2.0          && eta > -2.5)    sf_ =  1.01598;
             else if(eta <= -1.566   && eta > -2.0)    sf_ =  1.01443;
             else if(eta <= -1.4442  && eta > -1.566)  sf_ =  0.984127;
             else if(eta <= -0.8     && eta > -1.4442) sf_ =  0.989305;
             else if(eta <= 0.0      && eta > -0.8)    sf_ =  0.989328;
             else if(eta <= 0.8      && eta > 0.0)     sf_ =  0.989328;
             else if(eta <= 1.4442   && eta > 0.8)     sf_ =  0.989305;
             else if(eta <= 1.566    && eta > 1.4442)  sf_ =  0.984127;
             else if(eta <= 2.0      && eta > 1.566)   sf_ =  1.01443;
             else if(eta < 2.5       && eta > 2.0)     sf_ =  1.01598;
          }
       }//end LOOSE and zelel
       if (type_ == LOOSE && zdecayMode_ == "zmumu"){
          if(pt > 120.) pt = 120.; 
          if (pt > 20 && pt <= 25){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.993395;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.99804;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.997042;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.986261;
          }
          else if (pt > 25 && pt <= 30){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.992441;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.997301;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.990131;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.993439;
          }
          else if (pt > 30 && pt <= 40){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.996364;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.999038;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.997546;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.99785;
          }
          else if (pt > 40 && pt <= 50){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.995477;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.999201;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.997946;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.998379;
          }
          else if (pt > 50 && pt <= 60){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.993172;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.996878;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.996469;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.996717;
          }
          else if (pt > 60 && pt <= 120){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.990613;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.998005;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.997551;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.997595;
          }  
       }//LOOSE and zmumu
       if (type_ == TIGHT && zdecayMode_ == "zmumu"){
          if(pt > 120) pt = 120;
          if (pt > 20 && pt <= 25){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.978453;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.992952;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.977758;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.975358;
          }
          else if (pt > 25 && pt <= 30){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.976408;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.989996;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.976121;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.98281;
          }
          else if (pt > 30 && pt <= 40){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.978308;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.992301;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.980376;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.98664;
          }
          else if (pt > 40 && pt <= 50){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.977546;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.991254;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.980181;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.987303;
          }
          else if (pt > 50 && pt <= 60){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.972767;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.989062;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.976583;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.982278;
          }
          else if (pt > 60 && pt <= 120){
             if (abs(eta) <= 2.4 && abs(eta) > 2.1)       sf_ = 0.964052;
             else if (abs(eta) <= 2.1 && abs(eta) > 1.2)  sf_ = 0.990666;
             else if (abs(eta) <= 1.2 && abs(eta) > 0.9)  sf_ = 0.984312;
             else if (abs(eta) <= 0.9 && abs(eta) > 0.0)  sf_ = 0.985663;
          }
       }//TIGHT and zmumu
       return sf_ ; 
    }
  private: 
    double sf_ ;
    const std::string zdecayMode_ ; 
    LEPTONIDTYPES_t type_ ; 
};
#endif 
