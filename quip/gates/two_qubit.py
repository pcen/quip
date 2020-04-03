import numpy as np
from quip.gates.quantum_gate import QuantumGate
from quip.math.common_values import i

def gen_cu_matrix(target, gate):
    matrix = np.eye(4)
    if target == 0:
        matrix[0:2,0:2] = gate.matrix
    elif target == 1:
        matrix[2:4,2:4] = gate.matrix
    return matrix

class controlled_U(QuantumGate):
    width = 2
    symbol = 'CU'
    def __init__(self, control, target, gate):
        if control | target != 1:
            print('invalid controled-U parameters')
        if gate.width != 1:
            print(f'invalid controlled gate: {gate.symbol}')
        self.matrix = gen_cu_matrix(target, gate)

class swap(QuantumGate):
    width = 2
    symbol = 'SW'
    matrix = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])

class sqrt_swap(QuantumGate):
    width = 2
    symbol = 'SSW'
    matrix = np.array([
        [1,             0,             0, 0],
        [0, 0.5 * (1 + i), 0.5 * (1 - i), 0],
        [0, 0.5 * (1 - i), 0.5 * (1 + i), 0],
        [0,             0,             0, 1]
    ])
