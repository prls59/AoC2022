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

div_product = 1

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
    for monkey in range(8):
        div_product *= operations[monkey][DIVISOR]
    # keep away game
    for round in range(10000):
        for monkey in range(8):
            if len(items[monkey]) > 0:
                inspections[monkey] += len(items[monkey])
                opr = operations[monkey][OPERATOR]
                opd = operations[monkey][OPERAND]
                div = operations[monkey][DIVISOR]
                tru = operations[monkey][TRUE_MONKEY]
                fal = operations[monkey][FALSE_MONKEY]
                if opr == "**":
                    items[monkey] = list(map(lambda a : (a * a) % div_product, items[monkey]))
                elif opr == "*":
                    items[monkey] = list(map(lambda a : (a * opd) % div_product, items[monkey]))
                else:
                    items[monkey] = list(map(lambda a : (a + opd) % div_product, items[monkey]))
                items[tru].extend([x for x in items[monkey] if x % div == 0])
                items[fal].extend([x for x in items[monkey] if x % div != 0])
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