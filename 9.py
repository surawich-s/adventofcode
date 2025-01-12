

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
                for _ in range(int(text[i])):
                    disk_map.append(str(index_count))
                disk_map_2.append((i//2+1, int(text[i])))
                index_count += 1
            else:
                disk_map.append(int(text[i]))
                disk_map_2.append((0, int(text[i])))

    return disk_map, disk_map_2

def calculate_checksum(map):
    checksum = 0
    # print(map)
    for i in range(len(map)):
        if(map[i] == '.' or map[i] == -1):
            continue
        checksum += i * int(map[i])
    return checksum

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
    items = disk_map
    # print(items)
    for i in range(len(items))[::-1]:
        for j in range(i):
            i_data, i_size = items[i]
            j_data, j_size = items[j]

            if i_data and not j_data and i_size <= j_size:
                items[i] = (0, i_size)
                items[j] = (0, j_size - i_size)
                items.insert(j, (i_data, i_size))   
        # print(items)
        

    # Flatten the disk map
    # print(items)
    flat_map = []
    for file_id, size in items:
        flat_map.extend([file_id-1] * size)

    # flatten = lambda x: [x for x in x for x in x]


    # print(sum(i*(c-1) for i,c in enumerate(flatten(
    # [d]*s for d,s in items)) if c))    

    # print(flat_map)
    return flat_map


disk_map, disk_map_2 = read_file_to_list('9.txt')

# print(disk_map_2)

file_system_1 = moving_file_by_Ids(disk_map)

file_system_2 = moving_whole_files(disk_map_2)

print('Checksum 1:', calculate_checksum(file_system_1))
print('Checksum 2:', calculate_checksum(file_system_2))
