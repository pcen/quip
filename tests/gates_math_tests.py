import unittest
from numpy import array_equal
from quip.gates import *
from quip.math.speedy_gates import *

class GatesMathTest(unittest.TestCase):

    def test_validate_speedy_gates(self):
        I = identity()
        h = hadamard()
        gs = [h,I,I,I,I,h,I]

        feq = parallel_gates_equiv(gs)

        npeq = plain_kronecker(gs)

        self.assertTrue(array_equal(feq, npeq))
