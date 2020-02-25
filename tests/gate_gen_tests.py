import unittest
from numpy import array_equal, eye, rot90
from quip.gates import *

class GateGenTest(unittest.TestCase):

    def test_cu_hadamard(self):
        cu = controlled_U(0, 1, hadamard())
        correct = eye(4)
        correct[2:4,2:4] = hadamard.matrix
        self.assertTrue(array_equal(cu.matrix, correct))

        cu = controlled_U(1, 0, hadamard())
        correct = eye(4)
        correct[0:2,0:2] = hadamard.matrix
        self.assertTrue(array_equal(cu.matrix, correct))

    def test_toffoli_0_1_2(self):
        tof = toffoli(0,1,2)
        correct = eye(8)
        correct[6:8, 6:8] = rot90(np.eye(2))
        self.assertTrue(array_equal(tof.matrix, correct))
