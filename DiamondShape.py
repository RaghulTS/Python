import math
def printDiamondShape(givLen):

    givLenEmptySpaces = []

    for i in range(givLen):
        givLenEmptySpaces += ' '
    startFromCentre = math.ceil(givLen//2)

    for i in range(startFromCentre + 1):
        givLenEmptySpaces[startFromCentre] = givLenEmptySpaces[startFromCentre - i] = givLenEmptySpaces[startFromCentre + i] = '*'
        for i in givLenEmptySpaces:
            print(i, end='')
        print()
    givLenEmptySpaces = []


    for i in range(givLen):
        givLenEmptySpaces += '*'

    for i in range(1, startFromCentre + 1):
        givLenEmptySpaces[i - 1] = givLenEmptySpaces[-i] = ' '
        for i in givLenEmptySpaces:
            print(i, end='')
        print()

printDiamondShape(13)

