outfile = "output"

ebeam = 8. #GeV
zmin = 50. #cm
zmax = 500. #cm
e_zmin = 50. #cm
e_zmax = 70. #cm
h_zmin = 95. #cm
h_zmax = 500. #cm
eot = 1.e14
ecal_background = 32        #including intermediate region
hcal_background = 0.5
combined_background = 37

#12/2023 --> 26 Ecal/6 intermediate/5 Hcal

NepsBins = 1000
epsmin = -7 #logeps
epsmax = -2 #logeps

nMass = 1000
massmin = -3 #logmass GeV       #change to -3 if using fancy plot (-2 for regular)
massmax = 0 #logmass GeV


ecal_eff = 0.55      
hcal_eff = 0.6       


csvoutput = True      #default to True
plotoutput = False     #default to True
eps2 = True          #default to False, calculates eps^2 (True) or eps (False) values for CSV
eatvis = False        #default to False, Ecal as Target



########### set only one of these to True at a time ###########

Ecal = False          #default to False, select Ecal only parameters
Hcal = True          #default to False, select Hcal only parameters
Combined = False      #default to False, combine ecal/hcal parameters (distance, background, and efficiency)



#things that may be used in the future
mass_values = [0.01, 0.05] #GeV
