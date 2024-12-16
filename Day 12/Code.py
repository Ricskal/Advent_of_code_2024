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
expectedTestOutputPart1 = 0
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    _list0 = []
    flowerfieldDict, flowerCountDict = {}, {}
    with open(filepath, 'r') as file:
        for line in file:
            _list0.append(line.strip())
    
    yCord = -1
    for _line in _list0:
        yCord += 1
        xCord = -1
        for _tile in _line:
            xCord += 1
            flowerfieldDict[(xCord, yCord)] = _tile
    
    for flower in flowerfieldDict.values():
        flowerCountDict[flower] = flowerCountDict.get(flower, 0) + 1
        
    return flowerfieldDict, flowerCountDict

def part_1(flowerfieldDict, flowerCountDict):
    part1answer = 0
    flowerSumDict = {}
    directionDict = {
        'North': (0, -1),
        'East': (1, 0), 
        'South': (0, 1),
        'West': (-1, 0)
    }
    for flowerCor in flowerfieldDict:
        
        flower = flowerfieldDict[flowerCor]
        notSameFlowerCount = flowerfieldDict.get(flowerCor[1], 0)
        newFlower = flowerfieldDict.get((flowerCor[0] + directionDict['North'][0], flowerCor[1] + directionDict['North'][1]), '&')[0]
        if newFlower != flower:
            notSameFlowerCount += 1
            flowerfieldDict[flowerCor] = [flower, notSameFlowerCount]
            
        newFlower = flowerfieldDict.get((flowerCor[0] + directionDict['East'][0], flowerCor[1] + directionDict['East'][1]), '&')[0]
        if newFlower != flower:
            notSameFlowerCount += 1
            flowerfieldDict[flowerCor] = [flower, notSameFlowerCount]

        newFlower = flowerfieldDict.get((flowerCor[0] + directionDict['South'][0], flowerCor[1] + directionDict['South'][1]), '&')[0]
        if newFlower != flower:
            notSameFlowerCount += 1
            flowerfieldDict[flowerCor] = [flower, notSameFlowerCount]

        newFlower = flowerfieldDict.get((flowerCor[0] + directionDict['West'][0], flowerCor[1] + directionDict['West'][1]), '&')[0]
        if newFlower != flower:
            notSameFlowerCount += 1
            flowerfieldDict[flowerCor] = [flower, notSameFlowerCount]
        
        if not isinstance(flowerfieldDict[flowerCor], list): 
            flowerfieldDict[flowerCor] = [flower, 0]

    for flower in flowerfieldDict.values():
        flowerSumDict[flower[0]] = flowerSumDict.get(flower[0], 0) + flower[1]
        # flowerSumDict[flower[0]] = flowerSumDict.get(flower[0], 0) + flowerfieldDict[flower[1]]
        
    
    print(flowerSumDict)
    
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
flowerfieldDict, flowerCountDict = parse_file(filePaths[choice])
part1answer = part_1(flowerfieldDict, flowerCountDict)
part2answer = part_2(input)

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