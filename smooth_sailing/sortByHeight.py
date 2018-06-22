def sortByHeight(a):
    tree_count = a.count(-1)
    if tree_count == 0:
        return sorted(a)
    elif tree_count == len(a):
        return a
    else:
        indices = [i for i, x in enumerate(a) if x == -1]
        sorted_list = sorted(a)
        print(sorted_list)
        print(indices)
        del sorted_list[0:len(indices)]
        for index in indices:
            sorted_list.insert(index, -1)
        return sorted_list
