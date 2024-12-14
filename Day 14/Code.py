import re

## Variables and Configuration ##
# Extract the current day number from the file path
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define file paths for input and test input files
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt'
}
mapDimensions = {
    '1': [101, 103], # width, height
    '2': [11, 7]
}
# Default configuration for input file and expected outputs for tests
defaultFile = True
expectedTestOutputPart1 = 12
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    robotDict = {}
    robotID = 0
    with open(filepath, 'r') as file:
        for line in file:
            position, velocity = line.strip().split(' ')
            position = position.split('=')[1].split(',')
            velocity = velocity.split('=')[1].split(',')
            position = [int(x) for x in position]
            velocity = [int(x) for x in velocity]
            robotDict[robotID] = [position, velocity]
            robotID += 1
    return robotDict

def calculate_position(position, velocity, seconds, bounds):
    # (position + (velocity * Seconds)) % bounds = new position
    xP, yP = position
    xV, yV = velocity
    xB, yB = bounds
    newPosition = [(xP + (xV * seconds)) % xB, (yP + (yV * seconds)) % yB]
    return newPosition

def calculate_quadrant_score(robotDict, bounds):
    xB, yB = bounds
    middleX = xB // 2 
    middleY = yB // 2 
    q1Score, q2Score, q3Score, q4Score, otherScore = 0, 0, 0, 0, 0
    for robotID in robotDict:
        xP, yP = robotDict[robotID][0]
        # upper left quadrant 1
        if (xP >= 0 and xP < middleX) and (yP >= 0 and yP < middleY):
            q1Score += 1
        # upper right quadrant 2  
        elif (xP > middleX and xP < xB) and (yP >= 0 and yP < middleY):
            q2Score += 1
        # lower left quadrant 3
        elif (xP >= 0 and xP < middleX) and (yP > middleY and yP < yB):
            q3Score += 1
        # lower right quadrant 4  
        elif (xP > middleX and xP < xB) and (yP > middleY and yP < yB):
            q4Score += 1
        else:
            otherScore += 1
    score = q1Score * q2Score * q3Score * q4Score
    return score

def part_1(robotDict, bounds):
    part1answer = 0
    seconds = 100
    for robotID in robotDict:
        robotDict[robotID][0] = calculate_position(robotDict[robotID][0], robotDict[robotID][1], seconds, bounds)
    part1answer = calculate_quadrant_score(robotDict, bounds)
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
robotDict = parse_file(filePaths[choice])
bounds = mapDimensions[choice]


# Output results for both parts and verify test results if applicable
# Part 1 outputs
part1answer = part_1(robotDict, bounds)
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