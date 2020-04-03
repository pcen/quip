from quip.interpreter.gate_lookup import *
from quip.circuit import Circuit

def read_file_lines(file_path):
    with open(file_path) as file:
        for line in file.readlines():
            if not line.strip():
                continue
            yield line.strip('\n').split(';')[0]

def parse_instruction(line_start, tokens):
    if '(' in line_start and ')' in line_start:
        tokens['instruction'] = line_start.split('(')[0]
        value = line_start.split('(')[-1].split(')')[0].strip()
        try:
            tokens['params'] = [float(value)]
        except Exception as e:
            print(f'invalid gate parameter {value}')
    else:
        tokens['instruction'] = line_start

    check_gate(tokens['instruction'])

def parse_qubits(line, tokens):
    if len(line) < gate_width(tokens['instruction']):
        print(f'missing qubits for {tokens["instruction"]}')

    qubits = []
    controlled = 0
    if is_controlled(tokens['instruction']):
        controlled = 1
        if not line[0].strip() or not line[0].strip().isdecimal():
            print(f'invalid control qubit')
        tokens['control'] = int(line[0].strip())

    for i in range(controlled, len(line)):
        if not line[i].strip():
            continue
        if line[i].strip().isdecimal():
            qubits.append(int(line[i].strip()))
    tokens['qubits'] = qubits

    if controlled:
        tokens['offset'] = min(tokens['qubits'] + [tokens['control']])
    else:
        tokens['offset'] = min(tokens['qubits'])

    if len(qubits) + controlled != gate_width(tokens['instruction']):
        print(f'wrong number of qubits for {tokens["instruction"]}')

def parse_line(line):
    tokens = {}
    params = []

    line = line.split(' ')

    parse_instruction(line[0], tokens)
    parse_qubits(line[1:], tokens)

    tokens['controlled'] = is_controlled(tokens['instruction'])
    tokens['parameterized'] = is_parameterized(tokens['instruction'])
    return tokens

def tokenize(code):
    tokenized = []
    lines = iter(read_file_lines(code))
    next(lines)
    for line in lines:
        tokenized.append(parse_line(line))
    return tokenized

def generate_circuit(parsed_code, width):
    qcircuit = Circuit(width)
    pos = 0
    for tkn in parsed_code:
        qcircuit.put(tkn['offset'], pos, create_gate(tkn))
        pos += 1
    return qcircuit

def assemble_circuit(program):
    tokens = tokenize(program)
    width = int(open(program).readline().split(' ')[-1].strip('\n'))
    return generate_circuit(tokens, width)
