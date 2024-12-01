file = open('Day 1\Input files\InputDay1.txt', 'r')
line_list = file.readlines()
list1 = []
list2 = []

for line in line_list:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1.sort()
list2.sort()

# Part 1
part1answer = 0
for number1, number2 in zip(list1, list2):
    distance = number1 - number2
    if distance < 0:
        distance = distance * -1
    part1answer += distance

print(f'The answer to day 1 part 1 = {part1answer}')


# Part 2
part2answer = 0
for number1 in list1:
    same_number_counter = 0
    for number2 in list2:
        if number2 == number1:
            same_number_counter += 1 
    part2answer += number1 * same_number_counter

print(f'The answer to day 1 part 2 = {part2answer}')