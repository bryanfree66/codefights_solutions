def isLucky(n):
    numbers_list = [int(i) for i in str(n)]
    total_length = len(numbers_list)
    half_length = int(total_length / 2)
    first_half = numbers_list[:half_length]
    second_half = numbers_list[half_length:]
    first_half_sum = sum(first_half)
    second_half_sum = sum(second_half)
    if first_half_sum == second_half_sum:
        return True
    else:
        return False
