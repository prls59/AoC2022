def crane_move(stacks, step):
    count = step[0]
    from_stack = step[1] - 1
    to_stack = step[2] - 1
    crane_load = stacks[from_stack][0-count:]
    crane_load.reverse()
    stacks[to_stack].extend(crane_load)
    for n in range(count):
        stacks[from_stack].pop()
    return stacks

stacks = [[],[],[],[],[],[],[],[],[]]

try:
    input_file = open("05.txt")
    for line in input_file:
        if line[:1] == '\n':
            # End of stacks
            print('''
            Initial stacks:
            ''',stacks)
        elif line[1:2] == '1':
            # Stack numbers - reverse the stacks
            for n in range(len(stacks)):
                stack = stacks[n]
                stack.reverse()
                stacks[n] = stack
        elif line[:1] == 'm':
            # crane move
            step = [int(x) for x in line.replace('move ','').replace(' from ',',').replace(' to ',',').split(',')]
            stacks = crane_move(stacks, step)
        else:
            # build the stacks
            for n in range((len(line)+1)//4):
                crate = line[n*4+1:n*4+2]
                if crate != ' ':
                    stacks[n].append(crate)

finally:
    input_file.close()
    message = ''
    for stack in stacks:
        message += stack[-1]
    print('''
    Final stacks:
    ''',stacks,'''
    
    Elf message: ''',message)