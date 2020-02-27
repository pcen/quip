import unittest

from quip.circuit import Circuit
from quip.quantum_system import QuantumSystem
from quip.gates import *

class MiscCircuitTest(unittest.TestCase):

    def test_3qb_fredkin(self):
        f = fredkin(2,0,1)

        c = Circuit(3)
        c.put(0,0,pauli_x())
        c.put(2,0,pauli_x())
        c.put(0,1,f)

        r = QuantumSystem(3)
        c.compile()
        c.run(r)

        self.assertTrue(r.measure() == '011')
