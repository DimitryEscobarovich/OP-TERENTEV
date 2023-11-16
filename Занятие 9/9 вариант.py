# 1
def multiplicity_matrix(matrix, k):
    array = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % k == 0:
                array.append(matrix[i][j])
    return array
matrix = [[12, 36, 63, 75], [21, 93, 56, 62], [53, 35, 18, 60], [98, 59, 64, 46]]
k = 3
a = multiplicity_matrix(matrix, k)
print(len(a), max(a))
# 2
def show(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="\t")
        print()
def get_max(matrix):
    imax = jmax = maxx = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(matrix[i][j]) > maxx:
                maxx = abs(matrix[i][j])
                imax = i
                jmax = j
    print(maxx)
    newmatrix = remove_matrix(matrix, imax, jmax)
    return newmatrix
def remove_matrix(matrix, imax, jmax):
    for i in range(len(matrix)):
        del matrix[i][jmax]
    del matrix[imax]
    return matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
show(matrix)
show(get_max(matrix))
