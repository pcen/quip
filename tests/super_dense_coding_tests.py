import unittest

from quip.circuit import Circuit
from quip.quantum_system import QuantumSystem
from quip.gates import *

def sdc_setup():
    h = hadamard()
    sdc = Circuit(2)
    reg = QuantumSystem(2)
    cn = CNOT(0,1)
    sdc.put(0,0,h)
    sdc.put(0,1,cn)
    sdc.put(0,3,cn)
    sdc.put(0,4,h)
    return reg, sdc, h, cn

class SuperDenseCodingTest(unittest.TestCase):

    def test_sdc_00(self):
        reg, sdc, h, cn = sdc_setup()
        sdc.put(0,2,identity())
        sdc.compile()
        sdc.run(reg)
        self.assertTrue(reg.measure() == [0, 0])

    def test_sdc_01(self):
        reg, sdc, h, cn = sdc_setup()
        sdc.put(0,2,pauli_x())
        sdc.compile()
        sdc.run(reg)
        self.assertTrue(reg.measure() == [0, 1])

    def test_sdc_10(self):
        reg, sdc, h, cn = sdc_setup()
        sdc.put(0,2,pauli_z())
        sdc.compile()
        sdc.run(reg)
        self.assertTrue(reg.measure() == [1, 0])

    def test_sdc_11(self):
        h = hadamard()
        sdc = Circuit(2)
        reg = QuantumSystem(2)
        cn = CNOT(0,1)
        sdc.put(0,0,h)
        sdc.put(0,1,cn)
        sdc.put(0,2,pauli_z())
        sdc.put(0,3,pauli_x())
        sdc.put(0,4,cn)
        sdc.put(0,5,h)
        sdc.compile()
        sdc.run(reg)
        self.assertTrue(reg.measure() == [1, 1])
