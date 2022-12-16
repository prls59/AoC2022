FROM = 0
TO = 1

overlap_count = 0

try:
    input_file = open("04.txt")
    for line in input_file:
        range = line.split(",")
        elf_1 = range[0].split("-")
        elf_2 = range[1].split("-")
        if int(elf_1[TO]) >= int(elf_2[FROM]) and int(elf_1[FROM]) <= int(elf_2[TO]):
            overlap_count += 1

finally:
    input_file.close()
    print('There are ', overlap_count, ' overlapping cases.')