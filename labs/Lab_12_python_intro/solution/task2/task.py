import heapq

def SumMedians(numbersCount, listNumbers):
    max_heap, min_heap, result_sum = [], [], 0
    for i in range(numbersCount):
        heapq.heappush(max_heap, -listNumbers[i])
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        result_sum -= max_heap[0]

    return result_sum



if __name__ == "__main__":
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