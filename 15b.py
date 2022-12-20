# 1. read in all sensors
# 2. work out manhattan distance covered by each sensor
# 3. scan area looking for unreached position (excluding detected beacons)

def manhattan(from_x, from_y, to_x, to_y):
    return abs(from_x - to_x) + abs(from_y - to_y)

sensor = []
sensor_range = []
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
        sensor_range.append(manhattan(sensor[n][0], sensor[n][1], sensor[n][2], sensor[n][3]))

    # 3. scan area looking for unreached position (excluding detected beacons)
    beacon_found = False
    x = 0
    while x <= max_x and not beacon_found:
        y = 0
        while y <= max_y and not beacon_found:
            beacon_found = True
            for s in range(sensor_count):
                s_dist = manhattan(x,y,sensor[s][0],sensor[s][1])
                if s_dist <= sensor_range[s] or (sensor[s][2] == x and sensor[s][3] == y):
                    beacon_found = False
                    # jump to end of sensor's reach
                    y = sensor[s][1] + sensor_range[s] - abs(x - sensor[s][0])
                    break
            if beacon_found:
                break
            else:
                y += 1
        if beacon_found:
            break
        else:
            # print(".", end="")
            x += 1

    if beacon_found:
        freq = (x * 4000000) + y
        print('Distress beacon at ',x,',',y,' Tuning frequency = ',freq)
    else:
        print('Not found :(')

finally:
    input.close()