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

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'h')
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

if(eps2):
    outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}hcalbkg_{6:.0f}eff_eps2".format(outfile, eot, ebeam, h_zmin, h_zmax, hcal_background, eff_const*100)
else:
    outbasename = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}-{4:.0f}cm_{5:.0f}hcalbkg_{6:.0f}eff".format(outfile, eot, ebeam, h_zmin, h_zmax, hcal_background, eff_const*100)

minSignal = rc.MinSignal(hcal_background)

if(plotoutput):
    outplot = outbasename
    p.MakePlots(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, ebeam, eot, e_zmin, e_zmax, eff_const, outplot, eatvis = eatvis)

if(csvoutput):
    _, _, detectable = p.MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, h_zmin, h_zmax, eff_const, eatvis = eatvis)
    outcsv = outbasename + ".csv"
    if(eps2):
        import ContourCSVeps2 as c
        c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)
    else:
        import ContourCSV as c
        c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)
