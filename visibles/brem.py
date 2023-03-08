from LDMX.SimCore import simulator
from LDMX.SimCore import generators
from LDMX.SimCore import bias_operators
from LDMX.Biasing import filters
from LDMX.Biasing import util
#from LDMX.Biasing import include as includeBiasing

from LDMX.Framework import ldmxcfg
import sys

p = ldmxcfg.Process('v14')
p.outputFiles = [sys.argv[2]]
p.maxEvents = 100000 #int(sys.argv[5])
#p.logFrequency = 1
p.termLogLevel = 0
p.run = int(sys.argv[1])

sim = simulator.simulator("target-brem")

# Set the path to the detector to use.
#   the second parameter says we want to include scoring planes
sim.setDetector( "ldmx-det-v14" , True )

# Set run parameters
sim.description = "Target Brem"
sim.beamSpotSmear = [20., 80., 0.] #mm

generator = generators.single_4gev_e_upstream_target()

sim.generators.append( generator )

# Enable and configure the biasing
#sim.biasing_operators = [ bias_operators.PhotoNuclear('ecal',450.,2500.,only_children_of_primary = True) ]

# the following filters are in a library that needs to be included
#includeBiasing.library()

# Configure the sequence in which user actions should be called.
sim.actions.extend([
        #filters.TaggerVetoFilter(),
        # Only consider events where a hard brem occurs
        filters.TargetBremFilter(),
        # Only consider events where a PN reaction happnes in the ECal
        #filters.EcalProcessFilter(),
        # Tag all photo-nuclear tracks to persist them to the event.
        #util.TrackProcessFilter.photo_nuclear()
        util.DecayChildrenKeeper([22])
])

from LDMX.Ecal import EcalGeometry
from LDMX.Hcal import HcalGeometry
import LDMX.Ecal.ecal_hardcoded_conditions as ecal_conditions
import LDMX.Hcal.hcal_hardcoded_conditions as hcal_conditions
import LDMX.Ecal.digi as ecal_digi
import LDMX.Ecal.vetos as ecal_vetos
import LDMX.Hcal.hcal as hcal_py
import LDMX.Hcal.digi as hcal_digi
#from LDMX.Recon.simpleTrigger import simpleTrigger

p.sequence=[
        sim,
        ecal_digi.EcalDigiProducer(),
        ecal_digi.EcalRecProducer(),
        ecal_vetos.EcalVetoProcessor(),
        hcal_digi.HcalDigiProducer(),
        hcal_digi.HcalRecProducer(),
        hcal_py.HcalVetoProcessor(),
        ]
