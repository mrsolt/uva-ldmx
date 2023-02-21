import numpy as np
import sys

def N_ap(m, eps, eot):
    return 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_ap_eatvis(m, eps, eot):
    return 20 * 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_sig(Naprime, zmin, zmax, gctau):
    return Naprime * (np.exp(-zmin / gctau) - np.exp(-zmax / gctau))

def GammaCTau(E, m, eps):
    return 65. * (E/8.) * pow(1.e-5 / eps, 2) * pow(0.1/m, 2)

#The table here is provided by S. Yellin from arXiv:physics/0203002v2
#It needs to be double checked if this is appropriate or not
def MinSignal(b):
    if(b > 39):
        print("Background levels not computed above 39 expected background events. Try again.")
        sys.exit(0)
    n = [2.303, 3.890, 5.800, 7.491, 9.059, 10.548, 12.009, 13.433,
            14.824, 16.196, 17.540, 18.891, 20.208, 21.520, 22.821,
            24.119, 25.400, 26.669, 27.926, 29.197, 30.457, 31.690,
            32.972, 34.203, 35.422, 36.632, 37.849, 39.108, 40.333,
            41.546, 42.768, 43.978, 45.164, 46.351, 47.544, 48.734,
            49.944, 51.139, 52.314, 53.488]
    xp = []
    for i in range(len(n)):
        xp.append(i)
    s = np.interp(b, xp, n)
    print("Contours made for an expected signal of {0}".format(s))
    return s

if (__name__ == '__main__'):
    print("Do Calculations")
