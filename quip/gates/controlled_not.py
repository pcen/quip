import numpy as np
from quip.gates.quantum_gate import QuantumGate

def b(val, len):
    return format(val, f'0{len - 1}b')

def gen_matrix(width, control, target):
    print((1 << (width - 1)))
    target_qb = (1 << (width - 1)) >> target
    control_qb = (1 << (width - 1)) >> control

    n = width ** 2
    m = np.eye(n)
    swaps = [(i, i ^ target_qb) for i in range(n) if i & control_qb]
    print(swaps)

    return m


class CNOT(QuantumGate):

    symbol = 'C'

    def __init__(self, control, target):
        width = max(control, target) + 1
        if width <= 0 or control == target:
            del self
        matrix = gen_matrix(width, control, target)
