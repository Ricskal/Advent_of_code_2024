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
expectedTestOutputPart1 = 36
expectedTestOutputPart2 = 0
possibleTileDict = {}
nineTilePathsPart1 = set()
nineTilePathsPart2 = set()

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

def calculate_paths(topographicTileDict, trailheadList):
    part1answer, part2answer = 0, 0
    
    for coordinate in topographicTileDict:
        possibleTileDict = get_possible_tiles(topographicTileDict, coordinate)

    for trailhead in trailheadList:
        
        # Stack to manage paths in a depth-first manner
        stack = [(trailhead, [trailhead])]
        all_paths = []
        while stack:
            current_node, path = stack.pop()
            
            # If there are no more children, record the complete path
            if current_node not in possibleTileDict or not possibleTileDict[current_node]:
                all_paths.append(path)
                continue
            
            # Explore all next nodes
            for next_node in possibleTileDict.get(current_node, []):
                new_path = path + [next_node]
                stack.append((next_node, new_path))
                
        # Print all paths found from this start node
        for end_path in all_paths:
            # print(f"Complete path: {end_path}")
            if len(end_path) == 10: nineTilePathsPart1.add((end_path[0], end_path[-1]))
        part1answer = len(nineTilePathsPart1)
        
        # Print all paths found from this start node
        for end_path in all_paths:
            # print(f"Complete path: {end_path}")
            if len(end_path) == 10: part2answer +=1
        
    return part1answer, part2answer


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
part1answer, part2answer = calculate_paths(topographicTileDict, trailheadList)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')