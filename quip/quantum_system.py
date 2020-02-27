import numpy as np
from quip.utils import ket

class QuantumSystem:
    state = None
    width = 0
    measured = False
    collapsed_state = None

    def __init__(self, num: int):
        self.state = np.array([np.complex(0)] * (2 ** num))
        self.state.itemset(0, 1)
        self.width = num

    @property
    def probabilities(self):
        return [np.absolute(a) ** 2 for a in np.nditer(self.state)]

    def measure(self):
        self.measured = True
        state = np.random.choice(a = list(range(2 ** self.width)), p = self.probabilities)
        self.collapsed_state = ket(state, self.width)
        return self.collapsed_state

    def print(self):

        print('State:\n  ', end='')
        for i, e in enumerate(self.state):
            if not i:
                print(e, end='')
            else:
                print(',', e, end='')
        print()

        print('Probabilities:')
        for i, p in enumerate(self.probabilities):
            print('  ' + ket(i, self.width) + ":", str(p)[:6])

        if self.measured:
            print(f'Collapsed State:\n  {self.collapsed_state}')

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return self.__str__()
