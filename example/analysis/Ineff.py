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
import numpy as np
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

#Output File
outfile = remainder[0]
outfileroot = TFile(remainder[0]+".root","RECREATE")

#Input File
infile = TFile(remainder[1])

histo = infile.Get("myana/myana_lambda")
nevents = histo.GetEntries()

h = TH1F("h", "h", histo.GetNbinsX(), histo.GetXaxis().GetBinLowEdge(1), histo.GetXaxis().GetBinUpEdge(histo.GetNbinsX()))

#Calculate the Inefficieny
for i in range(h.GetNbinsX()):
    n = histo.Integral(1,i)
    ineff = 1 - n / float(nevents)
    err = np.sqrt(nevents - n)/nevents #Need to double check if this is calculated correctly
    h.SetBinContent(i, ineff)
    h.SetBinError(i, err)

#Draw and Save the Histogram
openPDF(outfile,c)
h.GetYaxis().SetRangeUser(0.0000005, 1)
h.Draw()
h.SetTitle("Inefficiency For 1 GeV Neutrons {0}".format(label))
h.GetXaxis().SetTitle("#lambda")
h.GetYaxis().SetTitle("Inefficiency")
c.SetLogy(1)
c.Print(outfile+".pdf")

closePDF(outfile,c)
