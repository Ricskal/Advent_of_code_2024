## variables ##
filePaths = {
    '1': 'Day X\Input files\Input.txt',
    '2': 'Day X\Input files\TestInput.txt',
    '3': 'Day X\Input files\TestInputPart2.txt'
}

## Methods ##
def parseFile(filepath):
    parsedFile = ""
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile += line
    return parsedFile

def part1(input):
    part1answer = 0
    return part1answer

def part2(input):
    part2answer = 0
    return part2answer

## Main execution ##
# Prompt user for input choice and parse file
print("""
Select input file to use:
    1. Main Input
    2. Test Input
    3. Test Input part 2
""")
choice = input("Enter choice (1/2/3): ")
input = parseFile(filePaths[choice])

# Part 1
print(f'The answer to day 1 part 1 = {part1(input)}')

# Part 2
# print(f'The answer to day 1 part 2 = {part2(input)}')