def getPosition(x, arr):
    for i in range(16):
        for j in range(16):
            if x == arr[i][j]:
                return i, j


def playfairEnc(list, matrix):
    maxlis = []
    if len(list) % 2 == 1:
        length = len(list)-1
    else:
        length = len(list)
    # i = 0
    for i in range(0, length, 2):
        if list[i] == list[i+1]:
            maxlis.append((list[i]))
            maxlis.append((list[i+1]))
        else:
            x1, y1 = getPosition(list[i], matrix)  # i = x # j = y
            # i sama = dalam baris sama # y sama dalam kolom sama
            x2, y2 = getPosition(list[i+1], matrix)
            if y1 != y2 and x1 == x2:
                a = matrix[x1][(y1+2) % 16]
                b = matrix[x2][(y2+2) % 16]
                maxlis.append(a)
                maxlis.append(b)
            if y1 == y2 and x1 != x2:
                a = matrix[(x1+2) % 16][y1]
                b = matrix[(x2+2) % 16][y2]
                maxlis.append(a)
                maxlis.append(b)
            if y1 != y2 and x1 != x2:
                a = matrix[x1][y2]
                b = matrix[x2][y1]
                maxlis.append(a)
                maxlis.append(b)
    if len(list) % 2 == 1:
        maxlis.append(list[-1])
    return maxlis


def playfairDec(list, matrix):
    maxlis = []
    if len(list) % 2 == 1:
        length = len(list)-1
    else:
        length = len(list)
    i = 0
    for i in range(0, length, 2):
        if list[i] == list[i+1]:
            maxlis.append((list[i]))
            maxlis.append((list[i+1]))
        else:
            x1, y1 = getPosition(list[i], matrix)  # i = x # j = y
            # i sama = dalam baris sama # y sama dalam kolom sama
            x2, y2 = getPosition(list[i+1], matrix)
            if y1 != y2 and x1 == x2:
                a = matrix[x1][(y1-2) % 16]
                b = matrix[x2][(y2-2) % 16]
                maxlis.append(a)
                maxlis.append(b)
            if y1 == y2 and x1 != x2:
                a = matrix[(x1-2) % 16][y1]
                b = matrix[(x2-2) % 16][y2]
                maxlis.append(a)
                maxlis.append(b)
            if y1 != y2 and x1 != x2:
                a = matrix[x1][y2]
                b = matrix[x2][y1]
                maxlis.append(a)
                maxlis.append(b)
    if len(list) % 2 == 1:
        maxlis.append(list[-1])
    return maxlis
