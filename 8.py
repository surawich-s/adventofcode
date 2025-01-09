def read_file_to_list(file_path):
    maps = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    maps = text.strip().split('\n')
    maps = [list(line) for line in maps]


    return maps

maps = read_file_to_list('example.txt')

# print(maps)

# find those unique frequencies in maps
unique_frequency = {}
for y in range(len(maps)):
    for x in range(len(maps[0])):
        if not maps[y][x] == '.':
            # get indices of each unique frequencies
            if maps[y][x] not in unique_frequency:
                unique_frequency[maps[y][x]] = [[y,x]]
            else:
                unique_frequency[maps[y][x]].append([y,x])

# print(unique_frequency)

unique_antinode_locations = {}

def setup_antinode(xA,yA,xB,yB):
    # print(xA,yA,xB,yB)
    dy = abs(yA-yB)
    dx = abs(xA-xB)





# for each unique frequencies, run operations to set up antinodes
for positions in unique_frequency:
    for i in range(len(unique_frequency[positions])-1):
        for j in range(i+1, len(unique_frequency[positions])):
            # print(unique_frequency[positions][j])

            # compare current position of antenna then process with another antenna within same frequency
            setup_antinode(*unique_frequency[positions][i],*unique_frequency[positions][j])



    

    # determine if possible to setup an antinode, store this position [y,x]

