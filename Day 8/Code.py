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
expectedTestOutputPart2 = 34

## Methods ##
def parseFile(filepath):
    parsedFile = []
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    return parsedFile

def mapTheAntennas(parsedFile):
    # Maps antenna positions to coordinates and organizes them into a dictionary
    # (xCord , yCord) = antenna
    antennaMapDict = {}
    yCord = -1
    for line in parsedFile:
        yCord += 1
        xCord = -1
        for antenna in line:
            xCord += 1
            # Logic to skip empty positions '.' and map antenna coordinates
            if antenna != '.':
                if antenna not in antennaMapDict: antennaMapDict[antenna] = [(xCord, yCord)]
                else: antennaMapDict[antenna].append((xCord, yCord))
   # Define boundaries for the antenna map
    maxBound = (xCord, yCord)
    minBound = (0, 0)
    return antennaMapDict, minBound, maxBound

def pairAntennas(antennaMapDict):
    # Creates all unique pairs of coordinates for each type of antenna
    antennaPairDict = {}
    for antenna in antennaMapDict.keys():
        antennaPairDict[antenna] = list(combinations(antennaMapDict[antenna], 2))
    return antennaPairDict

# def part1(antennaPairDict, minBound, maxBound):
#     # Computes positions for potential antinodes and applies boundary filtering
#     antinodesSet = set()
#     for antenna in antennaPairDict.keys():
#         antennaPairList = antennaPairDict[antenna]
#         for antennaPair in antennaPairList:
#             antenna1 = antennaPair[0]
#             antenna2 = antennaPair[1]
#             offset = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
#             # Calculate potential antinodes for both antennas in the pair
#             # Adding and subtracting offset from each coordinate
#             antinodesList = [
#                 (antenna1[0] + offset[0], antenna1[1] + offset[1]),
#                 (antenna1[0] - offset[0], antenna1[1] - offset[1]),
#                 (antenna2[0] + offset[0], antenna2[1] + offset[1]),
#                 (antenna2[0] - offset[0], antenna2[1] - offset[1])
#             ]    
#             # Add valid antinodes, they cannot overlap their own antenna's
#             for antinode in antinodesList:
#                 if antinode not in (antenna1, antenna2):
#                     antinodesSet.add(antinode)
#     # Filtering antinodes that are out of specified bounds
#     invalidAntinodesSet = set()
#     for antinode in antinodesSet:
#         if antinode[0] > maxBound[0] or antinode[0] < minBound[0]: invalidAntinodesSet.add(antinode)
#         elif antinode[1] > maxBound[1] or antinode[1] < minBound[1]: invalidAntinodesSet.add(antinode)
#     antinodesSet = antinodesSet - invalidAntinodesSet
#     return len(antinodesSet)

def part2(antennaPairDict, minBound, maxBound):
    # Computes positions for potential antinodes and applies boundary filtering
    antinodesSet = set()
    for antenna in antennaPairDict.keys():
        antennaPairList = antennaPairDict[antenna]
        for antennaPair in antennaPairList:
            antenna1 = antennaPair[0]
            antenna2 = antennaPair[1]
            offset = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])

            i = 0
            antinodesList = []
            while i < 1000:
            
                antinodesList.append((antenna1[0] + offset[0] *i, antenna1[1] + offset[1] *i))
                antinodesList.append((antenna1[0] - offset[0] *i, antenna1[1] - offset[1] *i))
                antinodesList.append((antenna2[0] + offset[0] *i, antenna2[1] + offset[1] *i))
                antinodesList.append((antenna2[0] - offset[0] *i, antenna2[1] - offset[1] *i))

                i +=1
            
            # Add valid antinodes, they cannot overlap their own antenna's
            for antinode in antinodesList:
                # if antinode not in (antenna1, antenna2):
                antinodesSet.add(antinode)
    # Filtering antinodes that are out of specified bounds
    invalidAntinodesSet = set()
    for antinode in antinodesSet:
        if antinode[0] > maxBound[0] or antinode[0] < minBound[0]: invalidAntinodesSet.add(antinode)
        elif antinode[1] > maxBound[1] or antinode[1] < minBound[1]: invalidAntinodesSet.add(antinode)
    antinodesSet = antinodesSet - invalidAntinodesSet
    print(antinodesSet)
    return len(antinodesSet)

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
    
# Process file into antenna data structure
input = parseFile(filePaths[choice])
antennaMapDict, minBound, maxBound = mapTheAntennas(input)
antennaPairDict = pairAntennas(antennaMapDict)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
# part1answer = part1(antennaPairDict, minBound, maxBound)
# print(f'The answer to day {day} part 1 = {part1answer}')
# if choice == '2':
#     testCorrect = part1answer == expectedTestOutputPart1
#     print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
part2answer = part2(antennaPairDict, minBound, maxBound)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')