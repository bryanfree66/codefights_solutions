def sumofdigits(n, m):
    if n < 10:
        return m
    else:
        temp = 0
        while n > 0:
            temp += n%10
            n //= 10
        return sumofdigits(temp, m + 1)

def digitDegree(n):
     return sumofdigits(n, 0)
