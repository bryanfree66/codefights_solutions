def bishopAndPawn(bishop, pawn):
    bishop_list = list(bishop)
    pawn_list = list(pawn)
    bishop_list[0] = ord(bishop_list[0])
    bishop_list[1] = int(bishop_list[1])
    pawn_list[0] = ord(pawn_list[0])
    pawn_list[1] = int(pawn_list[1])
    print(bishop_list)
    print(pawn_list)
    if bishop_list[0] == pawn_list[0]:
        return False
    row_offset = abs(bishop_list[0] - pawn_list[0])
    column_offset = abs(bishop_list[1] - pawn_list[1])
    if row_offset == column_offset:
        return True
    else:
        return False
