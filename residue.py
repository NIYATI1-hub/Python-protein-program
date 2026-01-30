from atom import Atom
class Residue:
    def __init__(self,resname,resid,chain):
        self.resname=resname
        self.resid=resid
        self.chain=chain
        self.atoms=[]

    def add_atom(self,atom):
        self.atoms.append(atom)

    def __repr__(self):
        return f"<Residue {self.resname}{self.resid} Atoms={len(self.atoms)}>"

    

        