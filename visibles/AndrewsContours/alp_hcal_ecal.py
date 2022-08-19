import numpy as np
import sys
import array
tmpargv = sys.argv
sys.argv = []
import getopt
import ROOT
from ROOT import gROOT, TFile, TTree, TChain, gDirectory, TLine, gStyle, TCanvas, TLegend, TH1, TH1F, TH2F, TF1, TLatex
sys.argv = tmpargv
dtype=np.float128

def openPDF(outfile,canvas):
	canvas.Print(outfile+".pdf[")

def closePDF(outfile,canvas):
	canvas.Print(outfile+".pdf]")

def N_alp(m, lam, eot, pdom=False):
        if(pdom): 
                return 90. * pow(1e4/lam, 2)
        else:
                return 8. * pow(100./lam, 2) * pow(0.1/m, 2)

def N_sig(Naprime, zmin, zmax, gctau):
    return Naprime * (np.exp(-zmin / gctau) - np.exp(-zmax / gctau))

def GammaCTau(E, m, lam, pdom=False):
        if(pdom):
                return 32. * (E/8) * pow(lam/(1e4), 2) * pow(0.1/m, 4)
        else:
                return 15. * (E/8) * pow(lam/(1e2), 2) * pow(0.1/m, 2)

label = ""
pdom = False

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'hl:p')

# Parse the command line arguments
for opt, arg in options:
		if opt=='-l':
			label = arg
		if opt=='-p':
			pdom = True
                        print("photon dominated")
		if opt=='-h':
			print_usage()
			sys.exit(0)

gStyle.SetOptStat(0)
c = TCanvas("c","c",800,600)

outfile = remainder[0]

ebeam = 4. #GeV
ebeam2 = 8.
zmin = 43. #cm
zmax = 315. #cm
eot = 1.e14
eot2 = 1.e16
minSignal = 14

NlamInvBins = 100
lamInvmin = -4 
lamInvmax = 0

nMass = 100
#massmin = 10
#massmax = 1000
massmin = -2
massmax = 0

if(pdom):
        lamInvmin = -5
        lamInvmax = -2

Medges = array.array('d')
LamInvedges = array.array('d')
for i in range(0,nMass+1):
    #Medges.append(massmin/1.e3+(i-0.5)*(massmax/1.e3-massmin/1.e3)/float(nMass-1))
    Medges.append(10**(massmin+(i-0.5)*(massmax-massmin)/float(nMass-1)))
for j in range(0,NlamInvBins+1):
	LamInvedges.append(10**(lamInvmin+(j-0.5)*(lamInvmax-lamInvmin)/float(NlamInvBins-1)))

NAlp = TH2F("NAlp", "NAlp", nMass, Medges, NlamInvBins, LamInvedges)
GamCTau = TH2F("GamCTau", "GamCTau", nMass, Medges, NlamInvBins, LamInvedges)
detectable = TH2F("detectable", "detectable", nMass, Medges, NlamInvBins, LamInvedges)
NAlp2 = TH2F("NAlp2", "NAlp2", nMass, Medges, NlamInvBins, LamInvedges)
GamCTau2 = TH2F("GamCTau2", "GamCTau2", nMass, Medges, NlamInvBins, LamInvedges)
detectable2 = TH2F("detectable2", "detectable2", nMass, Medges, NlamInvBins, LamInvedges)

for i in range(0, nMass):
    logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
    mass = 10**logmass
    for j in range(0, NlamInvBins):
        loglamInv = (lamInvmax - lamInvmin)/float(NlamInvBins - 1) * j + lamInvmin
        lamInv = 10**loglamInv
        lam = 1./lamInv
        Nalp = N_alp(mass, lam, eot, pdom)
        gctau = GammaCTau(ebeam, mass, lam)
        nsig = N_sig(Nalp, zmin, zmax, gctau)
        NAlp.Fill(mass, lamInv, Nalp)
        GamCTau.Fill(mass, lamInv, gctau)
        detectable.Fill(mass, lamInv, nsig)
        Nalp2 = N_alp(mass, lam, eot2, pdom)
        gctau2 = GammaCTau(ebeam2, mass, lam)
        nsig2 = N_sig(Nalp2, zmin, zmax, gctau2)
        NAlp2.Fill(mass, lamInv, Nalp2)
        GamCTau2.Fill(mass, lamInv, gctau2)
        detectable2.Fill(mass, lamInv, nsig2)

openPDF(outfile,c)
c.SetLogx(1)
c.SetLogy(1)
c.SetLogz(1)
NAlp.Draw("COLZ")
NAlp.SetTitle("Number of ALP's Produced, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam, eot, label))
NAlp.GetXaxis().SetTitle("mass [GeV]  ")
NAlp.GetYaxis().SetTitle("1/#Lambda")
c.Print(outfile+".pdf")
NAlp2.Draw("COLZ")
NAlp2.SetTitle("Number of ALP's Produced, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam2, eot2, label))
NAlp2.GetXaxis().SetTitle("mass [GeV]  ")
NAlp2.GetYaxis().SetTitle("1/#Lambda")
c.Print(outfile+".pdf")
GamCTau.Draw("COLZ")
GamCTau.SetTitle("Gamma CTau, {0:.0f} GeV Beam {1}".format(ebeam, label))
GamCTau.GetXaxis().SetTitle("mass [GeV]  ")
GamCTau.GetYaxis().SetTitle("1/#Lambda")
c.Print(outfile+".pdf")
GamCTau2.Draw("COLZ")
GamCTau2.SetTitle("Gamma CTau, {0:.0f} GeV Beam {1}".format(ebeam2, label))
GamCTau2.GetXaxis().SetTitle("mass [GeV]  ")
GamCTau2.GetYaxis().SetTitle("1/#Lambda")
c.Print(outfile+".pdf")
detectable.Draw("COLZ")
detectable.SetTitle("Number of Signal Events, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam, eot, label))
detectable.GetXaxis().SetTitle("mass [GeV]  ")
detectable.GetYaxis().SetTitle("1/#Lambda")
c.Print(outfile+".pdf")
detectable2.Draw("COLZ")
detectable2.SetTitle("Number of Signal Events, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam2, eot2, label))
detectable2.GetXaxis().SetTitle("mass [GeV]  ")
detectable2.GetYaxis().SetTitle("1/#Lambda")
c.Print(outfile+".pdf")

nlevels = 1
contour = array.array('d')
contour.append(minSignal)
detectable.SetContour(1, contour)
detectable.SetLineColor(1)
detectable.Draw("cont2")
detectable2.SetContour(1, contour)
detectable2.Draw("SAME cont2")
detectable.SetTitle("Contour for {0} Signal Events, {1:.0f} ({2:.0f}) GeV Beam, {3} ({4}) EOT {5}".format(minSignal, ebeam, ebeam2, eot, eot2, label))
detectable2.GetXaxis().SetTitle("mass [GeV]  ")
detectable2.GetYaxis().SetTitle("1/#Lambda")
legend = TLegend(0.6, 0.7, 0.9, 0.9)
legend.AddEntry(detectable, "{0:.0f} GeV, {1} EoT".format(ebeam, eot))
legend.AddEntry(detectable2, "{0:.0f} GeV, {1} EoT".format(ebeam2, eot2))
legend.Draw()
c.Print(outfile+".pdf")

closePDF(outfile,c)
