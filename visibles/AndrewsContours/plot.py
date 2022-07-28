import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
  
x1 = []
y1 = []
with open('test_1e14eot_4gev.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in lines:
        x1.append(float(row[0]))
        y1.append(float(row[1]))
plt.plot(x1, y1, label = "1e14 eot, 4 GeV")

x2 = []
y2 = []
with open('test_1e16eot_8gev.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in lines:
        x2.append(float(row[0]))
        y2.append(float(row[1]))
plt.plot(x2, y2, label = "1e16 eot, 8 GeV")
  
plt.xlabel('Mass')
plt.ylabel('Epsilon')
plt.xlim([0.01, 1])
plt.ylim([0.0000001, 0.01])
plt.xscale('log')
plt.yscale('log')
plt.title('Replotted AP Contour')
plt.legend()
plt.savefig('plot.pdf')  
