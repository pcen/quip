import unittest

from quip.circuit import Circuit
from quip.quantum_system import QuantumSystem
from quip.gates.single_qubit import *


class HadamardCircuitTest(unittest.TestCase):

    def test_hadamard_circuit(self):
        c = Circuit(1)
        qs = QuantumSystem(1)
        c.put(0,1,hadamard())
        c.compile()
        c.run(qs)
        for p in qs.probabilities:
            self.assertTrue(0.4999 < p < 0.5001)
