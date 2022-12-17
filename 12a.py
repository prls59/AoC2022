height = []
start = 0
end = 0

distance = []
queue = []
visited = []

def new_dist(here, there, height, distance):
    dist = distance[there]
    if height[there] <= height[here] + 1:
        if distance[here] + 1 < distance[there]:
            dist = distance[here] + 1
    return dist

try:
    input = open("12.txt")
    # initialise
    row = 0
    for line in input:
        column = 0
        for spot_height in line[:-1]:
            if spot_height == "S":
                start = (len(line) - 1) * row + column
                height.append(0)
            elif spot_height == "E":
                end = (len(line) - 1) * row + column
                height.append(25)
            else:
                height.append(ord(spot_height)-ord('a'))
            column += 1
        row += 1
    tot_rows = row
    tot_columns = column
    # for purposes of the path finding algorithm, 'too_far' is 1 larger than the longest path
    too_far = tot_rows * tot_columns
    distance.extend([too_far for x in range(too_far)])
    # start at distance 0
    distance[start] = 0
    # fill the queue
    queue.extend([x for x in range(too_far)])
    # start searching
    while len(queue) > 0 and distance[end] == too_far:
        # find closest unvisited destination
        here = 0
        closest_distance = too_far + 1
        for q in range(len(queue)):
            if distance[queue[q]] < closest_distance:
                here = queue[q]
                closest_distance = distance[queue[q]]
                qpop = q
        # look North
        there = here - tot_columns
        if there > 0 and there in queue:
            distance[there] = new_dist(here, there, height, distance)
        # look South
        there = here + tot_columns
        if there < too_far and there in queue:
            distance[there] = new_dist(here, there, height, distance)
        # look West
        there = here - 1
        if here % tot_columns != 0 and there in queue:
            distance[there] = new_dist(here, there, height, distance)
        # look East
        there = here + 1
        if there % tot_columns != 0 and there in queue:
            distance[there] = new_dist(here, there, height, distance)
        # mark as visited
        queue.pop(qpop)
        visited.append(here)
    # report result
    if distance[end] == too_far:
        print('Endpoint unreachable.')
    else:
        print('Endpoint reachable after ', distance[end],' steps.')

finally:
    input.close()