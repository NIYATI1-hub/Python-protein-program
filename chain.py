
class Chain:
    def __init__(self,chain_id):
        self.chain_id=chain_id
        self.residues=[]

    def add_residue(self,residue):
        self.residues.append(residue)

    def __repr__(self):
        return f"<Chain {self.chain_id} Residues={len(self.residues)}>"


