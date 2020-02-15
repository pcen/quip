import numpy as np
from quip.gates import identity
from quip.math.speedy_gates import parallel_gates_equiv


class GateLayout:
    grid = None
    width = 0
    length = 0

    def __init__(self, width):
        self.grid = [[identity()] for _ in range(width)]
        self.width = width
        self.length = 1


    def place(self, y, x, gate):
        if not 0 <= y < self.width or x < 0:
            print(f'invalid gate position ({y}, {x})')
            return False
        if x >= self.length:
            self.extend(x)

        self.grid[y][x] = gate
        return True


    def extend(self, index):
        diff = index + 1 - self.length
        [path.extend([identity()] * diff) for path in self.grid]
        self.length += diff


    @property
    def parallel_equivs(self):
        for i in range(self.length):
            yield parallel_gates_equiv([path[i] for path in self.grid])


    def equivalent_matrix(self):
        equivalent = np.eye(2 ** self.width)
        for g in self.parallel_equivs:
            equivalent = equivalent @ g
        return equivalent


    def __str__(self):
        return ''.join('--'.join(str(g) for g in path) + '\n' for path in self.grid)


    def __repr_(self):
        return self.__str__()
