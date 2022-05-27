from LDMX.Framework import ldmxcfg
from LDMX.SimCore import simulator
import sys

#Example command:
#ldmx fire ap_producer.py <run number> <dark brem file> <ap decay file> <output file>

proc = 'v12'
p = ldmxcfg.Process(proc)
p.outputFiles = [sys.argv[4]]
p.maxEvents = 32000
p.logFrequency = 1
p.termLogLevel = 0
p.run = int(sys.argv[1])

sim = simulator.simulator('visible_signal')
sim.description = "A' -> ee visible signal decay"
sim.setDetector('ldmx-det-v12',True)
sim.runNumber = int(sys.argv[1])

# Generators
from LDMX.SimCore import generators
dark_brem_file = sys.argv[2]
ap_decay_file = sys.argv[3]
dark_brem = generators.lhe('dark_brem', dark_brem_file)
ap_decay  = generators.lhe('ap_decay' , ap_decay_file)
sim.generators = [ dark_brem, ap_decay ]

# Producers
from LDMX.Ecal import EcalGeometry
from LDMX.Hcal import HcalGeometry
import LDMX.Ecal.ecal_hardcoded_conditions as ecal_conditions
import LDMX.Hcal.hcal_hardcoded_conditions as hcal_conditions
import LDMX.Ecal.digi as ecal_digi
import LDMX.Ecal.vetos as ecal_vetos
import LDMX.Hcal.hcal as hcal_py
import LDMX.Hcal.digi as hcal_digi
from LDMX.Recon.simpleTrigger import simpleTrigger

p.sequence=[
        sim,
        ecal_digi.EcalDigiProducer(),
        ecal_digi.EcalRecProducer(),
        ecal_vetos.EcalVetoProcessor(),
        hcal_digi.HcalDigiProducer(),
        hcal_digi.HcalRecProducer(),
        hcal_py.HcalVetoProcessor(),
        ]
