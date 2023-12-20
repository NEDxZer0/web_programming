import math

def SumMedians(numbersCount, listNumbers):
    sum = 0
    for i in range (numbersCount):
        currentNumber = listNumbers[i]
        listTemp = []
        for j in range(currentNumber):
            listTemp.append(int(listNumbers[j]))
        listTemp.sort()
        sum += listTemp[math.ceil(currentNumber/2) - 1]
    return sum

with open("input.txt", "r") as fInp:
    numbersCount = int(fInp.readline())
    listNumbers = []
    for i in range(numbersCount):
        listNumbers.append(int(fInp.read(2)))

sum = SumMedians(numbersCount, listNumbers)

with open("output.txt", "w") as fOutp:
    fOutp.write(str(sum))

fInp.close()
fOutp.close()