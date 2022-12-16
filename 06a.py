sop_length = 4
sop_buffer = ''
min_reads = sop_length
char_count = 0

try:
    input_file = open("06.txt")
    while min_reads > 0:
        char = input_file.read(1)
        char_count += 1
        sop_buffer = char + sop_buffer[0:3]
        repeat_pos = sop_buffer.find(char,1)
        if repeat_pos == -1:
            min_reads -= 1
        else:
            min_reads = max(min_reads - 1, 4 - repeat_pos)
finally:
    input_file.close()
    print('First start-of-packet marker complete after ', char_count, ' characters.')