def read_file_to_list(file_path):
    plots = []
    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()
        print(text)
        for row in text.split():
            plots.append(row)
    return plots

plots = read_file_to_list('12.txt')

# print(plots)

coordinates = set()

def count_sides(type, y, x, sides, area_count=0):
    if y < 0 or x < 0 or y == len(plots) or x == len(plots[0]) or plots[y][x] != type or (y,x) in coordinates:
        # Out of bound
        return sides, area_count
    
    # Increment area count for this cell
    area_count += 1
    
    if y == 0 or plots[y-1][x] != type:
        sides += 1
    if x == 0 or plots[y][x-1] != type:
        sides += 1
    if y == len(plots)-1 or plots[y+1][x] != type:
        sides += 1
    if x == len(plots[0])-1 or plots[y][x+1] != type:
        sides += 1

    # print(f"Count {type} at {(y,x)} add {sides} sides, area: {area_count}")

    coordinates.add((y,x))

    # Recursively check all 4 directions
    sides, area_count = count_sides(type, y-1, x, sides, area_count)  # Up
    sides, area_count = count_sides(type, y+1, x, sides, area_count)  # Down
    sides, area_count = count_sides(type, y, x-1, sides, area_count)  # Left
    sides, area_count = count_sides(type, y, x+1, sides, area_count)  # Right
    
    return sides, area_count


    

def already_count(y,x):
    if (y,x) in coordinates:
        return True

result = 0

for y in range(len(plots)):
    for x in range(len(plots[0])):
        type = plots[y][x]

        # check if this plot already count
        if not already_count(y,x):
            # print(f"Check for {plots[y][x]}")
            side_count, area = count_sides(type, y, x, 0, 0)
            # print(f"Found connected region of type {type} with area {area} and {side_count} sides")
            result += side_count * area

print(result)



        


 