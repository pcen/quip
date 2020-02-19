import numpy as np
from quip.gates.quantum_gate import QuantumGate
from quip.math.common_values import i

# Single qubit quantum gates
class OneQubitGate(QuantumGate):
    width = 1

class identity(OneQubitGate):
    symbol = 'I'
    matrix = np.eye(2)

class pauli_x(OneQubitGate):
    symbol = 'X'
    matrix = np.array([
        [0, 1],
        [1, 0]
    ])

class hadamard(OneQubitGate):
    symbol = 'H'
    matrix = np.array([
        [1, 1],
        [1,-1]
    ]) * (1 / np.sqrt(2))

class pauli_y(OneQubitGate):
    symbol = 'Y'
    matrix = np.array([
        [0,-i],
        [i, 0]
    ])

class pauli_z(OneQubitGate):
    symbol = 'Z'
    matrix = np.array([
        [1, 0],
        [0,-1]
    ])

class phase_shift(OneQubitGate):
    symbol = 'S'
    def __init__(self, phi):
        self.matrix = np.array([
            [1, 0],
            [0, np.exp(i * phi)]
        ])

class not_a_gate(OneQubitGate):
    symbol = '|'
    matrix = None
