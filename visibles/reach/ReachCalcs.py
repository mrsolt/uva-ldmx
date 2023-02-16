import numpy as np

def N_ap(m, eps, eot):
    return 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_ap_eatvis(m, eps, eot):
    return 20 * 7. * pow(eps/1.e-5, 2) * pow(0.1/m, 2) * eot / 1.e16

def N_sig(Naprime, zmin, zmax, gctau):
    return Naprime * (np.exp(-zmin / gctau) - np.exp(-zmax / gctau))

def GammaCTau(E, m, eps):
    return 65. * (E/8.) * pow(1.e-5 / eps, 2) * pow(0.1/m, 2)

def MinSignal(b):
	return 14.

if (__name__ == '__main__'):
    print("Do Calculations")
