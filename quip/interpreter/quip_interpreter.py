def read_file_lines(file_path):
    with open(file_path) as file:
        for line in file.readlines():
            if not line.strip():
                continue
            yield line.strip('\n').split(';')[0]

def parse_line(line):
    line = line.split(' ')
    instruction = line[0]
    qubits = []
    for q in line[1:]:
        if not q.strip():
            continue
        elif q.isdecimal():
            qubits.append(int(q))
        else:
            print(f'invalid value: {q}')
    return instruction, qubits

def tokenize(code):
    tokenized = []
    for line in read_file_lines(code):
        tokenized.append(parse_line(line))
    return tokenized

prog = "C:\cygwin64\home\Paul\Dev\quip\prog.q"

program = tokenize(prog)

for p in program:
    print(p)
