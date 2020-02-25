import numpy as np

class QuantumGate:
    matrix = np.eye(1)
    width = 0
    symbol = ''

    def __str__(self):
        s = ' ' + self.symbol
        while len(s) < 4:
            s += ' '
        return s

    def __repr__(self):
        return self.__str__()
