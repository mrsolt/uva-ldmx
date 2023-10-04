outfile = "output"

ebeam = 4. #GeV
zmin = 50. #cm
zmax = 500. #cm
e_zmin = 50. #cm
e_zmax = 70. #cm
h_zmin = 70. #cm
h_zmax = 500. #cm
eot = 4.e14
ecal_background = 5
hcal_background = 10
combined_background = 15

NepsBins = 1000
epsmin = -7 #logeps
epsmax = -2 #logeps

nMass = 1000
massmin = -2 #logmass GeV
massmax = 0 #logmass GeV

csvoutput = True      #default to True
plotoutput = True    #default to True
eps2 = False           #default to False, sets whether or not we want eps^2
eatvis = False        #default to False

#set only one of these to True at a time
Ecal = False          #default to False, select Ecal only parameters
Hcal = False          #default to False, select Hcal only parameters
Combined = False      #default to False, combine ecal/hcal parameters (distance and background amounts)

eff_const = 0.5

#things that may be used in the future
subsys_eff = False
mass_values = [0.01, 0.05] #GeV
ecal_eff = [0.5, 0.5] #GeV
hcal_eff = [0.5, 0.5] #GeV
