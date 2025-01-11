# recieve string of input

# for index that is even: add it to data list as a chunk of data [00,[],111,[],2222,...]

def read_file_to_list(file_path):
    disk_map = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
        text = text.strip()
        index_count = 0
        for i in range(len(text)):
            if i % 2 == 0:
                disk_map.append(str(index_count) * int(text[i]))
                index_count += 1
            else:
                if text[i] != '0':
                    disk_map.append(int(text[i]))
    return disk_map

disk_map = read_file_to_list('9.txt')

# print(disk_map)

# iterate through disk_map for i in range: if find certain chunk of free space, go to the string at last index of disk_map

# pop last char of this string and fill it in the certain chunk until filled
# if this string is empty (len = 0) remove it, if unfilled go to next last string
# if filled go next to another chunk
# do til no disk_map no longer have free space

for i,item in enumerate(disk_map):
    if type(item) == int:
        disk_map[i] = []
        for _ in range(item):
            # print(disk_map[-1], type(disk_map[-1]))
            if type(disk_map[-1]) == int:
                disk_map.pop()
            
            disk_map[i].append(disk_map[-1][-1])
            disk_map[-1] = disk_map[-1][:-1]
            if len(disk_map[-1]) == 0:
                disk_map.pop()
        disk_map[i] = ''.join(disk_map[i])

disk_map = ''.join(disk_map)
print(disk_map)
                
# calculate checksum
checksum = 0
for i in range(len(disk_map)):
    checksum += i * int(disk_map[i])

print('Checksum:', checksum)