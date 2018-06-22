def find_mines(matrix, row, column):
    try:
        if row < 0 or row > len(matrix):
            return 0
        if column > len(matrix) or column < 0:
            return 0
        if matrix[row][column] is True:
            return 1
    except IndexError:
        return 0
    return 0


def count_surrounding(matrix, row, column):
    top_right = find_mines(matrix, row-1, column+1)
    top = find_mines(matrix, row-1, column)
    top_left = find_mines(matrix, row-1, column-1)
    right = find_mines(matrix, row, column+1)
    bot_right = find_mines(matrix, row+1, column+1)
    bottom = find_mines(matrix, row+1, column)
    bot_left = find_mines(matrix, row+1, column-1)
    left = find_mines(matrix, row, column-1)
    sum = top_right + top + top_left + right + bot_right + bottom + bot_left + left
    return sum
