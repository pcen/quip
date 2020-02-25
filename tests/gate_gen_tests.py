import unittest
from numpy import array_equal, eye
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
