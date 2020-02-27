import unittest

from quip.quantum_system import QuantumSystem

class QuantumSystemTest(unittest.TestCase):

    def test_creation(self):
        qs = QuantumSystem(4)
        self.assertTrue(qs.state.size == 16)
        self.assertTrue(qs.state.item(0) == 1)
        for i in range(1, qs.state.size):
            self.assertTrue(qs.state.item(i) == 0)
        qs.measure()
        for b in qs.collapsed_state:
            self.assertTrue(b == '0')
        prob = qs.probabilities
        self.assertTrue(prob[0] == 1)
        for p in prob[1:]:
            self.assertTrue(p == 0)
