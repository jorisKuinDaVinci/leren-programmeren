def printAsText(anyType):
    print(str(anyType))

def showNumberTotal(maxNumber, prevNumber=0, total=0):
    number = prevNumber + 1
    total += number

    if(maxNumber == number):
        printAsText(total)
    else:
        showNumberTotal(maxNumber, number, total)

showNumberTotal(3)