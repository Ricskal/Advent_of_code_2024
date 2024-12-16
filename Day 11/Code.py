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
    with open(filepath, 'r') as file:
        stoneList = file.read().split(' ')
    return stoneList

def gekke_stenen_doen_dansjes_2(stoneList):
    aantal_knipper = 75
    for knipper in range(1, aantal_knipper +1):
        start_time = time.time() # Start the timer
        index = 0
        while index < len(stoneList):
            getal = stoneList[index]
            if getal == '0':
                stoneList[index] = '1'  # Directly assign '1' instead of converting
            elif len(getal) % 2 == 0: # Even aantal getallen
                helft = len(getal) // 2
                getal1 = getal[:helft]  # Convert slicing result to int
                getal2 = str(int(getal[helft:]))
                stoneList[index:index+1] = [getal1, getal2]  # Slice assignment avoids pop/insert
                index += 1
            else:
                stoneList[index] = str(int(getal) * 2024)  # Compute new value in-place
            index += 1
        end_time = time.time()
        aantal_stenen = len(stoneList)
        print(f'Na de {knipper}e keer knipperen hebben we: {aantal_stenen} stenen. Dit duurde {(end_time - start_time):.4f} seconde')
        # print(f'Stenen lijst: {stoneList}')
    return aantal_stenen

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
stoneList = parse_file(filePaths[choice])
part1answer = gekke_stenen_doen_dansjes_2(stoneList)

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