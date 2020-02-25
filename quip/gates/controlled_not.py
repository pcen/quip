import numpy as np
from quip.gates.quantum_gate import QuantumGate


def gen_cnot_matrix(width, control, target):
    target_qb = (1 << (width - 1)) >> target
    control_qb = (1 << (width - 1)) >> control
    n = (2 ** width)
    matrix = np.zeros((n, n), dtype = int)
    # print(f'width: {width}\nn: {n}\nmatrix: {matrix}\n')
    for i in range(n):
        if i & control_qb:
            matrix.itemset((i, i ^ target_qb), 1)
        else:
            matrix.itemset((i, i), 1)
    return matrix


class CNOT(QuantumGate):

    width = 2
    symbol = 'CN'

    def __init__(self, control, target):
        self.width = abs(control - target) + 1
        if self.width <= 0 or control == target:
            print('invalid CNOT parameters')
        self.matrix = gen_cnot_matrix(self.width, control, target)
