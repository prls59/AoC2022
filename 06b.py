marker_length = 14
read_buffer = ''
min_reads = marker_length
char_count = 0

try:
    input_file = open("06.txt")
    while min_reads > 0:
        char = input_file.read(1)
        char_count += 1
        read_buffer = char + read_buffer[0:marker_length - 1]
        repeat_pos = read_buffer.find(char,1)
        if repeat_pos == -1:
            min_reads -= 1
        else:
            min_reads = max(min_reads - 1, marker_length - repeat_pos)
finally:
    input_file.close()
    print('Marker completes after ', char_count, ' characters.')