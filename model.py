import re
class Model:
    def __init__(self):
        self.id= 1
    def set_data(self,line):
        if line.startswith("Model"):
            self.id= int(re.split(r'\s+', line)[1])

    def __repr__(self):
        return f"<Mod