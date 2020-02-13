import numpy as np

class qReg:
    state = None
    width = 0
    measured = False
    collapsed_state = None

    def __init__(self, num: int):
        self.state = np.matrix([np.complex(0)] * (1 << num))
        self.state.itemset(0, 1)
        self.width = num

    @property
    def probabilities(self):
        return [np.absolute(a) ** 2 for a in self.state.tolist()[0]]

    def measure(self):
        self.measured = True
        state = np.random.choice(a = [range(2 ** self.width)], p = self.probabilities)
        self.collapsed_state = [int(b) for b in format(state, f'0{self.width}b')]
        return self.collapsed_state

    def print(self):
        print(f'State:\n{str([s for s in self.state.tolist()[0]])}')
        print(f'Probabilities:\n{str([str(p)[:6] for p in self.probabilities])}')
        if self.measured:
            print(f'Collapsed State:\n{self.collapsed_state}')

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return self.__str__()
