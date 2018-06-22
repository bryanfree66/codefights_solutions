def evenDigitsOnly(n):
    number_list = [int(d) for d in str(n)]
    odd_numbers = [num for num in number_list if num % 2 != 0]
    if odd_numbers:
        return False
    else:
        return True
