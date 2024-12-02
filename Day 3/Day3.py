# variables
file = open('Day X\Input files\InputDayX.txt', 'r')
line_list = file.readlines()
list1 = []
list2 = []

# Process file
for line in line_list:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))
list1.sort()
list2.sort()

# Part 1
part1answer = 0
# print(f'The answer to day 1 part 1 = {part1answer}')


# Part 2
part2answer = 0
# print(f'The answer to day 1 part 2 = {part2answer}')