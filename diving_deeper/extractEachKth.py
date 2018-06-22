def extractEachKth(inputArray, k):
    return [item for index, item in enumerate(inputArray) if (index + 1) % k != 0]
