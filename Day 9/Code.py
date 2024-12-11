import re

## Variables and Configuration ##
# Extract the current day number from the file path using regex
folder = re.search(r'Day (\d{1,2})\\', __file__)
day = folder.group(1)

# Define file paths for input and test input files based on the extracted day number
filePaths = {
    '1': 'Day ' + str(day) + '\\Input files\\Input.txt',
    '2': 'Day ' + str(day) + '\\Input files\\TestInput.txt',
}

# Default configuration for using the input file and expected outputs for validation tests
defaultFile = False
expectedTestOutputPart1 = 1928
expectedTestOutputPart2 = 2858

## Methods ##
def parse_file(filepath):
    """Read and return the content of the file as a single string."""
    diskMap = ""
    with open(filepath, 'r') as file:
        for line in file:
            diskMap += line
    return diskMap

def convert_disk_map_to_list(diskMap):
    """Convert a disk map string into a list of blocks with IDs and empty spaces."""
    isFile = True  # Alternates between processing file blocks and empty blocks
    blockList = []
    fileID = -1
    for command in diskMap:
        command = int(command)
        if isFile:
            fileID += 1
            fileBlocks = command
            # Append the file ID for the number of blocks it occupies
            for i in range(fileBlocks):
                blockList.append(fileID)
            isFile = False  # Switch to processing empty blocks
        else:
            emptyBlocks = command
            # Append '.' for each empty block space
            for i in range(emptyBlocks):
                blockList.append('.')
            isFile = True  # Switch back to processing file blocks
    return blockList

def convert_disk_map_to_dict(diskMap):
    """Convert a disk map string into a dictionary representing blocks and empty spaces with start and end position"""
    isFile = True  # Alternates control between file and empty blocks
    blockDict = {}
    fileID = -1
    startBlock = 0
    for command in diskMap:
        command = int(command)
        if isFile:
            fileID += 1
            # Map the range of file blocks to the file ID
            blockDict[(startBlock, startBlock + command - 1)] = fileID
            startBlock += command  # Update start block to the new position
            isFile = False  # Switch to processing empty blocks
        elif not isFile:
            # If there are empty blocks, record their range in the dictionary
            if command != 0: 
                blockDict[(startBlock, startBlock + command - 1)] = '.'
            startBlock += command  # Continue from the next position
            isFile = True  # Switch back to processing file blocks
    return blockDict

def part_1(blockList):
    """Defragment the block list by moving files forward into empty spaces."""
    emptyBlockCount = 0  # Count of empty blocks to track when defragmentation is complete
    defragmentComplete = False
    # Count the total number of empty blocks
    for block in blockList:
        if block == '.': 
            emptyBlockCount += 1
    
    while not defragmentComplete:
        for block in blockList:
            if block == '.':
                emptyBlockIndex = blockList.index(block)
                # Find the last file block to be moved
                for blockToBeMovedIndex in range(len(blockList) - 1, -1, -1):
                    if blockList[blockToBeMovedIndex] != '.':
                        blockToBeMoved = blockList[blockToBeMovedIndex]
                        break
                # Move the last file block into the first empty space
                blockList[emptyBlockIndex] = blockToBeMoved
                blockList[blockToBeMovedIndex] = '.'
                break
        continousEmptyBlocks = True  # Check if all empty blocks are continuous at the end
        emptyBlockCountCheck = 0
        for block in reversed(blockList):
            if block == '.':
                emptyBlockCountCheck += 1
                # If the count of trailing empty blocks matches the total count, defragment is complete
                if emptyBlockCountCheck == emptyBlockCount: 
                    defragmentComplete = True
            else: 
                break
    return blockList

def part_2(blockDict):
    """Defragment the block dictionary by repositioning files to fill empty spaces."""
    newBlockList = []
    defragmentComplete = False
    movedFiles = []  # Track files that have already been moved

    def get_empty_block(blockDict, triedBlockList, fileBlockKey):
        """Identify an empty block with space before the current file block."""
        firstAvailableSpace = 9999999999999999
        foundAvailableSpace = False
        for emptyBlockKey in blockDict.keys():
            emptyBlock = blockDict[emptyBlockKey]
            emptyBlockStartPosition = emptyBlockKey[0]
            if emptyBlock == '.':
                if emptyBlockStartPosition < firstAvailableSpace:
                    # Ensure the block has not been tried and the space is before the fileBlockKey
                    if emptyBlockKey not in triedBlockList:
                        if emptyBlockKey[1] < fileBlockKey[0]:
                            firstAvailableSpace = emptyBlockStartPosition
                            firstEmptyBlockKey = emptyBlockKey
                            foundAvailableSpace = True
        if foundAvailableSpace:
            return firstEmptyBlockKey
        else:
            return 'Error'  # Return error if no suitable block is found
        
    def get_file_to_be_moved(blockDict):
        """Identify the next file block that needs to be moved, starting from the end."""
        foundAvailableBlock = False
        for fileBlockKey in reversed(blockDict.keys()):
            fileBlock = blockDict[fileBlockKey]
            if fileBlock != '.' and fileBlock not in movedFiles:
                # Track moved file to prevent moving it again
                movedFiles.append(fileBlock)
                foundAvailableBlock = True
                break
        if foundAvailableBlock:
            return fileBlockKey
        else:
            return 'Error'  # Return error if no moveable file block is found
        
    while not defragmentComplete:
        fileBlockKey = get_file_to_be_moved(blockDict)
        if fileBlockKey == 'Error':
            defragmentComplete = True
            break
        fileID = blockDict[fileBlockKey]  # Get the current file ID
        fileBlockLength = fileBlockKey[1] - fileBlockKey[0] + 1  # Calculate the file block size
        foundSpace = False
        triedBlockList = []  # Keep track of empty blocks already tried
        while not foundSpace:
            emptyBlockKey = get_empty_block(blockDict, triedBlockList, fileBlockKey)
            if emptyBlockKey == 'Error': break  # Break if no appropriate space is found
            emptyBlockLength = emptyBlockKey[1] - emptyBlockKey[0] + 1
            if fileBlockLength == emptyBlockLength:
                # Move entire file into the empty space if it fits exactly
                blockDict[emptyBlockKey] = fileID
                blockDict[fileBlockKey] = '.'
                foundSpace = True
            elif fileBlockLength < emptyBlockLength:
                # Split the empty block if the file fits within the start of the empty space
                del blockDict[emptyBlockKey]
                blockDict[(emptyBlockKey[0], emptyBlockKey[0] + fileBlockLength - 1)] = fileID
                blockDict[(emptyBlockKey[0] + fileBlockLength, emptyBlockKey[1])] = '.'
                blockDict[fileBlockKey] = '.'
                foundSpace = True
            else:
                # Add to list of tried blocks if the empty space isn't sufficient
                triedBlockList.append(emptyBlockKey)
                
    # Initialize the result list based on the maximum block index
    max_index = max(end for _, end in blockDict.keys())
    newBlockList = [None] * (max_index + 1)
    # Sort the block dictionary and fill the new block list with respective values
    sorted_items = sorted(blockDict.items())
    for (start, end), value in sorted_items:
        for i in range(start, end + 1):
            newBlockList[i] = value            
    return newBlockList

def calculate_filesystem_checksum(defragmentedBlockList):
    """Calculate a checksum based on block indices and values, excluding empty blocks."""
    filesystemChecksum = 0
    for blockIndex in range(len(defragmentedBlockList) - 1):
        block = defragmentedBlockList[blockIndex]
        if block != '.':
            # Add the product of the index and block value to the checksum
            filesystemChecksum += (blockIndex * block)
    return filesystemChecksum

## Main execution ##
# User input to select which file to parse, defaulting to test file if specified
if defaultFile: 
    choice = '2'
else:
    print("""
    Select input file to use:
        1. Main input
        2. Test input
    """)
    choice = input("Enter choice (1/2): ")
    
# Parse the input file and convert the contents into data structures
diskMap = parse_file(filePaths[choice])

# Output results for Part 1 and validate against expected test results if applicable
blockList = convert_disk_map_to_list(diskMap)
defragmentedBlockList = part_1(blockList)
part1answer = calculate_filesystem_checksum(defragmentedBlockList)
print(f'The answer to day {day} part 1 = {part1answer}')
if choice == '2':
    testCorrect = part1answer == expectedTestOutputPart1
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart1} and got {part1answer}')

# Output results for Part 2 and validate against expected test results if applicable
blockDict = convert_disk_map_to_dict(diskMap)
newBlockList = part_2(blockDict)
part2answer = calculate_filesystem_checksum(newBlockList)
print(f'The answer to day {day} part 2 = {part2answer}')
if choice == '2':
    testCorrect = part2answer == expectedTestOutputPart2
    print(f'This answer is {testCorrect}! Expected {expectedTestOutputPart2} and got {part2answer}')