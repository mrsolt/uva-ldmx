#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:59:09 2020

@author: matthewsolt
"""

import sys
tmpargv = sys.argv
sys.argv = []
import getopt
import ROOT
from ROOT import gROOT, TFile, TTree, TChain, gDirectory, TLine, gStyle, TCanvas, TLegend, TH1F, TLatex
sys.argv = tmpargv

#List arguments
def print_usage():
    print ("\nUsage: {0} <output file base name> <input file>".format(sys.argv[0]))
    print ('\t-l: plot label')
    print ('\t-h: this help message')
    print

label = ""

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'hl:')

# Parse the command line arguments
for opt, arg in options:
    if opt=='-l':
        label = str(arg)
    if opt=='-h':
        print_usage()
        sys.exit(0)
            
def openPDF(outfile,canvas):
	canvas.Print(outfile+".pdf[")

def closePDF(outfile,canvas):
	canvas.Print(outfile+".pdf]")

gStyle.SetOptStat(0)
c = TCanvas("c","c",800,600)

outfile = remainder[0]
outfileroot = TFile(remainder[0]+".root","RECREATE")

infile = TFile(remainder[1])
infile2 = TFile(remainder[2])
infile3 = TFile(remainder[3])

histo = infile.Get("myana/myana_lambda_min")
nevents = histo.GetEntries()

histo2 = infile2.Get("myana/myana_lambda_min")
nevents2 = histo2.GetEntries()

histo3 = infile3.Get("myana/myana_lambda_min")
nevents3 = histo3.GetEntries()

h = TH1F("h", "h", histo.GetNbinsX(), histo.GetXaxis().GetBinLowEdge(1), histo.GetXaxis().GetBinUpEdge(histo.GetNbinsX()))
h2 = TH1F("h2", "h2", histo2.GetNbinsX(), histo2.GetXaxis().GetBinLowEdge(1), histo2.GetXaxis().GetBinUpEdge(histo2.GetNbinsX()))
h3 = TH1F("h3", "h3", histo3.GetNbinsX(), histo3.GetXaxis().GetBinLowEdge(1), histo3.GetXaxis().GetBinUpEdge(histo3.GetNbinsX()))

for i in range(h.GetNbinsX()):
    n = histo.Integral(1,i)
    ineff = 1 - n / float(nevents)
    h.SetBinContent(i, ineff)
    
for i in range(h2.GetNbinsX()):
    n = histo2.Integral(1,i)
    ineff = 1 - n / float(nevents2)
    h2.SetBinContent(i, ineff)
    
for i in range(h3.GetNbinsX()):
    n = histo3.Integral(1,i)
    ineff = 1 - n / float(nevents3)
    h3.SetBinContent(i, ineff)
    
histo4 = infile.Get("myana/myana_lambda_max")
nevents4 = histo4.GetEntries()

histo5 = infile2.Get("myana/myana_lambda_max")
nevents5 = histo5.GetEntries()

histo6 = infile3.Get("myana/myana_lambda_max")
nevents6 = histo6.GetEntries()

h4 = TH1F("h4", "h4", histo4.GetNbinsX(), histo4.GetXaxis().GetBinLowEdge(1), histo4.GetXaxis().GetBinUpEdge(histo4.GetNbinsX()))
h5 = TH1F("h5", "h5", histo5.GetNbinsX(), histo5.GetXaxis().GetBinLowEdge(1), histo5.GetXaxis().GetBinUpEdge(histo5.GetNbinsX()))
h6 = TH1F("h6", "h6", histo6.GetNbinsX(), histo6.GetXaxis().GetBinLowEdge(1), histo6.GetXaxis().GetBinUpEdge(histo6.GetNbinsX()))

for i in range(h4.GetNbinsX()):
    n = histo4.Integral(1,i)
    ineff = 1 - n / float(nevents4)
    h4.SetBinContent(i, ineff)
    
for i in range(h5.GetNbinsX()):
    n = histo5.Integral(1,i)
    ineff = 1 - n / float(nevents5)
    h5.SetBinContent(i, ineff)
    
for i in range(h6.GetNbinsX()):
    n = histo6.Integral(1,i)
    ineff = 1 - n / float(nevents6)
    h6.SetBinContent(i, ineff)
    
openPDF(outfile,c)
h.SetLineColor(1)
h2.SetLineColor(2)
h3.SetLineColor(4)
h.Draw()
h.SetTitle("Inefficiency at Min Z {0}".format(label))
h.GetXaxis().SetTitle("#lambda")
h.GetYaxis().SetTitle("Inefficiency")
h2.Draw("same")
h3.Draw("same")
legend = TLegend(.58,.66,.92,.87)
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.035)
legend.AddEntry(h,"10.2","LP")
legend.AddEntry(h2,"10.3","LP")
legend.AddEntry(h3,"10.5","LP")
legend.Draw()
c.SetLogy(1)
c.Print(outfile+".pdf")

h4.SetLineColor(1)
h5.SetLineColor(2)
h6.SetLineColor(4)
h4.Draw()
h4.SetTitle("Inefficiency at Max Z {0}".format(label))
h4.GetXaxis().SetTitle("#lambda")
h4.GetYaxis().SetTitle("Inefficiency")
h5.Draw("same")
h6.Draw("same")
legend.Draw()
c.Print(outfile+".pdf")

closePDF(outfile,c)
