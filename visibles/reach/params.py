outfile = "output"

ebeam = 4. #GeV
zmin = 50. #cm
zmax = 500. #cm
e_zmin = 50. #cm
e_zmax = 70. #cm
h_zmin = 70. #cm
h_zmax = 500. #cm
eot = 4.e14
ecal_background = 5        #0, 2.5, 5
hcal_background = 15       #0, 5, 10, 15
combined_background = 15   #0, 5, 10, 15

#10/13/2023 --> 47 bkg in Hcal from Lincoln, ~ 10 (?) bkg in Ecal from Tyler

NepsBins = 1000
epsmin = -7 #logeps
epsmax = -2 #logeps

nMass = 1000
massmin = -2 #logmass GeV       #change to -3 if using fancy plot
massmax = 0 #logmass GeV


ecal_eff = 0.35       #based off of Tyler's most recent result (after all cuts)
hcal_eff = 0.3        #conservative guess, need input from Lincoln


csvoutput = True      #default to True
plotoutput = False     #default to True
eps2 = False          #default to False, calculates eps^2 (True) or eps (False) values for CSV
eatvis = False        #default to False, Ecal as Target



########### set only one of these to True at a time ###########

Ecal = False          #default to False, select Ecal only parameters
Hcal = False          #default to False, select Hcal only parameters
Combined = True      #default to False, combine ecal/hcal parameters (distance, background, and efficiency)



#things that may be used in the future
mass_values = [0.01, 0.05] #GeV
