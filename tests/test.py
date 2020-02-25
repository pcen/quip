import unittest as ut
from tests.quantum_system_tests import QuantumSystemTest as QST
from tests.single_qubit_circuit_tests import HadamardCircuitTest as HCT
from tests.super_dense_coding_tests import SuperDenseCodingTest as SDCT
from tests.gates_math_tests import GatesMathTest as GMT
from tests.gate_gen_tests import GateGenTest as GGT


test_classes = (QST, HCT, SDCT, GMT, GGT)


def every_unit_test():
    suite = ut.TestSuite()
    [suite.addTest(ut.makeSuite(tc)) for tc in test_classes]
    return suite


# run all unit tests
def test_all():
    r = ut.result.TestResult()
    every_unit_test().run(r)
    print(f'Passed {r.testsRun - len(r.failures) - len(r.errors)}/{r.testsRun} unit tests.')
    if r.failures:
        print(f'test failures:\n{r.failures}')
    if r.errors:
        print(f'test errors:\n{r.errors}')
    return r
