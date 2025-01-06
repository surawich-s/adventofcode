from collections import defaultdict, deque
def read_file_to_list(file_path):
    rules, updates = [], []
    # Open and read the file
    with open(file_path, 'r') as file:
        sections = file.read().strip().split('\n\n')
        rules = [[int(x) for x in line.split('|')] for line in sections[0].split('\n')]
        updates = [[int(x) for x in line.split(',')] for line in sections[1].split('\n')]

    return rules, updates

def create_rule_dict(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()

    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        nodes.add(x)
        nodes.add(y)

    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    
    return sorted_order
def validate_order(update, global_order):
    index_map = {page: i for i, page in enumerate(global_order)}
    for i in range(len(update) - 1):
        if index_map[update[i]] > index_map[update[i + 1]]:
            return False
    return True

def fix_update(update, global_order):
    index_map = {page: i for i, page in enumerate(global_order)}
    return sorted(update, key=lambda x: index_map[x])

def calculate_middle_pages(updates):
    return sum(update[len(update) // 2] for update in updates)

file_path = "example.txt"
rules, updates = read_file_to_list(file_path)
# print(rules)
global_order = create_rule_dict(rules)
print(global_order)

correct_updates = []
incorrect_updates = []

for update in updates:
    if validate_order(update, global_order):
        correct_updates.append(update)
    else:
        incorrect_updates.append(fix_update(update, global_order))
        
total_middle = calculate_middle_pages(correct_updates)    
total_fixed_middle = calculate_middle_pages(incorrect_updates)

print('total middle page number:', total_middle)
print('total fixed middle page number:', total_fixed_middle)