def addBorder(picture):
    width = len(picture[0])
    top_bottom_border = ['*' * width]
    picture = top_bottom_border + picture + top_bottom_border
    picture = ['*{0}*'.format(row) for row in picture]
    return picture
