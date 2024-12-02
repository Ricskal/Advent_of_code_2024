# variables
file = open('Day 2\Input files\InputDay2.txt', 'r')
# file = open('Day 2\Input files\TestInputDay2.txt', 'r')
lineList = file.readlines()
errorThreshold = 3
part1answer = 0
part2answer = 0
report = []

# Process file
reportList = []
for line in lineList:
    report = line.split()
    report = [int(x) for x in report]
    reportList.append(report)

# reportChecker
def reportChecker(reportList):
    report = reportList
    answer = 0
    unsafe = False
    isIncreasing = False
    isDecreasing = False
    previousLevel = report[0]
    level = report[1]
    if level > previousLevel: isIncreasing = True
    elif level < previousLevel:isDecreasing = True

    for level in report[1:]:
        levelDistance = level - previousLevel
        # Any two adjacent levels differ by at least one.
        if levelDistance == 0:
            print(f'Report: {report} is unsafe, {level} is the same as the previous level. The report is skipped!')
            unsafe = True
            break
        # The levels are either all increasing or all decreasing.
        elif levelDistance < 0 and isIncreasing:
            print(f'Report: {report} is unsafe, {level} is lower then {previousLevel} while levels should be increasing. The report is skipped!')
            unsafe = True
            break
        elif levelDistance > 0 and isDecreasing:
            print(f'Report: {report} is unsafe, {level} is higher then {previousLevel} while levels should be decreasing. The report is skipped!')
            unsafe = True
            break
        # Any two adjacent levels differ by at most three.
        elif abs(levelDistance) > errorThreshold:
            print(f'Report: {report} is unsafe, {level} and {previousLevel} are {abs(levelDistance)} apart instead of {errorThreshold}. The report is skipped!')
            unsafe = True
            break
        else: previousLevel = level
    return unsafe

# Part 1
for report in reportList:
    unsafe = reportChecker(report)
    if not unsafe:
        print(f'Report: {report} is safe!')
        part1answer += 1

# Part 2
reportDictPart2 = {}
# i = 0
for report in reportList:
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
            print(f'Report version: {reportVersion} of {report} is safe!')
            part2answer += 1
            break

print(f'The answer to day 1 part 1 = {part1answer}')   
print(f'The answer to day 1 part 2 = {part2answer}')

