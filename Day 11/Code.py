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
defaultFile = False
expectedTestOutputPart1 = 0
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    with open(filepath, 'r') as file:
        parsedFile=file.read().split(' ')
    return parsedFile


def gekke_stenen_doen_dansjes(parsedFile):
    aantal_knipper = 75
    for a in range(aantal_knipper):
        print(f'Na de {a+1}ste keer knipperen:')
        index = 0
        while index < len(parsedFile):
            getal = str(parsedFile[index])
            if str(getal) == '0':
                getal = '1'
                parsedFile[index] = getal
            elif len(getal) % 2 == 0:
                helft = int(len(getal) / 2)
                getal1 = int(getal[:helft]) #int om voorloopnullen weg te halen
                getal2 = int(getal[helft:])
                parsedFile.pop(index)  # Remove current element
                parsedFile.insert(index, str(getal2))  # Insert getal2 first
                parsedFile.insert(index, str(getal1))  # Insert getal1, keeping order
                index += 1  # Skip the next `getal`
            else:
                getal = str(int(getal) * 2024)
                parsedFile[index] = getal
            
            index += 1
        #print(f'Parsedfile is {parsedFile}')

    aantal_stenen = len(parsedFile)
    return aantal_stenen  
    
def part_1(input):
    part1answer = gekke_stenen_doen_dansjes(parse_file)
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
input = parse_file(filePaths[choice])

# Output results for both parts and verify test results if applicable
# Part 1 outputs
part1answer = gekke_stenen_doen_dansjes(input)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')
#223449 te hoog


# Part 2 outputs
part2answer = part_2(input)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')
    
    
    