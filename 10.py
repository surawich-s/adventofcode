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
    total_rating = 0
    for y in range(len(topo_map)):
        for x in range(len(topo_map[0])):
            if topo_map[y][x] == '0':
                rating, trailhead = hiking(y,x,0,set())
                total_trailhead += trailhead
                total_rating += rating
                # print(total_trailhead)

    return total_trailhead, total_rating


def hiking(y,x,expected_level,trailheads):
    # print(f'At {y} {x}, expected level: {expected_level}')
    if(x < 0 or x >= len(topo_map[0]) or y < 0 or y >= len(topo_map)):
        # print('Out of bound')
        return 0, len(trailheads)
    
    if topo_map[y][x] != str(expected_level):
        # print('Not expected level')
        return 0, len(trailheads)
    
    if expected_level == 9:
        # check if unique trailhead, if add to trailhead and count trailhead
        if (y,x) not in trailheads:
            trailheads.add((y,x))
            # print('Found trailhead')
        return 1, len(trailheads)
        
    
    expected_level += 1

    total_sum = 0
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # South, North, East, West
        result, _ = hiking(y + dy, x + dx, expected_level, trailheads)
        total_sum += result

    return total_sum, len(trailheads)



topo_map = read_file_to_list('10.txt')

total_trailhead, total_rating = find_starting_point(topo_map)

print(total_trailhead, total_rating)