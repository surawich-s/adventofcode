def read_file_to_list(file_path):
    maps = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    maps = text.strip().split('\n')
    maps = [list(line) for line in maps]


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
            
def traverse(x,y, dx=0, dy=-1, direction = 'n'):
    visited_positions = set()  # Track unique (x, y) positions
    visited_states = set()  # Track (x, y, direction) states
    while True:
        # maps[y][x] = 'x'
        # next_y, next_x = y + dy, x + dx
        #  # Debug prints
        # print(f"Current position: ({y}, {x})")
        # print(f"Trying to move to: ({next_y}, {next_x})")
        # print(f"Map bounds: height={len(maps)}, width={len(maps[0])}")
        visited_positions.add((x,y))
        state = (x, y, direction)
        if state in visited_states:
            return 0  # Loop detected
        visited_states.add(state)

        # found edges return value
        if y+dy < 0 or y+dy > len(maps)-1 or x+dx < 0 or x+dx > len(maps[0])-1:
            # print('Found exit!!')
            break

        # found next position is turning point
        if maps[y+dy][x+dx] == '#':
            # print('Next position is:', y+dy,x+dx, 'which is:',maps[y+dy][x+dx])
            direction = get_next_direction(direction)
            # print('Change direction to:', direction)
            dy,dx = direction_table[direction]
            # print('dy, dx:',dy,dx)
        else:
        
            # print('Traverse to:', y+dy, x+dx, 'direction:', direction)
            y += dy
            x += dx

    return len(visited_positions)
            
def traverse_with_imaginary_wall(maps):
    obstruction_positions = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
             if not maps[i][j] == '#' and not maps[i][j] == '^':
                
                original_char = maps[i][j]
                
                maps[i][j] = '#'

                if traverse(starting_point[0], starting_point[1]) == 0:
                    obstruction_positions += 1
                maps[i][j] = original_char
    return obstruction_positions

file_path = "6.txt"

maps = read_file_to_list(file_path)

starting_point = find_starting_point(maps)

x,y = starting_point[0], starting_point[1]

direction_table = {'n': [-1,0], 'e': [0,1], 's': [1,0], 'w': [0,-1]}

total_unique = traverse(x,y)

obstruction_positions = traverse_with_imaginary_wall(maps)

print('Total unique:',total_unique)

print('Obstruction Positions:', obstruction_positions)



