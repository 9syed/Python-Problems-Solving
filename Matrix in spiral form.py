def spiral(x, y, z):
    k = 0
    l = 0

    while (k < x and l < y):
        for i in range(l, y):
            print(z[k][i], end=' ')
        
        k += 1

        for i in range(k, x):
            print(z[i][y - 1], end=' ')

        y -= 1

        if (k < x):

            for i in range(y - 1, (l -1), -1):
                print(z[x - 1][i], end=' ')

            x -= 1

        if (l < y):
            for i in range(x - 1, k - 1, -1):
                print(z[i][l], end=' ')
            
            l += 1

z = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ]]

R = 4
C = 4

spiral(R, C, z)