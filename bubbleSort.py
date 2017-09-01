# Swap two items in a list
def swap (pos1, pos2):
    temp = numbers[pos1]
    numbers[pos1] = numbers[pos2]
    numbers[pos2] = temp

# Main sorting Logic
def bubbleSort (numbers):
    swapNum = 0
    comparisonNum = 0
    for i in range(0, len(numbers), 1):
        didSwap = False
        for j in range(0, len(numbers) - 1, 1):
            comparisonNum = comparisonNum + 1
            if (numbers[j] > numbers[j + 1]):
                swap(j, j + 1)
                didSwap = True
                swapNum = swapNum + 1
        if not didSwap:
            print('Early terminate Swaps: ', swapNum)
            print('Comparisons: ',comparisonNum)
            return
    print('Swaps: ', swapNum)
    print('Comparisons: ',comparisonNum)

# Convert a comma separated string to a list of inte
def stringToList (string):
    list = string.split(',')
    newList = []
    for item in list:
        newList.append(int(item))
    # Return list of integers
    return newList

# Process File input
def processFile (pathname):
    # Open file and read data removing '\n'
    # filename = '/Users/Richard/Desktop/numberList.txt'
    file = open(pathname, 'r')
    fileContents = file.read().split('\n')
    list = fileContents[0]
    # return a list of integers
    return stringToList(list)

# User specifies files or text as the input
# If text, input a string separated by comma's
# If file, input absolute path to the file

inputType = input('Choose input type \n 1. Text \n 2. File\n\n Input: ')
# Validate user input
if (inputType == '1' or inputType == 'Text' or inputType == 'text'):
    print('You selected Text')
    enteredList = input('Enter comma separated integers\n\nList: ')
    numbers = stringToList(enteredList)
elif (inputType == '2' or inputType == 'File' or inputType == 'file'):
    print('You selected File')
    pathname = input('Enter file path\npath: ')
    numbers = processFile(pathname)
else:
    print('Invalid Input, quitting now')
    quit()

bubbleSort(numbers)
print(numbers)
