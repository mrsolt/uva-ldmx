import sys
tmpargv = sys.argv
sys.argv = []
import getopt
sys.argv = tmpargv
import plotter as p
import ReachCalcs as rc
import os
import importlib.util

def load_module(file_name, module_name):
    spec = importlib.util.spec_from_file_location(module_name, file_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

options, remainder = getopt.gnu_getopt(sys.argv[1:], '')
paramfile = remainder[0]
my_module = load_module(paramfile, "params")
from params import *

minSignal = rc.MinSignal(background)

if(plotoutput):
    p.MakePlots(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, ebeam, eot, zmin, zmax, eff_const, outfile, eatvis = eatvis)

if(csvoutput):
    _, _, detectable = p.MakeHistos(massmin, massmax, nMass, epsmin, epsmax, NepsBins, ebeam, eot, zmin, zmax, eff_const, eatvis = eatvis)
    outcsv = "{0}_{1:.0e}eot_{2:.0f}gev_{3:.0f}to{4:.0f}cm.csv".format(outfile, eot, ebeam, zmin, zmax)
    import ContourCSV as c
    c.OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv)
