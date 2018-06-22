def arrayMaximalAdjacentDifference(inputArray):
    maxDifference = 0
    for i in range(len(inputArray) - 1):
        difference_up = inputArray[i] - inputArray[i + 1]
        difference_down = inputArray[i + 1] - inputArray[i]
        max_of_directions = max(difference_up, difference_down)
        if max_of_directions > maxDifference:
            maxDifference = max_of_directions
    return maxDifference
