from gate_layout import GateLayout

class Circuit:
    gates = None
    compiled = None

    def __init__(self, width):
        self.gates = GateLayout(width)
    
    def put(self, y, x, gate):
        return self.gates.place(y, x, gate)
    
    def compile(self):
        self.compiled = self.gates.equivalent_matrix()
    
    def __str__(self):
        return str(self.gates)
    
    def __repr__(self):
        return self.__str__()
