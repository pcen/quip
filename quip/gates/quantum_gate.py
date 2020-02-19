import numpy as np

class QuantumGate:
    matrix = np.eye(1)
    width = 0
    symbol = ''

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.__str__()
