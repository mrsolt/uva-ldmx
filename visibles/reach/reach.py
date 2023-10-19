import sys
tmpargv = sys.argv
sys.argv = []
import getopt
sys.argv = tmpargv
import plotter as p
import ReachCalcs as rc
import os
import importlib.util

def print_usage():
    print ("\nUsage: {0} <param file (default param.py)>".format(sys.argv[0]))
    print ('\t-h: this help message')

def load_module(file_name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'hcba:')
# Parse the command line arguments
for opt, arg in options:
    if opt=='-h':
        print_usage()
        sys.exit(0)

#paramfile = ""
try:
    paramfile = remainder[0]
except IndexError:
    paramfile = os.path.dirname(sys.argv[0]) + '/params.py'
    print("No parameter file specified, using default parameters")

print("Using file: {0}".format(paramfile))
print("")
f = open(paramfile, 'r')
file_contents = f.read()
print (file_contents)
f.close()

my_module = load_module(paramfile, "params")
from params import *

if(Ecal):
    if(eps2):
        outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}ecalbkg_{6:.0f}eff_eps2".format(outfile, eot, ebeam, e_zmin, e_zmax, ecal_background, ecal_eff*100)
    else:
        outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}ecalbkg_{6:.0f}eff".format(outfile, eot, ebeam, e_zmin, e_zmax, ecal_background, ecal_eff*100)

    minSignal = rc.MinSignal(ecal_background)

    if(plotoutput):
        outplot = outbasename
        p.MakePlots(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, ebeam, eot, zmin, zmax, ecal_eff, hcal_eff, outplot, eatvis = eatvis, ecal = Ecal, hcal = False, combo = False)

    if(csvoutput):
        _, _, detectable = p.MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, e_zmin, e_zmax, ecal_eff, hcal_eff, eatvis = eatvis, ecal = Ecal, hcal = Hcal, combo = Combined)
        outcsv = outbasename + ".csv"
        if(eps2):
            import ContourCSVeps2 as c
            c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)
        else:
            import ContourCSV as c
            c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)

elif(Hcal):
    if(eps2):
        outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}hcalbkg_{6:.0f}eff_eps2".format(outfile, eot, ebeam, h_zmin, h_zmax, hcal_background, hcal_eff*100)
    else:
        outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}hcalbkg_{6:.0f}eff".format(outfile, eot, ebeam, h_zmin, h_zmax, hcal_background, hcal_eff*100)

    minSignal = rc.MinSignal(hcal_background)

    if(plotoutput):
        outplot = outbasename
        p.MakePlots(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, ebeam, eot, zmin, zmax, ecal_eff, hcal_eff, outplot, eatvis = eatvis, ecal = False, hcal = Hcal, combo = False)

    if(csvoutput):
        _, _, detectable = p.MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, h_zmin, h_zmax, ecal_eff, hcal_eff, eatvis = eatvis, ecal = Ecal, hcal = Hcal, combo = Combined)
        outcsv = outbasename + ".csv"
        if(eps2):
            import ContourCSVeps2 as c
            c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)
        else:
            import ContourCSV as c
            c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)


elif(Combined):
    if(eps2):
        outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}combbkg_{6:.0f}ecaleff_{7:.0f}hcaleff_eps2".format(outfile, eot, ebeam, zmin, zmax, combined_background, ecal_eff*100, hcal_eff*100)
    else:
        outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}combbkg_{6:.0f}ecaleff_{7:.0f}hcaleff".format(outfile, eot, ebeam, zmin, zmax, combined_background, ecal_eff*100, hcal_eff*100)

    minSignal = rc.MinSignal(combined_background)

    if(plotoutput):
        outplot = outbasename
        p.MakePlots(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, ebeam, eot, zmin, zmax, ecal_eff, hcal_eff, outplot, eatvis = eatvis, ecal = False, hcal = False, combo = Combined)

    if(csvoutput):
        _, _, detectable = p.MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, zmin, zmax, ecal_eff, hcal_eff, eatvis = eatvis, ecal = False, hcal = False, combo = Combined)
        outcsv = outbasename + ".csv"
        if(eps2):
            import ContourCSVeps2 as c
            c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)
        else:
            import ContourCSV as c
            c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)


else:
    print("No detector or detector sub-system selected. See params.py to fix.")
    sys.exit(0)
