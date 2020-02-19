import numpy as np
from quip.gates.single_qubit import identity


def plain_kronecker(gates):
    product = np.eye(1)
    for g in gates:
        product = np.kron(product, g.matrix)
    return product


# Use a 4D array to compute matrix ⊗ I, where I is of size n
# Divakar's stack overflow answer: https://stackoverflow.com/a/44461842
def fast_kron_id(matrix, n):
    l, w = matrix.shape
    p = np.zeros((l, n, w, n))
    r = np.arange(n)
    p[:,r,:,r] = matrix
    p.shape = (l * n, w * n)
    return p


def is_id(gate):
    return isinstance(gate, identity) or gate is identity


def skip(column, width):
    for _ in range(width):
        if next(column, None) is None:
            break


def parallel_gates_equiv(gates):
    equiv = np.eye(1)
    c = 0
    gates= iter(gates)
    for g in gates:
        if is_id(g):
            c += 1
            continue
        elif c:
            equiv = fast_kron_id(equiv, 2 ** c)
            c = 0
        equiv = np.kron(equiv, g.matrix)
        skip(gates, g.width - 1)
    if c:
        equiv = fast_kron_id(equiv, 2 ** c)
    return equiv


# TODO: remove/relocate validation to unit test
def benchmark():
    from timeit import default_timer as t
    from quip.gates.single_qubit import hadamard
    iterations = 10
    I = identity()
    h = hadamard()
    gs = [h,I,I,I,I,h,I]

    s = t()
    for _ in range(iterations):
        feq = parallel_gates_equiv(gs)
    e = t()
    print(f'new: {e - s}')

    s = t()
    for _ in range(iterations):
        npeq = plain_kronecker(gs)
    e = t()
    print(f'old: {e - s}')

    if(np.array_equal(feq, npeq)):
        print('output arrays equal.')
    else:
        print('***output arrays different.')
