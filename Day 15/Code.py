import re
import os
import time

## Variables and Configuration ##
# Extract the current day number from the file path using a regular expression
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define file paths for input and test input files using the extracted day number
filePaths = {
    '1': 'Day ' + str(day) + '\Input files\Input.txt',
    '2': 'Day ' + str(day) + '\Input files\TestInput.txt',
}
# Default configuration for input file and expected outputs for testing purposes
defaultFile = False
expectedTestOutputPart1 = 10092
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
# Parse the input file into two parts: the warehouse map and instructions
    _list0, _list1, _list2 = [], [], []
    instructionTuple = tuple()
    warehouseMapDict = {}
    robotPositionList = []
    
    # Read file line by line into _list0
    with open(filepath, 'r') as file:
        for line in file:
            _list0.append(line.strip())
    
    # Identify the index of the blank line that separates sections
    index = _list0.index('')
    
    # Separate the first section of the file, storing each line
    for _text in _list0[:index]: 
        _list2.append(_text)
    
    # Translate each character in this section to coordinates in warehouseMapDict
    yCord = -1
    for _line in _list2:
        yCord += 1
        xCord = -1
        for _tile in _line:
            xCord += 1
            warehouseMapDict[(xCord, yCord)] = _tile
            if _tile == '@': 
                robotPositionList = [xCord, yCord]
    
    # Translate the second section of the file (instructions) into a tuple
    for _text in _list0[index + 1:]:
        for character in _text:
            _list1.append(character)
    instructionTuple = tuple(_list1)
    
    return warehouseMapDict, instructionTuple, robotPositionList

def display_warehouse(warehouseMapDict):
    # Find maximum x and y coordinates to determine the size of the display
    maxX = max(key[0] for key in warehouseMapDict.keys())
    maxY = max(key[1] for key in warehouseMapDict.keys())
    
    # Pause to make animation of the display visible
    time.sleep(0.1)
    
    # Clear the console screen for next frame of display
    os.system('cls')
    
    # Print the warehouse map representing it as lines of characters
    for y in range(maxY + 1):
        line = ""
        for x in range(maxX + 1):
            line += warehouseMapDict.get((x, y), ' ')  # Defaults to space if missing in map
        print(line)

def move_robot(warehouseMapDict, instruction, robotPositionList):
    # Dictionary linking movement instructions with coordinate changes
    instructDict = {
        '^': (0, -1), # Move north
        '>': (1, 0),  # Move east
        'v': (0, 1),  # Move south
        '<': (-1, 0), # Move west
    }
    boxList = []
    
    # Translate the instruction character to a coordinate change
    instruction = instructDict[instruction]
    currRobotPos = (robotPositionList[0], robotPositionList[1])
    newRobotPos = (currRobotPos[0] + instruction[0], currRobotPos[1] + instruction[1])
    
    # Check if the robot moves to an empty tile, update positions accordingly
    if warehouseMapDict[newRobotPos] == '.':
        warehouseMapDict[newRobotPos] = '@'
        warehouseMapDict[currRobotPos] = '.'
        currRobotPos = newRobotPos
    
    # Handling the scenario where the robot pushes a box
    if warehouseMapDict[newRobotPos] == 'O':
        currBoxPos = newRobotPos
        boxList.append([currBoxPos[0], currBoxPos[1]])
        newBoxPos = (currBoxPos[0] + instruction[0], currBoxPos[1] + instruction[1])
        while True:
            # Stop if there is a wall
            if warehouseMapDict[newBoxPos] == '#':
                break
            # Move the box if the next position is empty
            elif warehouseMapDict[newBoxPos] == '.':
                #update robot position
                warehouseMapDict[newRobotPos] = '@'
                warehouseMapDict[currRobotPos] = '.'
                # Update positions of any boxes
                for box in boxList:
                    warehouseMapDict[(box[0] + instruction[0], box[1] + instruction[1])] = 'O'
                currRobotPos = newRobotPos
                break
            # If there is another box, continue pushing
            elif warehouseMapDict[newBoxPos] == 'O':
                currBoxPos = newBoxPos
                newBoxPos = (currBoxPos[0] + instruction[0], currBoxPos[1] + instruction[1])
                boxList.append([currBoxPos[0], currBoxPos[1]])
    
    # Update the robot's position list before returning
    robotPositionList = [currRobotPos[0], currRobotPos[1]]
    return robotPositionList

def part_1(warehouseMapDict, instructionTuple, robotPositionList):
    currRobotPos = robotPositionList
    part1answer = 0
    
    # Execute each instruction to move the robot and display the updated warehouse
    for instruction in instructionTuple:
        currRobotPos = move_robot(warehouseMapDict, instruction, currRobotPos)
        display_warehouse(warehouseMapDict)
    
    # Calculate part1answer based on final positions of 'O' elements in map
    for coordinate, item in warehouseMapDict.items():
        if item == 'O': 
            part1answer += (100 * coordinate[1]) + coordinate[0]
    
    return part1answer

def part_2(input):
    part2answer = 0
    return part2answer

## Main execution ##
# Prompt user for input choice and parse the selected file
if defaultFile: 
    choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")
    
# Parse the input file and process it into data required for part_1 and part_2
warehouseMapDict, instructionTuple, robotPositionList = parse_file(filePaths[choice])
part1answer = part_1(warehouseMapDict, instructionTuple, robotPositionList)

# Output results and verify with expected results for testing accuracy
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