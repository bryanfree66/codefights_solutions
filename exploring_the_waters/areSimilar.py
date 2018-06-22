def areSimilar(a, b):
    tmp1 = list()
    tmp2 = list()
    for i in range(len(a)):
        if a[i] != b[i]:
            tmp1.append(a[i])
            tmp2.append(b[i])
    if len(tmp1) == 0:
        return True
    elif len(tmp1) > 2:
        return False
    else:
        return tmp1 == list(reversed(tmp2))
