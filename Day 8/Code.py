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
defaultFile = True
expectedTestOutputPart1 = 14
expectedTestOutputPart2 = 0

## Methods ##
def parseFile(filepath):
    parsedFile = []
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    return parsedFile

def mapTheAntennas(parsedFile):
    # (xCord , yCord) = frequency
    antennaMapDict = {}
    yCord = -1
    for line in parsedFile:
        yCord += 1
        xCord = -1
        for frequency in line:
            xCord += 1
            if frequency != '.':
                if frequency not in antennaMapDict: antennaMapDict[frequency] = [(xCord, yCord)]
                else: antennaMapDict[frequency].append((xCord, yCord))
    maxBound = (xCord, yCord)
    minBound = (0, 0)
    return antennaMapDict, minBound, maxBound

# def calculateAntinodes(antennaMapDict):
#     for antenna in antennaMapDict.keys():
    
    
def part1(input):
    part1answer = 0
    # pairs = list(combinations(inputs, 2))
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
input = parseFile(filePaths[choice])
antennaMapDict, minBound, maxBound = mapTheAntennas(input)
# calculateAntinodes(antennaMapDict)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
part1answer = part1(input)
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