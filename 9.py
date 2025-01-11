# recieve string of input

# for index that is even: add it to data list as a chunk of data [00,[],111,[],2222,...]

def read_file_to_list(file_path):
    disk_map = []
    disk_map_2 = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
        text = text.strip()
        index_count = 0
        for i in range(len(text)):
            if i % 2 == 0:
                for i in range(int(text[i])):
                    disk_map.append(str(index_count))
                    disk_map_2.append(str(index_count))
                index_count += 1
            else:
                if text[i] != '0':
                    disk_map.append(int(text[i]))
                    for x in range(int(text[i])):
                        disk_map_2.append('.')
    return disk_map, disk_map_2

def calculate_checksum(map):
    checksum = 0
    for i in range(len(map)):
        if(map[i] == '.' or type(map[i]) == int):
            continue
        checksum += i * int(map[i])
    return checksum

# iterate through disk_map for i in range: if find certain chunk of free space, go to the string at last index of disk_map

# pop last char of this string and fill it in the certain chunk until filled
# if this string is empty (len = 0) remove it, if unfilled go to next last string
# if filled go next to another chunk
# do til no disk_map no longer have free space

def moving_file_by_Ids(disk_map):
    map = disk_map.copy()
    product_disk_map = []

    for i,item in enumerate(map):
        if type(item) == int:
            map[i] = []
            for _ in range(item):
                # print(disk_map[-1], type(disk_map[-1]))
                if type(map[-1]) == int:
                    map.pop()

                if type(map[-1]) == list:
                    break
                map[i].append(map[-1])
                map.pop()
            # print(disk_map[i])
            product_disk_map.extend(map[i])
        else:
            product_disk_map.append(map[i])
    # print(product_disk_map)
    return product_disk_map

def moving_whole_files(disk_map):
    map = disk_map.copy()
    i = len(map)-1
    moving = False
    while True and i > -1:
        
        while type(map[i]) == int:
            i -= 1

        current_value = map[i]
        
        # print(f'Check current value: {current_value}')
        # find freq of current_value
        freq = map.count(current_value)
        size = freq * len(current_value)
        free_space = 0
        start = 0
        for j in range(0,i-1):
            # found free space
            if type(map[j]) == int:
                free_space += map[j]
                start = j
                if size <= free_space:
                    tmp_list = []
                    # replace free space
                    for _ in range(freq):
                        tmp_list.append(current_value)
                        i += 1
                    # left free space
                    if free_space - size > 0:
                        tmp_list.append(free_space - size)
                    else:
                        i -= 1
                    map[j:j+1]=tmp_list
                    moving = True
                    # print(f'Moving {current_value}')
                    break
            else:
                free_space = 0
                # free space in not enough
                # else:
                # print(f'Not enough space for {current_value}, need {freq} sizes but have {map[j]} at index {j}')
                    # continue

        # go to next Ids
        # print(f'Try to skip {map[i]} compare with {current_value}')
        while map[i] == current_value:
            if moving:
                # print(f'Remove map[i]: {map[i]}')
                map[i] = len(current_value)
            i -= 1
        # print(map)

        # 
        moving = False
    # print(map[:30])
    return map

disk_map, disk_map_2 = read_file_to_list('example.txt')

print(disk_map_2)

file_system_1 = moving_file_by_Ids(disk_map)

# file_system_2 = moving_whole_files(disk_map_2)



print('Checksum 1:', calculate_checksum(file_system_1))
# print('Checksum 2:', calculate_checksum(file_system_2))
