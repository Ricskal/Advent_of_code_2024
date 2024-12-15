import re
from sympy import symbols, Eq, solve

## Variables and Configuration ##
# Extract the current day number from the file path using a regular expression
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)  # Extract the day number from the regex match

# Define file paths for input and test input files based on the current day
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
# Configuration for whether to use the default file and expected outputs for tests
defaultFile = False
expectedTestOutputPart1 = 480
expectedTestOutputPart2 = 875318608908

## Methods ##
def parse_file(filepath):
    # Read and parse the input file into separate data sets
    data_sets = []
    with open(filepath, 'r') as file:
        content = file.read()
        # Split the content into separate datasets based on double newlines
        data_sets = content.strip().split('\n\n')
    print(data_sets)
    return data_sets

def part_1(data_sets):
    tokens = 0
    for index, dataset in enumerate(data_sets, start=1):
        # Extract numerical values from the dataset using regular expressions
        button_A_match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", dataset)
        button_B_match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", dataset)
        prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", dataset)
        
        # Convert the extracted string matches to integers for calculations
        button_A_X_increase = int(button_A_match.group(1))
        button_A_Y_increase = int(button_A_match.group(2))
        button_B_X_increase = int(button_B_match.group(1))
        button_B_Y_increase = int(button_B_match.group(2))
        X_Prize = int(prize_match.group(1))
        Y_Prize = int(prize_match.group(2))

        # Define symbolic variables for solving equations
        a, b = symbols('a b')
        
        # Create equations for solving the distribution of resources
        eq1 = Eq(a * button_A_X_increase + b * button_B_X_increase, X_Prize)
        eq2 = Eq(a * button_A_Y_increase + b * button_B_Y_increase, Y_Prize)
        
        # Solve the equations symbolically to find values of a and b
        solution = solve((eq1, eq2), (a, b))

        # Check if the solution exists and whether it's integral
        if solution and solution[a] == int(solution[a]) and solution[b] == int(solution[b]):
            a_value, b_value = solution[a], solution[b] 
            # Calculate the tokens based on the solution
            tokens += ((3*a_value) + b_value)    
    return tokens

def part_2(data_sets):
    tokens = 0
    for index, dataset in enumerate(data_sets, start=1):
        # Extract numerical values from the dataset using regular expressions
        button_A_match = re.search(r"Button A: X\+(\d+), Y\+(\d+)", dataset)
        button_B_match = re.search(r"Button B: X\+(\d+), Y\+(\d+)", dataset)
        prize_match = re.search(r"Prize: X=(\d+), Y=(\d+)", dataset)
        
        # Convert the extracted string matches to integers for calculations
        button_A_X_increase = int(button_A_match.group(1))
        button_A_Y_increase = int(button_A_match.group(2))
        button_B_X_increase = int(button_B_match.group(1))
        button_B_Y_increase = int(button_B_match.group(2))
        
        # Increase the prize values by a large number for part 2 computations
        X_Prize = int(prize_match.group(1)) + 10000000000000
        Y_Prize = int(prize_match.group(2)) + 10000000000000

        # Define symbolic variables for solving equations
        a, b = symbols('a b')
        
        # Create equations for solving the distribution of resources
        eq1 = Eq(a * button_A_X_increase + b * button_B_X_increase, X_Prize)
        eq2 = Eq(a * button_A_Y_increase + b * button_B_Y_increase, Y_Prize)
        
        # Solve the equations symbolically to find values of a and b
        solution = solve((eq1, eq2), (a, b))

        # Check if the solution exists and whether it's integral
        if solution and solution[a] == int(solution[a]) and solution[b] == int(solution[b]):
            a_value, b_value = solution[a], solution[b] 
            # Calculate the tokens based on the solution
            tokens += ((3*a_value) + b_value) 
    return tokens

## Main execution ##
# Prompt user to select which input file to use
if defaultFile: choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")
    
# Parse the input file and process it into data sets
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