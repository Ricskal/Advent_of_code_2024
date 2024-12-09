import re
from itertools import combinations

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
    # (xCord , yCord) = antenna
    antennaMapDict = {}
    yCord = -1
    for line in parsedFile:
        yCord += 1
        xCord = -1
        for antenna in line:
            xCord += 1
            if antenna != '.':
                if antenna not in antennaMapDict: antennaMapDict[antenna] = [(xCord, yCord)]
                else: antennaMapDict[antenna].append((xCord, yCord))
    maxBound = (xCord, yCord)
    minBound = (0, 0)
    return antennaMapDict, minBound, maxBound

def pairAntennas(antennaMapDict):
    antennaPairDict = {}
    for antenna in antennaMapDict.keys():
        antennaPairDict[antenna] = list(combinations(antennaMapDict[antenna], 2))
    return antennaPairDict
# 1 antenna???

def calculateAntinodes(antennaPairDict, minBound, maxBound):
    antinodesSet = set()
    for antenna in antennaPairDict.keys():
        antennaPairList = antennaPairDict[antenna]
        for antennaPair in antennaPairList:
            antenna1 = antennaPair[0]
            antenna2 = antennaPair[1]
            offset = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
            # antenna1 antinodes          
            antinode1 = (antenna1[0] + offset[0], antenna1[1] + offset[1])
            antinode2 = (antenna1[0] - offset[0], antenna1[1] - offset[1])
            if antinode1 != antenna2: antinodesSet.add(antinode1)
            if antinode2 != antenna2: antinodesSet.add(antinode2)
            # antenna2 antinodes
            antinode3 = (antenna2[0] + offset[0], antenna2[1] + offset[1])
            antinode4 = (antenna2[0] - offset[0], antenna2[1] - offset[1])
            if antinode3 != antenna1: antinodesSet.add(antinode3)
            if antinode4 != antenna1: antinodesSet.add(antinode4)
    invalidAntinodesSet = set()
    for antinode in antinodesSet:
        if antinode[0] > maxBound[0] or antinode[0] < minBound[0]: invalidAntinodesSet.add(antinode)
        elif antinode[1] > maxBound[1] or antinode[1] < minBound[1]: invalidAntinodesSet.add(antinode)
    antinodesSet = antinodesSet - invalidAntinodesSet
    print(antinodesSet)
    return antinodesSet

def part1(antinodesSet):
    part1answer = len(antinodesSet)
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
antennaPairDict = pairAntennas(antennaMapDict)
antinodesSet = calculateAntinodes(antennaPairDict, minBound, maxBound)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
part1answer = part1(antinodesSet)
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