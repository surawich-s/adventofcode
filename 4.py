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

file_path = "4.txt"
puzzle = read_file_to_list(file_path) or []

def word_search(word, puzzle):
    word_count = 0
    def traverse_puzzle(x,y,word_pos=1,dx=0, dy=0):
        if(x < 0 or x > len(puzzle[0])-1 or y < 0 or y > len(puzzle)-1 or puzzle[y][x] != word[word_pos-1]):
            return 0
        elif(word_pos == len(word)):
            if(puzzle[y][x] == word[word_pos-1]):
                return 1
            else:
                return 0
        else:
            if(word_pos == 1):
                return sum([
                traverse_puzzle(x, y+1, word_pos+1, 0, 1),    # south
                traverse_puzzle(x+1, y+1, word_pos+1, 1, 1),  # southeast
                traverse_puzzle(x-1, y+1, word_pos+1, -1, 1), # southwest
                traverse_puzzle(x, y-1, word_pos+1, 0, -1),   # north
                traverse_puzzle(x+1, y-1, word_pos+1, 1, -1), # northeast
                traverse_puzzle(x-1, y-1, word_pos+1, -1, -1),# northwest
                traverse_puzzle(x+1, y, word_pos+1, 1, 0),    # east
                traverse_puzzle(x-1, y, word_pos+1, -1, 0)    # west
                ])
             # Continue in same direction using dx, dy
            return traverse_puzzle(x + dx, y + dy, word_pos+1, dx, dy)

    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            # traverse through puzzle 
            word_count += traverse_puzzle(j,i)
            # print(word_count, j, i)
    return word_count

def word_search_xmas(puzzle):
    word_count = 0
    m_count = 0
    s_count = 0
    def traverse_puzzle(x,y,word_pos=1):
        nonlocal m_count, s_count
        if(x < 0 or x > len(puzzle[0])-1 or y < 0 or y > len(puzzle)-1 or word_pos > 2 or m_count > 2 or s_count > 2):
            return 0
        # if(word_pos == 1):
        #     if(puzzle[y][x] != 'A'):
        #         return 0
        #     else:
        #         print('found A at position:',x,y)
        if(word_pos == 2):
            if(puzzle[y][x] == 'M'):
                m_count += 1
                print('found M at position:',x,y,'dmcount:', m_count)
            elif(puzzle[y][x] == 'S'):
                s_count += 1
                print('found S at position:',x,y,'dscount:', s_count)
            else:
                return 0
            if(m_count == 2 and s_count == 2):
                return 1
        return sum([
            traverse_puzzle(x+1, y+1, word_pos+1), # southeast
            traverse_puzzle(x-1, y+1, word_pos+1), # southwest
            traverse_puzzle(x+1, y-1, word_pos+1), # northeast
            traverse_puzzle(x-1, y-1, word_pos+1), # northwest
        ])

    for i in range(1,len(puzzle)-1):
        for j in range(1,len(puzzle[0])-1):
            # traverse through puzzle 
            
            if(puzzle[i][j] == 'A'):
                s_count = 0
                m_count = 0
                word_count += traverse_puzzle(j,i)
            
            # print(word_count, j, i)
    return word_count

result = word_search('XMAS', puzzle)
result2 = word_search_xmas(puzzle)
# print(result)
print(result2)