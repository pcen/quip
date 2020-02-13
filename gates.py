import numpy as np

i = np.complex(0, 1)

class one_qubit_gate:
    matrix = np.eye(1)
    symbol = ''

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return self.__str__()

class identity(one_qubit_gate):
    symbol = 'I'
    matrix = np.eye(2)

class pauli_x(one_qubit_gate):
    symbol = 'X'
    matrix = np.matrix([
        [0, 1],
        [1, 0]
    ])

class hadamard(one_qubit_gate):
    symbol = 'H'
    matrix = np.matrix([
        [1, 1],
        [1,-1]
    ]) * (1 / np.sqrt(2))

class pauli_y(one_qubit_gate):
    symbol = 'Y'
    matrix = np.matrix([
        [0,-i],
        [i, 0]
    ])

class pauli_z(one_qubit_gate):
    symbol = 'Z'
    matrix = np.matrix([
        [1, 0],
        [0,-1]
    ])

class not_a_gate(one_qubit_gate):
    symbol = ' '
    matrix = None
