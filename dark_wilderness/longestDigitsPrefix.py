def longestDigitsPrefix(inputString):
    result = []
    for x in inputString:
        try:
            result.append(int(x))
        except ValueError:
            break
    return ''.join(str(e) for e in result)
