import re

# variables
file = open('Day 3\Input files\Input.txt', 'r')
# file = open('Day 3\Input files\TestInput.txt', 'r')
# file = open('Day 3\Input files\TestInputPart2.txt', 'r')
lineList = file.readlines()
memory = ''
part1answer = 0
part2answer = 0

# Process file
for line in lineList:
    memory += line

# Part 1
uncorruptMemory = []
patternPart1 = r"(mul)\((\d{1,3}),(\d{1,3})\)"
uncorruptMemory = re.findall(patternPart1, memory)
for multiplication in uncorruptMemory:
    part1answer += (int(multiplication[1]) * int(multiplication[2]))

# Part 2
uncorruptMemory = []
patternPart2 = r"don't\(\)(.*?)do\(\)"
donotMemory = re.findall(patternPart2, memory, re.DOTALL)
for memory in donotMemory:
    print(memory)
    uncorruptMemory = re.findall(patternPart1, memory)
    for multiplication in uncorruptMemory:
        print(multiplication)
        part2answer += (int(multiplication[1]) * int(multiplication[2]))

part2answer = part1answer - part2answer

print(f'The answer to day 1 part 1 = {part1answer}')
print(f'The answer to day 1 part 2 = {part2answer}')