def read_file_to_list(file_path):
    # Initialize an empty list to store lines
    lines_list = []
    
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read each line and append to list
        for line in file:
            # Remove trailing whitespace and newlines
            lines_list.append(line.strip())
            
    return lines_list

file_path = "1.txt"
result = read_file_to_list(file_path)

loc_1 = []
loc_2 = []
freq = [0] * 100000  # Initialize list with zeros (adjust size as needed)

for line in result:
    tmpline = line.split()
    loc_1.append(int(tmpline[0]))
    loc_2.append(int(tmpline[1])) 
    freq[int(tmpline[1])] += 1

loc_1.sort()
loc_2.sort()

distance = 0
similarity = 0

for x, y in zip(loc_1, loc_2):
    distance += abs(x - y)
    similarity += x * freq[x]
print("First answer:",distance)
print("Second answer:",similarity)