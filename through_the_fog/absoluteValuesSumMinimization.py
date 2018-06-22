import sys


def absoluteValuesSumMinimization(a):
    minimum_sum = sys.maxsize
    minimum_value = 0
    for i in range(0, len(a)):
        temp = 0
        for j in range(0, len(a)):
            temp += abs(a[j] - a[i])
        if temp < minimum_sum:
            minimum_sum = temp
            minimum_value = a[i]
    return minimum_value
