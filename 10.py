def read_file_to_list(file_path):
    topo_map = []
    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()
        topo_map = text.strip().split('\n')
        topo_map =[list(line) for line in topo_map]
    return topo_map

def find_starting_point(topo_map):
    total_trailhead = 0
    for y in range(len(topo_map)):
        for x in range(len(topo_map[0])):
            if topo_map[y][x] == '0':
                total_trailhead += hiking(y,x,0,set())
                # print(total_trailhead)

    return total_trailhead


def hiking(y,x,expected_level,trailheads):
    # print(f'At {y} {x}, expected level: {expected_level}')
    if(x < 0 or x >= len(topo_map[0]) or y < 0 or y >= len(topo_map)):
        # print('Out of bound')
        return 0
    
    if topo_map[y][x] != str(expected_level):
        # print('Not expected level')
        return 0
    
    if expected_level == 9:
        # check if unique trailhead, if add to trailhead and count trailhead
        if (y,x) not in trailheads:
            trailheads.add((y,x))
            # print('Found trailhead')
            return 1
    
    expected_level += 1

    return sum([
        hiking(y + 1, x, expected_level,trailheads),  # South
        hiking(y - 1, x, expected_level,trailheads),  # North
        hiking(y, x + 1, expected_level,trailheads),  # East
        hiking(y, x - 1, expected_level,trailheads)   # West
    ])



topo_map = read_file_to_list('10.txt')

total_trailhead = find_starting_point(topo_map)

print(total_trailhead)