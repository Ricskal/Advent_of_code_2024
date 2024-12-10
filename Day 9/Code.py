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
defaultFile = True
expectedTestOutputPart1 = 1928
expectedTestOutputPart2 = 0

## Methods ##
def parse_file(filepath):
    diskMap = ""
    with open(filepath, 'r') as file:
        for line in file:
            diskMap += line
    return diskMap

def convert_disk_map(diskMap):
    isFile = True
    blockList = []
    fileID = -1
    for command in diskMap:
        command = int(command)
        if isFile:
            fileID += 1
            fileBlocks = command
            for i in range(fileBlocks):
                blockList.append(fileID)
            isFile = False
        else:
            emptyBlocks = command
            for i in range(emptyBlocks):
                blockList.append('.')
            isFile = True
    return blockList

# 00...111...2...333.44.5555.6666.777.888899
# fileID = 0: 2 blocks
# fileID = 1: 3 blocks

# (0,1) = 0
# (2,4) = .
# (5,7) = 1

def convert_disk_map_part_2(diskMap):
    isFile = True
    blockList = {}
    fileID = -1
    for command in diskMap:
        command = int(command)
        if isFile:
            fileID += 1
            fileBlocks = command
            for i in range(fileBlocks):
                blockList.append(fileID)
            isFile = False
        else:
            emptyBlocks = command
            for i in range(emptyBlocks):
                blockList.append('.')
            isFile = True
    print(blockList)
    return blockList

def part_1(blockList):
    emptyBlockCount = 0
    defragmentComplete = False
    for block in blockList:
        if block == '.': emptyBlockCount += 1
    while not defragmentComplete:
        for block in blockList:
            if block == '.':
                emptyBlockIndex = blockList.index(block)
                for blockToBeMovedIndex in range(len(blockList) - 1, -1, -1):
                    if blockList[blockToBeMovedIndex] != '.':
                        blockToBeMoved = blockList[blockToBeMovedIndex]
                        break
                blockList[emptyBlockIndex] = blockToBeMoved
                blockList[blockToBeMovedIndex] = '.'
                break
        continousEmptyBlocks = True
        emptyBlockCountCheck = 0
        for block in reversed(blockList):
            if block == '.':
                emptyBlockCountCheck += 1
                if emptyBlockCountCheck == emptyBlockCount: defragmentComplete = True
            else: break
    return blockList

def part_2(blockList):
    # print(blockList)
    
    return blockList

def calculate_filesystem_checksum(defragmentedblockList):
    filesystemChecksum = 0
    for blockIndex in range(len(defragmentedblockList) -1):
        block = defragmentedblockList[blockIndex]
        if block != '.':
            filesystemChecksum += (blockIndex * block)
    return filesystemChecksum

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
diskMap = parse_file(filePaths[choice])

blockList = convert_disk_map(diskMap)
defragmentedBlockList = part_1(blockList)
part1answer = calculate_filesystem_checksum(defragmentedBlockList)

blockList = convert_disk_map_part_2(diskMap)
defragmentedBlockList = part_2(blockList)
part2answer = calculate_filesystem_checksum(defragmentedBlockList)


# Output results for both parts and verify test results if applicable
# Part 1 outputs
# part1answer = part_1(diskMap)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')