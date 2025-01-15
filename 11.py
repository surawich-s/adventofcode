from collections import defaultdict

def read_file_to_list(file_path):
    stones = []
    # Open and read the file
    with open(file_path, 'r') as file:
        text = file.read()
        stones = defaultdict(int)
        for stone in text.split():
            stone = int(stone)
            stones[stone] += 1
    return stones

def blink_time(blinks):
    for i in range(blinks):
        blink()
        # print(i+1, stones)
    return

def blink():
    tmp_stone = dict(stones)

    for stone, count in tmp_stone.items():
        if count == 0: continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid = len(str_stone) // 2
            first = int(str_stone[:mid])
            second = int(str_stone[mid:])
            stones[first] += count
            stones[second] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count
    return
    

stones = read_file_to_list('11.txt')
number_of_blink = 75
# print(stones)
blink_time(number_of_blink)
print(f'Stones = {sum(stones.values())}')







# print(list)