package require pbctools

mol new namd/protein_explicit.psf
mol addfile namd/rest.coor
pbc readxst namd/rest.xsc
mol addfile namd/free.coor
pbc readxst namd/free.xsc

animate goto 0
animate write gro gromacs/rest.gro
animate goto 1
animate write gro gromacs/free.gro

quit

