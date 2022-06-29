import numpy as np
import os
import decimal
import re
import sys
import array
tmpargv = sys.argv
sys.argv = []
sys.argv = tmpargv
import getopt

#List arguments
def print_usage():
    print ('\nOptions')
    print ('\t-a: beam energy (default 4 GeV)')
    print ('\t-l: input LHE file')
    print ('\t-o: output directory')
    print ('\t-n: output files base name')
    print ('\t-e: epsilon (default 1e-5)')
    print ('\t-m: A prime mass in GeV (default 0.050 GeV)')
    print ('\t-y: minimum z value for decay in mm (default 0 mm)')
    print ('\t-z: maximum z value for decay in mm (default 7000 mm)')
    print ('\t-u: uniform decay (default False)')
    print ('\t-h: this help message')

def Rfunc(s):
    if np.sqrt(s) >= 0.36:
        return Rvals_interp(np.sqrt(s))
    else:
        return 0.

def gamma_ap_to_ll(mAp,ml,eps):
    if mAp < 2.*ml:
        return 0.

    aEM=1/137.035999679

    beta=1. - (2*ml/mAp)**2

    return (1./3.)*(aEM*eps**2)*mAp*np.sqrt(beta)*(1 + (2*ml**2)/mAp**2)

# Total decay rate of Ap into electrons and muons and hadrons
# Valid for mAp > 2*me
# Width is returned in GeV
def gamma_ap_tot(mAp, epsilon):
    me = 0.51099895/1000.
    mmu = 105.6583745/1000.
    return gamma_ap_to_ll(mAp,me,epsilon) \
            + gamma_ap_to_ll(mAp,mmu,epsilon)*(1. + Rfunc(mAp**2))

def numsInLine(line_w_nums):

    """ Find numbers in line """

    nums =  re.findall(r' [\d,\.,e,\-,\+]+', line_w_nums) # Seems close enough

    return [ num[1:] for num in nums ]

def rescaleLine(line_w_nums, scale=decimal.Decimal('0.1'), tokens=[0]):

    """ Replace numbers at given tokens (indicies) with scaled versions """

    numbers = numsInLine(line_w_nums)
    #print(numbers)
    numbers = [ numbers[i] for i in tokens ] # Get numbers at desired indicies
    scaled_line = line_w_nums

    for number in numbers:
        scaled_line = re.sub(re.sub(r'\+', r'\\+', number), # looks like - equiv not needed
                            str(decimal.Decimal(number)*scale), scaled_line,
                            count=1)

    return scaled_line

def replaceNums(line_w_nums, tokens, new_vals):

    """ Replace numbers at given tokens (indicies) with specific new_vals """

    numbers = numsInLine(line_w_nums)
    numbers = [ numbers[i] for i in tokens ]# Numbers we care about
    new_line = line_w_nums

    for number, new_val in zip(numbers,new_vals):
        new_line = re.sub(number, str(new_val), new_line, count=1)

    return new_line

def Tau(mAp, epsilon):

    """ Lifetime of A' """

    return hbar / gamma_ap_tot(mAp, epsilon)
    #return 8.e-2 * (1.e-8 / epsilon**2) * (0.1 / mAp) / c

lhe = ""
mAp = 0.05 # GeV
eps = 1.e-5
zmin = 0.
zmax = 7000.
hbar = 6.582e-25 # GeV*s
c_speed = 299792458000. # mm/s
uniform = False
energy = 4.0 # beam energy GeV

outdir = ""
outname = ""

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'ha:l:o:n:e:m:y:z:u')

# Parse the command line arguments
for opt, arg in options:
    if opt=='-a':
        energy = float(arg)
    if opt=='-l':
        lhe = str(arg)
    if opt=='-o':
        outdir = str(arg)
    if opt=='-n':
        outname = str(arg)
    if opt=='-e':
        eps = float(arg)
    if opt=='-m':
        mAp = float(arg) #GeV
    if opt=='-y':
        zmin = float(arg)
    if opt=='-z':
        zmax = float(arg)
    if opt=='-u':
        uniform = True
    if opt=='-h':
        print_usage()
        sys.exit(0)

decay_width = gamma_ap_tot(mAp, eps)
tau = Tau(mAp, eps)

tmin = zmin / c_speed / (energy / mAp)
tmax = zmax / c_speed / (energy / mAp)
print("{0} {1}".format(tmin, tmax))
# Create outdir if needed
if not os.path.exists(outdir): os.makedirs(outdir)

# Outfile names
bremfile = f'{outdir}/{outname}_brem.lhe'
decayfile = f'{outdir}/{outname}_decay.lhe'
decay_vs = f'{outdir}/{outname}_decay.dat'
print( f'Reformatting:\n{lhe}\nInto:\n{bremfile}\n{decayfile}')
print( f'And verticies to:\n{decay_vs}')
nevents_used = 0

with open(lhe, 'r') as ogfile, open(bremfile, 'w') as bremf, open(decayfile, 'w') as decayf, open(decay_vs, 'w') as decayvs:
    # Write lims to .dat (plus extra 0s to maintain array shape)
    decayvs.write( f'{zmin} {zmax} 0 0\n' )
    scaling_mass = False
    for line in ogfile:
        #print(line)
        # ebeams
        if re.search(r'ebeam',line):
            line = rescaleLine(line)
        # Masses
        if line[:10] == 'BLOCK MASS':
            scaling_mass = True # Indicate following lines should be scaled
            continue
        if line[0] == '#':
            scaling_mass = False
        if scaling_mass:
            line = rescaleLine(line, tokens=[1])

        # Decay Width
        if re.match(r'DECAY +622', line):
            line = replaceNums(line, [1], [decay_width])

        # Break from header/init
        if line == '</init>\n':
            bremf.write(line)
            decayf.write(line)
            break

        bremf.write(line)
        decayf.write(line)

    ##################################################
    # Edit events
    ##################################################
    event_num = 0
    event_line = 0
    current_line = 0
    for line in ogfile: # Picks up where last loop leaves off
        current_line += 1

        # Scale relevant lines
        if line == '<event>\n':
            event_num += 1
            event_line = 0
            event_brem_lines = []
            event_decay_lines = ['<event>\n']

            if event_num % 1000 == 0:
                print( 'Reformatting event: {}'.format(event_num) )

        else: event_line += 1
        if 1 < event_line < 9:
            line = rescaleLine(line, tokens=range(6,11))

        # Event info line
        if event_line ==1:
            # Correct particle number
            event_brem_lines.append(replaceNums(line, [0], [5]))
            event_decay_lines.append(replaceNums(line, [0], [2]))

        elif event_line < 7: # If first 5 write to bremfile
            event_brem_lines.append(line)

            if event_line == 6: # Take note of Ap info for projection
                px,py,pz = [float(v) for v in numsInLine(line)[6:9]]
                Ap_3mom = np.array((px,py,pz))

        elif event_line < 9: # decay electrons
            event_decay_lines.append( replaceNums(line, [2,3], [-1,-1]) )

        # Skip mgrwt. add appropriate vertex, and end event
        elif event_line == 16 :
            t = 0.
            if(uniform):
                t = np.random.uniform(tmin, tmax)
            else:
                t = np.random.exponential(tau)
            x,y,z,t = 0., 0., 0., t
            c_vertex = np.array((x,y,z))
            d_vertex = c_vertex + Ap_3mom * c_speed / mAp * t

            # If not in allowed z, don't write event
            if not (zmin < d_vertex[2] < zmax):
                continue
            nevents_used += 1 # Else, count event as used

            # If it is allowed, catch up the writing
            for ln in event_brem_lines: bremf.write(ln)
            for ln in event_decay_lines: decayf.write(ln)

            # Then add the verticies
            bremf.write( '#vertex {} {} {}\n'.format(x,y,z) )
            decayf.write( '#vertex {} {} {} {}\n'.format(*d_vertex,t) )
            decayvs.write( '{} {} {} {}\n'.format(*d_vertex,t) )

            # And end event
            bremf.write(line)
            decayf.write(line)

        # End both
        elif line == '</LesHouchesEvents>\n':
            bremf.write(line)
            decayf.write(line)

print(f'Using {nevents_used} events')
