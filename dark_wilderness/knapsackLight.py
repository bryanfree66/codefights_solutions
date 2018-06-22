def knapsackLight(value1, weight1, value2, weight2, maxW):
    return value1 + value2 if weight1 + weight2 <= maxW \
        else (value1 if value1 > value2 and \
              weight1 <= maxW else (value2 if weight2 <= maxW \
                                    else (value1 if weight1 <= maxW else 0)))
