class Atom:
    def __init__(self):
        self.name=None
        self.x=None
        self.y=None
        self.z=None
        self.resname=None
        self.resid=None
        self.chain=None

    def set_data(self,line):
        self.name=line[12:16].strip()
        self.x=float(line[30:38])
        self.y=float(line[38:46])
        self.z=float(line[46:54])
        self.resname=line[17:20].strip()
        self.resid=line[22:26].strip()
        self.chain=line[21]

    def __repr__(self):
        return f"<Atom {self.name} {self.resname}{self.resid} Chain {self.chain}>"
