import numpy as np
from quip.gates import identity

def plain_kronecker(gates):
    product = np.eye(1)
    for g in gates:
        product = np.kron(product, g.matrix)
    return product

def fast_kron_id(matrix, id_size):
    l, w = matrix.shape
    p = np.zeros((l, id_size, w, id_size))
    r = np.arange(id_size)
    p[:,r,:,r] = matrix
    p.shape = (l * id_size, w * id_size)
    return p

def parallel_gates_equiv(gates):
    equiv = np.eye(1)
    c = 0
    for g in gates:
        if isinstance(g, identity):
            c += 1
            continue
        elif c:
            equiv = fast_kron_id(equiv, 2 ** c)
            c = 0
        equiv = np.kron(equiv, g.matrix)
    if c:
        equiv = fast_kron_id(equiv, 2 ** c)
    return equiv

def benchmark():
    from timeit import default_timer as t
    from quip.gates import hadamard
    iterations = 10
    i = identity()
    h = hadamard()
    gs = [h,i,i,h,i]

    s = t()
    for i in range(iterations):
        feq = parallel_gates_equiv(gs)
    e = t()
    print(f'new: {e - s}')

    s = t()
    for i in range(iterations):
        npeq = plain_kronecker(gs)
    e = t()
    print(f'old: {e - s}')

    if(np.array_equal(feq, npeq)):
        print('output arrays equal.')
    else:
        print('***output arrays different.')
