def allLongestStrings(inputArray):
    longest_lengths = max(len(x) for x in inputArray)
    result_string = [x for x in inputArray if len(x) == longest_lengths]
    return result_string
