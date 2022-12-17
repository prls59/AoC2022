index = 1
packets = []
left = []
right = []

def correct_order(l, r):
    if isinstance(l,int) and isinstance(r, int):
        if l > r:
            return -1
        elif r > l:
            return 1
        else:
            return 0
    elif isinstance(l,list) and isinstance(r,list):
        len_l = len(l)
        len_r = len(r)
        for x in range(min(len_l,len_r)):
            result = correct_order(l[x],r[x])
            if result != 0:
                return result
        if len_l > len_r:
            return -1
        elif len_r > len_l:
            return 1
        else:
            return 0
    else:
        if isinstance(l,int):
            return correct_order([l],r)
        else:
            return correct_order(l,[r])

try:
    # initialise
    input = open("13.txt")
    index = 0
    for line in input:
        if line != "\n":
            packets.append([])
            packets[index].extend(eval(line[:-1]))
            index += 1
    packets.append([])
    packets[index].extend([[2]])
    index += 1
    packets.append([])
    packets[index].extend([[6]])
    # sort
    count = index + 1
    index = 0
    already_sorted = False
    while index < count and not already_sorted:
        already_sorted = True
        for j in range(count - index - 1):
            if correct_order(packets[j],packets[j+1]) == -1:
                packets[j], packets[j+1] = packets[j+1], packets[j]
                already_sorted = False
    # find dividers
    decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print('''
    Decoder key: ''', decoder_key, '''
    ''')
finally:
    input.close()