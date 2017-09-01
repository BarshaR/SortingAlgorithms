# User specifies files or text as the input
# If text, input a string separated by comma's
# If file, pass in absolute path to the file

inputType = input("Choose input type: \n 1. Text \n 2. File")
print("You selected: ", inputType)

numbers = [8,2,3,5,4,12,7,6,20,15,67,34,54,64]


#numbers = [1,2,3,6,5,7,8,9]

def swap (pos1, pos2):
    temp = numbers[pos1]
    numbers[pos1] = numbers[pos2]
    numbers[pos2] = temp


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
            print("Early terminate Swaps: ", swapNum)
            print("Comparisons: ",comparisonNum)
            return
    print("Swaps: ", swapNum)
    print("Comparisons: ",comparisonNum)

bubbleSort(numbers)
print(numbers)
