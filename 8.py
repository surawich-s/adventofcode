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
    print(f"compare {yA} {xA} with {yB} {xB}")
    dy = abs(yA-yB)
    dx = abs(xA-xB)

    newYA = yA - dy if yA < yB else yA + dy
    newXA = xA - dx if xA < xB else xA + dx
    newXB = xB - dx if xB < xA else xB + dx
    newYB = yB - dy if yB < yA else yB + dy


    # determine if possible to setup an antinode, store this position [y,x]

    # check if this indices permissable

    newA = [newYA,newXA]
    newB = [newXB,newYB]

    def checkValid(y, x):
        # 1. Check bounds first
        if not (0 <= y <= ylen) or not (0 <= x <= xlen):
            print(f"Position {y},{x} is out of bounds")  # Added debug print
            return False
        
        # Didn't need to check for vacant because antinode can be overlapped with antenna
        # 2. Should check new_maps instead of maps
        # if new_maps[y][x] == '#':  # Simplified comparison
        #     print(f"Position {y},{x} is occupied by {new_maps[y][x]}")  # Added debug print
        #     return False
        
        print(f"Valid position: {y},{x}")
        return True

    if checkValid(*newA):
        unique_antinode_locations.add((newYA, newXA))
        print(f"Add antinodes on {maps[newYA][newXA]}")
        if new_maps[newYA][newXA] == '.':
            new_maps[newYA][newXA] = '#'
    if checkValid(*newB):
        unique_antinode_locations.add((newYB, newXB))
        print(f"Add antinodes on {maps[newYB][newXB]}")
        if new_maps[newYB][newXB] == '.':
            new_maps[newYB][newXB] = '#'

maps = read_file_to_list('example.txt')

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

# for each unique frequencies, run operations to set up antinodes
for positions in unique_frequency:
    print(positions, unique_frequency[positions])
    for i in range(len(unique_frequency[positions])-1):
        for j in range(i+1, len(unique_frequency[positions])):
            

            # compare current position of antenna then process with another antenna within same frequency
            setup_antinode(*unique_frequency[positions][i],*unique_frequency[positions][j])

print('\n'.join(''.join(row) for row in new_maps))
print(len(unique_antinode_locations))

    

    

