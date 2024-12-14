import copy
import re
from PIL import (ImageDraw, ImageFont, Image)
import texttoimage

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
defaultFile = False
expectedTestOutputPart1 = 12
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    robotDict = {}
    robotID = 0
    with open(filepath, 'r') as file:
        for line in file:
            # Split line into position and velocity parts; assume consistent format
            position, velocity = line.strip().split(' ')

            # Extract numeric values from position and velocity strings
            position = position.split('=')[1].split(',')
            velocity = velocity.split('=')[1].split(',')
            
            # Convert extracted string values to integers for processing
            position = [int(x) for x in position]
            velocity = [int(x) for x in velocity]
            
            # Store parsed position and velocity data in a dictionary by robotID
            robotDict[robotID] = [position, velocity]
            robotID += 1  # Increment robotID for next entry
    return robotDict

def calculate_position(position, velocity, seconds, bounds):
    # Calculate new position, taking map boundaries into account using modulo to wrap
    # Calculation: # (position + (velocity * Seconds)) % bounds = new position
    xP, yP = position
    xV, yV = velocity
    xB, yB = bounds
    newPosition = [(xP + (xV * seconds)) % xB, (yP + (yV * seconds)) % yB]
    return newPosition

def calculate_quadrant_score(robotDict, bounds):
    xB, yB = bounds  # Total map dimensions
    middleX = xB // 2  # Midpoint for dividing map into quadrants
    middleY = yB // 2
    
    # Initialize counters for each quadrant and an 'other' category
    q1Score, q2Score, q3Score, q4Score, otherScore = 0, 0, 0, 0, 0
    
    for robotID in robotDict:
        xP, yP = robotDict[robotID][0]
        # Determine which quadrant the robot's position is in and update score
        if (xP >= 0 and xP < middleX) and (yP >= 0 and yP < middleY):
            q1Score += 1  # Upper left quadrant
        elif (xP > middleX and xP < xB) and (yP >= 0 and yP < middleY):
            q2Score += 1  # Upper right quadrant
        elif (xP >= 0 and xP < middleX) and (yP > middleY and yP < yB):
            q3Score += 1  # Lower left quadrant
        elif (xP > middleX and xP < xB) and (yP > middleY and yP < yB):
            q4Score += 1  # Lower right quadrant
        else:
            # Handles cases that fall outside normal quadrant division
            otherScore += 1
    
    # Final score is product of all quadrant scores
    score = q1Score * q2Score * q3Score * q4Score
    return score

def display_map(robotDict, bounds):
    # Extract coordinates and remove duplicates by converting to a set
    unique_coordinates = {tuple(coord[0]) for coord in robotDict.values()}
    width, height = bounds # Define the size of the grid
    grid = [] # Create and initialize the grid

    # Iterate over the range equal to the height of the grid
    for _ in range(height):
        # Create a row filled with dots ('.'), representing empty spaces
        row = ['.' for _ in range(width)]
        # Append the row to the grid
        grid.append(row)
    # Mark the unique coordinates with an "X"
    for x, y in unique_coordinates:
        grid[y][x] = '■'
    # Prepare the grid output for display and export
    grid_output = "\n".join("".join(row) for row in grid)
    print(grid_output)

def draw_pixels_from_dict(robotDict, bounds, second):
# Function to draw pixels from a dictionary onto a PNG image
    # Create a new image with white background
    width, height = bounds
    image = Image.new('RGB', [width, height], (255, 255, 255))
    pixels = image.load()
    # Iterate over the dictionary
    for value in robotDict.items():
        # Extract x, y from the first list in the value and paint the pixel black
        x, y = value[1][0]
        pixels[x, y] = (0, 0, 0)
    # Save the image
    image.save(f'Day 14\Part 2 images\{second}.png')

def part_1_2(robotDict, bounds):
    part1answer = 0
    seconds = 10000  # Time interval for simulation
    # Make a deep copy of the original dictionary
    originalRobotDict = copy.deepcopy(robotDict)
    for second in range(seconds):
        for robotID in robotDict:
            robotDict[robotID][0] = calculate_position(robotDict[robotID][0], robotDict[robotID][1], second, bounds)
        draw_pixels_from_dict(robotDict, bounds, second)
        if second == 100 :  # Calculate part 1 after 100 seconds
            part1answer = calculate_quadrant_score(robotDict, bounds)
        if second == 7055: # Display the output after 7055 seconds to see the christmas tree
            print(f'The answer to day {day} part 2 =')
            display_map(robotDict, bounds)
        robotDict = copy.deepcopy(originalRobotDict)
    return part1answer

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
bounds = mapDimensions[choice]  # Get map dimensions

# Output results for both parts and verify test results if applicable
# Part 1 outputs
part1answer = part_1_2(robotDict, bounds)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')