# recieve string of input

# for index that modular 2 == 1 (odd): add it to free space list as a chunk of free space [3,3,...]

# for index that is even: add it to data list as a chunk of data [00,[],111,[],2222,...]


def read_file_to_list(file_path):
    disk_map = []
    free_chunk = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
        index_count = 0
        for i in range(len(text)):
            if i % 2 == 0:
                disk_map.append(str(index_count) * int(text[i]))
                index_count += 1
            else:
                disk_map.append([int(text[i])])
    return disk_map

result = read_file_to_list('example.txt')

print(result)