import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import sys
tmpargv = sys.argv
sys.argv = []
import getopt
sys.argv = tmpargv

#List arguments
def print_usage():
    print ("\nUsage: {0} <csv file list> <labels list>".format(sys.argv[0]))
    print ('\t-t: plot title (default none)')
    print ('\t-e: use eps^2 (default False)')
    print ('\t-o: output file base name (default plot)')
    print ('\t-h: this help message')

title = ""
eps2 = False
output = "plot"

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'ht:eo:')

# Parse the command line arguments
for opt, arg in options:
    if opt=='-t':
        title = str(arg)
    if opt=='-o':
        output = str(arg)
    if opt=='-e':
        eps2 = True
    if opt=='-h':
        print_usage()
        sys.exit(0)

files = []
for i in range(int(len(remainder)/2)):
    files.append(str(remainder[i]))

labels = []
for i in range(int(len(remainder)/2), len(remainder)):
    labels.append(str(remainder[i]))

for i in range(len(files)):
    file = files[i]
    with open(file,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(csvfile)
        x = []
        y = []
        for row in lines:
            eps = float(row[1])
            if (eps2):
                eps = eps**2
            x.append(float(row[0]))
            y.append(eps)
    plt.plot(x, y, label = labels[i])
    del x, y

ylabel = "$\epsilon$"
if(eps2):
    ylabel = "$\epsilon^2$"
plt.xlabel('Mass [GeV]')
plt.ylabel(ylabel)
plt.xlim([0.01, 1])
plt.ylim([0.000001, 0.01])
if(eps2):
    plt.ylim([0.000001**2, 0.01**2])
plt.xscale('log')
plt.yscale('log')
plt.title(title)
plt.legend()
plt.savefig(output+'.pdf')
