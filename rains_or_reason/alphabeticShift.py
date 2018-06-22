def alphabeticShift(inputString):
    character_list = list(inputString)
    int_list = [ord(i) for i in character_list]
    for n, i in enumerate(int_list):
        if int_list[n] == 122:
            int_list[n] = 97
        else:
            int_list[n] += 1
    result_list = [chr(i) for i in int_list]
    return ''.join(result_list)
