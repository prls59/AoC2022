scan = []

def build_cave(scan,start,end):
    # expand array if nec...
    current_max_x = len(scan) - 1
    if current_max_x >= 0:
        current_max_y = len(scan[0]) - 1
    else:
        current_max_y = -1
    new_max_x = max(start[0],end[0])
    new_max_y = max(start[1],end[1])
    if new_max_y > current_max_y:
        # extend existing rows
        for x in range(current_max_x + 1):
            scan[x].extend([[] for i in range(new_max_y - current_max_y)])
    if new_max_x > current_max_x:
        # add new rows
        scan.extend([[] for i in range(new_max_x - current_max_x)])
        # ... & extend them
        for x in range(current_max_x + 1, new_max_x + 1):
            scan[x].extend([[] for i in range(max(current_max_y, new_max_y) + 1)])
    # plot rock...
    for x in range(min(start[0],end[0]),max(start[0],end[0])+1):
        for y in range(min(start[1],end[1]),max(start[1],end[1])+1):
            scan[x][y] = "#"
    return scan

def display_scan(scan):
    for y in range(len(scan[0])):
        for x in range(len(scan)):
            if scan[x][y]:
                print(scan[x][y], end ="")
            else:
                print('.', end ="")
        print('')

def drop_sand(scan):
    x = 500
    y = 0
    finished = False
    while not finished:
        y += 1
        if y < len(scan[0]):
            if scan[x][y]:
                x -= 1
                if x >= 0:
                    if scan[x][y]:
                        x += 2
                        if x < len(scan):
                            if scan[x][y]:
                                x -= 1
                                y -= 1
                                finished = True
                        else:
                            finished = True
                else:
                    finished = True
        else:
            finished = True
    return [x,y]

try:
    input = open("14.txt")
    for line in input:
        line = line[:-1]
        gf_coord = []
        f_coord = []
        s_coord = []
        for coord in line.split(" -> "):
            gf_coord = f_coord
            f_coord = s_coord
            s_coord = [int(c) for c in coord.split(",")]
            if s_coord != f_coord and s_coord != gf_coord and f_coord != []:
                scan = build_cave(scan,f_coord,s_coord)
    # floor
    scan = build_cave(scan, [0,len(scan[0])+1],[1000,len(scan[0])+1])
    display_scan(scan)
    # sand...
    grain_count = 0
    blocked = False
    while not blocked:
        grain_rest = drop_sand(scan)
        if grain_rest[0] < 0 or grain_rest[0] >= len(scan) or grain_rest[1] >= len(scan[0]):
            break
        else:
            scan[grain_rest[0]][grain_rest[1]] = "o"
            grain_count += 1
            if grain_rest[0] == 500 and grain_rest[1] == 0:
                blocked = True
    display_scan(scan)
    if blocked:
        print('Blocked at ',grain_count,' units of sand.')
    else:
        print('FAILED at ',grain_count,' units of sand.')

finally:
    input.close()