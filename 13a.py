index = 1
correctly_ordered = []
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
    while True:
        line = input.readline()
        if not line:
            break
        left = eval(line[:-1])
        line = input.readline()
        right = eval(line[:-1])
        line = input.readline()
        if correct_order(left, right) == 1:
            correctly_ordered.append(index)
        index+=1
    print('''
    There are ''', sum(correctly_ordered), ''' correctly ordered pairs.
    ''')
finally:
    input.close()