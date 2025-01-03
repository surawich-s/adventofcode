def read_file_to_list(file_path):
    rule = []
    order = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    list = text.split('\n\n')

    for i in list[0].split('\n'):
        rule.append([int(x) for x in i.split('|')])

    # print(rule)

    for i in list[1].split('\n'):
        order.append([int(x) for x in i.split(',')])

    # print(order)
    return rule, order
file_path = "5.txt"
rule, order = read_file_to_list(file_path)
print( order)