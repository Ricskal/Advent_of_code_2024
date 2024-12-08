from itertools import product
import re

## Variables and Configuration ##
# Extract the day number from the file path using a regular expression
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define the file paths for input and test input files based on the day number
filePaths = {
    '1': 'Day ' + str(day) + '\\Input files\\Input.txt',
    '2': 'Day ' + str(day) + '\\Input files\\TestInput.txt',
}

# Default file configuration and expected outputs for testing
defaultFile = False
expectedTestOutputPart1 = 3749
expectedTestOutputPart2 = 11387

## Methods ##
# Function to parse the input file and return a dictionary of outcomes and number lists
def parseFile(filepath):
    calculationDict = {}
    with open(filepath, 'r') as file:
        for line in file:
            # Split each line into outcome and numbers
            outcome, numbersStr = line.split(':')
            # Convert the number strings into a list of integers
            numbersStrList = numbersStr.strip().split(' ')
            numberList = [int(number) for number in numbersStrList]
            # Add to the dictionary with the outcome as the key
            calculationDict[int(outcome)] = numberList
    return calculationDict

# Generate all possible expressions with combinations of numbers and operators
def generateExpressions(numberList, operators):
    n = len(numberList)
    expressionsList = []
    # Generate all combinations of operators for the number of gaps between numbers
    for ops in product(operators, repeat=n-1):
        expression = []
        for i in range(n):
            # Add number to expression list
            expression.append(str(numberList[i]))
            # Add operator if not at the last number
            if i < n-1:
                expression.append(ops[i])
        expressionsList.append(expression)
    return expressionsList

# Evaluate the generated expressions to find the desired outcome
def evaluateExpressions(calculationDict, operators):
    outcomeSum = 0
    # Iterate over each key in the calculation dictionary
    for key in calculationDict.keys():
        desiredOutcome = key
        # Generate possible expressions for a given number list
        expressionList = generateExpressions(calculationDict[key], operators)
        # Evaluate each expression
        for expression in expressionList:
            while len(expression) > 1:
                # Evaluate the first operator and two numbers
                number1 = expression[0]
                operator = expression[1]
                number2 = expression[2]
                if operator != '||': 
                    # Calculate outcome with operator and replace first three elements
                    outcome = str(eval(number1 + operator + number2))
                    expression[0: 3] = [outcome]
                else:
                    # Concatenate the numbers as a string without evaluating
                    outcome = str(number1) + number2
                    expression[0: 3] = [outcome]
            # If desired outcome is achieved, add to the total outcome sum
            if desiredOutcome == int(expression[0]):
                outcomeSum += int(expression[0])
                break
    return outcomeSum

# Run Part 1 of the solution using the specified operators
def part1(calculationDict):
    operators = ['+', '*']
    part1answer = evaluateExpressions(calculationDict, operators)
    return part1answer

# Run Part 2 of the solution with an additional concatenation operator
def part2(input):
    operators = ['+', '*', '||']
    part2answer = evaluateExpressions(calculationDict, operators)
    return part2answer

## Main execution ##
# Choose the input file and parse it into a usable dictionary
if defaultFile: 
    choice = '2'
else:
    # Prompt user for input file selection
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")
    
# Parse the selected input file
calculationDict = parseFile(filePaths[choice])

# Part 1 outputs and test verification if using the test input
part1answer = part1(calculationDict)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs and test verification if using the test input
part2answer = part2(calculationDict)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')