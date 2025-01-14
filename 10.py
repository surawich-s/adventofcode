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
                total_trailhead += hiking(y,x,0)
                print(total_trailhead)


def hiking(y,x,expected_level):
    
    if(x < 0 or x > len(topo_map[0])-1 or y < 0 or y > len(topo_map)-1):
        print('Out of bound')
        return 0
    
    print(f'At {y} {x}, level: {topo_map[y][x]}, expected level: {expected_level}')
    
    if topo_map[y][x] != str(expected_level):
        print('Not expected level')
        return 0
    
    if expected_level == '9':
        print('Found trailhead')
        return 1
    
    expected_level += 1

    return sum([hiking(y+1,x,expected_level), hiking(y-1,x,expected_level), hiking(y,x+1,expected_level), hiking(y,x-1,expected_level)])




topo_map = read_file_to_list('example.txt')

total_trailhead = find_starting_point(topo_map)

print(total_trailhead)