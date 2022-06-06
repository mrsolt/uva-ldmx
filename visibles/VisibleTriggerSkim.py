#!/usr/bin/python

import sys
import os
import json

# we need the ldmx configuration package to construct the object

from LDMX.Framework import ldmxcfg

# first, we define the process, which must have a name which identifies this
# processing pass ("pass name").
# the other two pass names refer to those of the input files which will be combined in this job.
thisPassName="v3.0.0" #overlay"
simPassName="v12"
nElectrons=1
p=ldmxcfg.Process( thisPassName )

#import all processors

# Ecal hardwired/geometry stuff
from LDMX.Ecal import EcalGeometry
import LDMX.Ecal.ecal_hardcoded_conditions
egeom = EcalGeometry.EcalGeometryProvider.getInstance()

from LDMX.Ecal import digi as eDigi
from LDMX.Ecal import vetos

from LDMX.Recon.electronCounter import ElectronCounter
from LDMX.Recon.simpleTrigger import simpleTrigger

RUNNUMBER = int(sys.argv[1])
INPUTNAME = sys.argv[3]
p.run = RUNNUMBER
p.inputFiles =[ INPUTNAME ]

#and Ecal
ecalReDigi   =eDigi.EcalDigiProducer('ecalReDigi')
ecalReReco   =eDigi.EcalRecProducer('ecalReRecon')
ecalRerecoVeto   =vetos.EcalVetoProcessor('ecalVetoRerecoBDT')

#here the pass name is extremely important
ecalReDigi.inputPassName  = simPassName #start from old sim
ecalReReco.simHitPassName  = simPassName #rereco on this digi pass
ecalReReco.digiPassName = thisPassName
ecalRerecoVeto.rec_pass_name = thisPassName

# electron counter so simpletrigger doesn't crash
eCount = ElectronCounter( nElectrons, "ElectronCounter") # first argument is number of electrons in simulation
eCount.use_simulated_electron_number = True #False
eCount.input_pass_name=thisPassName

#trigger skim
simpleTrigger.start_layer= 0   #make sure it doesn't start from 1 (old default bug)
simpleTrigger.end_layer= 20
simpleTrigger.input_pass=thisPassName
p.skimDefaultIsDrop()
p.skimConsider("simpleTrigger")

p.sequence = [ecalReDigi, ecalReReco, eCount, simpleTrigger]

p.outputFiles= [sys.argv[2]]

#drop some scoring plane hits to make space, and old ecal digi+reco; only the veto and trigger results remain from the pure PN hits. also, keep sim hits for now, to be able to rerun reco/overlay if needed.
p.keep = ["drop EcalDigis_v12", "drop trigScintDigisTag_"+simPassName, "drop trigScintDigisUp_"+simPassName, "drop trigScintDigisDn_"+simPassName, "drop TriggerPadTaggerClusters_"+simPassName, "drop TriggerPadUpClusters_"+simPassName, "drop TriggerPadDownClusters_"+simPassName]

p.termLogLevel = 0  # default is 2 (WARNING); but then logFrequency is ignored. level 1 = INFO.
#print this many events to stdout (independent on number of events, edge case: round-off effects when not divisible. so can go up by a factor 2 or so)
logEvents=20
if p.maxEvents < logEvents :
     logEvents = p.maxEvents
p.logFrequency = int( p.maxEvents/logEvents )

# if it's not set, it's because we're doing pileup, right, and expect on order 10k events per job
if not p.maxEvents:
     p.logFrequency = 1000
