## TODO
## Build new rule using topological sort

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
file_path = "example.txt"
rule, order = read_file_to_list(file_path)

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

for x in order:
    matching_rules = []
    count = 0
    tmp_fix = x.copy()
    for i in range(len(x)-1):
        matching_rules = rule_dict.get(x[i]) or []
        # print(matching_rules)
        if [x[i], x[i+1]] not in matching_rules:
            break
        else:
            count += 1
    # print(count)
    if count == len(x)-1:
        # print('legit:',x,'middle:',x[int(len(x)/2)])
        total_middle += x[int(len(x)/2)]

print('total middle page number:', total_middle)
print('total fixed middle page number:', total_fixed_middle)