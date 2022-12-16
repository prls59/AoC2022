tail_track = {}
tail_x = 0
tail_y = 0
head_x = 0
head_y = 0

def move_rope(dir, hx, hy, tx, ty):
    if dir == 'U':
        hy += 1
    elif dir == 'D':
        hy -= 1
    elif dir == 'L':
        hx -= 1
    else:
        hx += 1
    if abs(hx - tx) == 2 or abs(hy - ty) == 2:
        if hx == tx:
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        elif hy == ty:
            if hx > tx:
                tx += 1
            else:
                tx -= 1
        else:
            # diagonal move required
            if hy > ty:
                ty += 1
            else:
                ty -= 1
            if hx > tx:
                tx += 1
            else:
                tx -= 1
    return hx, hy, tx, ty

try:
    input_file = open("09.txt")
    for line in input_file:
        direction = line[0:1]
        distance = int(line[2:])
        for n in range(distance):
            head_x, head_y, tail_x, tail_y = move_rope(direction, head_x, head_y, tail_x, tail_y)
            tail_track[str(tail_x)+','+str(tail_y)] = 1
    
finally:
    input_file.close()
    print('''
    Tail has visited ''',len(tail_track.keys()),''' positions.
    ''')