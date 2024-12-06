import re

## variables ##
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
defaultFile = False
expectedTestOutputPart1 = 143
expectedTestOutputPart2 = 0

## Methods ##
def parseFile(filepath):
    parsedFile, parsedList1, parsedList2 = [], [], []
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    index = parsedFile.index('')
    list1 = parsedFile[:index]
    for pair in list1:
        parsedList1.append(pair.split('|'))
        pageOrderList = [[int(x) for x  in sublist] for sublist in parsedList1]
    list2 = parsedFile[index +1:]
    for numberString in list2:
        parsedList2.append(numberString.split(','))
        pageList = [[int(x) for x in sublist] for sublist in parsedList2]
    return pageOrderList, pageList

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


def part1(input1, input2):
    part1answer = 0
    for numberList in input2:
        numberListValid = True
        for number in numberList:
            numberIndex = numberList.index(number)
            beforeNumberList = numberList[:numberIndex]
            afterNumberList = numberList[numberIndex +1:]
            allowedBeforeNumber = input1[number][0]
            allowedAfterNumber = input1[number][1]
            for beforeNumber in beforeNumberList:
                if beforeNumber in allowedAfterNumber:
                    # print(f'Found number {beforeNumber} before number {number}. This is not allowed.')
                    numberListValid = False
            for afterNumber in afterNumberList:
                if afterNumber in allowedBeforeNumber:
                    # print(f'Found number {afterNumber} after number {number}. This is not allowed.')
                    numberListValid = False
        if numberListValid:
            # print(f'List {numberList} is vallid')
            middleIndex = len(numberList) // 2
            part1answer += numberList[middleIndex]
        else: 
            1 == 1
            # print(f'List {numberList} is not vallid')
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

# Part 1
part1answer = part1(parsePageOrderList(input1), input2)
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