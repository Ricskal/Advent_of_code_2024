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
expectedTestOutputPart2 = 123

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
    unvalidPageList = []
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
            # print(f'List {numberList} is not vallid')
            unvalidPageList.append(numberList)
    return part1answer, unvalidPageList

def part2(unvalidPageList, pageOrderDict):
    part2answer = 0
    for unvalidPage in unvalidPageList:
        reorderdList = []
        for number in unvalidPage:     

            beforeNumberMaxIndex = None
            allowedBeforeNumberList = pageOrderDict[number][0]
            allowedBeforeNumberIndexList = []
            for allowedBeforeNumber in allowedBeforeNumberList:
                if allowedBeforeNumber in reorderdList:
                    allowedBeforeNumberIndexList.append(reorderdList.index(allowedBeforeNumber))
            if allowedBeforeNumberIndexList: beforeNumberMaxIndex = max(allowedBeforeNumberIndexList)

            afterNumberMinIndex = None
            allowedAfterNumberList = pageOrderDict[number][1]
            allowedAfterNumberIndexList = []
            for allowedAfterNumber in allowedAfterNumberList:
                if allowedAfterNumber in reorderdList:
                    allowedAfterNumberIndexList.append(reorderdList.index(allowedAfterNumber))
            if allowedAfterNumberIndexList: afterNumberMinIndex = min(allowedAfterNumberIndexList)
            
            if beforeNumberMaxIndex is None and afterNumberMinIndex is None:
                reorderdList.insert(0, number)
            elif beforeNumberMaxIndex is not None and afterNumberMinIndex is None:
                reorderdList.insert(beforeNumberMaxIndex +1, number)
            elif beforeNumberMaxIndex is None and afterNumberMinIndex is not None:
                reorderdList.insert(afterNumberMinIndex, number)
            elif beforeNumberMaxIndex is not None and afterNumberMinIndex is not None:
                reorderdList.insert(afterNumberMinIndex, number)
            
            print(reorderdList)
        print(reorderdList)
        middleIndex = len(reorderdList) // 2
        part2answer += reorderdList[middleIndex]
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

pageOrderList, pageList = parseFile(filePaths[choice])
pageOrderDict = parsePageOrderList(pageOrderList)
part1answer, unvalidPageList = part1(pageOrderDict, pageList)
part2answer = part2(unvalidPageList, pageOrderDict)

# Part 1
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')