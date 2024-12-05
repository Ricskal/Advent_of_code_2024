import re

## variables ##
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
defaultFile = True
expectedTestOutputPart1 = 143
expectedTestOutputPart2 = 0

## Methods ##
def parseFile(filepath):
    parsedFile = []
    newPageOrderList =[]
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    index = parsedFile.index('')
    pageOrderList = parsedFile[:index]
    for pair in pageOrderList:
        number1, number2 = pair.split('|')
        newPageOrderList.append([int(number1), int(number2)])
    pageList = parsedFile[index +1:]
    return newPageOrderList, pageList

def parsePageOrderList(input):
    beforeAfterNumberDict = {}
    for pair in input:
        number1, number2 = pair[0], pair[1]
        if number1 not in beforeAfterNumberDict:
            beforeAfterNumberDict[number1] = [[],[number2]]
        else:
            beforeAfterNumberDict[number1][1].append(number2)
            
        if number2 not in beforeAfterNumberDict:
            beforeAfterNumberDict[number2] = [[number1],[]]
        else:
            beforeAfterNumberDict[number2][0].append(number1)
    return beforeAfterNumberDict


def part1(input):
    part1answer = 0
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
input1, input2 = parseFile(filePaths[choice])
print(parsePageOrderList(input1))
print(input2)

# Part 1
part1answer = part1(input)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2
part2answer = part2(input)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')