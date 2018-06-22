from collections import Counter

def palindromeRearranging(inputString):
    counts = Counter(inputString)
    if len(inputString) == 1:
        return True
    elif len(inputString)%2 == 0:
        for x in counts:
            key = x
            value = counts[key]
            if value%2 != 0:
                return False
        return True
    else:
        sum_of_odds = 0
        for x in counts:
            key = x
            value = counts[key]
            if value%2 != 0:
                sum_of_odds +=1
        if sum_of_odds > 1:
            return False
        else:
            return True
