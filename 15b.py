# 1. read in all sensors
# 2. work out manhattan distance covered by each sensor
# 3. scan area looking for unreached position (excluding detected beacons)

def manhattan(from_x, from_y, to_x, to_y):
    return abs(from_x - to_x) + abs(from_y - to_y)

sensor = []
distance = []
min_max = []

min_x = 0
min_y = 0
max_x = 4000000
max_y = 4000000
sensor_count = 0

try:
    # 1. read in all sensors
    input = open("15.txt")
    n = 0
    for line in input:
        line = line.replace("Sensor at x=","").replace(", y=",",").replace(": closest beacon is at x=",",")[:-1]
        sensor.append([])
        sensor[n] = eval("["+line+"]")
        n += 1
    sensor_count = n

    # 2. work out manhattan distance covered by each sensor
    for n in range(len(sensor)):
        distance.append(manhattan(sensor[n][0], sensor[n][1], sensor[n][2], sensor[n][3]))

    # 3. scan area looking for unreached position (excluding detected beacons)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            found = True
            for b in range(sensor_count):
                if manhattan(x,y,sensor[b][0],sensor[b][1]) <= distance[b] or (sensor[b][2] == x and sensor[b][3] == y):
                    found = False
                    break
            if found:
                break
        if found:
            break

    if found:
        freq = (x * 4000000) + y
        print('Distress beacon at ',x,',',y,' Tuning frequency = ',freq)
    else:
        print('Not found :(')

finally:
    input.close()