# 1. read in all sensors
# 2. work out manhattan distance covered by each sensor
# 3. delete irrelevant sensors
# 4. work out min and max (x) for each sensor at target row
# 5. from min(x) to max(x), count covered positions

target_row = 2000000
sensor = []
distance = []
min_max = []

try:
    # 1. read in all sensors
    input = open("15.txt")
    n = 0
    for line in input:
        line = line.replace("Sensor at x=","").replace(", y=",",").replace(": closest beacon is at x=",",")[:-1]
        sensor.append([])
        sensor[n] = eval("["+line+"]")
        n += 1

    # 2. work out manhattan distance covered by each sensor
    for n in range(len(sensor)):
        md = abs(sensor[n][0] - sensor[n][2]) + abs(sensor[n][1] - sensor[n][3])
        distance.append(md)

    # 3. delete irrelevant sensors
    for n in range(len(sensor) - 1, -1, -1):
        if abs(target_row - sensor[n][1]) > distance[n]:
            sensor.pop(n)
            distance.pop(n)

    # 4. work out min and max (x) for each sensor at target row
    for n in range(len(sensor)):
        min_max.append([])
        min_max[n].append(sensor[n][0] - (distance[n] - abs(sensor[n][1] - target_row)))
        min_max[n].append(sensor[n][0] + (distance[n] - abs(sensor[n][1] - target_row)))

    # 5. from min(x) to max(x), count covered positions (excluding detected beacons)
    min_x = min_max[0][0]
    max_x = min_max[0][1]
    for n in range(len(min_max)):
        if min_max[n][0] < min_x:
            min_x = min_max[n][0]
        if min_max[n][1] > max_x:
            max_x = min_max[n][1]
    count = 0
    for x in range(min_x, max_x + 1):
        for b in range(len(sensor)):
            if x >= min_max[b][0] and x <= min_max[b][1] and not (sensor[b][3] == target_row and sensor[b][2] == x):
                count += 1
                break

    print(count,' positions cannot contain a beacon.')

finally:
    input.close()