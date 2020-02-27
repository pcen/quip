import numpy as np
from quip.gates.quantum_gate import QuantumGate


def gen_cnot_matrix(width, control, target):
    msb = (1 << (width - 1))
    target_qb = msb >> target
    control_qb = msb >> control
    n = 2 ** width
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        if i & control_qb:
            matrix.itemset((i, i ^ target_qb), 1)
        else:
            matrix.itemset((i, i), 1)
    return matrix

class CNOT(QuantumGate):

    symbol = 'CX'

    def __init__(self, control, target):
        self.width = abs(control - target) + 1
        if self.width < 2 or control == target:
            print('invalid CNOT parameters')
        self.matrix = gen_cnot_matrix(self.width, control, target)


def gen_toffoli_matrix(width, c1, c2, target):
    msb = (1 << (width - 1))
    target_qb = msb >> target
    c1_qb = msb >> c1
    c2_qb = msb >> c2
    n = 2 ** width
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        if i & c1_qb and i & c2_qb:
            matrix.itemset((i, i ^ target_qb), 1)
        else:
            matrix.itemset((i, i), 1)
    return matrix

class toffoli(QuantumGate):

    symbol = 'CCX'

    def __init__(self, c1, c2, target):
        self.width = max(c1, c2, target) - min(c1, c2, target) + 1
        if self.width < 3 or c1 == target or c2 == target:
            print('invalid toffoli parameters')
        self.matrix = gen_toffoli_matrix(self.width, c1, c2, target)


def gen_fredkin_matrix(width, control, t1, t2):
    msb = (1 << (width - 1))
    t1_qb = msb >> t1
    t2_qb = msb >> t2
    control_qb = msb >> control
    n = 2 ** width
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        if i & control_qb and bool(i & t1_qb) ^ bool(i & t2_qb):
            matrix.itemset((i, i ^ (t1_qb | t2_qb)), 1)
        else:
            matrix.itemset((i, i), 1)
    return matrix

class fredkin(QuantumGate):

    symbol = 'F'

    def __init__(self, control, t1, t2):
        self.width = max(t1, t2, control) - min(t1, t2, control) + 1
        if self.width < 3 or control in (t1, t2) or t1 == t2:
            print(f'invalid Fredkin parameters')
        self.matrix = gen_fredkin_matrix(self.width, control, t1, t2)
