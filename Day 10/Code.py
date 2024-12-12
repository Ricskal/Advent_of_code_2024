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
expectedTestOutputPart1 = 2
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    topographicTileList = []
    with open(filepath, 'r') as file:
        for line in file:
            topographicTileList.append(line.strip())
    return topographicTileList

def map_topographic_tiles(topographicMapList):
    # Map topographic map positions to coordinates and organizes them into a dictionary
    # (xCord , yCord) = tile
    topographicTileDict = {}
    trailheadList = []
    yCord = -1
    for topographicMap in topographicMapList:
        yCord += 1
        xCord = -1
        for tile in topographicMap:
            xCord += 1
            if tile.isdigit(): tile = int(tile)
            topographicTileDict[(xCord, yCord)] = tile
            if tile == 0: trailheadList.append((xCord, yCord))
    maxBound = (xCord, yCord)
    print(f'trailheadList = {trailheadList}')
    return topographicTileDict, trailheadList, maxBound

possibleTileDict = {}
def get_possible_tiles(topographicTileDict, coordinate):
    possibleTileList = []
    currentTileValue = topographicTileDict[coordinate]
    serroundingTileList = [
        (coordinate[0], coordinate[1] -1) # North
        ,(coordinate[0] +1, coordinate[1]) # East
        ,(coordinate[0], coordinate[1] +1) # South
        ,(coordinate[0] -1, coordinate[1]) # West
    ]
    for serroundingTile in serroundingTileList:
        serroundingTileValue = topographicTileDict.get(serroundingTile, currentTileValue)
        if serroundingTileValue - currentTileValue == 1:
            possibleTileList.append(serroundingTile)
    if possibleTileList: possibleTileDict[coordinate] = possibleTileList
    return possibleTileDict

def part_1(topographicTileDict, trailheadList, maxBound):
    part1answer = 0
    for coordinate in topographicTileDict:
        possibleTileDict = get_possible_tiles(topographicTileDict, coordinate)
    print(possibleTileDict)
    return part1answer

def part_2(input):
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
topographicTileList = parse_file(filePaths[choice])
topographicTileDict, trailheadList, maxBound = map_topographic_tiles(topographicTileList)
part1answer = part_1(topographicTileDict, trailheadList, maxBound)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
part2answer = part_2(input)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')