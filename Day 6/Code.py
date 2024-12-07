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
    # time.sleep(0.1)
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
            cell_content = theLabMapDict.get((x, y), '.')

            # Check if cell_content is a list and access index 0 if it is
            if isinstance(cell_content, list) and len(cell_content) > 1:
                row += cell_content[0]
            else:
                row += cell_content
        print(row)

def part1(theLabMapDict, guardInitLocation, choice):
    printTrue = False
    part1answer = 0  
    guardCurrentLocation = list(guardInitLocation)  # Start at the initial location of the guard
    guardCurrentDirection = 'North'  # Initial direction of the guard
    # Dictionaries defining turning and movement logic based on direction
    guardTurnDirectionDict = {'North': 'East', 'East': 'South', 'South': 'West', 'West': 'North'}
    guardDirectionDict = {'North': (0, -1), 'East': (1, 0), 'South': (0, 1), 'West': (-1, 0)}
    loopCounter = 0
    guardPreviousLocation = []
    guardPreviousDirection = 'North'
    
    # Main loop, effectively simulating the guard's path until it's terminated
    while True:
        
        # Logic for moving north
        if guardCurrentDirection == 'North':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['North'][0],
                                guardCurrentLocation[1] + guardDirectionDict['North'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation, '&')  # Fetch what's at the new location
            # Move forward if path is clear ('.' or already visited 'X')
            if guardNewLocationThingy != '#' and guardNewLocationThingy != '&':
                
                # Detect if guard is in a loop (part 2)
                if isinstance(theLabMapDict[(guardNewLocation[0], guardNewLocation[1])], list):
                    if theLabMapDict[(guardNewLocation[0], guardNewLocation[1])][1] == 'North':
                        if printTrue: print(f'We are in a loop')
                        loopCounter += 1
                        if printTrue: time.sleep(5)
                        break
                         
                # Mark current location as visited ('X') and move '^' to new location
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                guardPreviousDirection = guardCurrentDirection
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                if printTrue: printTheLabMapDict(theLabMapDict, choice)  # Update map display
            # Turn right if there's a wall ('#')
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['North']
            # Terminate if out of bounds (None)
            elif guardNewLocationThingy == '&':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
                if printTrue: print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break

        # Logic for moving east
        if guardCurrentDirection == 'East':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['East'][0],
                                guardCurrentLocation[1] + guardDirectionDict['East'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation, '&')
            if guardNewLocationThingy != '#' and guardNewLocationThingy != '&':
                
                # Detect if guard is in a loop (part 2)
                if isinstance(theLabMapDict[(guardNewLocation[0], guardNewLocation[1])], list):
                    if theLabMapDict[(guardNewLocation[0], guardNewLocation[1])][1] == 'East':
                        if printTrue: print(f'We are in a loop')
                        loopCounter += 1
                        if printTrue: time.sleep(5)
                        break
                    
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                guardPreviousDirection = guardCurrentDirection
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['East']
            elif guardNewLocationThingy == '&':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
                if printTrue: print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break

        # Logic for moving south
        if guardCurrentDirection == 'South':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['South'][0],
                                guardCurrentLocation[1] + guardDirectionDict['South'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation, '&')
            if guardNewLocationThingy != '#' and guardNewLocationThingy != '&':

                # Detect if guard is in a loop (part 2)
                if isinstance(theLabMapDict[(guardNewLocation[0], guardNewLocation[1])], list):
                    if theLabMapDict[(guardNewLocation[0], guardNewLocation[1])][1] == 'South':
                        if printTrue: print(f'We are in a loop')
                        loopCounter += 1
                        if printTrue: time.sleep(5)
                        break

                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                guardPreviousDirection = guardCurrentDirection
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['South']
            elif guardNewLocationThingy == '&':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
                if printTrue: print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break

        # Logic for moving west
        if guardCurrentDirection == 'West':
            guardNewLocation = (guardCurrentLocation[0] + guardDirectionDict['West'][0],
                                guardCurrentLocation[1] + guardDirectionDict['West'][1])
            guardNewLocationThingy = theLabMapDict.get(guardNewLocation, '&')
            if guardNewLocationThingy != '#' and guardNewLocationThingy != '&':

                # Detect if guard is in a loop (part 2)
                if isinstance(theLabMapDict[(guardNewLocation[0], guardNewLocation[1])], list):
                    if theLabMapDict[(guardNewLocation[0], guardNewLocation[1])][1] == 'West':
                        if printTrue: print(f'We are in a loop')
                        loopCounter += 1
                        if printTrue: time.sleep(5)
                        break

                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                guardPreviousDirection = guardCurrentDirection
                theLabMapDict[guardNewLocation] = '^'
                guardCurrentLocation = guardNewLocation
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
            elif guardNewLocationThingy == '#':
                guardCurrentDirection = guardTurnDirectionDict['West']
            elif guardNewLocationThingy == '&':
                theLabMapDict[(guardCurrentLocation[0], guardCurrentLocation[1])] = ['X', guardPreviousDirection]
                if printTrue: printTheLabMapDict(theLabMapDict, choice)
                if printTrue: print(f'Out of bound! Last known location: {guardCurrentLocation}')
                break
    
    # Count all locations marked as visited ('X')
    if loopCounter == 0:
        for value in theLabMapDict.values():
            if isinstance(value, list):
                if value[0] == 'X':
                    part1answer += 1
    return part1answer, loopCounter

def part2(theLabMapDict, guardInitLocation, choice):
    part2answer = 0
    numberOfLoops = 0
    for key in theLabMapDict.keys():
        numberOfLoops += 1
        print(f'Loop: {numberOfLoops} out of ~16.900')
        for key2 in theLabMapDict.keys():
            if isinstance(theLabMapDict[key2], list) or theLabMapDict[key2] == '^': theLabMapDict[key2] = '.'
        if key == guardInitLocation: continue
        elif theLabMapDict[key] == '#': continue
        elif theLabMapDict[key] == '.': 
            theLabMapDict[key] = '#'
            # print(f'Placed # at {key}')
        part1answer, loopCounter = part1(theLabMapDict, guardInitLocation, choice)
        theLabMapDict[key] = '.'
        part2answer += loopCounter
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
part1answer, loopCounter = part1(theLabMapDict, guardInitLocation, choice)
part2answer = part2(theLabMapDict, guardInitLocation, choice)

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