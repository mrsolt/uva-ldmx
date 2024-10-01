import numpy as np
import sys
from scipy.stats import poisson

def N_ap(m, eps, eot):
    return 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_ap_eatvis(m, eps, eot):
    return 20 * 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_sig(Naprime, zmin, zmax, gctau):
    return Naprime * (np.exp(-zmin / gctau) - np.exp(-zmax / gctau))

def GammaCTau(E, m, eps):
    return 65. * (E/8.) * pow(1.e-5 / eps, 2) * pow(0.1/m, 2)

######### to calc. the expected signal, using CLs method, which according to Cam (SLAC) means we have to have 95% confidence level ##############
###############              CL_s(mu) = p_mu/(1-p_b)             #################

#originally written by Matt Solt
#def ExpectedEvents(b):
#    confidence_level = 0.95

#    k = 0.0

#    while True:
#        cdf = poisson.cdf(k,b)
#        print(cdf)
#        if (cdf >= confidence_level):
#            print(f"The expected number of observed events with at least {confidence_level*100}% CL is {k:.3f}")
#            break
        #else:
            #print("Not a high enough confidence level.")

#        k += 0.0125

#    return k


def MinSignal(b):                    #here b is expected background, set by the user in the params.py file
    confidence_level = 0.90            #want our exclusion at a 90% confidence level if using CLs, but able to be changed here

    S = 0.0                            #set upper limit of expected signal to start at 0


    while True:
        cdf = poisson.cdf(b, S+b)

        #Check if the CDF has reached (1 - confidence_level) --> 90% exclusion means CDF value (p-value) <= 0.1
        if cdf <= 0.5*(1 - confidence_level):         #p_b is .5 (50%) because we are using the mean value of our background distribution, cdf "side" is equal to right side of CL_s eqn, not left side! So you have to move the 0.5 in denom to the other side
            print(cdf)
            print(f"The upper limit on expected signal with {confidence_level*100}% CL_s is {S:.3f} for {b} background")
            break
        #else:
            #print(f"The CDF value is not less than or equal to {1-confidence_level:.2f}.")

        S += 0.0125                   #increment the upper limit of expected signal

    return S



#The table here is provided by S. Yellin from arXiv:physics/0203002v2
#It needs to be double checked if this is appropriate or not

#Changing to Table XII, 90% C.L. from Feldman and Cousins (arXiv:physics/9711021v2)
    
    #if(b > 15):
    #    print("Background levels not computed above 15 expected background events. Try again.")
    #    sys.exit(0)

    #n = [2.44, 2.86, 3.28, 3.62, 3.94, 4.20, 4.42, 4.63, 4.83, 5.18, 
    #     5.53, 5.90, 6.18, 6.49, 6.76, 7.02, 7.28, 7.51, 7.75, 7.99]

    #number of background events that match values in table above
    #xp = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 
    #      7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]

    #Previous table from S. Yellin    
    #n = [2.303, 3.890, 5.800, 7.491, 9.059, 10.548, 12.009, 13.433,
    #        14.824, 16.196, 17.540, 18.891, 20.208, 21.520, 22.821,
    #        24.119, 25.400, 26.669, 27.926, 29.197, 30.457, 31.690,
    #        32.972, 34.203, 35.422, 36.632, 37.849, 39.108, 40.333,
    #        41.546, 42.768, 43.978, 45.164, 46.351, 47.544, 48.734,
    #        49.944, 51.139, 52.314, 53.488]

    #s = np.interp(b, xp, n)
    #print("Contours made for an expected signal of {0}".format(s))
    #return s

if (__name__ == '__main__'):
    print("Do Calculations")
