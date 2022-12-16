cycles = []
crt = [[],[],[],[],[],[]]

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
    cycle = 1
    for row in range(6):
        for pixel in range(40):
            if abs(cycles[cycle] - pixel) < 2:
                print('#',end='')
            else:
                print('.',end='')
            cycle += 1
        print('')
finally:
    input_file.close()
