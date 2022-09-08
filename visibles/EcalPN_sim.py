#!/bin/python3

import os
import sys

from LDMX.Framework import ldmxcfg

# set a 'pass name'; avoid sim or reco(n) as they are apparently overused
p=ldmxcfg.Process("v12")

#import all processors
from LDMX.SimCore import generators
from LDMX.SimCore import simulator
from LDMX.SimCore import bias_operators
from LDMX.Biasing import filters
from LDMX.Biasing import util
from LDMX.Biasing import include as includeBiasing

# Ecal hardwired/geometry stuff
import LDMX.Ecal.EcalGeometry
import LDMX.Ecal.ecal_hardcoded_conditions

import LDMX.Hcal.HcalGeometry
import LDMX.Hcal.hcal_hardcoded_conditions

from LDMX.Ecal import digi
from LDMX.Ecal import vetos
from LDMX.Hcal import hcal
from LDMX.Hcal import digi as hdigi
from LDMX.Recon.simpleTrigger import simpleTrigger
from LDMX.TrigScint.trigScint import TrigScintDigiProducer

from LDMX.Detectors.makePath import *

from LDMX.SimCore import simcfg

#
# Instantiate the simulator.
#
sim = simulator.simulator("mySim")

#
# Set the path to the detector to use.
#
sim.setDetector( 'ldmx-det-v12', True  )
sim.scoringPlanes = makeScoringPlanesPath('ldmx-det-v12')

#
# Set run parameters
#
RUNNUMBER = int(sys.argv[1])
p.run = RUNNUMBER
sim.description = "ECal photo-nuclear, xsec bias 450"
sim.beamSpotSmear = [20., 80., 0]

#
# Fire an electron upstream of the tagger tracker
#
sim.generators = [ generators.single_4gev_e_upstream_tagger() ]


#
# Enable and configure the biasing
#
sim.biasing_operators = [ bias_operators.PhotoNuclear('old_ecal',450.,2500.,only_children_of_primary = True) ]

#
# Configure the sequence in which user actions should be called.
#

includeBiasing.library()

sim.actions = [ filters.TaggerVetoFilter(),
                                    filters.TargetBremFilter(),
                                    filters.EcalProcessFilter(),
                                    util.TrackProcessFilter.photo_nuclear()]

#findableTrack = ldmxcfg.Producer("findable", "ldmx::FindableTrackProcessor", "EventProc")
#trackerVeto = ldmxcfg.Producer("trackerVeto", "ldmx::TrackerVetoProcessor", "EventProc")


ecalDigi   =digi.EcalDigiProducer('EcalDigis')
ecalSim2Rec=digi.EcalRecProducer('ecalRecon')
ecalVeto   =vetos.EcalVetoProcessor('ecalVetoBDT')
hcalDigis  =hdigi.HcalDigiProducer('hcalDigis')
hcalRec  =hdigi.HcalRecProducer('hcalRecon')
hcalVeto   =hcal.HcalVetoProcessor('hcalVeto')

tsDigisTag  =TrigScintDigiProducer.tagger()
tsDigisUp  =TrigScintDigiProducer.up()
tsDigisDown  =TrigScintDigiProducer.down()

#p.sequence=[ sim, ecalDigi, ecalSim2Rec, ecalVeto, hcalDigis, hcalVeto, tsDigisTag, tsDigisUp, tsDigisDown, trackerHitKiller, simpleTrigger, findableTrack, trackerVeto ]
p.sequence=[ sim, ecalDigi, ecalSim2Rec, ecalVeto, hcalDigis, hcalRec, hcalVeto, tsDigisTag, tsDigisUp, tsDigisDown, simpleTrigger]#, findableTrack, trackerVeto ]

p.outputFiles= [sys.argv[2]]

p.maxEvents = 100000

p.logFrequency = 100
