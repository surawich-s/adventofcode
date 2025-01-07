def read_file_to_list(file_path):
    maps = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    maps = text.split('\n')


    return maps

def find_starting_point(maps):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if(maps[i][j] == '^'):
                return [j,i]
            
def get_next_direction(current_key):
    keys = list(direction_table.keys())
    current_index = keys.index(current_key)
    next_index = (current_index + 1) % len(keys)
    return keys[next_index]
            
def traverse_map(maps, starting_point):

    index_map = []

    x,y = starting_point[0], starting_point[1]

    def traverse(x,y, dx=0, dy=-1, direction = 'n', total_unique=0):
        print('Starting at:',y,x)

        # found edges return value
        if y+dy < 0 or y+dy > len(maps)-1 or x+dx < 0 or x+dx > len(maps[0])-1:
            print('Found exit!!')
            return total_unique
        
        # check if this position is unique
        if [y,x] not in index_map:
            index_map.append([y,x])
            total_unique += 1

        # found next position is turning point
        print('Next position is:', y+dy,x+dx, 'which is:',maps[y+dy][x+dx])
        if maps[y+dy][x+dx] == '#':
            direction = get_next_direction(direction)
            print('Change direction to:', direction)
            dy,dx = direction_table[direction]
            print('dy, dx:',dy,dx)

        print('Traverse to:', y+dy, x+dx, 'direction:', direction)

        return traverse(x+dx, y+dy, dx, dy, direction, total_unique)

    total = traverse(x,y)
    return total + 1
            
        
        


file_path = "example.txt"
maps = read_file_to_list(file_path)

print(maps)

starting_point = find_starting_point(maps)

direction_table = {'n': [-1,0], 'e': [0,1], 's': [1,0], 'w': [0,-1]}

total_unique = traverse_map(maps, starting_point)

print(total_unique)



