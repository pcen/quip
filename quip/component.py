from quip.gates import QuantumGate

import pickle as pkl

class Component(QuantumGate):
    def __init__(self, circuit):
        self.width = circuit.gates.width ** 2
        self.matrix = circuit.compiled
        self.symbol = 'Cmp'

def save_circuit(circuit, path):
    with open(path, 'wb') as f:
        pkl.dump(circuit, f)

def read_circuit(path):
    with open(path, 'rb') as f:
        circuit = pkl.load(f)
    return circuit

def save_gate(gate, path):
    with open(path, 'wb') as f:
        pkl.dump(gate, f)

def read_gate(path):
    with open(path, 'rb') as f:
        gate = pkl.load(f)
    return gate

def read_circuit_as_gate(path):
    circuit = read_circuit(path)
    return Component(circuit)

def save_circuit_as_gate(circuit, path):
    gate = Component(circuit)
    save_gate(gate, path)
