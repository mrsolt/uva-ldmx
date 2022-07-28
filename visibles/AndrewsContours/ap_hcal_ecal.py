import numpy as np
import sys
import array
tmpargv = sys.argv
sys.argv = []
import getopt
import ROOT
from ROOT import gROOT, TFile, TTree, TChain, gDirectory, TLine, gStyle, TCanvas, TLegend, TH1, TH1F, TH2F, TF1, TLatex
import csv
sys.argv = tmpargv
dtype=np.float128

def openPDF(outfile,canvas):
	canvas.Print(outfile+".pdf[")

def closePDF(outfile,canvas):
	canvas.Print(outfile+".pdf]")

def N_ap(m, eps, eot, eatvis=False):
	if(not eatvis):
		return 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16
	else:
		return 20 * 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_sig(Naprime, zmin, zmax, gctau):
    return Naprime * (np.exp(-zmin / gctau) - np.exp(-zmax / gctau))

def GammaCTau(E, m, eps):
    return 65. * (E/8.) * pow(1.e-5 / eps, 2) * pow(0.1/m, 2)

label = ""
eatvis = False

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'hl:e')

# Parse the command line arguments
for opt, arg in options:
		if opt=='-l':
			label = arg
		if opt=='-e':
                        print("beam dump")
			eatvis = True
		if opt=='-h':
			print_usage()
			sys.exit(0)

gStyle.SetOptStat(0)
c = TCanvas("c","c",800,600)

outfile = remainder[0]

ebeam = 4. #GeV
ebeam2 = 8.
zmin = 500. #cm
zmax = 1000000. #cm
eot = 1.e14
eot2 = 1.e16
minSignal = 14

NepsBins = 1000
epsmin = -7
epsmax = -2

nMass = 1000
#massmin = 10
#massmax = 1000
massmin = -2
massmax = 0

Medges = array.array('d')
Epsedges = array.array('d')
for i in range(0,nMass+1):
    #Medges.append(massmin/1.e3+(i-0.5)*(massmax/1.e3-massmin/1.e3)/float(nMass-1))
    Medges.append(10**(massmin+(i-0.5)*(massmax-massmin)/float(nMass-1)))
for j in range(0,NepsBins+1):
	Epsedges.append(10**(epsmin+(j-0.5)*(epsmax-epsmin)/float(NepsBins-1)))

NAprime = TH2F("NAprime", "NAprime", nMass, Medges, NepsBins, Epsedges)
GamCTau = TH2F("GamCTau", "GamCTau", nMass, Medges, NepsBins, Epsedges)
detectable = TH2F("detectable", "detectable", nMass, Medges, NepsBins, Epsedges)
NAprime2 = TH2F("NAprime2", "NAprime2", nMass, Medges, NepsBins, Epsedges)
GamCTau2 = TH2F("GamCTau2", "GamCTau2", nMass, Medges, NepsBins, Epsedges)
detectable2 = TH2F("detectable2", "detectable2", nMass, Medges, NepsBins, Epsedges)

for i in range(0, nMass):
        logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
        mass = 10**logmass
        for j in range(0, NepsBins):
                logeps = (epsmax - epsmin)/float(NepsBins - 1) * j + epsmin
                eps = 10**logeps
                Naprime = N_ap(mass, eps, eot, eatvis)
                gctau = GammaCTau(ebeam, mass, eps)
                nsig = N_sig(Naprime, zmin, zmax, gctau)
                NAprime.Fill(mass, eps, Naprime)
                GamCTau.Fill(mass, eps, gctau)
                detectable.Fill(mass, eps, nsig)
                Naprime2 = N_ap(mass, eps, eot2, eatvis)
                gctau2 = GammaCTau(ebeam2, mass, eps)
                nsig2 = N_sig(Naprime2, zmin, zmax, gctau2)
                NAprime2.Fill(mass, eps, Naprime2)
                GamCTau2.Fill(mass, eps, gctau2)
                detectable2.Fill(mass, eps, nsig2)


with open(outfile+'_1e14eot_4gev.csv', 'w') as f1: # creates csv
        f1_write = csv.writer(f1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        f1_write.writerow(["Mass", "Epsilon"])
        with open(outfile+'_1e16eot_8gev.csv', 'w') as f2:
                f2_write = csv.writer(f2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                f2_write.writerow(["Mass", "Epsilon"])
                for i in range(0, nMass):
                        logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
                        mass = 10**logmass
                        edge1 = False
                        edge2 = False
                        for j in range(0, NepsBins):
                                logeps = (epsmax - epsmin)/float(NepsBins - 1) * j + epsmin
                                eps = 10**logeps
                                nsig = detectable.GetBinContent(i, j)
                                nsig2 = detectable2.GetBinContent(i, j)
                                if(nsig >= minSignal and edge1 == False):
                                        f1_write.writerow([str(mass), str(eps)])
                                        edge1 = True
                                if(nsig2 >= minSignal and edge2 == False):
                                        f2_write.writerow([str(mass), str(eps)])
                                        edge2 = True
                for i in reversed(range(0, nMass)):
                        logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
                        mass = 10**logmass
                        edge1 = False
                        edge2 = False
                        for j in reversed(range(0, NepsBins)):
                                logeps = (epsmax - epsmin)/float(NepsBins - 1) * j + epsmin
                                eps = 10**logeps
                                nsig = detectable.GetBinContent(i, j)
                                nsig2 = detectable2.GetBinContent(i, j)
                                if(nsig >= minSignal and edge1 == False):
                                        f1_write.writerow([str(mass), str(eps)])
                                        edge1 = True
                                if(nsig2 >= minSignal and edge2 == False):
                                        f2_write.writerow([str(mass), str(eps)])
                                        edge2 = True

openPDF(outfile,c)
c.SetLogx(1)
c.SetLogy(1)
c.SetLogz(1)
NAprime.Draw("COLZ")
NAprime.SetTitle("Number of A's Produced, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam, eot, label))
NAprime.GetXaxis().SetTitle("mass [GeV]  ")
NAprime.GetYaxis().SetTitle("#epsilon")
c.Print(outfile+".pdf")
NAprime2.Draw("COLZ")
NAprime2.SetTitle("Number of A's Produced, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam2, eot2, label))
NAprime2.GetXaxis().SetTitle("mass [GeV]  ")
NAprime2.GetYaxis().SetTitle("#epsilon")
c.Print(outfile+".pdf")
GamCTau.Draw("COLZ")
GamCTau.SetTitle("Gamma CTau, {0:.0f} GeV Beam {1}".format(ebeam, label))
GamCTau.GetXaxis().SetTitle("mass [GeV]  ")
GamCTau.GetYaxis().SetTitle("#epsilon")
c.Print(outfile+".pdf")
GamCTau2.Draw("COLZ")
GamCTau2.SetTitle("Gamma CTau, {0:.0f} GeV Beam {1}".format(ebeam2, label))
GamCTau2.GetXaxis().SetTitle("mass [GeV]  ")
GamCTau2.GetYaxis().SetTitle("#epsilon")
c.Print(outfile+".pdf")
detectable.Draw("COLZ")
detectable.SetTitle("Number of Signal Events, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam, eot, label))
detectable.GetXaxis().SetTitle("mass [GeV]  ")
detectable.GetYaxis().SetTitle("#epsilon")
c.Print(outfile+".pdf")
detectable2.Draw("COLZ")
detectable2.SetTitle("Number of Signal Events, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam2, eot2, label))
detectable2.GetXaxis().SetTitle("mass [GeV]  ")
detectable2.GetYaxis().SetTitle("#epsilon")
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
detectable2.GetYaxis().SetTitle("#epsilon")
legend = TLegend(0.6, 0.7, 0.9, 0.9)
legend.AddEntry(detectable, "{0:.0f} GeV, {1} EoT".format(ebeam, eot))
legend.AddEntry(detectable2, "{0:.0f} GeV, {1} EoT".format(ebeam2, eot2))
legend.Draw()
c.Print(outfile+".pdf")
closePDF(outfile,c)
