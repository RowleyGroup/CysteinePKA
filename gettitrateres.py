import Bio.PDB
import sys

# read
parser = Bio.PDB.PDBParser(PERMISSIVE=1)
structure = parser.get_structure('MD_system', sys.argv[1])

model=structure[0]

for residue in model.get_residues():
    resname=residue.get_resname()
    resid=residue.id[1]
    if(resname[0]=='H' or resname=='GLU' or resname=='ASP'
       or resname=='CYS' or resname=='ARG' or resname=='LYS'
       or resname=='TYR'):
        print resname + str(resid)
        
        
    
