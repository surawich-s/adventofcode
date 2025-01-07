def read_file_to_list(file_path):
    maps = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    maps = text.strip().split('\n')


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
            
def traverse(x,y, dx=0, dy=-1, direction = 'n', total_unique=0):
    exit = False
    while not exit:
        next_y, next_x = y + dy, x + dx
        #  # Debug prints
        # print(f"Current position: ({y}, {x})")
        # print(f"Trying to move to: ({next_y}, {next_x})")
        # print(f"Map bounds: height={len(maps)}, width={len(maps[0])}")

        # found edges return value
        if y+dy < 0 or y+dy > len(maps)-1 or x+dx < 0 or x+dx > len(maps[0])-1:
            print('Found exit!!')
            exit = True
            break
        
        # check if this position is unique
        if [y,x] not in index_map:
            index_map.append([y,x])
            total_unique += 1

        # found next position is turning point
        if maps[y+dy][x+dx] == '#':
            # print('Next position is:', y+dy,x+dx, 'which is:',maps[y+dy][x+dx])
            direction = get_next_direction(direction)
            # print('Change direction to:', direction)
            dy,dx = direction_table[direction]
            # print('dy, dx:',dy,dx)

        # print('Traverse to:', y+dy, x+dx, 'direction:', direction)
        y += dy
        x += dx

    return total_unique + 1
            

file_path = "6.txt"
maps = read_file_to_list(file_path)

starting_point = find_starting_point(maps)

index_map = []

x,y = starting_point[0], starting_point[1]

direction_table = {'n': [-1,0], 'e': [0,1], 's': [1,0], 'w': [0,-1]}

total_unique = traverse(x,y)

print(total_unique)



