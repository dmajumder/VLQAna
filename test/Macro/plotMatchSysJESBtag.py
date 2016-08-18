#! /usr/bin/env python

# Import everything from ROOT
import sys
from ROOT import *
import math
#from setTDRStyle import *
#setTDRStyle()
gROOT.Macro("~/rootlogon.C")
gStyle.SetOptStat(0)
#gStyle.SetTitleFillColor(10)
#gStyle.SetTitleBorderSize(0)
#gStyle.SetOptStat(000000)
# =============== 
# options
# ===============
from optparse import OptionParser
parser = OptionParser()	  				  				  					  			  					  				  
parser.add_option('--var', metavar='T', type='string', action='store',
                  default='ht',
                  dest='var',
                  help='variable to plot')
parser.add_option('--runEle', action='store_true',
                  default=False,
                  help='run on electron selections')
(options,args) = parser.parse_args()
# ==========end: options =============
var = options.var
runEle = options.runEle

if runEle:
        Path  ='/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/Systematics/muons/'
        title = "#it{e + jets}"
	dist = 'ele'
else:
        #Path  ='/home/tmitchell/Documents/Systematics/muons'
	Path='/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/Systematics/muons/'
        title = "#it{#el +jets}"
	dist = 'el'

f_nom       = TFile(Path+'ana_'+var+'.root')
f_Pup     =  TFile(Path+'anaPileupUp_'+var+'.root')
f_Pdn     = TFile(Path+'anaPileupDown_'+var+'.root')
f_JECup   = TFile(Path+'anaJecUp_'+var+'.root')
f_JECdn   = TFile(Path+'anaJecDown_'+var+'.root')
f_JERup   = TFile(Path+'anaJerUp_'+var+'.root')
f_JERdn   = TFile(Path+'anaJerDown_'+var+'.root')
# f_BTagSFup   = TFile(Path+'anabcUp_'+var+'.root')
# f_BTagSFdn   = TFile(Path+'anabcDown_'+var+'.root')
#f_lTagSFup   = TFile(Path+'analightUp_'+var+'.root')
#f_lTagSFdn = TFile(Path+'analightDown_'+var+'.root')

leg = TLegend(0.60, 0.60, 0.88, 0.88)
leg.SetBorderSize(0)
leg.SetFillColor(0)

leg2 = TLegend(0.60, 0.60, 0.88, 0.88)
leg2.SetBorderSize(0)
leg2.SetFillColor(0)

leg3 = TLegend(0.60, 0.60, 0.88, 0.88)
leg3.SetBorderSize(0)
leg3.SetFillColor(0)

leg4 = TLegend(0.60, 0.60, 0.88, 0.88)
leg4.SetBorderSize(0)
leg4.SetFillColor(0)

leg5 = TLegend(0.60, 0.60, 0.88, 0.88)
leg5.SetBorderSize(0)
leg5.SetFillColor(0)

#h_data_nom = f_nom.Get(var) 
h_nom = f_nom.Get(var)
h_Pup = f_Pup.Get(var)
h_Pdn = f_Pdn.Get(var)
#h_lTagSFup = f_lTagSFup.Get(var)
#h_lTagSFdn = f_lTagSFdn.Get(var)
h_JECup = f_JECup.Get(var)
h_JECdn = f_JECdn.Get(var)
h_JERup = f_JERup.Get(var)
h_JERdn = f_JERdn.Get(var)
h_BTagSFup = f_BTagSFup.Get(var)
h_BTagSFdn = f_BTagSFdn.Get(var)

htitle = ''
if var == 'njets':
    htitle = 'N_{jets}'
elif var == 'ht':
    htitle = 'H_{T} (GeV)' 

h_Pup.SetTitle("Pileup, "+title+";"+htitle) 
h_Pdn.SetTitle("Pileup, "+title+";"+htitle)
#h_lTagSFup.SetTitle("lightTagSF, "+title+";"+htitle)
#h_lTagSFdn.SetTitle("lightTagSF, "+title+";"+htitle)
h_JECup.SetTitle("JEC, "+title+";"+htitle)
h_JECdn.SetTitle("JEC, "+title+";"+htitle)
h_JERup.SetTitle("JER, "+title+";"+htitle)
h_JERdn.SetTitle("JER, "+title+";"+htitle)
h_BTagSFup.SetTitle("BTagSF, "+title+";"+htitle)
h_BTagSFdn.SetTitle("BTagSF, "+title+";"+htitle)

###style
#h_data_nom.SetMarkerStyle(8)
h_nom.SetLineColor(2)
h_Pup.SetLineColor(4)
#h_lTagSFup.SetLineColor(4)
h_JERup.SetLineColor(4)
h_JECup.SetLineColor(4)
h_BTagSFup.SetLineColor(4)
h_Pdn.SetLineColor(8)
#h_lTagSFdn.SetLineColor(8)
h_JECdn.SetLineColor(8)
h_JERdn.SetLineColor(8)
h_BTagSFdn.SetLineColor(8)
h_nom.SetLineWidth(2)
h_Pup.SetLineWidth(2)
h_Pdn.SetLineWidth(2)
#h_lTagSFup.SetLineWidth(2)
#h_lTagSFdn.SetLineWidth(2)
h_JECup.SetLineWidth(2)
h_JECdn.SetLineWidth(2)
h_JERup.SetLineWidth(2)
h_JERdn.SetLineWidth(2)
h_BTagSFup.SetLineWidth(2)
h_BTagSFdn.SetLineWidth(2)

c1 = TCanvas('c1', 'c1', 600, 600)

#leg.AddEntry(h_data_nom, 'Data', 'p')
leg.AddEntry(h_nom, 'default', 'l')
leg.AddEntry(h_JECup, 'JEC up', 'l')
leg.AddEntry(h_JECdn, 'JEC down', 'l')

#h_data_nom.SetTitle("JES, "+title+";"+htitle)
h_nom.SetTitle("JES, "+title+";"+htitle)
#h_data_nom.Draw('hist,e')
h_JECup.Draw('hist')
h_nom.Draw('hist same')
h_JECdn.Draw('hist same')
h_JECup.Draw('hist same')
    
leg.Draw()

delta_accp_up  = ((h_nom.Integral()-h_JERup.Integral())/h_nom.Integral())*100
delta_accp_dn  = ((h_nom.Integral()-h_JERdn.Integral())/h_nom.Integral())*100
print '_____#Delta A; >=4j,>=1t_____'
print 'Delta_A_JERup = {0:3.1f} %, Delta_A_JERdn = {1:3.1f} %, Ave = {2:3.1f}%'.format(
    delta_accp_up, delta_accp_dn, (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2)

#c1.Print('/Users/skhalil/Desktop/FigAN/sys_JES_'+var+'_'+dist+'.gif', 'gif')
c1.Print('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/JEC_'+var+'_'+dist+'.pdf', 'pdf')
c1.SaveAs('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/JEC_'+var+'_'+dist+'.root')

###========
c2 = TCanvas('c2', 'c2', 600, 600)

#leg2.AddEntry(h_data_nom, 'Data', 'p')
leg2.AddEntry(h_nom, 'default', 'l')
leg2.AddEntry(h_BTagSFup, 'BTagSF up', 'l')
leg2.AddEntry(h_BTagSFdn, 'BTagSF down', 'l')

#h_data_nom.SetTitle("BTagSF, "+title+";"+htitle)
h_nom.SetTitle("BTagSF, "+title+";"+htitle)
#h_data_nom.Draw('hist,e')
h_BTagSFdn.Draw('hist')
h_nom.Draw('hist same')
h_BTagSFup.Draw('hist same')   

leg2.Draw()

delta_accp_up  = ((h_nom.Integral()-h_BTagSFup.Integral())/h_nom.Integral())*100
delta_accp_dn  = ((h_nom.Integral()-h_BTagSFdn.Integral())/h_nom.Integral())*100
print '_____#Delta A; >=4j,>=1t_____'
print 'Delta_A_BTagSFup = {0:3.1f} %, Delta_A_BTagSFdn = {1:3.1f} %, Ave = {2:3.1f}%'.format(
    delta_accp_up, delta_accp_dn, (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2)

#c2.Print('/Users/skhalil/Desktop/FigAN/sys_btag_'+var+'_'+dist+'.gif', 'gif')
c2.Print('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/btag_'+var+'_'+dist+'.pdf', 'pdf')
c2.SaveAs('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/btag_'+var+'_'+dist+'.root')

#================
c3 = TCanvas('c3', 'c3', 600, 600)

#leg3.AddEntry(h_data_nom, 'Data', 'p')
leg3.AddEntry(h_nom, 'default', 'l')
leg3.AddEntry(h_JERdn, 'JER down', 'l')
leg3.AddEntry(h_JERup, 'JER up', 'l')

#h_data_nom.SetTitle("JER, "+title+";"+htitle)
h_nom.SetTitle("JER, "+title+";"+htitle)
#h_data_nom.Draw('hist,e')
h_JERdn.Draw('hist')
h_nom.Draw('hist same')
h_JERup.Draw('hist same')

leg3.Draw()

delta_accp_up  = ((h_nom.Integral()-h_JERup.Integral())/h_nom.Integral())*100
delta_accp_dn  = ((h_nom.Integral()-h_JERdn.Integral())/h_nom.Integral())*100
print '_____#Delta A; >=4j,>=1t_____'
print 'Delta_A_JERup = {0:3.1f} %, Delta_A_JERdn = {1:3.1f} %, Ave = {2:3.1f}%'.format(
    delta_accp_up, delta_accp_dn, (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2)

#c3.Print('/Users/skhalil/Desktop/FigAN/sys_JER_'+var+'_'+dist+'.gif', 'gif')
c3.Print('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/JER_'+var+'_'+dist+'.pdf', 'pdf')
c3.SaveAs('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/JER_'+var+'_'+dist+'.root')

c4 = TCanvas('c4', 'c4', 600, 600)

#leg4.AddEntry(h_data_nom, 'Data', 'p')
leg4.AddEntry(h_nom, 'default', 'l')
leg4.AddEntry(h_Pup, 'PU up', 'l')
leg4.AddEntry(h_Pdn, 'PU down', 'l')

#h_data_nom.SetTitle("PU, "+title+";"+htitle)
h_nom.SetTitle("PU, "+title+";"+htitle)
#h_data_nom.Draw('hist,e')
h_Pdn.Draw('hist')
h_nom.Draw('hist same')
h_Pup.Draw('hist same')

leg4.Draw()

delta_accp_up  = ((h_nom.Integral()-h_Pup.Integral())/h_nom.Integral())*100
delta_accp_dn  = ((h_nom.Integral()-h_Pdn.Integral())/h_nom.Integral())*100
print '_____#Delta A; >=4j,>=1t_____'
print 'Delta_A_PUup = {0:3.1f} %, Delta_A_PUdn = {1:3.1f} %, Ave = {2:3.1f}%'.format(
    delta_accp_up, delta_accp_dn, (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2)

#c4.Print('/Users/skhalil/Desktop/FigAN/sys_PU_'+var+'_'+dist+'.gif', 'gif')
c4.Print('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/PU_'+var+'_'+dist+'.pdf', 'pdf')
c4.SaveAs('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/PU_'+var+'_'+dist+'.root')

# c5 = TCanvas('c5', 'c5', 600, 600)

# #leg5.AddEntry(h_data_nom, 'Data', 'p')
# leg5.AddEntry(h_nom, 'default', 'l')
# leg5.AddEntry(h_Pup, 'lightTagSF up', 'l')
# leg5.AddEntry(h_Pdn, 'lightTagSF down', 'l')

# #h_data_nom.SetTitle("lightTagSF, "+title+";"+htitle)
# h_nom.SetTitle("lightTagSF, "+title+";"+htitle)
# #h_data_nom.Draw('hist,e')
# h_lTagSFdn.Draw('hist ')
# h_nom.Draw('hist same')
# h_lTagSFup.Draw('hist same')

# leg5.Draw()

# delta_accp_up  = ((h_nom.Integral()-h_lTagSFup.Integral())/h_nom.Integral())*100
# delta_accp_dn  = ((h_nom.Integral()-h_lTagSFdn.Integral())/h_nom.Integral())*100
# print '_____#Delta A; >=4j,>=1t_____'
# print 'Delta_A_lTagup = {0:3.1f} %, Delta_A_lTagdn = {1:3.1f} %, Ave = {2:3.1f}%'.format(
#     delta_accp_up, delta_accp_dn, (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2)

# #c5.Print('/Users/skhalil/Desktop/FigAN/sys_VTagSF_'+var+'_'+dist+'.gif', 'gif')
# c5.Print('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/lTagSF_'+var+'_'+dist+'.pdf', 'pdf')
# c5.SaveAs('/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/lTagSF_'+var+'_'+dist+'.root')

raw_input("hold on")

