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

def check_safe_report(report):
    mode = 'default'
    for i in range(len(report)):
        if(i == 0): #init
            tmp = report[i]
        else:
            if(report[i] == tmp or abs(report[i]-tmp) > 3): #check level differ
                return 0 #unsafe report
            if(abs(report[i]-tmp) > 0):
                tmp_mode = "increasing" if(report[i] > tmp) else "decreasing"
                if(mode == "default"): 
                    mode = "increasing" if(report[i] > tmp) else "decreasing" #init mode
                else: #to compare mode
                    if (tmp_mode != mode):
                        return 0 #inconsitent mode unsafe
                    else:
                        mode = tmp_mode
                tmp = report[i] #update tmp
    return 1

safe_count = 0
for report in reports:
    safe_count += check_safe_report(report)
print('number of safe reports:', safe_count)

