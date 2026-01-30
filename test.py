
from pdb_io import read_pdb

chains=read_pdb("6B1E.pdb")

for cid,chain in chains.items():
    print(chain)
    for res in chain.residues:
        print(" ",res)
        for atom in res.atoms:
            print("   ",atom)
