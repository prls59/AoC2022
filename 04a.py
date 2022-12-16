FROM = 0
TO = 1

contained_count = 0

try:
    input_file = open("04.txt")
    for line in input_file:
        range = line.split(",")
        elf_1 = range[0].split("-")
        elf_2 = range[1].split("-")
        if (int(elf_1[FROM]) >= int(elf_2[FROM]) and int(elf_1[TO]) <= int(elf_2[TO])) or (int(elf_1[FROM]) <= int(elf_2[FROM]) and int(elf_1[TO]) >= int(elf_2[TO])):
            contained_count += 1

finally:
    input_file.close()
    print('In ', contained_count, ' cases, assignment pairs fully overlap.')