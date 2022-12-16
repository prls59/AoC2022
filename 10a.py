cycles = []

try:
    input_file = open("10.txt")
    x = 1
    cycles.append(x)
    for line in input_file:
        op = line[0:4]
        if op == "addx":
            arg = int(line[5:])
            cycles.append(x)
            cycles.append(x)
            x += arg
        else:
            # noop
            cycles.append(x)
    tot = 0
    for i in range(20,240,40):
        tot += i * cycles[i]
finally:
    input_file.close()
    print('''
    Sum of signal strengths: ''',tot,'''
    ''')