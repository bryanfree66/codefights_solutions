def arrayMaxConsecutiveSum(inputArray, k):
    first = sum(inputArray[0:k])
    maximum = first

    for i in range(k,len(inputArray)):
	    first = first - inputArray[i-k] + inputArray[i]
	    if first > maximum:
	        maximum = first
    return maximum
