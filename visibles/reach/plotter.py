import array
import ROOT
from ROOT import gROOT, TFile, TTree, TChain, gDirectory, TLine, gStyle, TCanvas, TLegend, TH1, TH1F, TH2F, TF1, TLatex
import ReachCalcs as rc

def openPDF(outfile,canvas):
    canvas.Print(outfile+".pdf[")

def closePDF(outfile,canvas):
    canvas.Print(outfile+".pdf]")

def MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, zmin, zmax, ecal_eff, hcal_eff, eatvis = False, ecal = False, hcal = False, combo = False):
    Medges = array.array('d')
    Epsedges = array.array('d')
    for i in range(0,nMass+1):
        Medges.append(10**(massmin+(i-0.5)*(massmax-massmin)/float(nMass-1)))
    for j in range(0,NepsBins+1):
        Epsedges.append(10**(epsmin+(j-0.5)*(epsmax-epsmin)/float(NepsBins-1)))

    NAprime = TH2F("NAprime", "NAprime", nMass, Medges, NepsBins, Epsedges)
    GamCTau = TH2F("GamCTau", "GamCTau", nMass, Medges, NepsBins, Epsedges)
    detectable = TH2F("detectable", "detectable", nMass, Medges, NepsBins, Epsedges)

    full_detect = 0

    for i in range(0, nMass):
        logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
        mass = 10**logmass
        for j in range(0, NepsBins):
                logeps = (epsmax - epsmin)/float(NepsBins - 1) * j + epsmin
                eps = 10**logeps
                Naprime = 0
                if(not eatvis):
                    Naprime = rc.N_ap(mass, eps, eot)
                else:
                    Naprime = rc.N_ap_eatvis(mass, eps, eot)
                gctau = rc.GammaCTau(ebeam, mass, eps)
               

                if(ecal):
                    nsig = rc.N_sig(Naprime, zmin, zmax, gctau)
                    detectable.Fill(mass, eps, nsig*ecal_eff)

                elif(hcal):
                    nsig = rc.N_sig(Naprime, zmin, zmax, gctau)
                    detectable.Fill(mass, eps, nsig*hcal_eff)

                elif(combo):
                    nsig_ecal = rc.N_sig(Naprime, zmin, zmax, gctau)
                    nsig_hcal = rc.N_sig(Naprime, zmin, zmax, gctau)
                    ecal_detect = nsig_ecal*ecal_eff
                    hcal_detect = nsig_hcal*hcal_eff
                    full_detect = ecal_detect + hcal_detect    #combined detector efficiency, at each z position/mass/eps point
                    #print("The combined detector efficiency is ", full_detect)
                    detectable.Fill(mass, eps, full_detect)

                else:
                    print("No detector selected.")

                NAprime.Fill(mass, eps, Naprime)
                GamCTau.Fill(mass, eps, gctau)

    return NAprime, GamCTau, detectable

def SaveToPDF(NAprime, GamCTau, detectable, minSignal, ebeam, eot, outfile, nlevels = 1, label = ""):
    gStyle.SetOptStat(0)
    c = TCanvas("c","c",800,600)

    openPDF(outfile,c)
    c.SetLogx(1)
    c.SetLogy(1)
    c.SetLogz(1)
    NAprime.SetTitle("Number of A's Produced, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam, eot, label))
    NAprime.GetXaxis().SetTitle("mass [GeV]  ")
    NAprime.GetYaxis().SetTitle("#epsilon")
    NAprime.Draw("COLZ")
    c.Print(outfile+".pdf")

    GamCTau.SetTitle("Gamma CTau, {0:.0f} GeV Beam {1}".format(ebeam, label))
    GamCTau.GetXaxis().SetTitle("mass [GeV]  ")
    GamCTau.GetYaxis().SetTitle("#epsilon")
    GamCTau.Draw("COLZ")
    c.Print(outfile+".pdf")

    detectable.SetTitle("Number of Signal Events, {0:.0f} GeV Beam, {1} EOT {2}".format(ebeam, eot, label))
    detectable.GetXaxis().SetTitle("mass [GeV]  ")
    detectable.GetYaxis().SetTitle("#epsilon")
    detectable.Draw("COLZ")
    c.Print(outfile+".pdf")

    contour = array.array('d')
    contour.append(minSignal)
    detectable.SetContour(1, contour)
    detectable.SetLineColor(1)
    detectable.SetTitle("Contour for {0} Signal Events, {1:.0f} GeV Beam, {2} EOT {3}".format(minSignal, ebeam, eot, label))
    detectable.Draw("cont2")
    c.Print(outfile+".pdf")
    closePDF(outfile,c)

def MakePlots(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, ebeam, eot,  zmin, zmax, ecal_eff, hcal_eff, outfile, nlevels = 1, label = "", eatvis = False, ecal = False, hcal = False, combo = False):
	NAprime, GamCTau, detectable = MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, zmin, zmax, ecal_eff, hcal_eff, eatvis, ecal, hcal, combo)
	SaveToPDF(NAprime, GamCTau, detectable, minSignal, ebeam, eot, outfile, nlevels = 1, label = "")

if (__name__ == '__main__'):
    print("Making Histograms.")
