from collections import defaultdict, deque
def read_file_to_list(file_path):
    rules, updates = [], []
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read entire file as one string
        text = file.read()
    list = text.split('\n\n')

    for i in list[0].split('\n'):
        rules.append([int(x) for x in i.split('|')])

    for i in list[1].split('\n'):
        updates.append([int(x) for x in i.split(',')])

    return rules, updates

def create_rule_dict(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()

    # Each pair in the rules list represents a dependency
    for rule in rules:
        # We're getting all possible pairs from the rule list
        # instead of just adjacent pairs
        x, y = rule  # This assumes only 2 numbers per rule
        graph[x].append(y)
        in_degree[y] += 1
        nodes.add(x)
        nodes.add(y)
    
    print(in_degree)

    no_outgoing = [node for node in nodes if not graph[node]]
    print("Nodes with no outgoing edges:", no_outgoing)

    self_loops = [node for node in graph if node in graph[node]]
    print("Self-loops:", self_loops)

    queue = deque([node for node in nodes if in_degree[node] == 0])

    sorted_order = []

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

     # Detect remaining nodes with non-zero in-degree (cycles)
    remaining = [node for node, degree in in_degree.items() if degree > 0]
    if remaining:
        print("Cycle detected! Remaining nodes with non-zero in-degree:", remaining)
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

file_path = "5.txt"
rules, updates = read_file_to_list(file_path)

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