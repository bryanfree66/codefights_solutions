import itertools


def different_by_one(a, b):
    if len(a) != len(b):
        return False
    if a == b:
        return False
    count = 0
    for z, y in zip(a, b):
        if z != y:
            count += 1
    if count == 1:
        return True
    return False

def stringsRearrangement(inputArray):
    perms = itertools.permutations(inputArray)
    perms = [i for i in perms]
    for perm in perms:
        i = 0
        diff_by_one = True
        while i < len(perm)-1:
            if not different_by_one(perm[i], perm[i + 1]):
                diff_by_one = False
                break
            i += 1
        if diff_by_one:
            return True
    return False
