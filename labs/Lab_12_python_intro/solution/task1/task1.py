def CountWays(x, y):
    arr = [[0] * y for z in range (x)]
    arr[0][0] = 1

    for i in range(x):
        for j in range(y):
            if(i >= 2 and j >= 1):
                arr[i][j] += arr[i-2][j-1] 
            if(j >= 2 and i >= 1):
                arr[i][j] += arr[i-1][j-2]
    
    return(arr[x-1][y-1])

with open("input1.txt", "r") as fInp:
    a = int(fInp.read(1))
    b = int(fInp.read(2))

c = CountWays(a, b)

with open("output1.txt", "w") as fOutp:
    fOutp.write(str(c))

fInp.close()
fOutp.close()