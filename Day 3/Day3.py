import re

## variables ##
patternPart1 = r"(mul)\((\d{1,3}),(\d{1,3})\)"
patternPart2 = r"don't\(\)(.*?)do\(\)"
filePaths = {
    '1': 'Day 3\Input files\Input.txt',
    '2': 'Day 3\Input files\TestInput.txt',
    '3': 'Day 3\Input files\TestInputPart2.txt'
}

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
print("""
Select input file to use:
    1. Main Input
    2. Test Input
    3. Test Input Part 2
""")
choice = input("Enter choice (1/2/3): ")
input = parseFile(filePaths[choice])

# Part 1
print(f'The answer to day 1 part 1 = {part1(input)}')

# Part 2
print(f'The answer to day 1 part 2 = {part2(input, part1(input))}')