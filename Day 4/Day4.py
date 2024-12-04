## variables ##
filePaths = {
    '1': 'Day 4\Input files\Input.txt',
    '2': 'Day 4\Input files\TestInput.txt',
    '3': 'Day 4\Input files\TestInputPart2.txt'
}
defaultFile = True
expectedTestOutputPart1 = 18
expectedTestOutputPart2 = 0

## Methods ##
def parseFile(filepath):
    parsedFile = []
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile.append(line.strip())
    return parsedFile

## (xCord , yCord) = Letter
def mapLetters(input):
    letterMap = {}
    yCord = -1
    for line in input:
        yCord += 1
        xCord = -1
        for letter in line:
            xCord += 1
            letterMap[(xCord, yCord)] = letter
    return letterMap

def part1(input):
    part1answer = 0
    xmasDict = {}
    for key in input.keys():
        if input[key] == 'X':
            above, aboveRight, right, belowRight, below, belowLeft, left, aboveLeft = '', '', '', '', '', '', '', '' 
            for i in range(1,4):
                #Check above [X, Y -1]
                above += input.get((key[0],key[1] -i), '#')
                #Check above right [X +1, Y -1]
                aboveRight += input.get((key[0] +i,key[1] -i), '#')
                #Check right [X +1, Y]
                right += input.get((key[0] +i,key[1]), '#')
                #Check below right [X +1, Y +1]
                belowRight += input.get((key[0] +i,key[1] +i), '#')
                #Check below [X, Y -1]
                below += input.get((key[0],key[1] -i), '#')
                #Check below left [X -1, Y +1]
                belowLeft += input.get((key[0] -i,key[1] +i), '#')           
                #Check left [X -1, Y]
                left += input.get((key[0] -i,key[1]), '#')          
                #Check above left [X -1, Y -1]
                aboveLeft += input.get((key[0] -i,key[1] -i), '#')                
            xmasDict[key] = [above, aboveRight, right, belowRight, below, belowLeft, left, aboveLeft]
    for values in xmasDict.values():
        for tekst in values:
            if ('X' + tekst) == 'XMAS': 
                part1answer += 1
                print(f'Found X{tekst}')
    return part1answer

def part2(input):
    part2answer = 0
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
        3. Test input part 2
    """)
    choice = input("Enter choice (1/2/3): ")
input = parseFile(filePaths[choice])



# Part 1
part1answer = part1(mapLetters(input))
print(f'The answer to day 4 part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2
part2answer = part2(input)
print(f'The answer to day 4 part 2 = {part2answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')