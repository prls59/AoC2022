current_cals = 0
top_cals = [0, 0, 0]
top_n = len(top_cals)
try:
    input_file = open("01.txt")
    for line in input_file:
        if line == '\n':
            n = 0
            while n < top_n:
                if current_cals > top_cals[n]:
                    i = top_n - 1
                    while i > n:
                        top_cals[i] = top_cals[i-1]
                        i -= 1
                    top_cals[n] = current_cals
                    break
                n += 1
            current_cals = 0
        else:
            current_cals += int(line)
finally:
    input_file.close()
    sum_cals = 0
    for cals in top_cals:
        sum_cals += cals
    print('Top ',top_n,' elves carrying ',sum_cals,' calories in total.')