import re
import time

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
expectedTestOutputPart1 = 55312
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    stoneDict = {}
    with open(filepath, 'r') as file:
        stoneList = file.read().split(' ')
    for stone in stoneList:
        stoneDict[stone] = 1
    return stoneList, stoneDict

def part_1(stoneList):
    numberOfBlinks = 25
    for blink in range(1, numberOfBlinks + 1):
        startTime = time.time()  # Start the timer
        index = 0
        while index < len(stoneList):
            number = stoneList[index]
            if number == '0':
                stoneList[index] = '1'
            elif len(number) % 2 == 0:
                half = len(number) // 2  # Half
                number1 = number[:half]
                number2 = str(int(number[half:]))
                stoneList[index:index+1] = [number1, number2]
                index += 1
            else:
                stoneList[index] = str(int(number) * 2024)
            index += 1
        endTime = time.time()
        numberOfStones = len(stoneList)
        # print(f'After the {blink}th blink, we have: {numberOfStones} stones. This took {(endTime - startTime):.4f} seconds')
        # print(f'Stone list: {stoneList}')
    return numberOfStones

def part_2(stoneDict):
    numberOfBlinks = 75
    for blink in range(1, numberOfBlinks + 1):
        startTime = time.time()  # Start the timer
        for stoneNumber in list(stoneDict.keys()):
            stoneQuantity = stoneDict[stoneNumber]
            if stoneNumber == '0':
                stoneDict['1'] = stoneDict.get('1', 0) + stoneQuantity
                del stoneDict[stoneNumber]
            elif len(stoneNumber) % 2 == 0:
                half = len(stoneNumber) // 2  # Half
                number1 = stoneNumber[:half]
                number2 = str(int(stoneNumber[half:]))
                stoneDict[number1] = stoneDict.get(number1, 0) + stoneQuantity
                stoneDict[number2] = stoneDict.get(number2, 0) + stoneQuantity
                del stoneDict[stoneNumber]
            else:
                newStoneNumber = str(int(stoneNumber) * 2024)
                stoneDict[newStoneNumber] = stoneDict.get(newStoneNumber, 0) + stoneQuantity
                del stoneDict[stoneNumber]
        endTime = time.time()
        numberOfStones = len(stoneList)
        print(f'After the {blink}th blink, we have: {numberOfStones} stones. This took {(endTime - startTime):.4f} seconds')
        # print(f'Stone list: {stoneDict}')
    return numberOfStones

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
stoneList, stoneDict = parse_file(filePaths[choice])
# part1answer = part_1(stoneList)
part1answer = 0
part2answer = part_2(stoneDict)

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