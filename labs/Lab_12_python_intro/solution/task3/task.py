def LettersGraph(dict):
    max = 0
    for i in dict:
        if dict[i] > max:
            max = dict[i]
    array = ['' for t in range (max + 1)]
    for i in range (len(dict)):
        array[max] += list(dict)[i]
    for j in range(max):
        for i in range(len(dict)):
            if(max - j <= dict[array[max][i]]):
                array[j] += '#'
            else:
                array[j] += ' '
    return array

with open("input.txt", "r") as fInp:
    dict = {}
    while True:
        temp = fInp.read(1)
        if not temp:
            break
        if (temp == '\n' or temp == ' ' or temp == '\t' or temp == '\r'):
            continue
        if temp in dict:
            dict[temp] += 1
        else:
            dict.update({temp : 1})

array = LettersGraph(dict)

with open("output.txt", "w") as fOutp:
    for i in range(len(array)):
        fOutp.write(array[i])
        fOutp.write('\n')

fInp.close()
fOutp.close()