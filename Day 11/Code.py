import re
import copy

## Variables and Configuration ##
# Extract the current day number from the file path using a regular expression
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define file paths for input and test input files based on the current day
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
# Default configuration for input file and expected outputs for tests
defaultFile = False
expectedTestOutputPart1 = 55312
expectedTestOutputPart2 = 65601038650482

## Methods ##
def parse_file(filepath):
    stoneDict = {}
    with open(filepath, 'r') as file:
        # Read the file content and split by spaces to get individual stones
        stoneList = file.read().split(' ')
    for stone in stoneList:
        stoneDict[stone] = 1
    return stoneList, stoneDict

def part_1_2(stoneDict, numberOfBlinks):
    oldStoneDict = copy.deepcopy(stoneDict)  # Duplicate the dictionary to maintain original data
    for blink in range(1, numberOfBlinks + 1):
        newStoneDict = {}
        numberOfStones = 0
        for stoneNumber in list(oldStoneDict.keys()):
            stoneQuantity = oldStoneDict[stoneNumber]
            if stoneNumber == '0':
                # Convert stone number '0' to '1' and move its quantity
                newStoneDict['1'] = newStoneDict.get('1', 0) + stoneQuantity
            elif len(stoneNumber) % 2 == 0:
                # Split stone number into two halves for even-length strings
                half = len(stoneNumber) // 2
                number1 = stoneNumber[:half]
                number2 = str(int(stoneNumber[half:]))
                # Add quantities to both new stone numbers created by splitting
                newStoneDict[number1] = newStoneDict.get(number1, 0) + stoneQuantity
                newStoneDict[number2] = newStoneDict.get(number2, 0) + stoneQuantity
            else:
                # Multiply stone number by 2024 for odd-length strings and update its quantity
                newStoneNumber = str(int(stoneNumber) * 2024)
                newStoneDict[newStoneNumber] = newStoneDict.get(newStoneNumber, 0) + stoneQuantity
        oldStoneDict = copy.deepcopy(newStoneDict)  # Update old stone dictionary for the next iteration
        numberOfStones = sum(oldStoneDict.values())  # Sum all quantities to get total number of stones
    print(f'After the {blink}th blink, we have: {numberOfStones} stones.')
    numberOfStones = sum(oldStoneDict.values())
    return numberOfStones

## Main execution ##
# Prompt user for input choice, using test input file by default if specified
if defaultFile: choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")  # User selects which input file to process
    
# Parse the input file and process it into data structures
stoneList, stoneDict = parse_file(filePaths[choice])
# part1answer = part_1(stoneList)
part1answer = part_1_2(stoneDict, 25)
part2answer = part_1_2(stoneDict, 75)

# Output results for both parts and verify test results if using test input
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