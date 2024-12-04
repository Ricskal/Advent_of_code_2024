## variables ##
day = 1
filePaths = {
    '1': 'Day ' + str(day) +'\Input files\Input.txt',
    '2': 'Day ' + str(day) +'\Input files\TestInput.txt',
}
defaultFile = False
expectedTestOutputPart1 = 11
expectedTestOutputPart2 = 31

## Methods ##
def parseFile(filepath):
    list1, list2 = [], []
    with open(filepath, 'r') as file:
        for line in file:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))
        list1.sort()
        list2.sort()
    return list1, list2

def part1(input1, input2):
    part1answer = 0
    for number1, number2 in zip(input1, input2):
        distance = abs(number1 - number2)
        part1answer += distance
    return part1answer

def part2(input1, input2):
    part2answer = 0
    for number1 in input1:
        same_number_counter = 0
        for number2 in input2:
            if number2 == number1:
                same_number_counter += 1 
        part2answer += number1 * same_number_counter
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
part1answer = part1(input1, input2)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2
part2answer = part2(input1, input2)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')