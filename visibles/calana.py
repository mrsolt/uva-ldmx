
from LDMX.Framework import ldmxcfg

p=ldmxcfg.Process('ana')

# Create an instance of the HCal veto analyzer. This analyzer is used to create
# an ntuple and plots with results from the neutron gun.
from LDMX.Analysis import CalAnalyzer
calana = CalAnalyzer.CalAnalyzer("myana")

# Define the order in which the analyzers will be executed.
p.sequence=[calana]

# input the file as an argument on the command line
import sys
p.inputFiles=[sys.argv[2]]

# Specify the output file.  When creating ntuples or saving histograms, the
# output file name is specified by setting the attribute histogramFile.
p.histogramFile=sys.argv[1]
