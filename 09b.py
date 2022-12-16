def move_head(dir, coords):
    if dir == 'U':
        coords[1] += 1
    elif dir == 'D':
        coords[1] -= 1
    elif dir == 'L':
        coords[0] -= 1
    else:
        coords[0] += 1
    return coords

def move_rope(lead_knot, trailing_knot):
    hx = lead_knot[0]
    hy = lead_knot[1]
    tx = trailing_knot[0]
    ty = trailing_knot[1]

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
    trailing_knot[0] = tx
    trailing_knot[1] = ty
    return trailing_knot

tail_track = {}
knots = []

try:
    for n in range(10):
        knots.append([])
        knots[n].append(0)
        knots[n].append(0)
    input_file = open("09.txt")
    for line in input_file:
        direction = line[0:1]
        distance = int(line[2:])
        for n in range(distance):
            knots[0] = move_head(direction, knots[0])
            knot = 1
            still_moving = True
            while knot < 10 and still_moving:
                oldx = knots[knot][0]
                oldy = knots[knot][1]
                knots[knot] = move_rope(knots[knot - 1], knots[knot])
                still_moving == (oldx != knots[knot][0] or oldy != knots[knot][1])
                knot += 1
            if knot == 10:
                tail_track[str(knots[9][0])+','+str(knots[9][1])] = 1
    
finally:
    input_file.close()
    print('''
    Tail has visited ''',len(tail_track.keys()),''' positions.
    ''')