import unittest as ut
from tests.quantum_system_tests import QuantumSystemTest as QST
from tests.single_qubit_circuit_tests import HadamardCircuitTest as HCT
from tests.super_dense_coding_tests import SuperDenseCodingTest as SDCT
from tests.gates_math_tests import GatesMathTest as GMT

def test_all():
    s = ut.TestSuite()
    s.addTest(ut.makeSuite(QST))
    s.addTest(ut.makeSuite(HCT))
    s.addTests(ut.makeSuite(SDCT))
    s.addTests(ut.makeSuite(GMT))
    r = ut.result.TestResult()
    s.run(r)
    print(r)
    if r.failures:
        print(f'test failures:\n{r.failures}')
    return r
