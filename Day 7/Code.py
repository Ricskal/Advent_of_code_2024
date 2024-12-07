from itertools import product
import re

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
expectedTestOutputPart1 = 3749
expectedTestOutputPart2 = 0

## Methods ##
def parseFile(filepath):
    calculationDict = {}
    with open(filepath, 'r') as file:
        for line in file:
            outcome, numbersStr = line.split(':')
            numbersStrList = numbersStr.strip().split(' ')
            numberList = [int(number) for number in numbersStrList]
            calculationDict[int(outcome)] = numberList
    return calculationDict

def generateExpressions(numberList):
    operators = ['+', '*']
    n = len(numberList)
    expressions = []
    numberOfBrackets = n -1
    
    # Generate all combinations of operators for n-1 slots
    for ops in product(operators, repeat=n-1):
        firstNumber = True
        expression = []
        for j in range(numberOfBrackets): expression.append('(')
        for i in range(n):
            expression.append(str(numberList[i]))
            if not firstNumber: expression.append(')')
            if i < n-1:
                expression.append(ops[i])
            firstNumber = False
        expressions.append(' '.join(expression))
    return expressions

def part1(calculationDict):
    part1answer = 0
    for key in calculationDict.keys():
        outcome = key
        expressionList = generateExpressions(calculationDict[key])
        for expression in expressionList:
            if eval(expression) == outcome:
                print(f'Expression: {expression} evaluates to {outcome}')
                part1answer += outcome
                break
    return part1answer

def part2(input):
    part2answer = 0
    return part2answer

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
calculationDict = parseFile(filePaths[choice])
part1answer = part1(calculationDict)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
part2answer = part2(input)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')