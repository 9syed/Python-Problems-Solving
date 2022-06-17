X = 4
Y = 5

def common_elements(matrix):
 
    z = dict()

    for j in range(Y):
        z[matrix[0][j]] = 1

    for i in range(1, X):
        for j in range(Y):

            if (matrix[i][j] in z.keys() and
                             z[matrix[i][j]] == i):

                z[matrix[i][j]] = i + 1

                if i == X - 1:
                    print(matrix[i][j], end = " ")

matrix = [[1, 2, 1, 4, 8],
          [3, 7, 8, 5, 1],
          [8, 7, 7, 3, 1],
          [8, 1, 2, 7, 9]]
 
common_elements(matrix)