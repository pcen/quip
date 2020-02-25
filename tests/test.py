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

def test_all():
    results = ut.result.TestResult()
    every_unit_test().run(results)
    print(results)
    if results.failures:
        print(f'test failures:\n{r.failures}')
    return results
