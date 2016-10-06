#! /usr/bin/env python
import math

optEffPoint = TGraph()
optSigPoint = TGraph()
effGraph = [TGraph(), TGraph(), TGraph(), TGraph(), TGraph(), TGraph()]
optGraph = [TGraph(), TGraph(), TGraph(), TGraph(), TGraph(), TGraph()]
#effGraph = []
#optGraph = []
effMultiGraph = TMultiGraph()
optMultiGraph = TMultiGraph()
effMultiGraph.SetTitle("efficiency;"+ var+"; eff")
optMultiGraph.SetTitle("significance;"+var+"; S/ #sqrt{B}")
Nbins = templates[0].GetNbinsX()
sOverb = 0
igraph=0
optsOverb = 0
optEff = 0
optVal = 0
optBin = 0

leg_eff = TLegend(0.65,0.8,0.99,1.00)
#Ysize = max(4, last-1)
# Ysize = max(4, 8)
# leg_eff.SetY1(1-0.05*Ysize)
leg_eff.SetBorderSize(1)
leg_eff.SetFillColor(10)

bkg_hist = templates[0].Clone()
bkg_hist.Reset()

#stack all backgrounds
for idist in templates[0:3] :
#	print "histo here", idist.legentry
	bkg_hist.Add(idist)
        
for idist in templates[3:]:
        # print "histo here for eff", idist.legentry
	# print 'bin & \%dec in eff & \frac{S}{\sqrt{B}}\\\ '
	# print 'QCD', templates[1].hist.Integral()
	for ibin in range(Nbins):
		mybin = ibin+1
		top=bkg_hist.Integral(mybin, Nbins)
		sig = idist.Integral(mybin, Nbins)
		#top = bkg_hist.Integral(1, mybin)
		#sig = idist.Integral(1, mybin)
		eff = sig/idist.Integral(1, Nbins)
		eff_bkg = top/idist.Integral(1, Nbins)
		xAxis = idist.GetBinCenter(mybin)
		#print 'eff = {0:<5.3f}, xAxis = {1:<5.1f}'.format(eff, xAxis)	
		effGraph[igraph].SetPoint(ibin, xAxis, eff)	
		if math.sqrt(top)!=0:
			#if idist.hist.Integral(1, mybin) !=0:
			#sOverb = sig/math.sqrt(top+sig)
			sOverb = eff/(1 + math.sqrt(top))
			print '>{0:<5.1f} & {1:<5.1f} & {2:<5.2f}\\\ '.format((xAxis-5), (1-eff)*100, sOverb)
			#optGraph[igraph].SetPoint(ibin, xAxis, sOverb)
			optGraph[igraph].SetPoint(ibin, xAxis, sOverb)
			if sOverb > optsOverb:
				optsOverb = sOverb
				optVal = xAxis
				optEff = eff
				optBin = ibin
				
	print '_______'
	print 'optsoverb = {0:<5.1f}, optVal = {1:<5.1f}, opteff = {2:<5.1f}'.format(
		optsOverb, optVal, optEff
		)
	optEffPoint.SetPoint(optBin, optVal, optEff)
	optSigPoint.SetPoint(optBin, optVal, optsOverb)
	effGraph[igraph].SetLineColor(igraph+2)
        effGraph[igraph].SetMarkerColor(igraph+2)
	effMultiGraph.Add(effGraph[igraph])
	optGraph[igraph].SetLineColor(igraph+2)
	optGraph[igraph].SetMarkerColor(igraph+2)
	optMultiGraph.Add(optGraph[igraph])
	leg_eff.AddEntry(effGraph[igraph], idist.GetName(),'l')
	print 'igraph', igraph
	igraph = igraph + 1

# draw
c1 = TCanvas('c1', 'c1')
c1.SetGrid()
effMultiGraph.Draw("ALP*")
leg_eff.Draw()
c1.SaveAs(plotDir+var+"_eff.gif")
c1.SaveAs(plotDir+var+"_eff.pdf")

c2 = TCanvas('c2', 'c2')
c2.SetGrid()
optMultiGraph.Draw("ALP*")
leg_eff.Draw()


c2.SaveAs(plotDir+var+"_opt.gif")
c2.SaveAs(plotDir+var+"_opt.pdf")
