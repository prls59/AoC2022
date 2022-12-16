forest =[]
scenic_scores = []
rows = 0
columns = 0

def tree_score(wood, row, column):
    north = 0
    east = 0
    south = 0
    west = 0
    tree_height = wood[row][column]
    # look South
    r = row + 1
    while r < rows:
        south += 1
        if forest[r][column] >= tree_height:
            break
        else:
            r += 1
    # look West
    c = column - 1
    while c >= 0:
        west += 1
        if forest[row][c] >= tree_height:
            break
        else:
            c -= 1
    # look North
    r = row - 1
    while r >= 0:
        north += 1
        if forest[r][column] >= tree_height:
            break
        else:
            r -= 1
    # look East
    c = column + 1
    while c < columns:
        east += 1
        if forest[row][c] >= tree_height:
            break
        else:
            c += 1
    return north * south * east * west
try:
    input_file = open("08.txt")
    # plant forest
    for line in input_file:
        line = line[0:-1]
        forest.append(list(int(x) for x in line))
        rows += 1
    columns = len(forest[0])
    # seed the scenic scores map
    for r in range(rows):
        scenic_scores.append(list())
        for c in range(columns):
            scenic_scores[r].append(0)
    # check each tree
    max_tree = 0
    for r in range(1,rows - 1):
        for c in range(1, columns - 1):
            this_tree = tree_score(forest,r,c)
            scenic_scores[r][c] = this_tree
            if this_tree > max_tree:
                max_tree = this_tree

finally:
    input_file.close()
    print('''
    
    Highest scenic score: ''',max_tree,'''
    
    ''')