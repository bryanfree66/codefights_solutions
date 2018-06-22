def firstDigit(inputString):
    input_list = list(inputString)
    for x in input_list:
        try:
            digit = int(x)
            return str(digit)
        except ValueError:
            continue
