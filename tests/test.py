import unittest as ut
from tests.quantum_system_tests import QuantumSystemTest as QST
from tests.single_qubit_circuit_tests import HadamardCircuitTest as HCT

def test_all():
    s = ut.TestSuite()
    s.addTest(QST('test_creation'))
    s.addTest(HCT('test_hadamard_circuit'))
    r = ut.result.TestResult()
    s.run(r)
    print(r)
    if r.failures:
        print(f'test failures:\n{r.failures}')
    return r
