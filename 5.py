## TODO
## Build new example using topological sort

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
file_path = "test.txt"
rule, order = read_file_to_list(file_path)
# print(rule)

def create_rule_dict(rules):
    rule_dict = {}
    for rule in rules:
        if rule[0] not in rule_dict:
            rule_dict[rule[0]] = []
        rule_dict[rule[0]].append(rule)
    return rule_dict

rule_dict = create_rule_dict(rule)
# matching_rules = rule_dict.get(5, [])
total_middle = 0
total_fixed_middle = 0
to_fix = []
example = []

for key in rule_dict.keys():
    if key not in example:
        # print(key, ' not in example')
        example.append(key)
    # print(example)
    # print(rule_dict[key])
    for x in rule_dict[key]:
        if x[1] not in example:
            # print(x[1], ' not in example')
            example.append(x[1])
        # else:
        #     if(example.index(x[1]) < example.index(x[0])):
        #         example.remove(x[0])
        #         # print('remove:',x[0])
        #         example.insert(example.index(x[1]), x[0])
        #         # print('move:', x[0],' to:', example.index(x[1])
    for i in range(len(example)-1):
        tmp = example[i]
        for j in range(i, len(example)-1):
            matching_rules = rule_dict.get(tmp)
            # print(matching_rules)
            if [example[j], example[j+1]] not in matching_rules:
                example.remove(tmp)
                print('remove:', tmp, 'and move to:', j+1)
                example.insert(j+1, tmp)
            else:
                break
print(example)

def fix_order(order):
    for i in range(0, len(order)-1):
        tmp = order[i]
        for j in range(i+1, len(order)):
            if example.index(tmp) > example.index(order[j]):
                order.remove(tmp)
                # print('remove:', tmp, 'and move to:', j)
                order.insert(j, tmp)
                # print(order)
    return order

for x in order:
    matching_rules = []
    count = 0
    tmp_fix = x.copy()
    for i in range(len(x)-1):
        matching_rules = rule_dict.get(x[i]) or []
        # print(matching_rules)
        if [x[i], x[i+1]] not in matching_rules:
            # print(x[i],x[i+1])
            # tmp_fix[i+1] = x[i]
            # tmp_fix[i] = x[i+1]
            break
        else:
            count += 1
    # print(count)
    if count == len(x)-1:
        # print('legit:',x,'middle:',x[int(len(x)/2)])
        total_middle += x[int(len(x)/2)]
        # if(example and len(x) > len(example)):
        #     example = x
        # if(not example):
        #     example = x
    else:
        # print(x, tmp_fix)
        tmp_fix = fix_order(tmp_fix)
        # print('fixed:',tmp_fix)
        total_fixed_middle += tmp_fix[int(len(x)/2)]

            
        
print('total middle page number:', total_middle)
print('total fixed middle page number:', total_fixed_middle)