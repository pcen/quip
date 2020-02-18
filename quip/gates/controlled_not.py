import numpy as np
from quip.gates.quantum_gate import QuantumGate

def gen_matrix(width, control, target):
    n = width ** 2
    m = np.eye(n)
    for i in range(n):
        if i & (1 << control):
            print(i)

    return m


class CNOT(QuantumGate):
    pass
