def priority(char):
    asc = ord(char)
    if asc > 96:
        return asc - 96
    else:
        return asc - 38

elf_1 = ""
elf_2 = ""
elf_3 = ""
priority_sum = 0

try:
    input_file = open("03.txt")
    elf_1 = input_file.readline()
    while elf_1 != '':
        elf_1 = list(dict.fromkeys(elf_1))
        elf_2 = list(dict.fromkeys(input_file.readline()))
        elf_3 = list(dict.fromkeys(input_file.readline()))
        for item in elf_1:
            if item in elf_2 and item in elf_3:
                priority_sum += priority(item)
                break
        elf_1 = input_file.readline()
        
finally:
    input_file.close()
    print('Priority sum: ',priority_sum)
    