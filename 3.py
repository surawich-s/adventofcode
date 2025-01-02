import re
def read_file_to_list(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        return file.read()
    
def process_mul(text, enabled = False):
    result = 0
    mode = enabled
    x = re.findall(r"mul\((\d+),(\d+)\)|(do|don't)\(\)", text)
    # print(x)
    for set in x:
        if(set[2]):
            mode = True if set[2] == 'do' else False
        else:
            if(enabled and mode):
                result += int(set[0])*int(set[1])
            elif(not enabled):
                result += int(set[0])*int(set[1])
    return result

file_path = "3.txt"
text = read_file_to_list(file_path)
result = process_mul(text)
result2 = process_mul(text, True)
print('results of the multiplications:',result)
print('results of the enabled multiplications:',result2)



