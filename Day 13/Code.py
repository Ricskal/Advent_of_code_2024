import re
from sympy import symbols, Eq, solve

## Variables and Configuration ##
# Extract the current day number from the file path
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define file paths for input and test input files
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
# Default configuration for input file and expected outputs for tests
defaultFile = False
expectedTestOutputPart1 = 480
expectedTestOutputPart2 = 0


## Methods ##
def parse_file(filepath):
    data_sets = []
    with open(filepath, 'r') as file:
        content = file.read()
        # Split de inhoud volgens het formaat van je gegevens
        data_sets = content.strip().split('\n\n')
    print(data_sets)
    return data_sets

def part_1(data_sets):
    tokens=0
    for index, dataset in enumerate(data_sets, start=1):
        button_A_match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", dataset)
        button_B_match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", dataset)
        prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", dataset)
        button_A_X_increase = int(button_A_match.group(1))
        button_A_Y_increase = int(button_A_match.group(2))
        button_B_X_increase = int(button_B_match.group(1))
        button_B_Y_increase = int(button_B_match.group(2))
        X_Prize = int(prize_match.group(1))
        Y_Prize = int(prize_match.group(2))
        a, b = symbols('a b')
        eq1 = Eq(a * button_A_X_increase + b * button_B_X_increase, X_Prize)
        eq2 = Eq(a * button_A_Y_increase + b * button_B_Y_increase, Y_Prize)
        solution = solve((eq1, eq2), (a, b))
        if solution and solution[a] == int(solution[a]) and solution[b] == int(solution[b]):
            a_value, b_value = solution[a], solution[b] 
            tokens += ((3*a_value)+b_value)    
    return tokens

def part_2(data_sets):
    tokens=0
    for index, dataset in enumerate(data_sets, start=1):
        button_A_match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", dataset)
        button_B_match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", dataset)
        prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", dataset)
        button_A_X_increase = int(button_A_match.group(1))
        button_A_Y_increase = int(button_A_match.group(2))
        button_B_X_increase = int(button_B_match.group(1))
        button_B_Y_increase = int(button_B_match.group(2))
        X_Prize = int(prize_match.group(1))+10000000000000
        Y_Prize = int(prize_match.group(2))+10000000000000
        a, b = symbols('a b')
        eq1 = Eq(a * button_A_X_increase + b * button_B_X_increase, X_Prize)
        eq2 = Eq(a * button_A_Y_increase + b * button_B_Y_increase, Y_Prize)
        solution = solve((eq1, eq2), (a, b))
        if solution and solution[a] == int(solution[a]) and solution[b] == int(solution[b]):
            a_value, b_value = solution[a], solution[b] 
            tokens += ((3*a_value)+b_value) 
    return tokens

## Main execution ##
# Prompt user for input choice and parse file
if defaultFile: choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")
    
# Parse the input file and process it into data
data_sets = parse_file(filePaths[choice])
part1answer = part_1(data_sets)
part2answer = part_2(data_sets)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')