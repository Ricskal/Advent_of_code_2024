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
expectedTestOutputPart1 = 1928
expectedTestOutputPart2 = 2858

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
def convert_disk_map_part_2(diskMap):
    isFile = True
    blockDict = {}
    fileID = -1
    startBlock = 0
    for command in diskMap:
        command = int(command)
        if isFile:
            fileID += 1
            blockDict[(startBlock, startBlock + command -1)] = fileID
            startBlock += command
            isFile = False
        elif not isFile:
            if command != 0: blockDict[(startBlock, startBlock + command -1)] = '.'
            startBlock += command    
            isFile = True
    return blockDict

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

def part_2(blockDict):
    newBlockList = []
    defragmentComplete = False
    movedFiles = []

    def get_empty_block(blockDict, triedBlockList, fileBlockKey):
        firstAvailableSpace = 9999999999999999
        foundAvailableSpace = False
        for emptyBlockKey in blockDict.keys():
            emptyBlock = blockDict[emptyBlockKey]
            emptyBlockStartPosition = emptyBlockKey[0]
            if emptyBlock == '.' and emptyBlockStartPosition < firstAvailableSpace and emptyBlockKey not in triedBlockList and emptyBlockKey[1] < fileBlockKey[0]:
                firstAvailableSpace = emptyBlockStartPosition
                firstEmptyBlockKey = emptyBlockKey
                foundAvailableSpace = True
        if foundAvailableSpace:
            return firstEmptyBlockKey
        else:
            return 'Error'
    
    def get_file_to_be_moved(blockDict):
        foundAvailableBlock = False
        for fileBlockKey in reversed(blockDict.keys()):
            fileBlock = blockDict[fileBlockKey]
            if fileBlock != '.' and fileBlock not in movedFiles:
                movedFiles.append(fileBlock)
                foundAvailableBlock = True
                break
        if foundAvailableBlock:
            return fileBlockKey
        else:
            return 'Error'
        
    while not defragmentComplete:
        fileBlockKey = get_file_to_be_moved(blockDict)
        if fileBlockKey == 'Error':
            defragmentComplete = True
            break
        fileID = blockDict[fileBlockKey]
        print(fileID)
        fileBlockLength = fileBlockKey[1] - fileBlockKey[0] +1
        foundSpace = False
        triedBlockList = []
        while not foundSpace:
            emptyBlockKey = get_empty_block(blockDict, triedBlockList, fileBlockKey)
            if emptyBlockKey == 'Error': break
            emptyBlockLength = emptyBlockKey[1] - emptyBlockKey[0] +1
            if fileBlockLength == emptyBlockLength:
                blockDict[emptyBlockKey] = fileID
                blockDict[fileBlockKey] = '.'
                foundSpace = True
            elif fileBlockLength < emptyBlockLength:
                del blockDict[emptyBlockKey]
                blockDict[(emptyBlockKey[0], emptyBlockKey[0] + fileBlockLength -1)] = fileID
                blockDict[(emptyBlockKey[0] + fileBlockLength, emptyBlockKey[1])] = '.'
                blockDict[fileBlockKey] = '.'
                foundSpace = True
            else:
                triedBlockList.append(emptyBlockKey)
                
    for blockKey in blockDict.keys():
        block = blockDict[blockKey]
        for i in range(blockKey[0],blockKey[1] +1):
            newBlockList.insert(i,block)
    print(newBlockList)
    return newBlockList

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

blockDict = convert_disk_map_part_2(diskMap)
newBlockList = part_2(blockDict)
part2answer = calculate_filesystem_checksum(newBlockList)


# Output results for both parts and verify test results if applicable
# Part 1 outputs
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Part 2 outputs
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')