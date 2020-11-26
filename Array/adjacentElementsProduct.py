def biggestSum(inputArray):
    if inputArray[0] > inputArray[1]:
        i = inputArray[0]
        j = inputArray[1]
    else:
        i = inputArray[1]
        j = inputArray[0]

    for num in range(2, len(inputArray)):
        if inputArray[num] > i:
            j = i
            i = inputArray[num]
    return j*i

def adjacentElementsProduct(inputArray):
    score = inputArray[0] * inputArray[1]
    for i in range(2, len(inputArray)):
        if inputArray[i] * inputArray[i-1] > score:
            score = inputArray[i] * inputArray[i-1]
    return score


def main():
    inputArray = [-23, 4]
    print(adjacentElementsProduct(inputArray))

if __name__ == "__main__":
    main()