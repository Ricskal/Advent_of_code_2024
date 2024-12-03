# variables
part1answer = 0
part2answer = 0

def parse_file(filepath):
    parsedFile = ""
    with open(filepath, 'r') as file:
        for line in file:
            parsedFile += line
    return parsedFile

def part1(input):
    return part1answer

def part2(input):
    return part1answer

# input = parse_file('Day X\Input files\Input.txt')
input = parse_file('Day X\Input files\TestInput.txt')
# input = parse_file('Day X\Input files\TestInputPart2.txt')

# Part 1
print(f'The answer to day 1 part 1 = {part1(input)}')

# Part 2
# print(f'The answer to day 1 part 2 = {part2(input)}')