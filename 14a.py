scan = []

def build_cave(scan,start,end):
    # expand array if nec...
    current_max_y = len(scan)
    if current_max_y > 0:
        current_max_x = len(scan[0])
    else:
        current_max_x = 0
    new_max_x = max(start[0],end[0])
    new_max_y = max(start[1],end[1])
    if current_max_y < new_max_y:
        scan.extend([[] for i in range(new_max_y - current_max_y)])
    if current_max_x < new_max_x:
        for y in range(new_max_y):
            scan[y].extend([[] for i in range(new_max_x - current_max_x)])
    # plot rock...

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
            s_coord = coord.split(",")
            if s_coord != f_coord and s_coord != gf_coord and f_coord != []:
                scan = build_cave(scan,f_coord,s_coord)