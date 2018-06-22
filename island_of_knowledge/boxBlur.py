def boxBlur(image):
    x = len(image[0]) - 2;
    y = len(image) - 2;
    b = [[0 for i in range(x)] for j in range(y)]

    for i in range(y):
        for j in range(x):
            b[i][j] = image[i][j] + image[i][j+1] + image[i][j+2] + image[i+1][j] \
              + image[i+1][j+1] + image[i+1][j+2] + image[i+2][j] + image[i+2][j+1] + image[i+2][j+2]
            b[i][j] //= 9
    return b
