
from atom import Atom
from residue import Residue
from chain import Chain

def read_pdb(filename):
    chains={}
    current_residue=None

    with open(filename) as f:
        for line in f:
            if line.startswith(("ATOM","HETATM")):
                atom=Atom()
                atom.set_data(line)

                if atom.chain not in chains:
                    chains[atom.chain]=Chain(atom.chain)

                chain=chains[atom.chain]

                if (current_residue is None or
                    current_residue.resid!=atom.resid or
                    current_residue.chain!=atom.chain):

                    residue=Residue(atom.resname,atom.resid,atom.chain)
                    chain.add_residue(residue)
                    current_residue=residue

                current_residue.add_atom(atom)

    return chains


        