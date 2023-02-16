import csv

def OutputCSV(massmin, massmax, nMass, epsmin, epsmax, NepsBins, minSignal, detectable, outcsv):
    with open(outcsv, 'w') as f: # creates csv
            f = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            f.writerow(["Mass", "Epsilon"])
            for i in range(0, nMass):
                logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
                mass = 10**logmass
                edge = False
                for j in range(0, NepsBins):
                    logeps = (epsmax - epsmin)/float(NepsBins - 1) * j + epsmin
                    eps = 10**logeps
                    nsig = detectable.GetBinContent(i, j)
                    if(nsig >= minSignal and edge == False):
                        f.writerow([str(mass), str(eps)])
                        edge = True
            for i in reversed(range(0, nMass)):
                logmass = (massmax - massmin)/float(nMass - 1) * i + massmin
                mass = 10**logmass
                edge = False
                for j in reversed(range(0, NepsBins)):
                    logeps = (epsmax - epsmin)/float(NepsBins - 1) * j + epsmin
                    eps = 10**logeps
                    nsig = detectable.GetBinContent(i, j)
                    if(nsig >= minSignal and edge == False):
                        f.writerow([str(mass), str(eps)])
                        edge = True

if (__name__ == '__main__'):
    print("Outputing Contour to CSV.")
