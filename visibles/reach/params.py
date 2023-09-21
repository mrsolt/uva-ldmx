outfile = "output"

ebeam = 4. #GeV
#e_zmin = 50. #cm
#e_zmax = 70. #cm
h_zmin = 70. #cm
h_zmax = 500. #cm
eot = 4.e14
#ecal_background = 0
hcal_background = 10

NepsBins = 1000
#epsmin = -7 #logeps
#epsmax = -2 #logeps
epsmin = -11
epsmax = -4

nMass = 1000
massmin = -2 #logmass GeV
massmax = 0 #logmass GeV

csvoutput = True      #default to True
plotoutput = False    #default to True
eps2 = True           #default to False, sets whether or not we want eps^2
eatvis = False        #default to False

eff_const = 0.5
subsys_eff = False
mass_values = [0.01, 0.05] #GeV
ecal_eff = [0.5, 0.5] #GeV
hcal_eff = [0.5, 0.5] #GeV
