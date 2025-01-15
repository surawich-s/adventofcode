def read_file_to_list(file_path):
    stones = []
    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()
        stones = text.strip().split(' ')
    return stones

def change_stone(stone):

    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        mid_position = len(stone)//2
        first = str(int(stone[0:mid_position]))
        second = str(int(stone[mid_position:]))
        return [first, second]
    return [str(int(stone)*2024)]

stones = read_file_to_list('11.txt')
number_of_blink = 25

for i in range(number_of_blink):
    new_stones = []
    for x in stones:
        stone = change_stone(x)
        new_stones.extend(stone)
    stones = new_stones.copy()
    # print(stones)
print(stones)
print(len(stones))