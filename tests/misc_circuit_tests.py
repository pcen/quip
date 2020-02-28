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

    def test_full_adder(self):
        f1 = fredkin(0,3,4)
        f2 = fredkin(0,2,3)
        f3 = fredkin(0,1,2)
        f4 = fredkin(1,0,2)
        f5 = fredkin(0,1,3)
        c = Circuit(5)
        x = pauli_x()
        c.put(4,0,x)
        c.put(0,0,x)
        c.put(1,0,x)
        c.put(0,1,f1)
        c.put(1,2,f2)
        c.put(2,3,f3)
        c.put(2,4,f4)
        c.put(1,5,f5)
        r = QuantumSystem(5)
        c.compile()
        c.run(r)
        self.assertTrue(r.measure() == '11100')
