from quip.gates import *

gate_table =  {
    # atomic gates
    'hdm'  : (1, 0, False, hadamard,     None),
    'plx'  : (1, 0, False, pauli_x,      None),
    'ply'  : (1, 0, False, pauli_y,      None),
    'plz'  : (1, 0, False, pauli_z,      None),
    'phs'  : (1, 1, False, phase_shift,  None),
    'fdk'  : (3, 0, True,  fredkin,      None),
    'tfl'  : (3, 0, True,  toffoli,      None),
    'cnt'  : (2, 0, True,  CNOT,         None),
    'swp'  : (2, 0, False, swap,         None),
    'srw'  : (2, 0, False, sqrt_swap,    None),

    # controlled versions of single qubit gates
    'chdm' : (2, 0, True,  controlled_U, hadamard),
    'cplx' : (2, 0, True,  controlled_U, pauli_x),
    'cply' : (2, 0, True,  controlled_U, pauli_y),
    'cplz' : (2, 0, True,  controlled_U, pauli_z),
    'cphs' : (2, 1, True,  controlled_U, phase_shift)
}

def check_gate(instruction):
    if instruction not in gate_table:
        print(f'unknown instruction {instruction}')
        return False
    return True

def compound_gate(instruction):
    if not check_gate(instruction):
        return False

    return (gate_table[instruction][4] is not None)

def num_gate_params(instruction):
    if not check_gate(instruction):
        return False

    return gate_table[instruction][1]

def gate_width(instruction):
    if not check_gate(instruction):
        return -1

    return gate_table[instruction][0]

def is_controlled(instruction):
    if not check_gate(instruction):
        return False

    return gate_table[instruction][2]

def is_parameterized(instruction):
    if not check_gate(instruction):
        return False

    return bool(gate_table[instruction][1])
