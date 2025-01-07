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
            
def traverse(x,y, dx=0, dy=-1, direction = 'n', total_unique=0):
    exit = False
    obstruction_positions = 0
    while not exit:
        # next_y, next_x = y + dy, x + dx
        #  # Debug prints
        # print(f"Current position: ({y}, {x})")
        # print(f"Trying to move to: ({next_y}, {next_x})")
        # print(f"Map bounds: height={len(maps)}, width={len(maps[0])}")

        # found edges return value
        if y+dy < 0 or y+dy > len(maps)-1 or x+dx < 0 or x+dx > len(maps[0])-1:
            print('Found exit!!')
            exit = True
            break

        if not maps[y+dy][x+dx] == '#':
            # print(f"From direction: {direction}")
            tmp_direction = get_next_direction(direction)
            # print(f"New direction: {tmp_direction}")
            tmp_dy,tmp_dx = direction_table[tmp_direction]
            # print(f"tmp_dy, tmp_dx: ({tmp_dy},{tmp_dx})")
            startx, starty = x,y
            # print(f"Starting at {y} {x}")
            obstruction_positions += traverse_with_imaginary_wall(x+tmp_dx,y+tmp_dy,tmp_dx,tmp_dy,tmp_direction, startx, starty, direction)
        
        # check if this position is unique
        if (y,x) not in index_map:
            index_map[y,x] = direction
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

    return total_unique + 1, obstruction_positions
            
def traverse_with_imaginary_wall(x,y, dx, dy, direction, startx, starty, start_direction):

    visited = set()
    while True:

        # Debug prints
        # print(f"Current position: ({y}, {x})")
        # print(f"dy, dx: ({dy},{dx})")

        current_state = (x, y, direction)
        if current_state in visited:
            return False  # We're in a cycle that's not returning to start
        visited.add(current_state)

        
        # found edges, impossible to be loop
        if y+dy < 0 or y+dy > len(maps)-1 or x+dx < 0 or x+dx > len(maps[0])-1:
            # print(f"\n\n Out of bound !! \n\n")
            return False
        
        if startx == x and starty == y and direction == start_direction:
            # print(f"Back to starting point: ({y},{x})")
            # print(f"\n\n Loop \n\n")
            return True
    
        # found next position is turning point
        # print('Next position is:', y+dy,x+dx, 'which is:',maps[y+dy][x+dx])
        if maps[y+dy][x+dx] == '#':
            
            direction = get_next_direction(direction)
            # print('Change direction to:', direction)
            dy,dx = direction_table[direction]
            # print('dy, dx:',dy,dx)
        
        y += dy
        x += dx

file_path = "6.txt"
maps = read_file_to_list(file_path)

starting_point = find_starting_point(maps)

index_map = {}

x,y = starting_point[0], starting_point[1]

direction_table = {'n': [-1,0], 'e': [0,1], 's': [1,0], 'w': [0,-1]}

total_unique, obstruction_positions = traverse(x,y)

# print(index_map)
maps = [''.join(line) for line in maps]
# print('\n'.join(maps))

print('Total unique:',total_unique)

print('Obstruction Positions:', obstruction_positions)



