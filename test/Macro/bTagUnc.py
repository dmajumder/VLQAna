#! /usr/bin/env python

import sys
from ROOT import gROOT, gStyle,  Double
from ROOT import TFile, TIter, TH1F, TDirectory, TMath, TCanvas, TLegend
import math
gROOT.Macro("~/rootlogon.C")
gStyle.SetOptStat(0)

from optparse import OptionParser
parser = OptionParser()	  				  				  					  			  					  				  
parser.add_option('--name', metavar='T', type='string', action='store',
                  default='ttbar',
                  dest='name',
                  help='variable to plot')
(options,args) = parser.parse_args()

var = 'chi_mass_H'
name = options.name

path = '/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/Histograms/withSystematics/electrons/'

f = TFile(path+name+'.root')

h_nom = f.Get('ana/sig/'+var).Clone()
h_bUp = f.Get('anabcUp/sig/'+var).Clone()
h_bDown = f.Get('anabcDown/sig/'+var).Clone()
h_lUp = f.Get('analightUp/sig/'+var).Clone()
h_lDown = f.Get('analightDown/sig/'+var).Clone()

hs_dn_new = h_bDown.Clone()
hs_dn_new.Reset()
hs_dn_new.SetDirectory(0)
hs_up_new = h_bUp.Clone()
hs_up_new.Reset()
hs_up_new.SetDirectory(0)

h_up_hf_diff = h_bUp.Clone()
h_dn_hf_diff = h_bDown.Clone()
h_up_lf_diff = h_lUp.Clone()
h_dn_lf_diff = h_lDown.Clone()
h_dn_hf_diff.Add(h_lDown, -1)
h_dn_lf_diff.Add(h_bDown, -1)
h_up_hf_diff.Add(h_lUp, -1)
h_up_lf_diff.Add(h_bUp, -1)



#h_dn_hf_diff.Draw()
#raw_input("holdon")

nbins = hs_dn_new.GetNbinsX()
for ibin in range(0, nbins+1):
    sumErrUp2 = 0
    sumErrDn2 = 0

    var_dn_hf = h_dn_hf_diff.GetBinContent(ibin+1)
    var_dn_lf = h_dn_lf_diff.GetBinContent(ibin+1)
    var_up_hf = h_up_hf_diff.GetBinContent(ibin+1)
    var_up_lf = h_up_lf_diff.GetBinContent(ibin+1)

    bin_up_var_hf = max(var_dn_hf,var_up_hf) # find the largest positive bin content variation due to SFb variation (set to 0 if both negative)
    if( bin_up_var_hf < 0. ): bin_up_var_hf = 0.
    bin_dn_var_hf = min(var_dn_hf,var_up_hf) # find the largest negative bin content variation due to SFb variation (set to 0 if both positive)
    if( bin_dn_var_hf > 0. ): bin_dn_var_hf = 0.

    bin_up_var_lf = max(var_dn_lf,var_up_lf) # find the largest positive bin content variation due to SFl variation (set to 0 if both negative)
    if( bin_up_var_lf < 0. ): bin_up_var_lf = 0.
    bin_dn_var_lf = min(var_dn_lf,var_up_lf) # find the largest negative bin content variation due to SFl variation (set to 0 if both positive)
    if( bin_dn_var_lf > 0. ): bin_dn_var_lf = 0.

    bin_up_var = math.sqrt( bin_up_var_hf**2 + bin_up_var_lf**2 )
    bin_dn_var = math.sqrt( bin_dn_var_hf**2 + bin_dn_var_lf**2 )

    hs_up_new.SetBinContent(ibin+1, h_nom.GetBinContent(ibin+1) + bin_up_var)
    hs_dn_new.SetBinContent(ibin+1, h_nom.GetBinContent(ibin+1) - bin_dn_var)

###write two output root file:
f_dn = TFile('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/El_'+name+'_'+var+"_BTagSFdown.root", "RECREATE")
f_dn.cd()
hs_dn_new.Write()
f_dn.Close()

f_up = TFile('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/El_'+name+'_'+var+"_BTagSFup.root", "RECREATE")
f_up.cd()
hs_up_new.Write()
f_up.Close()


    
# DY = [f_DY100to200, f_DY200to400, f_DY400to600, f_DY600toInf]
# hist_up_new = []
# hist_dn_new = []

# for hist  in DY:
#     h_nom = hist.Get('ana/sig/'+var).Clone()
#     h_bUp = hist.Get('anabcUp/sig/'+var).Clone()
#     h_bDown = hist.Get('anabcDown/sig/'+var).Clone()
#     h_lUp = hist.Get('analightUp/sig/'+var).Clone()
#     h_lDown = hist.Get('analightDown/sig/'+var).Clone()
    
#     h_dn_hf_diff = h_bUp.Clone()
#     h_dn_lf_diff = h_bDown.Clone()
#     h_up_hf_diff = h_lUp.Clone()
#     h_up_lf_diff = h_lDown.Clone()
#     h_dn_hf_diff.Add(h_bUp, -1)
#     h_dn_lf_diff.Add(h_bDown, -1)
#     h_up_hf_diff.Add(h_lUp, -1)
#     h_up_lf_diff.Add(h_lDown, -1)

#     hs_dn_new = h_bDown.Clone()
#     hs_dn_new.Reset()
#     hs_dn_new.SetDirectory(0)
#     hs_up_new = h_bUp.Clone()
#     hs_up_new.Reset()
#     hs_up_new.SetDirectory(0)
    
#     nbins = hs_dn_new.GetNbinsX()
#     nbins = hs_dn_new.GetNbinsX()
#     for ibin in range(0, nbins+1):
#         sumErrUp2 = 0
#         sumErrDn2 = 0

#         var_dn_hf = h_dn_hf_diff.GetBinContent(ibin+1)
#         var_dn_lf = h_dn_lf_diff.GetBinContent(ibin+1)
#         var_up_hf = h_up_hf_diff.GetBinContent(ibin+1)
#         var_up_lf = h_up_lf_diff.GetBinContent(ibin+1)

#         bin_up_var_hf = max(var_dn_hf,var_up_hf) # find the largest positive bin content variation due to SFb variation (set to 0 if both negative)
#         if( bin_up_var_hf < 0. ): bin_up_var_hf = 0.
#         bin_dn_var_hf = min(var_dn_hf,var_up_hf) # find the largest negative bin content variation due to SFb variation (set to 0 if both positive)
#         if( bin_dn_var_hf > 0. ): bin_dn_var_hf = 0.
        
#         bin_up_var_lf = max(var_dn_lf,var_up_lf) # find the largest positive bin content variation due to SFl variation (set to 0 if both negative)
#         if( bin_up_var_lf < 0. ): bin_up_var_lf = 0.
#         bin_dn_var_lf = min(var_dn_lf,var_up_lf) # find the largest negative bin content variation due to SFl variation (set to 0 if both positive)
#         if( bin_dn_var_lf > 0. ): bin_dn_var_lf = 0.
        
#         bin_up_var = math.sqrt( bin_up_var_hf**2 + bin_up_var_lf**2 )
#         bin_dn_var = math.sqrt( bin_dn_var_hf**2 + bin_dn_var_lf**2 )
        
#         hs_up_new.SetBinContent(ibin+1, h_nom.GetBinContent(ibin+1) + bin_up_var)
#         hs_dn_new.SetBinContent(ibin+1, h_nom.GetBinContent(ibin+1) - bin_dn_var)

#     hist_up_new.append(hs_up_new)
#     hist_dn_new.append(hs_dn_new)

# f_dn =  TFile('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/Mu_DY_'+var+"_BTagSFdown.root", "RECREATE")
# f_dn.cd()
# for hist in hist_dn_new:
#     hist.Write()
# f_dn.Close()

# f_up =  TFile('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/Mu_DY_'+var+"_BTagSFup.root", "RECREATE")
# f_up.cd()
# for hist in hist_up_new:
#     hist.Write()
# f_up.Close()  
