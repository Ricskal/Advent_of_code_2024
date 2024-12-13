import re

## Variables and Configuration ##
# Extract the current day number from the file path
# Using a regular expression to match and extract the day number from the script's file path
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)  # Extract the day number from the match

# Define file paths for main and test input files, dynamically including the day number
filePaths = {
    '1': f'Day {day}\\Input files\\Input.txt',
    '2': f'Day {day}\\Input files\\TestInput.txt',
}

# Default configuration and expected test outputs
defaultFile = False  # Determines which file is used by default
expectedTestOutputPart1 = 36  # Known expected output for the test input, part 1
expectedTestOutputPart2 = 0   # Known expected output for the test input, part 2
possibleTileDict = {}         # To store possible paths from each tile
nineTilePathsPart1 = set()    # To track unique paths of length 9 tiles for part 1
nineTilePathsPart2 = set()    # To track unique paths of length 9 tiles for part 2

## Methods ##
# Function to read lines from the specified file and return as a list
def parse_file(filepath):
    topographicTileList = []
    with open(filepath, 'r') as file:
        for line in file:
            topographicTileList.append(line.strip())  # Strip whitespace/newlines
    return topographicTileList

# Function to map the topographic tiles from the list into a dictionary with coordinates as keys
def map_topographic_tiles(topographicMapList):
    topographicTileDict = {}   # Dictionary to map coordinates to tile values
    trailheadList = []         # List to store coordinates of trailheads (tiles with value 0)
    yCord = -1
    # Iterate over each line to assign coordinates and values
    for topographicMap in topographicMapList:
        yCord += 1
        xCord = -1
        for tile in topographicMap:
            xCord += 1
            if tile.isdigit():
                tile = int(tile)  # Convert tile character to integer if it's a digit
            topographicTileDict[(xCord, yCord)] = tile
            if tile == 0:
                trailheadList.append((xCord, yCord))  # Add trailhead coordinates
    maxBound = (xCord, yCord)  # Record maximum bounds of the map
    print(f'trailheadList = {trailheadList}')
    return topographicTileDict, trailheadList, maxBound

# Function to determine potential tiles that could be visited from a given tile
def get_possible_tiles(topographicTileDict, coordinate):
    possibleTileList = []  # List to hold possible adjacent tiles
    currentTileValue = topographicTileDict[coordinate]
    # Create a list of the surrounding tile coordinates
    serroundingTileList = [
        (coordinate[0], coordinate[1] - 1),  # North
        (coordinate[0] + 1, coordinate[1]),  # East
        (coordinate[0], coordinate[1] + 1),  # South
        (coordinate[0] - 1, coordinate[1]),  # West
    ]
    # Evaluate each surrounding tile to see if it's a valid move
    for serroundingTile in serroundingTileList:
        serroundingTileValue = topographicTileDict.get(serroundingTile, currentTileValue)
        if serroundingTileValue - currentTileValue == 1:
            possibleTileList.append(serroundingTile)  # Append valid next tile
    if possibleTileList:
        possibleTileDict[coordinate] = possibleTileList
    return possibleTileDict

# Function to calculate all paths within the topographic tiles starting from each trailhead
def calculate_paths(topographicTileDict, trailheadList):
    part1answer, part2answer = 0, 0  # Initialize answers for parts 1 and 2

    # Determine possible tiles to move to from each tile
    for coordinate in topographicTileDict:
        possibleTileDict = get_possible_tiles(topographicTileDict, coordinate)

    # For each trailhead, calculate all possible paths
    for trailhead in trailheadList:
        # Stack to manage paths in a depth-first manner
        stack = [(trailhead, [trailhead])]
        all_paths = []
        while stack:
            current_node, path = stack.pop()
            
            # If there are no more child nodes, record the complete path
            if current_node not in possibleTileDict or not possibleTileDict[current_node]:
                all_paths.append(path)
                continue
            
            # Explore all next nodes
            for next_node in possibleTileDict.get(current_node, []):
                new_path = path + [next_node]
                stack.append((next_node, new_path))
        
        # Processing complete paths for part 1
        for end_path in all_paths:
            if len(end_path) == 10:
                nineTilePathsPart1.add((end_path[0], end_path[-1]))
        part1answer = len(nineTilePathsPart1)
        
        # Processing complete paths for part 2
        for end_path in all_paths:
            if len(end_path) == 10:
                part2answer += 1
        
    return part1answer, part2answer


## Main execution ##
# User input to select specific input file to proceed with
if defaultFile:
    choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")
    
# Parse the selected input file into the topographic tile list
topographicTileList = parse_file(filePaths[choice])

# Map these tiles into a dictionary, record trailheads and boundaries
topographicTileDict, trailheadList, maxBound = map_topographic_tiles(topographicTileList)

# Calculate paths and get results for both parts
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