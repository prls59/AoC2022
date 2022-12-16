current_elf = 1
current_tot = 0
max_elf = 0
max_tot = 0
try:
    input_file = open("01.txt")
    for line in input_file:
        if line == '\n':
            if current_tot > max_tot:
                max_elf = current_elf
                max_tot = current_tot
            current_elf += 1
            current_tot = 0
        else:
            current_tot += int(line)
finally:
    input_file.close()
    print('Elf ',max_elf,' is carrying ',max_tot,' calories')