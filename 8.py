def read_file_to_list(file_path):
    maps = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    maps = text.strip().split('\n')
    maps = [list(line) for line in maps]


    return maps

def setup_antinode(yA,xA,yB,xB):

    def checkValid(y, x):
        # 1. Check bounds first
        if not (0 <= y <= ylen) or not (0 <= x <= xlen):
            # print(f"Position {y},{x} is out of bounds")  # Added debug print
            return False
        # print(f"Valid position: {y},{x}")
        return True
    
    # print(f"compare {yA} {xA} with {yB} {xB}")

    dy = abs(yA-yB)
    dx = abs(xA-xB)

    dYA = -dy if yA < yB else dy
    dXA = -dx if xA < xB else dx
    dYB = -dy if yB < yA else dy
    dXB = -dx if xB < xA else dx


    unique_antinode_locations_new_mode.add((yA, xA))
    unique_antinode_locations_new_mode.add((yB, xB))

    # do iteration
    count = 0
    while True:
        newYA = yA + dYA
        newXA = xA + dXA
        newYB = yB + dYB
        newXB = xB + dXB

        newA = [newYA,newXA]
        newB = [newXB,newYB]

        checkA = checkValid(*newA)
        checkB = checkValid(*newB)

        if checkA:
            if count == 0:
                unique_antinode_locations.add((newYA, newXA))
            unique_antinode_locations_new_mode.add((newYA, newXA))
            # print(f"Add antinodes on {newYA} {newXA}")
            if new_maps[newYA][newXA] == '.':
                new_maps[newYA][newXA] = '#'
        if checkB:
            if count == 0:
                unique_antinode_locations.add((newYB, newXB))
            unique_antinode_locations_new_mode.add((newYB, newXB))
            # print(f"Add antinodes on {newYB} {newXB}")
            if new_maps[newYB][newXB] == '.':
                new_maps[newYB][newXB] = '#'

        if not checkA and not checkB:
            break
        
        count += 1
        yA, xA = newYA, newXA
        yB, xB = newYB, newXB

maps = read_file_to_list('8.txt')

new_maps = maps.copy()

ylen = len(maps)-1
xlen = len(maps[0])-1

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

unique_antinode_locations = set()
unique_antinode_locations_new_mode = set()

# for each unique frequencies, run operations to set up antinodes
for positions in unique_frequency:
    # print(positions, unique_frequency[positions])
    for i in range(len(unique_frequency[positions])-1):
        for j in range(i+1, len(unique_frequency[positions])):
            # compare current position of antenna then process with another antenna within same frequency
            setup_antinode(*unique_frequency[positions][i],*unique_frequency[positions][j])

# print('\n'.join(''.join(row) for row in new_maps))
print('Number of unique antinode locations:',len(unique_antinode_locations))
print('Number of unique antinode locations with new mode:',len(unique_antinode_locations_new_mode))

    

    

