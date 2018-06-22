def depositProfit(deposit, rate, threshold):
    years = 0
    interest_rate = rate * .01
    while deposit < threshold:
        deposit += (deposit * interest_rate)
        years += 1
    return years
