#!/bin/python

import os
import sys

from LDMX.Framework import ldmxcfg

# set a 'pass name'
# the other two pass name refers to that of the input files which will be combined in this job.

thisPassName="tskim"
inputPassName="v14"
nElectrons=1
p=ldmxcfg.Process( thisPassName )

#import all processors

# Ecal hardwired/geometry stuff
import LDMX.Ecal.EcalGeometry
import LDMX.Ecal.ecal_hardcoded_conditions
#Hcal hardwired/geometry stuff
from LDMX.Hcal import HcalGeometry
import LDMX.Hcal.hcal_hardcoded_conditions

from LDMX.Recon.electronCounter import ElectronCounter
from LDMX.Recon.simpleTrigger import simpleTrigger

#
# Set run parameters
#
p.inputFiles = [ sys.argv[2] ]
p.run = int(sys.argv[1])

# electron counter so simpletrigger doesn't crash
eCount = ElectronCounter( nElectrons, "ElectronCounter") # first argument is number of electrons in simulation
eCount.use_simulated_electron_number = True #False
eCount.input_pass_name=thisPassName

#trigger skim
simpleTrigger.start_layer= 0   #make sure it doesn't start from 1 (old default bug)
simpleTrigger.input_pass=inputPassName
p.skimDefaultIsDrop()
p.skimConsider("simpleTrigger")

p.sequence=[ eCount, simpleTrigger ]

p.outputFiles=[sys.argv[3]]

#p.termLogLevel = 0  # default is 2 (WARNING); but then logFrequency is ignored. level 1 = INFO.
#print this many events to stdout (independent on number of events, edge case: round-off effects when not divisible. so can go up by a factor 2 or so)
#p.logFrequency = 1000
