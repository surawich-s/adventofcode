def read_file_to_list(file_path):
    rules = []
    updates = []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    list = text.split('\n\n')

    for i in list[0].split('\n'):
        rules.append([int(x) for x in i.split('|')])

    # print(rule)

    for i in list[1].split('\n'):
        updates.append([int(x) for x in i.split(',')])

    # print(order)
    return rules, updates

def create_rule_dict(rules):
    rule_dict = {}
    for rule in rules:
        if rule[0] not in rule_dict:
            rule_dict[rule[0]] = []
        rule_dict[rule[0]].append(rule)
    return rule_dict

def validate_update(update):
    count = 0
    for i in range(len(update)-1):
        matching_rules = rule_dict.get(update[i]) or []
        # print(matching_rules)
        if [update[i], update[i+1]] not in matching_rules:
            # print(update[i],update[i+1])
            break
        else:
            count += 1
    if count == len(update)-1:
        # print('legit:',x,'middle:',x[int(len(x)/2)])
        return True
    else:
        return False
    
def fix_update(update):
    update = update.copy()  # Create a copy to avoid modifying the original
    n = len(update)
    fixed = False
    
    while not fixed:
        fixed = True
        for i in range(n-1):
            matching_rules = rule_dict.get(update[i]) or []
            # If current pair doesn't follow rules, swap them
            if [update[i], update[i+1]] not in matching_rules:
                update[i], update[i+1] = update[i+1], update[i]
                fixed = False
    
    return update
    
def calculate_middle_pages(updates):
    return sum(update[len(update) // 2] for update in updates)

file_path = "5.txt"
rules, updates = read_file_to_list(file_path)
# print(rule)s

rule_dict = create_rule_dict(rules)

correct_updates = []
incorrect_updates = []
# matching_rules = rule_dict.get(5, [])

for update in updates:
    if validate_update(update):
        correct_updates.append(update)
    else:
        incorrect_updates.append(fix_update(update))
    
total_middle = calculate_middle_pages(correct_updates)
total_fixed_middle = calculate_middle_pages(incorrect_updates)
print('total middle page number:', total_middle)
print('total fixed middle page number:', total_fixed_middle)