def priority(char):
    asc = ord(char)
    if asc > 96:
        return asc - 96
    else:
        return asc - 38

compartment_1 = ""
compartment_2 = ""
split = 0
priority_sum = 0

try:
    input_file = open("03.txt")
    for line in input_file:
        split = (len(line)-1) // 2
        compartment_1 = list(dict.fromkeys(line[:split]))
        compartment_2 = list(dict.fromkeys(line[split:split+split]))
        for item in compartment_1:
            if item in compartment_2:
                priority_sum += priority(item)
                break
finally:
    input_file.close()
    print('Priority sum: ',priority_sum)
    