## variables ##
filePaths = {
    '1': 'Day 4\Input files\Input.txt',
    '2': 'Day 4\Input files\TestInput.txt',
    '3': 'Day 4\Input files\TestInputPart2.txt'
}
expectedTestOutputPart1 = 0
expectedTestOutputPart2 = 0

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
    1. Main input
    2. Test input
    3. Test input part 2
""")
choice = input("Enter choice (1/2/3): ")
input = parseFile(filePaths[choice])

# Part 1
part1answer = part1(input)
print(f'The answer to day 4 part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2
part2answer = part2(input)
print(f'The answer to day 4 part 2 = {part2answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')