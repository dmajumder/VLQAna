#! /user/bin/env python

import sys
from ROOT import *
import math

gROOT.Macro("~/rootlogon.C")
gStyle.SetOptStat(0)

from optparse import OptionParser
parser = OptionParser()
parser.add_option('--ext', type='string', action='store', 
                  default='sys/muons/',
                  help='path from Macro to root files'
)
parser.add_option('--var', type='string', action='store',
                  default='st',
                  help='variable to plot',
)
(options, args) = parser.parse_args()
ext= options.ext
var = options.var

if 'muon' in ext:
    lep = 'mu'
elif 'electron' in ext:
    lep = 'el'

Path = '/uscms_data/d3/tmitchel/76X_test/CMSSW_7_6_5/src/Analysis/VLQAna/test/Macro/'
f_sys = TFile(Path+ext+var+'.root')

h_list_plus = []
h_list_minus = []
h_nom = f_sys.Get('di'+lep+'__Top').Clone()
h_top = f_sys.Get('di'+lep+'__Top').Clone()
h_dy = f_sys.Get('di'+lep+'__DY').Clone()
h_vv = f_sys.Get('di'+lep+'__VV').Clone()
h_nom.Add(h_dy)
h_nom.Add(h_vv)
h_top.Reset()
h_dy.Reset()
h_vv.Reset()
syst = [ '__bTag__', '__Jer__', '__Jec__', '__Pileup__']

for sy in syst:
    h_top.Reset()
    h_dy.Reset()
    h_vv.Reset()
    h_top = f_sys.Get('di'+lep+'__Top'+sy+'plus')
    h_vv = f_sys.Get('di'+lep+'__VV'+sy+'plus')
    h_dy = f_sys.Get('di'+lep+'__DY'+sy+'plus')
    h_tot_plus = h_top.Clone()
    h_tot_plus.Add(h_vv)
    h_tot_plus.Add(h_dy)
    h_list_plus.append(h_tot_plus)

for sy in syst:
    h_top.Reset()
    h_dy.Reset()
    h_vv.Reset()
    h_top = f_sys.Get('di'+lep+'__Top'+sy+'minus')
    h_vv = f_sys.Get('di'+lep+'__VV'+sy+'minus')
    h_dy = f_sys.Get('di'+lep+'__DY'+sy+'minus')
    h_tot_minus = h_top.Clone()
    h_tot_minus.Add(h_vv)
    h_tot_minus.Add(h_dy)
    h_list_minus.append(h_tot_minus)

for i in range(4):
    delta_accp_up  = ((h_nom.Integral()-h_list_plus[i].Integral())/h_nom.Integral())*100                                                                               
    delta_accp_dn  = ((h_nom.Integral()-h_list_minus[i].Integral())/h_nom.Integral())*100
    print '_____#Delta A; >=4j,>=1t_____'
    print 'Delta_A'+syst[i], 'up = {0:1.1f} % '.format(delta_accp_up)
    print 'Delta_A'+syst[i], 'down = {0:1.1f} % '.format(delta_accp_dn)
    print 'Ave = {0:1.1f} %'.format( (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2)
    #print 'Delta_A_'+syst[i]+'up = {0:3.1f} %, Delta_A_'+syst[i]+'down = {1:3.1f} %, Ave = {2:3.1f}%'.format(
        #delta_accp_up, delta_accp_dn, (math.fabs(delta_accp_up)+math.fabs(delta_accp_dn))/2) 



        

