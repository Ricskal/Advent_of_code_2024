import re

## variables ##
patternPart1 = r"(mul)\((\d{1,3}),(\d{1,3})\)"
patternPart2 = r"don't\(\)(.*?)do\(\)"
filePaths = {
    '1': 'Day 3\Input files\Input.txt',
    '2': 'Day 3\Input files\TestInput.txt',
    '3': 'Day 3\Input files\TestInputPart2.txt'
}
defaultFile = False
expectedTestOutputPart1 = 161
expectedTestOutputPart2 = 48

## Methods ##
def parseFile(filepath):
    parsedFile = ""
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile += line
    # This is needed for part 2
    parsedFile += 'do()'
    return parsedFile

def part1(input):
    part1answer = 0
    uncorruptMemory = re.findall(patternPart1, input)
    for multiplication in uncorruptMemory:
        part1answer += (int(multiplication[1]) * int(multiplication[2]))
    return part1answer

def part2(input, part1answer):
    part2answer = 0
    doNotMemoryList = re.findall(patternPart2, input, re.DOTALL)
    for donotMemory in doNotMemoryList:
        multiplicationList = re.findall(patternPart1, donotMemory)
        for multiplication in multiplicationList:
            part2answer += (int(multiplication[1]) * int(multiplication[2]))
    return part1answer - part2answer

## Main execution ##
# Prompt user for input choice and parse file
if defaultFile: choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
        3. Test input part 2
    """)
    choice = input("Enter choice (1/2): ")
input = parseFile(filePaths[choice])

# Part 1
part1answer = part1(input)
print(f'The answer to day 3 part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2
part2answer = part2(input, part1answer)
print(f'The answer to day 3 part 2 = {part2answer}')
if choice == '3':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')