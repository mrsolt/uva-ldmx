from LDMX.Framework import ldmxcfg
from LDMX.SimCore import generators
from LDMX.SimCore import simulator
import sys

p=ldmxcfg.Process("egsim")
p.run = int(sys.argv[1])
sim = simulator.simulator( "neutron" )
sim.setDetector( "ldmx-det-v12" )
sim.runNumber = int(sys.argv[1])
sim.description = "Neutron fired from upstream of the HCal"

neutron_gun = generators.gun('neutron_gun')
neutron_gun.particle = 'neutron'
neutron_gun.energy = 1.0 # GeV
neutron_gun.position = [0., 0., 840.]
neutron_gun.direction = [0., 0., 1.]
sim.generators.append(neutron_gun)

import LDMX.Ecal.EcalGeometry
from LDMX.Hcal import hcal
p.sequence=[  
        sim, 
        hcal.HcalDigiProducer(),
        hcal.HcalVetoProcessor()
]

p.outputFiles=[sys.argv[2]]
p.maxEvents = 10000
p.logFrequency = 1
