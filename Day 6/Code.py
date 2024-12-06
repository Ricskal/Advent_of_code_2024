import re
import os
import time
import sys

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
expectedTestOutputPart1 = 41
expectedTestOutputPart2 = 6

## Methods ##
def parseFile(filepath):
    parsedFile = []
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    return parsedFile

def mapTheLab(parsedFile):
    # (xCord , yCord) = thingy
    theLabMapDict = {}
    yCord = -1
    for line in parsedFile:
        yCord += 1
        xCord = -1
        for thingy in line:
            xCord += 1
            theLabMapDict[(xCord, yCord)] = thingy
            if thingy == '^': guardInitLocation = (xCord, yCord)
    return theLabMapDict, guardInitLocation

def printTheLabMapDict(theLabMapDict, choice):
    # Pause to make animation visible
    time.sleep(0.2)

    # Clear the console screen
    os.system('cls')

    # Define the size of the grid
    if choice == '1':
        width = 130
        height = 130
    elif choice == '2':
        width = 10
        height = 10
    else:
        print("Error: can't print map of the lab.")
        return

    # Iterate over each row and column to print the grid
    for y in range(height):
        row = ""
        for x in range(width):
            # Fetch the character from the dictionary using the coordinates as a key
            row += theLabMapDict.get((x, y), '.')
        print(row)

def part1(theLabMapDict, guardInitLocation, choice):
    part1answer = 0  
    guardCurrentLocation = list(guardInitLocation)  # Start at the initial location of the guard
    guardCurrentDirection = 'North'  # Initial direction of the guard
    # Dictionaries defining turning and movement logic based on direction
    guardTurnDirectionDict = {'North': 'East', 'East': 'South', 'South': 'West', 'West': 'North'}
    guardDirectionDict = {'North': (0, -1), 'East': (1, 0), 'South': (0, 1), 'West': (-1, 0)}
    
    # Main loop, effectively simulating the guard's path until it's terminated
    while True:
        # Logic for moving north
        if guardCurrentDirection == 'North':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['North'][0],
                                guardCurrentLocation[1] + guardDirectionDict['North'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation)  # Fetch what's at the new location
            # Move forward if path is clear ('.' or already visited 'X')
            if guardNewLocationThingy == '.' or guardNewLocationThingy == 'X':
                # Mark current location as visited ('X') and move '^' to new location
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                printTheLabMapDict(theLabMapDict, choice)  # Update map display
            # Turn right if there's a wall ('#')
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['North']
            # Terminate if out of bounds (None)
            elif guardNewLocationThingy is None:
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                printTheLabMapDict(theLabMapDict, choice)
                print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break

        # Logic for moving east
        if guardCurrentDirection == 'East':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['East'][0],
                                guardCurrentLocation[1] + guardDirectionDict['East'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation)
            if guardNewLocationThingy == '.' or guardNewLocationThingy == 'X':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                printTheLabMapDict(theLabMapDict, choice)
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['East']
            elif guardNewLocationThingy is None:
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                printTheLabMapDict(theLabMapDict, choice)
                print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break

        # Logic for moving south
        if guardCurrentDirection == 'South':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['South'][0],
                                guardCurrentLocation[1] + guardDirectionDict['South'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation)
            if guardNewLocationThingy == '.' or guardNewLocationThingy == 'X':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                printTheLabMapDict(theLabMapDict, choice)
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['South']
            elif guardNewLocationThingy is None:
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                printTheLabMapDict(theLabMapDict, choice)
                print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break

        # Logic for moving west
        if guardCurrentDirection == 'West':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['West'][0],
                                guardCurrentLocation[1] + guardDirectionDict['West'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation)
            if guardNewLocationThingy == '.' or guardNewLocationThingy == 'X':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                printTheLabMapDict(theLabMapDict, choice)
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['West']
            elif guardNewLocationThingy is None:
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = 'X'
                printTheLabMapDict(theLabMapDict, choice)
                print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break
    
    # Count all locations marked as visited ('X')
    for value in theLabMapDict.values():
        if value == 'X':
            part1answer += 1
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
theLabMapList = parseFile(filePaths[choice])
theLabMapDict, guardInitLocation = mapTheLab(theLabMapList)
part1answer = part1(theLabMapDict, guardInitLocation, choice)

# Output results for both parts and verify test results if applicable
# Part 1 outputs
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