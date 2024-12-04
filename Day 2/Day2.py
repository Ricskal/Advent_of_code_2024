## variables ##
day = 2
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
defaultFile = False
expectedTestOutputPart1 = 2
expectedTestOutputPart2 = 4

## Methods ##
def parseFile(filepath):
    parsedFile = []
    with open(filepath, 'r') as file:
        for line in file:
            report = line.split()
            report = [int(x) for x in report]
            parsedFile.append(report)
    return parsedFile

def reportChecker(input):
    errorThreshold = 3
    unsafe = False
    isIncreasing = False
    isDecreasing = False
    previousLevel = input[0]
    level = input[1]
    if level > previousLevel: isIncreasing = True
    elif level < previousLevel:isDecreasing = True
    for level in input[1:]:
        levelDistance = level - previousLevel
        # Any two adjacent levels differ by at least one.
        if levelDistance == 0:
            # print(f'Report: {input} is unsafe, {level} is the same as the previous level. The report is skipped!')
            unsafe = True
            break
        # The levels are either all increasing or all decreasing.
        elif levelDistance < 0 and isIncreasing:
            # print(f'Report: {input} is unsafe, {level} is lower then {previousLevel} while levels should be increasing. The report is skipped!')
            unsafe = True
            break
        elif levelDistance > 0 and isDecreasing:
            # print(f'Report: {input} is unsafe, {level} is higher then {previousLevel} while levels should be decreasing. The report is skipped!')
            unsafe = True
            break
        # Any two adjacent levels differ by at most three.
        elif abs(levelDistance) > errorThreshold:
            # print(f'Report: {input} is unsafe, {level} and {previousLevel} are {abs(levelDistance)} apart instead of {errorThreshold}. The report is skipped!')
            unsafe = True
            break
        else: previousLevel = level
    return unsafe

def part1(input):
    part1answer = 0
    for report in input:
        unsafe = reportChecker(report)
        if not unsafe:
            # print(f'Report: {report} is safe!')
            part1answer += 1
    return part1answer

def part2(input):
    part2answer = 0
    reportDictPart2 = {}
    for report in input:
        reportListAlternative = []
        reportSize = len(report)
        for i in range(reportSize):
            reportListAlternative.append(report[:i] + report[i+1:])
        reportListAlternative.append(report)
        reportDictPart2[tuple(report)] = reportListAlternative
    for report in reportDictPart2:
        for reportVersion in reportDictPart2[report]:
            unsafe = reportChecker(reportVersion)
            if not unsafe:
                # print(f'Report version: {reportVersion} of {report} is safe!')
                part2answer += 1
                break
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
input = parseFile(filePaths[choice])

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