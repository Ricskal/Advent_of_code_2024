import re

## Variables and Configuration ##
# Extract the current day number from the file path
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define file paths for input and test input files
filePaths = {
    '1': 'Day ' + str(day) + '\Input files\Input.txt',
    '2': 'Day ' + str(day) + '\Input files\TestInput.txt',
}

# Default configuration for input file and expected outputs for tests
defaultFile = False
expectedTestOutputPart1 = 143
expectedTestOutputPart2 = 123

## Methods ##
def parseFile(filepath):
    # Parse the input file into two parts: pageOrderList and pageList
    parsedFile, parsedList1, parsedList2 = [], [], []
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    # Identify the index of the empty line separating the two data sections
    index = parsedFile.index('')
    
    # Process the first section of the file into pageOrderList
    list1 = parsedFile[:index]
    for pair in list1:
        parsedList1.append(pair.split('|'))
        pageOrderList = [[int(x) for x in sublist] for sublist in parsedList1]

    # Process the second section of the file into pageList
    list2 = parsedFile[index + 1:]
    for numberString in list2:
        parsedList2.append(numberString.split(','))
        pageList = [[int(x) for x in sublist] for sublist in parsedList2]

    return pageOrderList, pageList

def parsePageOrderList(pageOrderList):
    # Convert pageOrderList into a dictionary for easier lookups
    beforeAfterNumberDict = {}
    for pair in pageOrderList:
        number1, number2 = pair[0], pair[1]
        # Create or update dictionary entries for the relationship between numbers
        if number1 not in beforeAfterNumberDict:
            beforeAfterNumberDict[number1] = [[], [number2]]
        else:
            beforeAfterNumberDict[number1][1].append(number2)
        if number2 not in beforeAfterNumberDict:
            beforeAfterNumberDict[number2] = [[number1], []]
        else:
            beforeAfterNumberDict[number2][0].append(number1)
    return beforeAfterNumberDict

def part1(pageOrderDict, pageList):
    # Calculate the sum of middle values for valid number lists
    part1answer = 0
    invalidPageList = []
    for numberList in pageList:
        numberListValid = True
        for number in numberList:
            # Split current numberList into elements before and after the current number
            numberIndex = numberList.index(number)
            beforeNumberList = numberList[:numberIndex]
            afterNumberList = numberList[numberIndex + 1:]

            # Validate the order based on allowed numbers before and after each number
            allowedBeforeNumber = pageOrderDict[number][0]
            allowedAfterNumber = pageOrderDict[number][1]

            # Check for violations in the allowed order
            for beforeNumber in beforeNumberList:
                if beforeNumber in allowedAfterNumber:
                    # print(f'Found number {beforeNumber} before number {number}. This is not allowed.')
                    numberListValid = False
            for afterNumber in afterNumberList:
                if afterNumber in allowedBeforeNumber:
                    # print(f'Found number {afterNumber} after number {number}. This is not allowed.')
                    numberListValid = False

        # Calculate the part1 answer or add to the list of invalid pages
        if numberListValid:
            middleIndex = len(numberList) // 2
            part1answer += numberList[middleIndex]
        else:
            invalidPageList.append(numberList)
    return part1answer, invalidPageList

def part2(invalidPageList, pageOrderDict):
    # Reorder invalid pages and calculate the sum of middle values
    part2answer = 0
    for unvalidPage in invalidPageList:
        reorderdList = []
        for number in unvalidPage:     
            # Determine indices for correct placement of numbers according to the order
            beforeNumberMaxIndex = None
            allowedBeforeNumberList = pageOrderDict[number][0]
            allowedBeforeNumberIndexList = []
            for allowedBeforeNumber in allowedBeforeNumberList:
                if allowedBeforeNumber in reorderdList:
                    allowedBeforeNumberIndexList.append(reorderdList.index(allowedBeforeNumber))
            if allowedBeforeNumberIndexList: beforeNumberMaxIndex = max(allowedBeforeNumberIndexList)

            # Determine the lowest index of allowed numbers that appear after the current number in reorderdList
            afterNumberMinIndex = None
            allowedAfterNumberList = pageOrderDict[number][1]
            allowedAfterNumberIndexList = []
            for allowedAfterNumber in allowedAfterNumberList:
                if allowedAfterNumber in reorderdList:
                    allowedAfterNumberIndexList.append(reorderdList.index(allowedAfterNumber))
            if allowedAfterNumberIndexList: afterNumberMinIndex = min(allowedAfterNumberIndexList)

            # Insert 'number' into reorderdList based on the computed indices of beforeNumberMaxIndex and afterNumberMinIndex
            if beforeNumberMaxIndex is None and afterNumberMinIndex is None:
                reorderdList.insert(0, number)
            elif beforeNumberMaxIndex is not None and afterNumberMinIndex is None:
                reorderdList.insert(beforeNumberMaxIndex + 1, number)
            elif beforeNumberMaxIndex is None and afterNumberMinIndex is not None:
                reorderdList.insert(afterNumberMinIndex, number)
            elif beforeNumberMaxIndex is not None and afterNumberMinIndex is not None:
                reorderdList.insert(afterNumberMinIndex, number)
        
        # Log the original and re-ordered lists
        # print(f'Original list: {unvalidPage}. Reorderd list: {reorderdList}')
        middleIndex = len(reorderdList) // 2
        part2answer += reorderdList[middleIndex]
    return part2answer

## Main execution ##
# Prompt user for input choice and parse file
if defaultFile:
    choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")

# Parse the input file and process it into data
pageOrderList, pageList = parseFile(filePaths[choice])
pageOrderDict = parsePageOrderList(pageOrderList)
part1answer, invalidPageList = part1(pageOrderDict, pageList)
part2answer = part2(invalidPageList, pageOrderDict)

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