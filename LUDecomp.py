[3, 3, 4],
[3, 6, 4],
[5, 6, 2]

U =[
[21, 32, 14, 8, 6, 9, 11, 3, 5],
[17, 2, 8, 14, 55, 23, 19, 1, 6],
[41, 23, 13, 5, 11, 22, 26, 7, 9],
[12, 11, 5, 8, 3, 15, 7, 25, 19],
[14, 7, 3, 5, 11, 23, 8, 7, 9],
[2, 8, 5, 7, 1, 13, 23, 11, 17],
[11, 7, 9, 5, 3, 8, 26, 13, 17],
[23, 1, 5, 19, 11, 7, 9, 4, 16],
[31, 5, 12, 7, 13, 17, 24, 3, 11]
]

L = [
[1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1]
]

b = [[2],
     [5],
     [7],
     [1],
     [6],
     [9],
     [4],
     [8],
     [3]]

utest = [[4,2,3],[4,5,6],[7,-8,2]]
ltest = [[1,0,0],[0,1,0],[0,0,1]]
btest = [[3],[2],[1]]
size = 9

i = 0
j = 0
o = 0
while i < size: # the row being used to judge

    o = i + 1

    while o < size: #the other rows
        lnumber = -1 * U[o][i]
        multiplyer = lnumber / U[i][i]
        L[o][i] = -1 * multiplyer
        while j < size:
            addto = U[o][j]
            multiplyto = U[i][j]
            newsum = addto + (multiplyer * multiplyto)
            U[o][j] = newsum

            j = j + 1

        j = 0
        o = o + 1

    o = 0
    i = i + 1


i = 0
j = 0
o = 0
j2 = 0
while i < size: # the row being used to judge
    if i == j and L[i][j] != 1 and L[i][j] != 0:
        divider = L[i][j]

        tempb = b[i][0]
        tempb = tempb / divider
        b[i][0] = tempb
        u = 0
        while u < size:
            temp = L[i][u]
            if temp != 0:
                temp = temp / divider
                L[i][u] = temp
            u = u + 1

    while o < size: #the other rows
        if i == o:
            o = o + 1
        else:
            newadder = -1 * L[o][j]

            baddto = b[o][0]
            bmultiply = b[i][0] * newadder
            bsum = baddto + bmultiply
            b[o][0] = bsum

            while j2 < size: # we must do all the additions and subtractions
                    #a[o][j] is the number we want to make 0
                addto = L[o][j2]
                multiplyto = L[i][j2]
                newsum = addto + (newadder * multiplyto)
                L[o][j2] = newsum
                j2 = j2 + 1
            j2 = 0
            o = o + 1

    o = 0
    i = i + 1
    j = j + 1


i = 0
j = 0
o = 0
j2 = 0
while i < size: # the row being used to judge
    if i == j and U[i][j] != 1 and U[i][j] != 0:
        divider = U[i][j]

        tempb = b[i][0]
        tempb = tempb / divider
        b[i][0] = tempb
        u = 0
        while u < size:
            temp = U[i][u]
            if temp != 0:
                temp = temp / divider
                U[i][u] = temp
            u = u + 1

    while o < size: #the other rows
        if i == o:
            o = o + 1
        else:
            newadder = -1 * U[o][j]

            baddto = b[o][0]
            bmultiply = b[i][0] * newadder
            bsum = baddto + bmultiply
            b[o][0] = bsum

            while j2 < size: # we must do all the additions and subtractions
                    #a[o][j] is the number we want to make 0
                addto = U[o][j2]
                multiplyto = U[i][j2]
                newsum = addto + (newadder * multiplyto)
                U[o][j2] = newsum
                j2 = j2 + 1
            j2 = 0
            o = o + 1

    o = 0
    i = i + 1
    j = j + 1

t = 0
while t < size:
   print(f'X{t} = {b[t][0]}')
   t = t + 1
