import numpy as np

class GateLayout:
    grid = None
    width = 0
    length = 0

    def __init__(self, width):
        self.width = width
        self.length = 1
    
    def place(self, y, x, gate):
        return True
    
    def equivalent_matrix(self):
        return np.eye(1)
    
    def __str__(self):
        return ''
    
    def __repr_(self):
        return self.__str__()
