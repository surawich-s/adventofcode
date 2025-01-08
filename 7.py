def read_file_to_list(file_path):
    calibrations = {}
    # Open and read the file
    with open(file_path, 'r') as file:
        lines = file.read()
        lines = lines.split('\n')
        for line in lines:
            result, operators = line.strip().split(':')
            result = int(result)
            operators = [int(x) for x in operators.split()]
            
            if result in calibrations:
                calibrations[result].append(operators)
            else:
                calibrations[result] = [operators]
    return calibrations

calibrations = read_file_to_list('7.txt')

total_calibration_result = 0

for result in calibrations:
    for operators in calibrations[result]:
        def possible_result(index, sum, mode):

            
            
            if mode == '+':
                sum += operators[index]
                # print(f"result: {result}, operators: {operators}, sum: {sum}")
            if mode == '*':
                sum = sum * operators[index]
                # print(f"result: {result}, operators: {operators}, sum: {sum}")
            if mode == '||':
                sum = int(str(sum) + str(operators[index]))

            if sum > result:
                return False
            
            if index == len(operators)-1 :
                return sum == result

            return possible_result(index+1, sum, '+') or possible_result(index+1, sum, '*') or possible_result(index+1, sum, '||')

        if possible_result(0,0,'+'):
            total_calibration_result += result

print(total_calibration_result)
