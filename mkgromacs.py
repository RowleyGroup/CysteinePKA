import os
import sys

#1000000 101.045 0 0 0 78.57 0 0 0 86.1366 0 0 0 -3.55744e-06 -3.55744e-06 -3.55744e-06 0 0 0
os.system('vmd -e ../mkgromacs.tcl -eofexit')

fh=open('namd/rest.xsc', 'r')
lines=fh.readlines()
#for l in lines:
#    if(l[0]=='#'):
#        continue
fields=lines[2].split()

x=float(fields[1])/10.0
y=float(fields[5])/10.0
z=float(fields[9])/10.0

os.system('gmx editconf -f gromacs/rest.gro -box ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' -o gromacs/rest.gro')

fh=open('namd/free.xsc', 'r')
lines=fh.readlines()
for l in lines:
    if(l[0]=='#'):
       	continue
    fields=l.split()

x=float(fields[1])/10.0
y=float(fields[5])/10.0
z=float(fields[9])/10.0

os.system('gmx editconf -f gromacs/free.gro -box ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' -o gromacs/free.gro')

#eq_npt2.xsc
