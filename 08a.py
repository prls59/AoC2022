forest =[]
visible = []
rows = 0
columns = 0

try:
    input_file = open("08.txt")
    # plant forest
    for line in input_file:
        line = line[0:-1]
        forest.append(list(int(x) for x in line))
        rows += 1
    columns = len(forest[0])
    # seed the visibles map
    visible.append(list(1 for n in range(0, columns)))
    for r in range(1,rows - 1):
        visible.append(list())
        visible[r].append(1)
        for c in range(1,columns - 1):
            visible[r].append(0)
        visible[r].append(1)
    visible.append(list(1 for n in range(0, columns)))
    # look from the North
    for c in range(1,columns - 1):
        tallest = forest[0][c]
        r = 1
        while r < rows - 1 and tallest < 9:
            if forest[r][c] > tallest:
                visible[r][c] = 1
                tallest = forest[r][c]
            r += 1
    # look from the East
    for r in range(1,rows - 1):
        tallest = forest[r][columns - 1]
        c = columns - 2
        while c > 0 and tallest < 9:
            if forest[r][c] > tallest:
                visible[r][c] = 1
                tallest = forest[r][c]
            c -= 1
    # look from the South
    for c in range(1,columns - 1):
        tallest = forest[rows - 1][c]
        r = rows - 2
        while r > 0 and tallest < 9:
            if forest[r][c] > tallest:
                visible[r][c] = 1
                tallest = forest[r][c]
            r -= 1
    # look from the West
    for r in range(1,rows - 1):
        tallest = forest[r][0]
        c = 1
        while c < columns - 1 and tallest < 9:
            if forest[r][c] > tallest:
                visible[r][c] = 1
                tallest = forest[r][c]
            c += 1
    # count up
    total = 0
    for r in visible:
        for c in r:
            total += c

finally:
    input_file.close()
    print('''
    
    Visibles: ''',total,'''
    
    ''')