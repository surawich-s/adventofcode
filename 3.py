import re
def read_file_to_list(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        return file.read()
    
def process_mul(text):
    result = 0
    x = re.findall(r"mul\((\d+),(\d+)\)", text)
    for set in x:
        result += int(set[0])*int(set[1])
    return result

file_path = "3.txt"
text = read_file_to_list(file_path)
result = process_mul(text)
print('results of the multiplications:',result)


