def chessBoardCellColor(cell1, cell2):
    cell1_list = list(cell1)
    cell2_list = list(cell2)
    cell1_list[0] = ord(cell1_list[0])
    cell1_list[1] = int(cell1_list[1])
    cell2_list[0] = ord(cell2_list[0])
    cell2_list[1] = int(cell2_list[1])
    if abs(cell2_list[0] - cell1_list[0]) % 2 == 0 and \
        abs(cell2_list[1] - cell1_list[1]) % 2 == 0:
        return True
    elif abs(cell2_list[0] - cell1_list[0]) % 2 != 0 and \
        abs(cell2_list[1] - cell1_list[1]) % 2 != 0:
        return True
    else:
        return False
