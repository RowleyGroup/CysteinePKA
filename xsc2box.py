import os
import sys

#1000000 101.045 0 0 0 78.57 0 0 0 86.1366 0 0 0 -3.55744e-06 -3.55744e-06 -3.55744e-06 0 0 0

fh=open(sys.argv[1], 'r')
lines=fh.readlines()
for l in lines:
    if(l[0]=='#'):
        continue
    fields=l.split()

x=float(fields[1])/10.0
y=float(fields[5])/10.0
z=float(fields[9])/10.0

os.system('gmx editconf -f ' + sys.argv[2] + ' -box ' + str(x) + ' ' + str(y) + ' ' + str(z) + ' -o ' + sys.argv[2])
#eq_npt2.xsc
