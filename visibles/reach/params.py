outfile = "output"

ebeam = 4. #GeV
#zmin = 50. #cm  --> these are general parameters. Need to specify ecal/hcal
#zmax = 500. #cm
e_zmin = 23.
e_zmax = 70.
#h_zmin = 70.
#h_zmax = 500.
eot = 4.e14
ecal_background = 0
#hcal_background = 10

NepsBins = 1000
epsmin = -7 #logeps
epsmax = -2 #logeps

nMass = 1000
massmin = -2 #logmass GeV
massmax = 0 #logmass GeV

csvoutput = True
plotoutput = True
eatvis = False

eff_const = 0.5
subsys_eff = False
mass_values = [0.01, 0.05] #GeV
ecal_eff = [0.5, 0.5] #GeV
hcal_eff = [0.5, 0.5] #GeV
ecal_range = [23., 70.] #cm
hcal_range = [70., 500.] #cm
