monkey = 0
items = [[],[],[],[],[],[],[],[]]
operations = [[],[],[],[],[],[],[],[]]
inspections = [0,0,0,0,0,0,0,0]
worry = 0

OPERATOR = 0
OPERAND = 1
DIVISOR = 2
TRUE_MONKEY = 3
FALSE_MONKEY = 4

try:
    input = open("11.txt")
    # initialise
    for line in input:
        if line == "\n":
            pass
        elif line[0] == "M":
            monkey = int(line[7:-2])
        elif line[2] == "S":
            items[monkey] = [int(x) for x in line[18:-1].split(", ")]
        elif line[2] == "O":
            if line[19:28] == "old * old":
                operations[monkey].extend(["**",2])
            else:
                operations[monkey].extend([line[23],int(line[25:-1])])
        elif line[2] == "T":
            operations[monkey].append(int(line[21:-1]))
        elif line[7] == "t":
            operations[monkey].append(int(line[29:-1]))
        else:
            operations[monkey].append(int(line[30:-1]))
    # keep away game
    for round in range(20):
        for monkey in range(8):
            for item in items[monkey]:
                inspections[monkey] += 1
                if operations[monkey][OPERATOR] == "**":
                    worry = item ** operations[monkey][OPERAND]
                elif operations[monkey][OPERATOR] == "*":
                    worry = item * operations[monkey][OPERAND]
                else:
                    worry = item + operations[monkey][OPERAND]
                worry = worry // 3
                if worry % operations[monkey][DIVISOR] == 0:
                    items[operations[monkey][TRUE_MONKEY]].append(worry)
                else:
                    items[operations[monkey][FALSE_MONKEY]].append(worry)
            items[monkey].clear()
    # find the two winners
    winner = 0
    runner_up = 0
    for monkey in range(8):
        if inspections[monkey] > winner:
            runner_up = winner
            winner = inspections[monkey]
        elif inspections[monkey] > runner_up:
            runner_up = inspections[monkey]
    monkey_business = winner * runner_up
    print('''
    Monkey business = ''',monkey_business,'''
    ''')

finally:
    input.close()