def read_file_to_list(file_path):
    # Initialize an empty list to store lines
    lines_list = []
    
    # Open and read the file
    with open(file_path, 'r') as file:
        # Read each line and append to list
        for line in file:
            # Remove trailing whitespace and newlines
            lines_list.append(line.strip())
            
    return lines_list

file_path = "2.txt"
result = read_file_to_list(file_path)

reports = []

for line in result:
    tmpline = line.split()
    reports.append([int(x) for x in tmpline])

def check_safe_with_dampener(report):
    if check_safe_report(report):
        return True
    for i in range(len(report)):
        # Create a new report excluding the current level
        modified_report = report[:i] + report[i + 1:]
        if check_safe_report(modified_report):
            return True
    return False
def check_safe_report(report):
    mode = "increasing" if(report[1] > report[0]) else "decreasing"
    for i in range(1,len(report)):
        if( abs(report[i]-report[i-1]) < 1 or abs(report[i]-report[i-1]) > 3): #check level differ or equal
                return False
        else:
            new_mode = "increasing" if(report[i] > report[i-1]) else "decreasing"
            if new_mode != mode: # inconsistency in mode
                    return False
    return True

safe_count = 0
new_safe_count = 0
for report in reports:
    safe_count += check_safe_report(report)
    new_safe_count += check_safe_with_dampener(report)

# Your existing counting code below...
print('number of safe reports:', safe_count)
print('number of new safe reports:', new_safe_count)

