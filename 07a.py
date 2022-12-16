
# fs = {}
path = []
path_string = ''
# locn = fs

dir_sizes = {'/': 0}

try:
    input_file = open("07.txt")
    # construct tree
    for line in input_file:
        line = line[0:-1] # strip off \n
        start = line[0:1]
        if start == '$':
            # command
            command = line[2:4]
            if command == 'cd':
                target = line[5:]
                if target == '/':
                    path = []
                elif target == '..':
                    path.pop()
                else:
                    path.append(target)
                # locn = fs
                # for sub_dir in path:
                #     locn = locn[sub_dir]
                if len(path) > 0:
                    path_string = '/'.join(path)+'/'
                else:
                    path_string = ''
        elif start == 'd':
            # directory
            # locn[line[4:]] = {}
            dir_sizes['/' + path_string + line[4:]] = 0
        else:
            # file
            file_info = line.split()
            # locn[file_info[1]] = int(file_info[0])
            # update sizes
            for n in range(len(path)):
                dir_sizes['/'+'/'.join(path[0:n+1])] += int(file_info[0])
            dir_sizes['/'] += int(file_info[0])
    
finally:
    input_file.close()
    tot_size = 0
    for dir in dir_sizes:
        size = dir_sizes[dir]
        if size <= 100000:
            tot_size += size
    print('Total size: ',tot_size)